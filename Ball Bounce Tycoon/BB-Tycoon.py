import pygame
import random
import math

pygame.init()
pygame.mixer.init()

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
speed = 0.1
speedX = [0]
speedY = [-0.1]
bounces = 0
bounce = 1
ballTouch = 0

#buttons
button1 = pygame.Rect(10, 510, 180, 80)
button2 = pygame.Rect(210, 510, 180, 80)
button3 = pygame.Rect(410, 510, 180, 80)
button4 = pygame.Rect(610, 510, 180, 80)
buttonColor = [(20, 20, 40), (20, 20, 40), (20, 20, 40), (20, 20, 40)]
defaultColor = (20, 20, 40)
pressedColor = (10, 80, 10)
errorColor = (80, 10, 10)
price1 = 2
price2 = 20
price3 = 5000
price4 = 200
reset = 0

#text
font = pygame.font.Font(r'C:\Users\zevan\pygame\Ball Bounce Tycoon\Arial.ttf', 20)
textColor = (255,255,255)

#sounds
noteA = pygame.mixer.Sound(r'C:\Users\zevan\pygame\Ball Bounce Tycoon\piano-a_A_major.wav')
noteC = pygame.mixer.Sound(r'C:\Users\zevan\pygame\Ball Bounce Tycoon\piano-c_C_major.wav')
noteD = pygame.mixer.Sound(r'C:\Users\zevan\pygame\Ball Bounce Tycoon\piano-d_D_major.wav')
noteF = pygame.mixer.Sound(r'C:\Users\zevan\pygame\Ball Bounce Tycoon\piano-f_F_major.wav')

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
                    if reset == 1:
                        price1 = 2
                        reset = 0
                        buttonColor[0] = (0,0,0)
                    elif bounces >= price1:
                        ballX.append(400)
                        ballY.append(250)
                        speedX.append(0)
                        speedY.append(-speed)
                        bounces -= price1
                        price1 = math.floor(price1*1.5)
                        buttonColor[0] = pressedColor
                    else:
                        buttonColor[0] = errorColor
                elif button2.collidepoint(event.pos):
                    if reset == 1:
                        price2 = 20
                        reset = 0
                        buttonColor[1] = (0,0,0)
                    elif bounces >= price2:
                        speed += 0.1
                        bounces -= price2
                        price2 = price2*4
                        buttonColor[1] = pressedColor
                    else:
                        buttonColor[1] = errorColor
                elif button3.collidepoint(event.pos):
                    if bounces >= price3:
                        reset = 1
                        price3 *= 4
                        buttonColor[2] = pressedColor
                    else:
                        buttonColor[2] = errorColor
                elif button4.collidepoint(event.pos): 
                    if reset == 1:
                        price4 = 200
                        reset = 0
                        buttonColor[3] = (0, 0, 0)
                    elif bounces >= price4:
                        bounce += 1
                        bounces -= price4
                        price4 = math.floor(price4*1.2)
                        buttonColor[3] = pressedColor
                    else:
                        buttonColor[3] = errorColor
        elif event.type == pygame.MOUSEBUTTONUP:
            for i in range(len(buttonColor)):
                buttonColor[i] = defaultColor
    #background update
    screen.fill(color)
    pygame.draw.rect(screen, (10,10,20), (0, 500, 800, 100))

    #buttons
    pygame.draw.rect(screen, buttonColor[0], button1)
    pygame.draw.rect(screen, buttonColor[1], button2)
    pygame.draw.rect(screen, buttonColor[2], button3)
    pygame.draw.rect(screen, buttonColor[3], button4)

    #player update
    for i in range(len(ballX)):
        #movement
        ballX[i] += speedX[i]
        ballY[i] += speedY[i]
        #collisions
        if (ballY[i] >= 500):
            speedX[i] = random.uniform(-speed, speed)
            speedY[i] = -(math.sqrt(speed**2 - speedX[i]**2))
            bounces += bounce
            noteA.play()
        if (ballY[i] <= 0):
            speedX[i] = random.uniform(-speed, speed)
            speedY[i] = (math.sqrt(speed**2 - speedX[i]**2))
            bounces += bounce
            noteC.play()
        if (ballX[i] >= 800):
            speedY[i] = random.uniform(-speed, speed)
            speedX[i] = -(math.sqrt(speed**2 - speedY[i]**2))
            bounces += bounce
            noteD.play()
        if (ballX[i] <= 0):
            speedY[i] = random.uniform(-speed, speed)
            speedX[i] = (math.sqrt(speed**2 - speedY[i]**2))
            bounces += bounce
            noteF.play()
        
        #draw balls
        pygame.draw.circle(screen, (255, 255, 255), (ballX[i], ballY[i]), 5)

    #text
    scoreText = f"Bounce Score: {bounces}"
    scoreTextSurface = font.render(scoreText, True, textColor)
    screen.blit(scoreTextSurface, (5,5))
    text1 = f"+1 Ball: {price1}"
    button1Txt = font.render(text1, True, textColor)
    screen.blit(button1Txt, (10,535))
    text2 = f"+1 Speed: {price2}"
    button2Txt = font.render(text2, True, textColor)
    screen.blit(button2Txt, (210,535))
    text3 = f"Reset: {price3}"
    button3Txt = font.render(text3, True, textColor)
    screen.blit(button3Txt, (410,535))
    text4 = f"+1 Bounce: {price4}"
    button4Txt = font.render(text4, True, textColor)
    screen.blit(button4Txt, (610,535))
    #game update
    pygame.display.flip()

pygame.quit