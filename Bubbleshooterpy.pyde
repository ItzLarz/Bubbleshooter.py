# Dependencies
import random
import time


# Variables
gridList = [[0]*16 for i in range(16)]
colorsInGame = [1, 2, 3, 4, 5, 6]
startPosition = PVector(302, 617)
bubbleFlySpeed = 6
currentBubble = []
canShoot = True
gameOver = False
score = 69
rowIndent = False
colWidth = 30
nextColor = 1
bubbleSize = 30
spacing = 4
iter = 0


# Flying Bubble class
class FlyingBubble:
    def __init__(self, x, y, xSlow, ySlow, xSpeed, ySpeed, size, val):
        self.x = x
        self.y = y
        self.xSlow = xSlow
        self.ySlow = ySlow
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.size = size
        self.val = val
        self.dir = 1

    # Function to detect if flying bubble collided with stationary bubble
    def Collision(self, slow):
        global bubbleFlySpeed
        global bubbleSize

        if not slow:
            xComp = self.x
            yComp = self.y
        elif slow:
            xComp = self.xSlow
            yComp = self.ySlow


        for row in gridList:
            for statBubble in row:
                if statBubble != 0:
                    distX = xComp - statBubble.x
                    distY = yComp - statBubble.y
                    distance = sqrt((distX**2) + (distY**2))

                    if distance <= (bubbleSize-5):  # FIX COLLISION
                        return True

        return False
        
    # Function to bounce off walls
    def ChangeDirection(self):
        if self.x < 26 or self.x > 563:  # FIX BOUNDS
            self.dir *= -1

    # Function to move bubble
    def Move(self):
        self.xSlow = self.x
        self.ySlow = self.y
        self.x += self.xSpeed * self.dir
        self.y += self.ySpeed

    # Function to slowly move the bubble after a collision detection
    def SlowMove(self):
        global bubbleFlySpeed

        self.xSlow += self.xSpeed/bubbleFlySpeed * self.dir
        self.ySlow += self.ySpeed/bubbleFlySpeed

        if self.Collision(True):
            self.Teleport()

        else:
            self.SlowMove()

    # Function to display bubble
    def Display(self):
        ColorAssigner(self.val)
        stroke(1)
        ellipse(self.xSlow, self.ySlow, self.size, self.size)

    # Function to teleport bubble to nearest grid point
    def Teleport(self):
        global rowIndent
        global colWidth

        currentBubble.remove(self)

        rowNew = int(round((self.ySlow - colWidth) / (bubbleSize+4)))
        if rowNew > 15:
            rowNew = 15
        elif rowNew < 0:
            rowNew = 0


        if rowIndent:
            if rowNew % 2 == 0:
                rowWidth = 47
            else:
                rowWidth = 30

        else:
            if rowNew % 2 == 0:
                rowWidth = 30
            else:
                rowWidth = 47

        colNew = int(round((self.xSlow - rowWidth) / (bubbleSize+4)))
        if colNew > 15:
            colNew = 15
        elif colNew < 0:
            colNew = 0

        print((self.xSlow - rowWidth) / (bubbleSize+4),
              (self.ySlow - colWidth) / (bubbleSize+4))
        print(colNew, rowNew)
        gridList[rowNew][colNew] = StatBubble(
            rowNew, colNew, (bubbleSize+4)*colNew+rowWidth, (bubbleSize+4)*rowNew+colWidth, self.val)
        
        PopBubbles(gridList[rowNew][colNew])
        

# Stationary Bubble class
class StatBubble:
    def __init__(self, row, col, x, y, val):
        self.row = row
        self.col = col
        self.x = x
        self.y = y
        self.val = val

    def CheckNeighbours(self): # FIX
        global gridList
        global rowIndent

        neighbours = []

        if self.row > 0:
            neighbours.append(gridList[self.row-1][self.col])       # Above

        if self.row < 15:
            neighbours.append(gridList[self.row+1][self.col])       # Below

        if self.col > 0:
            neighbours.append(gridList[self.row][self.col-1])       # Left

            if (int(rowIndent == True) + self.row) % 2 == 0:        # Row Not Indented
                neighbours.append(gridList[self.row-1][self.col-1]) # Left Above
                neighbours.append(gridList[self.row+1][self.col-1]) # Left Below 

        if self.col < 15:
            neighbours.append(gridList[self.row][self.col+1])       # Right

            if (int(rowIndent == True) + self.row) % 2 != 0:        # Row Indented
                neighbours.append(gridList[self.row-1][self.col+1]) # Right Above
                neighbours.append(gridList[self.row+1][self.col+1]) # Right Below

        return neighbours




# Setup
def setup():
    size(800, 650)
    ellipseMode(CENTER)
    smooth()
    frameRate(600)
    clear()

    Start()

# Loop
def draw():
    global canShoot
    global gameOver
    global iter
    global rowIndent

    # iter += 1
    # if (iter % 30 == 0):
    #     print(int(frameRate))

    if not gameOver:
        background(unhex("ffc1c0ff"))
        Initialize()
        DrawBubble()
        # Checking if player is         FIX: Needs to be placed somewhere else (def CheckGameOver?)
        for col in range(16):
            if gridList[15][col] != 0:
                gameOver = True
                canShoot = False
                # GameOverScreen()
                break

    if mousePressed:
        if canShoot:
            FireBubble()

    if keyPressed:
        if key == " ":
            canShoot = True
        if key == "w":
            NewRow()
            time.sleep(0.1)
        if key == "r":
            gameOver = False
            canShoot = True
            Start()


# Function to fill the grid at the start of a game
def Start():
    global colWidth
    global rowIndent
    global bubbleSize

    for row in range(9):
        if rowIndent:
            rowWidth = 47
            rowIndent = False

        else:
            rowWidth = 30
            rowIndent = True

        for col in range(16):
            gridList[row][col] = StatBubble(row, col, (bubbleSize+4)*col+rowWidth,
                                            (bubbleSize+4)*row+colWidth, random.choice(colorsInGame))

    for row in range(9, 16):
        for col in range(16):
            gridList[row][col] = 0

# Function to initialize the game
def Initialize():
    global bubbleSize
    global rowIndent

    strokeWeight(10)
    stroke(unhex("ffc1c0ff"))
    fill(255)
    rect(4, 4, 580, 641)

    strokeWeight(1)
    x = 10
    while x < 580:
        stroke(-(x+590 >> 1 & 1))
        line(x, 590, x+5, 590)
        x += 6

    fill(unhex("ffc1c0ff"))
    strokeWeight(1)
    stroke(unhex("ffc1c0ff"))
    rect(595, 0, 224, 649)

    strokeWeight(1.3)
    stroke(0)
    fill(0)

    for i, row in enumerate(gridList):
        if rowIndent:
            rowWidth = 47
            rowIndent = False

        else:
            rowWidth = 30
            rowIndent = True

        for j, statBubble in enumerate(row):
            if statBubble != 0:
                statBubble.row = i
                statBubble.col = j
                statBubble.x = (bubbleSize+4)*j+rowWidth
                statBubble.y = (bubbleSize+4)*i+colWidth
                stroke(1)
                ColorAssigner(statBubble.val)
                ellipse(statBubble.x, statBubble.y, bubbleSize, bubbleSize)
                fill(0)
                ellipse(statBubble.x, statBubble.y, 1, 1)

# Function to fire bubble
def FireBubble():
    global currentBubble
    global canShoot
    global nextColor
    global startPosition
    global bubbleSize
    global bubbleFlySpeed

    mx = mouseX
    my = mouseY
    val = nextColor
    xSpeed = 0
    ySpeed = 0
    if my < 590 and my >= 10 and mx < 594 and mx >= 10:
        canShoot = False
        angle = atan2(float(mouseY)-(startPosition.y),
                      float(mouseX)-(startPosition.x))
        xSpeed = cos(angle)
        ySpeed = sin(angle)
        xSpeed *= bubbleFlySpeed
        ySpeed *= bubbleFlySpeed

        currentBubble.append(FlyingBubble(
            startPosition.x, startPosition.y, startPosition.x, startPosition.y, xSpeed, ySpeed, bubbleSize, val))
        nextColor = random.choice(colorsInGame)

# Function to draw bubble
def DrawBubble():
    global currentBubble
    global canShoot
    global nextColor
    global startPosition
    global bubbleSize

    if canShoot:
        pushMatrix()
        translate(startPosition.x, startPosition.y)
        stroke(1)
        ColorAssigner(nextColor)
        ellipse(0, 0, bubbleSize, bubbleSize)
        fill(0)
        ellipse(0, 0, 1, 1)
        popMatrix()

    for bubble in currentBubble:
        if bubble.Collision(False):
            bubble.SlowMove()
            canShoot = True

        else:
            bubble.ChangeDirection()
            bubble.Move()
            bubble.Display()


def PopBubbles(firedBubble): # FIX
    sameColor = set()
    for bubble in firedBubble.CheckNeighbours():
        print(bubble)
        if bubble != 0:
            if bubble.val == firedBubble.val:
                sameColor.add(bubble)
    
    length = 0
    while (len(sameColor) > length):
        length = len(sameColor)
        for bubble in sameColor:
            if bubble.val == firedBubble.val:
                sameColor.add(bubble)
                for neighbour in bubble.CheckNeighbours():
                    if neighbour != 0:
                        if neighbour.val == firedBubble.val:
                            sameColor.add(neighbour)

    if length > 2:
        for bubble in sameColor:
            gridList[bubble.row][bubble.col] = 0


    


# Function to create new row in the grid
def NewRow():
    global rowIndent
    global colWidth
    global bubbleSize
    global gameOver

    # Creating new row
    if not gameOver:
        # Changing rowWidth if it should be indented
        if rowIndent:
            rowWidth = 47
            rowIndent = False

        else:
            rowWidth = 30
            rowIndent = True

        gridList.pop()
        tempRow = [0] * 16
        for col in range(16):
            tempRow[col] = StatBubble(
                0, col, (bubbleSize+4)*col+rowWidth, colWidth, random.choice(colorsInGame))

        gridList.insert(0, tempRow)

# Function to check which colors are still in the game
def CheckColorsInGame():
    currentColorsInGame = []

    for row in range(16):
        for col in range(16):
            if gridList[row][col].val == 0:
                pass

            elif not currentColorsInGame.contains(gridList[row][col].val):
                currentColorsInGame.append(gridList[row][col].val)

    colorsInGame.clear()
    colorsInGame.extend(currentColorsInGame)

# Function to display the Game Over screen
def GameOverScreen():
    # Code for Game Over screen

    background(0)
    fill(79, 0, 0)
    textFont(loadFont("TimesNewRomanPSMT-48.vlw"), 60)
    textAlign(CENTER, CENTER)
    text("YOU DIED", width/2, height/2)
    textFont(loadFont("TimesNewRomanPSMT-48.vlw"), 20)
    textAlign(CENTER, CENTER)
    text("(With a score of " + str(score) + ")", width/2, 400)

# Function to decode values into hexes
def ColorAssigner(value):
    if value == 0:
        pass

    elif value == 1:
        # Red = ffef161a
        fill(unhex("ffef161a"))

    elif value == 2:
        # Green = ff00da00
        fill(unhex("ff00da00"))

    elif value == 3:
        # Yellow = fffeff00
        fill(unhex("fffeff00"))

    elif value == 4:
        # Purple = ffe500e6
        fill(unhex("ffe500e6"))

    elif value == 5:
        # Dark Blue = ff1e00fd
        fill(unhex("ff1e00fd"))

    elif value == 6:
        # Light Blue = ff02fafa
        fill(unhex("ff02fafa"))

    else:
        raise Exception("Encountered value " +
                        str(value) + " while initializing")
