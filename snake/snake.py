import pygame
import random

pygame.init()

#creating display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
caption = pygame.display.set_caption("Snake")

#clock
fps = 16
clock = pygame.time.Clock()

#font
font = pygame.font.Font(r'C:\Users\zevan\pygame\snake\Retro Gaming.ttf', 20)
endFont = pygame.font.Font(r'C:\Users\zevan\pygame\snake\Retro Gaming.ttf', 50)

#grid
grid_color = (20, 20, 30)
grid_spacing = 20

#player
playerX = [20]
playerY = [15]
score = 0
playerSpeed = 1
buttons = [0,0,0,0] #L,R,U,D

#food
foodX = 0
foodY = 0
def foodSpot():
    global foodX 
    foodX= random.randint(0, 39)
    global foodY 
    foodY = random.randint(0, 29)
    global playerX
    global playerY
    for i in range(len(playerX)):
        if foodX == playerX[i] and foodY == playerY[i]:
            foodSpot()
foodSpot()

endGame = 0
#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #self collision
    for i in range(len(playerX)):
        if i > 1:
            if playerX[0] == playerX[i] and playerY[0] == playerY[i]:
                endGame = 1

    #player array
    if endGame != 1:
        for i in range(len(playerX) - 1, -1, -1):
            if i > 0:
                playerX[i] = playerX[i-1]
                playerY[i] = playerY[i-1]
            else:
                playerX[i] = playerX[i]
                playerY[i] = playerY[i]

    #player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and buttons[1] != 1:
        buttons = [0,0,0,0]
        buttons[0] = 1
    if keys[pygame.K_RIGHT] and buttons[0] != 1:
        buttons = [0,0,0,0]
        buttons[1] = 1
    if keys[pygame.K_UP] and buttons[3] != 1:
        buttons = [0,0,0,0]
        buttons[2] = 1
    if keys[pygame.K_DOWN] and buttons[2] != 1:
        buttons = [0,0,0,0]
        buttons[3] = 1
    
    if buttons[0] == 1:
        playerX[0] -= playerSpeed
    elif buttons[1] == 1:
        playerX[0] += playerSpeed
    elif buttons[2] == 1:
        playerY[0] -= playerSpeed
    elif buttons[3] == 1:
        playerY[0] += playerSpeed

    #food collision
    if playerX[0] == foodX and playerY[0] == foodY:
        score += 1
        foodSpot()
        playerX.append(playerX[score-1])
        playerY.append(playerY[score-1])


    #wall collision
    if playerX[0] <= 0 or playerX[0] >= 40 or playerY[0] <= 0 or playerY[0] >= 30:
        endGame = 1

    # background update
    screen.fill((0,0,0))
    for y in range(0, screen_height, grid_spacing):
         pygame.draw.line(screen, grid_color, (0, y), (screen_width, y))
    for x in range(0, screen_width, grid_spacing):
         pygame.draw.line(screen, grid_color, (x, 0), (x, screen_height))

    #player update
    for i in range(len(playerX)):
        pygame.draw.rect(screen, (0,255,0), (playerX[i] * 20, playerY[i] * 20, 20, 20))

    #food update
    pygame.draw.rect(screen, (255,0,0), (foodX * 20, foodY * 20, 20, 20))

    #display text
    text = f"Score: {score}"
    text_color = (255, 255, 255) 
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, (5,5))

    #end screen
    if endGame == 1:
        endText = f"Game Over"
        endText_surface = endFont.render(endText, True, text_color)
        endText_rect = endText_surface.get_rect()
        screen.blit(endText_surface, (250,250))

        playerSpeed = 0

    pygame.display.flip()  # Update the display

    clock.tick(fps)



pygame.quit