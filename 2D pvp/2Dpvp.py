import pygame

pygame.init()

p1IdlePic = r"C:\Users\zevan\pygame\2D pvp\player1shoot.png"
p1WalkPic = r"C:\Users\zevan\pygame\2D pvp\player1move.png"
p2IdlePic = r"C:\Users\zevan\pygame\2D pvp\player2shoot.png"
p2WalkPic = r"C:\Users\zevan\pygame\2D pvp\player2move.png"

#display 
displayWidth = 800
displayHeight = 600
screen = pygame.display.set_mode((displayWidth, displayHeight))
caption = pygame.display.set_caption("2D PVP")
displayIcon = pygame.image.load(r"C:\Users\zevan\pygame\2D pvp\player1shoot.png")
pygame.display.set_icon(displayIcon)

#players
class players(pygame.sprite.Sprite):
    def __init__(self, path, x, y, up, left, right, direction):
        super().__init__()
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        self.hitbox = self.image.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.xSpeed = 0
        self.ySpeed = 0
        self.up = up
        self.left = left
        self.right = right
        self.direction = direction
    
    def forces(self):
        #ground and gravity
        if self.hitbox.y >= 522:
            self.hitbox.y = 522
            self.ySpeed = 0
        else:
            self.ySpeed += 0.1
        self.hitbox.x += self.xSpeed
        self.hitbox.y += self.ySpeed
        if self.hitbox.x <= 0:
            self.hitbox.x = 0
        if self.hitbox.x >= 775:
            self.hitbox.x = 775

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[self.up] and self.hitbox.y >= 522:
            self.hitbox.y -= 1
            self.ySpeed = -4
        if keys[self.left]:
            if self.xSpeed <= -4:
                self.xSpeed = -4
            else:
                self.xSpeed -= 0.1
            if self.direction == ">":
                self.direction = "<"
                self.image = pygame.transform.flip(self.image, True, False)
        elif keys[self.right]:
            if self.xSpeed >= 4:
                self.xSpeed = 4
            else:
                self.xSpeed += 0.1
            if self.direction == "<":
                self.direction = ">"
                self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.xSpeed = 0

  
player1 = players(p1IdlePic, 40, 400, pygame.K_w, pygame.K_a, pygame.K_d, ">")
player2 = players(p2IdlePic, 740, 200, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, "<")
player2.image = pygame.transform.flip(player2.image, True, False) #making p2 face correct direction

clock = pygame.time.Clock()
FPS = 100

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(FPS)

    #character stuff
    player1.movement()
    player2.movement()

    player1.forces()
    player2.forces()


    #update display
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 255, 255), (0, 560, 800, 40))

    #draw characters
    screen.blit(player1.image, player1.hitbox)
    screen.blit(player2.image, player2.hitbox)


    pygame.display.flip()

pygame.quit