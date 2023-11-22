import pygame
import random
import math

pygame.init()

#display 
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
caption = pygame.display.set_caption("Ball Bounce Tycoon")
icon = pygame.image.load(r"C:\Users\zevan\pygame\Ball Bounce Tycoon\controller-icon.png")
pygame.display.set_icon(icon)

#player
ballX = [400]
ballY = [250]
speed = 0.2
speedX = [-0.2]
speedY = [0]

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #background update
    screen.fill((20,20,40))
    pygame.draw.rect(screen, (10,10,20), (0, 500, 800, 100))

    #player update
    for i in range(len(ballX)):
        #movement
        ballX[i] += speedX[i]
        ballY[i] += speedY[i]
        #collisions
        if (ballY[i] >= 500):
            speedX[i] = random.uniform(-speed, speed)
            speedY[i] = -(math.sqrt(speed**2 - speedX[i]**2))
        if (ballY[i] <= 0):
            speedX[i] = random.uniform(-speed, speed)
            speedY[i] = (math.sqrt(speed**2 - speedX[i]**2))
        if (ballX[i] >= 800):
            speedY[i] = random.uniform(-speed, speed)
            speedX[i] = -(math.sqrt(speed**2 - speedY[i]**2))
        if (ballX[i] <= 0):
            speedY[i] = random.uniform(-speed, speed)
            speedX[i] = (math.sqrt(speed**2 - speedY[i]**2))
        #draw
        pygame.draw.circle(screen, (255, 255, 255), (ballX[i], ballY[i]), 5)
    

    #game update
    pygame.display.flip()

pygame.quit