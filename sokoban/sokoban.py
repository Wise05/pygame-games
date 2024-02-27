import pygame

pygame.init()

#visual stuff
floorImg = pygame.image.load(r"sokoban\images\soko_ground.png")
wallImg = pygame.image.load(r"sokoban\images\soko_wall.png")
destinationImg = pygame.image.load(r"sokoban\images\soko_destination.png")

def openLevelFile(file):
    i = 0
    map = []
    with open(file) as f:
        for line in f:
            map.append(line.split(","))
            map[i][len(map[i]) -1] = map[i][len(map[i]) - 1][:-1]
            i += 1
    return map

levelFiles = [r'sokoban\levels\level1.txt', r'sokoban\levels\level2.txt', r'sokoban\levels\level3.txt', r'sokoban\levels\level4.txt', r'sokoban\levels\level5.txt']
#levelFiles = [r'sokoban\levels\level5.txt']
levelMap = openLevelFile(levelFiles[0])
levelNum = 0
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
    
    def moveLeft(self):
        self.location[0] -= 1
    def moveRight(self):
        self.location[0] += 1
    def moveUp(self):
        self.location[1] -= 1
    def moveDown(self):
        self.location[1] += 1

crates = []
def findCrates():
    for i in range(30):
        for j in range(40):
            if levelMap[i][j] == 'b':
                crates.append(crate(j, i))
findCrates()

def checkIfCrateHere(location):
    for i in crates:
        if i.location == location:
            return i
    return None
        
def checkIfWall(object, direction):
    if direction == "left":
        return levelMap[object.location[1]][object.location[0] - 1] != 'w'
    if direction == "right":
        return levelMap[object.location[1]][object.location[0] + 1] != 'w'
    if direction == "up":
        return levelMap[object.location[1] - 1][object.location[0]] != 'w'
    if direction == "down":
        return levelMap[object.location[1] + 1][object.location[0]] != 'w'
            
class playerGuy():
    def __init__(self):
        self.playerImg = pygame.image.load(r"sokoban\images\the_MAN.png")
        self.location = [0,0]
        self.keyPressed = None

    def setLocation(self, x, y):
        self.location = [x,y]

    def getLocation(self):
        for i in range(30):
            for j in range(40):
                if levelMap[i][j] == 'p':
                    player.setLocation(j,i)

    def moveLeft(self):
        if checkIfWall(self, "left"):
            thisCrate = checkIfCrateHere([player.location[0] - 1, player.location[1]])
            if thisCrate != None:
                if checkIfWall(thisCrate, "left") and checkIfCrateHere([thisCrate.location[0] - 1, thisCrate.location[1]]) == None:
                    thisCrate.moveLeft()
                else:
                    self.location[0] += 1
            self.location[0] -= 1
    def moveRight(self):
        if checkIfWall(self, "right"):
            thisCrate = checkIfCrateHere([player.location[0] + 1, player.location[1]])
            if thisCrate != None:
                if checkIfWall(thisCrate, "right") and checkIfCrateHere([thisCrate.location[0] + 1, thisCrate.location[1]]) == None:
                    thisCrate.moveRight()
                else:
                    self.location[0] -= 1
            self.location[0] += 1
    def moveUp(self):
        if checkIfWall(self, "up"):
            thisCrate = checkIfCrateHere([player.location[0], player.location[1] - 1])
            if thisCrate != None:
                if checkIfWall(thisCrate, "up") and checkIfCrateHere([thisCrate.location[0], thisCrate.location[1] - 1]) == None:
                    thisCrate.moveUp()
                else:
                    self.location[1] += 1
            self.location[1] -= 1
    def moveDown(self):
        if checkIfWall(self, "down"):
            thisCrate = checkIfCrateHere([player.location[0], player.location[1] + 1])
            if thisCrate != None:
                if checkIfWall(thisCrate, "down") and checkIfCrateHere([thisCrate.location[0], thisCrate.location[1] + 1]) == None:
                    thisCrate.moveDown()
                else:
                    self.location[1] -= 1
            self.location[1] += 1
             
    def movement(self):
        if self.keyPressed is None:
            if keys[pygame.K_LEFT]:
                self.moveLeft()
                self.keyPressed = pygame.K_LEFT
            elif keys[pygame.K_RIGHT]:
                self.moveRight()
                self.keyPressed = pygame.K_RIGHT
            elif keys[pygame.K_UP]:
                self.moveUp()
                self.keyPressed = pygame.K_UP
            elif keys[pygame.K_DOWN]:
                self.moveDown()
                self.keyPressed = pygame.K_DOWN
        else:
            if not keys[self.keyPressed]:
                self.keyPressed = None
            
player = playerGuy()
player.getLocation()

destinations = []
def findDestinations():
    for i in range(30):
        for j in range(40):
            if levelMap[i][j] == 'd':
                destinations.append([j, i])
findDestinations()

def checkWin(destinations, crates):
    count = 0
    for i in range(len(destinations)):
        for j in range(len(crates)):
            if destinations[i] == crates[j].location:
                count += 1
    if count == len(destinations):
        return True
    return False

def boxDimensions(x, y):
    return (x * 20, y * 20, 20, 20)

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    player.movement()
    
    if checkWin(destinations, crates):
        levelNum += 1
        if levelNum < len(levelFiles):
            levelMap = openLevelFile(levelFiles[levelNum])
            destinations = []
            crates = []
            findCrates()
            findDestinations()
            player.getLocation()
        else:
            print("win!")
            
    #resets level
    if keys[pygame.K_r]:
        destinations = []
        crates = []
        findCrates()
        findDestinations()
        player.getLocation()

    #update display
    for i in range(30):
        for j in range(40):
            if levelMap[i][j] == 'w':
                screen.blit(wallImg, boxDimensions(j,i))
            elif levelMap[i][j] == 'd':
                screen.blit(destinationImg, boxDimensions(j,i))
            elif levelMap[i][j] == 'b' or levelMap[i][j] == 'p' or levelMap[i][j] == ' ':
                screen.blit(floorImg, boxDimensions(j,i))
    screen.blit(player.playerImg, boxDimensions(player.location[0], player.location[1]))
    for i in crates:
        screen.blit(i.crateImg, boxDimensions(i.location[0], i.location[1]))

    pygame.display.flip()

pygame.quit