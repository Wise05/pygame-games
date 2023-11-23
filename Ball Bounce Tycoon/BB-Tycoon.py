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

#color
color = (0,0,0)

#balls!
ballX = [400]
ballY = [250]
speed = 0.2
speedX = [0]
speedY = [-0.2]
bounces = 0
ballTouch = 0

#buttons
button1 = pygame.Rect(10, 510, 180, 80)
button2 = pygame.Rect(210, 510, 180, 80)
button3 = pygame.Rect(410, 510, 180, 80)
button4 = pygame.Rect(610, 510, 180, 80)
buttonColor = (20, 20, 40)
defaultColor = (20, 20, 40)
pressedColor = (40, 40, 60)

#text
font = pygame.font.Font(r'C:\Users\zevan\pygame\Ball Bounce Tycoon\Arial.ttf', 20)
textColor = (255,255,255)


#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #button presses
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if button1.collidepoint(event.pos):
                    ballX.append(400)
                    ballY.append(250)
                    speedX.append(0)
                    speedY.append(-0.2)
                elif button2.collidepoint(event.pos):
                    print("Pressed 2")
                elif button3.collidepoint(event.pos):
                    print("Pressed 3")
                elif button4.collidepoint(event.pos): 
                    print("Pressed 4")

    #background update
    screen.fill(color)
    pygame.draw.rect(screen, (10,10,20), (0, 500, 800, 100))

    #buttons
    buttonColor = (20, 20, 40)
    pressedColor = ()
    pygame.draw.rect(screen, buttonColor, button1)
    pygame.draw.rect(screen, buttonColor, button2)
    pygame.draw.rect(screen, buttonColor, button3)
    pygame.draw.rect(screen, buttonColor, button4)

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
        #fun stuff
        if (ballTouch == 0):
            if (ballY[i] >= 500 or ballY[i] <= 0 or ballX[i] >= 800 or ballX[i] <= 0):
                color = (random.randint(0,80), random.randint(0,80), random.randint(0,80))
                bounces += 1
                ballTouch = 1
                
        #draw balls
        pygame.draw.circle(screen, (255, 255, 255), (ballX[i], ballY[i]), 5)
    ballTouch = 0

    #text
    scoreText = f"Bounce Score: {bounces}"
    scoreTextSurface = font.render(scoreText, True, textColor)
    screen.blit(scoreTextSurface, (5,5))
    text1 = "+1 Ball: "
    button1Txt = font.render(text1, True, textColor)
    screen.blit(button1Txt, (10,535))
    text2 = "+1 Speed: "
    button2Txt = font.render(text2, True, textColor)
    screen.blit(button2Txt, (210,535))
    text3 = "+1 Block: "
    button3Txt = font.render(text3, True, textColor)
    screen.blit(button3Txt, (410,535))
    text4 = "Ball Fever: "
    button4Txt = font.render(text4, True, textColor)
    screen.blit(button4Txt, (610,535))
    #game update
    pygame.display.flip()

pygame.quit