import pygame

pygame.init()

#colors
white = (255,255,255)
black = (0,0,0)

#text
font = pygame.font.Font(r'C:\Users\zevan\pygame\Pong\Retro Gaming.ttf', 40)

#display 
displayWidth = 800
displayHeight = 600
screen = pygame.display.set_mode((displayWidth, displayHeight))
caption = pygame.display.set_caption("Pong")
displayIcon = pygame.image.load(r"C:\Users\zevan\pygame\Pong\Ping Pong paddle.png")
pygame.display.set_icon(displayIcon)

#paddles
paddleSpeed = 0.4
#paddle1 is AI
paddleX1 = 60
paddleY1 = []
paddle1 = []
#paddle2 is player
paddleX2 = 740
paddleY2 = []
paddle2 = []
for i in range(5): #paddle is several squares together that each give the ball a different y velocity when colliding
    paddleY1.append((275 + (i * 10)))
    paddleY2.append((275 + (i * 10)))
    paddle1.append(pygame.Rect(paddleX1, paddleY1[i], 10, 10))
    paddle2.append(pygame.Rect(paddleX2, paddleY2[i], 10, 10))

#scores
AI_score = 0
player_score = 0

#ball
ballX = 400
ballY = 300
ballSpeedX = 0.4
ballSpeedY = 0
ballRadius = 5
ballHitbox = pygame.Rect(ballX - ballRadius, ballY - ballRadius, ballRadius * 2, ballRadius * 2)

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if paddleY2[0] >= 0:
            for i in range(5):
                paddleY2[i] -= paddleSpeed
    if keys[pygame.K_DOWN]:
        if paddleY2[4] <= 600:
            for i in range(5):
                paddleY2[i] += paddleSpeed
    for i in range(5):
        paddle2[i] = pygame.Rect(paddleX2, paddleY2[i], 10, 10)

    #AI movement
    if ballY > paddleY1[3]:
        for i in range(5):
                paddleY1[i] += paddleSpeed
    if ballY < paddleY1[1]:
        for i in range(5):
                paddleY1[i] -= paddleSpeed
    for i in range(5):
        paddle1[i] = pygame.Rect(paddleX1, paddleY1[i], 10, 10)

    #ball movement
    ballX += ballSpeedX
    ballY += ballSpeedY
    ballHitbox = pygame.Rect(ballX - ballRadius, ballY - ballRadius, ballRadius * 2, ballRadius * 2)

    #ball and paddle collision
    if (ballHitbox.colliderect(paddle1[0])) or (ballHitbox.colliderect(paddle2[0])):
        ballSpeedX = -ballSpeedX
        ballSpeedY = -0.5
    elif (ballHitbox.colliderect(paddle1[1])) or (ballHitbox.colliderect(paddle2[1])):
        ballSpeedX = -ballSpeedX
        ballSpeedY = -0.2
    elif (ballHitbox.colliderect(paddle1[2])) or (ballHitbox.colliderect(paddle2[2])):
        ballSpeedX = -ballSpeedX
        ballSpeedY = 0
    elif (ballHitbox.colliderect(paddle1[3])) or (ballHitbox.colliderect(paddle2[3])):
        ballSpeedX = -ballSpeedX
        ballSpeedY = 0.2
    elif (ballHitbox.colliderect(paddle1[4])) or (ballHitbox.colliderect(paddle2[4])):
        ballSpeedX = -ballSpeedX
        ballSpeedY = 0.5
    
    #wall collisions and scoring
    if ballY <= 0 or ballY >= 600:
        ballSpeedY = -ballSpeedY
    if ballX <= 0:
        player_score += 1
        ballX = 400
        ballY = 300
        ballSpeedY = 0
        pygame.time.delay(500)
    elif ballX >= 800:
        AI_score += 1
        ballX = 400
        ballY = 300
        ballSpeedY = 0
        pygame.time.delay(500)
        
    #update background to screen
    screen.fill(black)
    for i in range(30):
        pygame.draw.rect(screen, white, (400, (i * 20) + 5, 5, 10))

    #update paddles to screen
    for i in range(5):
        pygame.draw.rect(screen, white, paddle1[i])
        pygame.draw.rect(screen, white, paddle2[i])

    #text
    text = f"{AI_score}"
    ai_score_txt = font.render(text, True, white)
    text = f"{player_score}"
    player_score_txt = font.render(text, True, white)
    screen.blit(ai_score_txt, (335, 10))
    screen.blit(player_score_txt, (440, 10))
    
    #drawing ball
    if AI_score != 10 and player_score != 10:
        pygame.draw.circle(screen, white, (ballX, ballY), 5)

    #end game
    if AI_score == 10 or player_score == 10:
        while(running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if AI_score == 10:
                endTxt = f"Player 1 Wins"
            else:
                endTxt = f"Player 2 Wins"
            endTxtRend = font.render(endTxt, True, white)
            screen.blit(endTxtRend, (225, 280))
            pygame.display.flip()

    pygame.display.flip()

pygame.quit