import pygame

pygame.init()

#colors and visual stuff
floorImg = pygame.image.load(r"sokoban\images\soko_ground.png")
wallImg = pygame.image.load(r"sokoban\images\soko_wall.png")
destinationImg = pygame.image.load(r"sokoban\images\soko_destination.png")
playerImg = pygame.image.load(r"sokoban\images\the_MAN.png")
boxImg = pygame.image.load(r"sokoban\images\the_BOX.png")

#levels
def openLevelFile(file):
    i = 0
    map = []
    with open(file) as f:
        for line in f:
            map.append(line.split(","))
            map[i][len(map[i]) -1] = map[i][len(map[i]) - 1][:-1]
            i += 1
    return map

levelFiles = [r'sokoban\levels\level1.txt']
levelMap = openLevelFile(levelFiles[0])
'''
Key for file
o = nothing or ground
w = wall
p = player
d = destination
b = box
'''

#display 
displayWidth = 800
displayHeight = 600
screen = pygame.display.set_mode((displayWidth, displayHeight))
caption = pygame.display.set_caption("Sokoban")
pygame.display.set_icon(boxImg)

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #update display
    for i in range(30):
        for j in range(40):
            if levelMap[i][j] == 'w':
                screen.blit(wallImg, (j * 20, i * 20, 20, 20))
            elif levelMap[i][j] == 'd':
                screen.blit(destinationImg, (j * 20, i * 20, 20, 20))
            elif levelMap[i][j] == 'b':
                screen.blit(boxImg, (j * 20, i * 20, 20, 20))
            elif levelMap[i][j] == 'p':
                screen.blit(floorImg, (j * 20, i * 20, 20, 20))
                screen.blit(playerImg, (j * 20, i * 20, 20, 20))
            elif levelMap[i][j] == 'o':
                screen.blit(floorImg, (j * 20, i * 20, 20, 20))

    pygame.display.flip()

pygame.quit