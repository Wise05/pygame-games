import pygame
import time

pygame.init()

#visual stuff
floorImg = pygame.image.load(r"sokoban\images\soko_ground.png")
wallImg = pygame.image.load(r"sokoban\images\soko_wall.png")
destinationImg = pygame.image.load(r"sokoban\images\soko_destination.png")

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
Key for file symbols
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
pygame.display.set_icon(wallImg)

class crate(): 
    def __init__(self, x, y):
        self.crateImg = pygame.image.load(r"sokoban\images\the_BOX.png")
        self.location = [x,y]
    
    def setLocation(self, x, y):
        self.location = [x,y]
    
    def moveLeft(self):
        if levelMap[self.location[1]][self.location[0] - 1] != 'w':
            self.location[0] -= 1
    def moveRight(self):
        if levelMap[self.location[1]][self.location[0] + 1] != 'w':
            self.location[0] += 1
    def moveUp(self):
        if levelMap[self.location[1] - 1][self.location[0]] != 'w':
            self.location[1] -= 1
    def moveDown(self):
        if levelMap[self.location[1] + 1][self.location[0]] != 'w':
            self.location[1] += 1

crates = []
for i in range(30):
    for j in range(40):
        if levelMap[i][j] == 'b':
            crates.append(crate(j, i))
            
class playerGuy():
    def __init__(self):
        self.playerImg = pygame.image.load(r"sokoban\images\the_MAN.png")
        self.location = [0,0]

    def setLocation(self, x, y):
        self.location = [x,y]

    def getLocation(self):
        for i in range(30):
            for j in range(40):
                if levelMap[i][j] == 'p':
                    player.setLocation(j,i)

    def moveLeft(self):
        if levelMap[self.location[1]][self.location[0] - 1] != 'w':
            self.location[0] -= 1
    def moveRight(self):
        if levelMap[self.location[1]][self.location[0] + 1] != 'w':
            self.location[0] += 1
    def moveUp(self):
        if levelMap[self.location[1] - 1][self.location[0]] != 'w':
            self.location[1] -= 1
    def moveDown(self):
        if levelMap[self.location[1] + 1][self.location[0]] != 'w':
            self.location[1] += 1
    
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.moveLeft()
            time.sleep(0.1)
        elif keys[pygame.K_RIGHT]:
            self.moveRight()
            time.sleep(0.1)
        elif keys[pygame.K_UP]:
            self.moveUp()
            time.sleep(0.1)
        elif keys[pygame.K_DOWN]:
            self.moveDown()
            time.sleep(0.1)
            
player = playerGuy()
player.getLocation()

def boxDimensions(x, y):
    return (x * 20, y * 20, 20, 20)

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player.movement()

    #update display
    for i in range(30):
        for j in range(40):
            if levelMap[i][j] == 'w':
                screen.blit(wallImg, boxDimensions(j,i))
            elif levelMap[i][j] == 'd':
                screen.blit(destinationImg, boxDimensions(j,i))
            elif levelMap[i][j] == 'b' or levelMap[i][j] == 'p' or levelMap[i][j] == 'o':
                screen.blit(floorImg, boxDimensions(j,i))
    screen.blit(player.playerImg, boxDimensions(player.location[0], player.location[1]))
    for i in crates:
        screen.blit(i.crateImg, boxDimensions(i.location[0], i.location[1]))

    pygame.display.flip()

pygame.quit