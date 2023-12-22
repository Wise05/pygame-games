import pygame
import random

pygame.init()

p1IdlePic = r"C:\Users\zevan\pygame\2D pvp\player1shoot.png"
p1WalkPic = r"C:\Users\zevan\pygame\2D pvp\player1move.png"
p2IdlePic = r"C:\Users\zevan\pygame\2D pvp\player2shoot.png"
p2WalkPic = r"C:\Users\zevan\pygame\2D pvp\player2move.png"

#text
font = pygame.font.Font(r'C:\Users\zevan\pygame\Pong\Retro Gaming.ttf', 40)

#display 
displayWidth = 800
displayHeight = 600
screen = pygame.display.set_mode((displayWidth, displayHeight))
caption = pygame.display.set_caption("2D PVP")
displayIcon = pygame.image.load(r"C:\Users\zevan\pygame\2D pvp\player1shoot.png")
pygame.display.set_icon(displayIcon)

#envornment generation
environment = [[0,0,0,0,0,0,0,0], 
               [0,0,0,0,0,0,0,0], 
               [0,0,0,0,0,0,0,0]]
for i in range(9):
    array = []
    for j in range(8):
        num = random.randint(-1, 1)
        array.append(num)
    environment.append(array)

squares = []
for i in range(12):
    for j in range(8):
        if environment[i][j] == 1:
            squares.append(pygame.Rect(j * 100, (i * 50) - 40, 100, 5))

#players
class players(pygame.sprite.Sprite):
    def __init__(self, path, pathW, x, y, up, left, right, direction):
        super().__init__()
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        self.idleImage = self.image
        self.walkImage = pygame.image.load(pathW).convert_alpha()
        self.walkImage = pygame.transform.scale(self.walkImage, (self.walkImage.get_width() * 2, self.walkImage.get_height() * 2))
        self.hitbox = self.image.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.xSpeed = 0
        self.ySpeed = 0
        self.up = up
        self.left = left
        self.right = right
        self.direction = direction
        self.bullets = pygame.sprite.Group()
        self.last_shoot_time = pygame.time.get_ticks()
        self.health = 10
        self.onGround = 0
    
    def forces(self):
        #walls and stuff
        for i in range(len(squares)):
            if self.hitbox.y + 19 < squares[i].y and self.hitbox.colliderect(squares[i]):
                if self.ySpeed > 0:
                    self.hitbox.y = squares[i].y - 37
                    self.ySpeed = 0
                    self.onGround = 1

        #ground and gravity
        if self.hitbox.y >= 522:
            self.hitbox.y = 522
            self.ySpeed = 0
            self.onGround = 1
        else:
            self.ySpeed += 0.1
        self.hitbox.x += self.xSpeed
        self.hitbox.y += self.ySpeed
        if self.hitbox.x <= 0:
            self.hitbox.x = 0
        if self.hitbox.x >= 775:
            self.hitbox.x = 775
                    
    def movement(self): #sorry for the long function
        #characters moving from input
        keys = pygame.key.get_pressed()
        if keys[self.up] and self.onGround == 1: #jump
            self.hitbox.y -= 2
            self.ySpeed = -4
            self.onGround = 0

        if keys[self.left]: #move left
            if self.xSpeed <= -4:
                self.xSpeed = -4
            else:
                self.xSpeed -= 0.1
            if self.direction == ">": #changing sprite direction
                self.direction = "<"
                self.idleImage = pygame.transform.flip(self.idleImage, True, False)
                self.walkImage = pygame.transform.flip(self.walkImage, True, False)
                self.image = self.idleImage

            #shooting left
            if pygame.time.get_ticks() - self.last_shoot_time > shoot_delay:
                bullet = Bullet(self.hitbox.x, self.hitbox.y + 19, "<")
                self.bullets.add(bullet)
                self.last_shoot_time = pygame.time.get_ticks()

                #walk animation
                if self.image == self.idleImage:
                    self.image = self.walkImage
                elif self.image == self.walkImage:
                    self.image = self.idleImage
        elif keys[self.right]: #move right
            if self.xSpeed >= 4:
                self.xSpeed = 4
            else:
                self.xSpeed += 0.1
            if self.direction == "<": #changing sprite direction
                self.direction = ">"
                self.idleImage = pygame.transform.flip(self.idleImage, True, False)
                self.walkImage = pygame.transform.flip(self.walkImage, True, False)
                self.image = self.idleImage

            #shooting right
            if pygame.time.get_ticks() - self.last_shoot_time > shoot_delay:
                bullet = Bullet(self.hitbox.x + 20, self.hitbox.y + 19, ">")
                self.bullets.add(bullet)
                self.last_shoot_time = pygame.time.get_ticks()
                #walk animation
                if self.image == self.idleImage:
                    self.image = self.walkImage
                elif self.image == self.walkImage:
                    self.image = self.idleImage
        else:
            self.xSpeed = 0
            self.image = self.idleImage
    
    def bulletHit(self, player):
        for i in self.bullets:
            if player.hitbox.colliderect(i):
                player.health -= 1
                self.bullets.remove(i)

#creating players 
player1 = players(p1IdlePic, p1WalkPic, 120, 520, pygame.K_w, pygame.K_a, pygame.K_d, ">")
player2 = players(p2IdlePic, p2WalkPic, 660, 520, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, "<")
player2.idleImage = pygame.transform.flip(player2.idleImage, True, False) #making p2 face correct direction
player2.walkImage = pygame.transform.flip(player2.walkImage, True, False)

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface((7, 3))
        self.image.fill((200, 200, 200))  # Red color for bullets
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 8
        self.randomness = random.uniform(-0.6, 0.6)
        self.direction = direction

    def update(self):
        if self.direction == "<":
            self.rect.x -= self.speed
        elif self.direction == ">":
            self.rect.x += self.speed
        self.rect.y += self.randomness #making bullets fun

clock = pygame.time.Clock()
FPS = 100
shoot_delay = 200 

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(FPS)
    doShoot = 1

    #character stuff
    player1.movement()
    player2.movement()

    player1.forces()
    player2.forces()

    player1.bullets.update()
    player2.bullets.update()

    player1.bulletHit(player2)
    player2.bulletHit(player1)

    #update display
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (200, 200, 200), (0, 560, 800, 40))

    #drawing environment
    for i in squares:
        pygame.draw.rect(screen, (200,200,200), i)

    #draw health bars
    pygame.draw.rect(screen, (0,0,255), (40, 40, player1.health * 20, 10))
    pygame.draw.rect(screen, (255,0,0), (540, 40, player2.health * 20, 10))

    #draw characters
    screen.blit(player1.image, player1.hitbox)
    screen.blit(player2.image, player2.hitbox)

    #draw bullets
    player1.bullets.draw(screen)
    player2.bullets.draw(screen)

    #win condition
    if player1.health <= 0:
        text = "Player 2 Wins!"
        rText = font.render(text, True, (255,0,0))
        screen.blit(rText, (220, 260))
        player2.health = 10
    if player2.health <= 0:
        text = "Player 1 Wins!"
        rText = font.render(text, True, (20,20,255))
        screen.blit(rText, (220, 260))
        player1.health = 10
    pygame.display.flip()

pygame.quit