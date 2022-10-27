#Dependencies
import random
import time


#Variables
gridList = [[0]*16 for i in range(16)]
colorsInGame = [1, 2, 3, 4, 5, 6]
startPosition = PVector(302, 617)
bubbleFlySpeed = 1
currentBubble = []
canShoot = True
gameOver = False
score = 69
rowIndent = False
colWidth = 30
nextColor = 1
bubbleSize = 30


#Flying Bubble class
class FlyingBubble:
    def __init__(self, x, y, xSpeed, ySpeed, size, val):
        self.x = x
        self.y = y
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.size = size
        self.val = val
        self.dir = 1
    
    #Function to detect if flying bubble is out of bounds    
    def OutOfBounds(self):
        global bubbleFlySpeed
        global bubbleSize

        if self.y < (bubbleSize + bubbleFlySpeed/2):
            return True

        else:
            return False

    #Function to detect if flying bubble collided with stationary bubble
    def Collision(self):
        # return False
        global bubbleFlySpeed
        global bubbleSize
        
        for row in gridList:
            for statBubble in row:
                if statBubble != 0:
                    distX = self.x - statBubble.x
                    distY = self.y - statBubble.y
                    distance = sqrt((distX*distX) + (distY*distY))
                    
                    if distance <= (bubbleSize + bubbleFlySpeed):
                        return True
                
        return False

    #Function to bounce off walls
    def ChangeDirection(self):
        if self.x < 26 or self.x > 570: #26, 563 for speed=1
            self.dir *= -1
  
    #Function to move bubble
    def Move(self):
        self.x += self.xSpeed * self.dir
        self.y += self.ySpeed
    
    #Function to display bubble
    def Display(self):
        ColorAssigner(self.val)
        stroke(1)
        ellipse(self.x, self.y, self.size, self.size)
        
    #Function to teleport bubble to nearest grid point
    def Teleport(self):
        global rowIndent
        global colWidth

        if rowIndent:
            rowWidth = 47
                
        else:
            rowWidth = 30

        currentBubble.remove(self)
        colNew = int(round((self.x - rowWidth) / (bubbleSize+bubbleSize/7)))
        rowNew = int(round((self.y - colWidth) / (bubbleSize+bubbleSize/7)))
        print(colNew, rowNew)
        gridList[rowNew][colNew] = StatBubble(rowNew, colNew, (bubbleSize+bubbleSize/7)*colNew+rowWidth, (bubbleSize+bubbleSize/7)*rowNew+colWidth, self.val)
        
        
#Stationary Bubble class
class StatBubble:
    def __init__(self, row, col, x, y, val):
        self.row = row
        self.col = col
        self.x = x
        self.y = y
        self.val = val

#Setup
def setup():
    size(800, 650)
    ellipseMode(CENTER)
    smooth()
    frameRate(600)
    clear()
    
    Start()

#Loop
def draw():
    global canShoot
    global gameOver

    print(frameRate)

    if not gameOver:
        background(unhex("ffc1c0ff"))
        Initialize()
        DrawBubble()
        #Checking if player is GameOver
        for col in range(16):
            if gridList[15][col] != 0:
                gameOver = True
                canShoot = False
                GameOverScreen()
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


#Function to fill the grid at the start of a game
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
            gridList[row][col] = StatBubble(row, col, (bubbleSize+bubbleSize/7)*col+rowWidth, (bubbleSize+bubbleSize/7)*row+colWidth, random.choice(colorsInGame))


    for row in range(9, 16):
        for col in range(16):
            gridList[row][col] = 0

#Function to initialize the game
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
        stroke(-(x+590>>1 & 1))
        line(x, 590, x+5, 590)
        x+=6
        
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
                statBubble.x = (bubbleSize+bubbleSize/7)*j+rowWidth
                statBubble.y = (bubbleSize+bubbleSize/7)*i+colWidth
                stroke(1)
                ColorAssigner(statBubble.val)
                ellipse(statBubble.x, statBubble.y, bubbleSize, bubbleSize)

#Function to fire bubble
def FireBubble():
    global currentBubble
    global canShoot
    global nextColor
    global startPosition
    global bubbleSize

    mx = mouseX
    my = mouseY
    val = nextColor
    xSpeed = 0
    ySpeed = 0
    if my < 590 and my >= 10 and mx < 594 and mx >= 10:
        canShoot = False
        angle = atan2(float(mouseY)-(startPosition.y), float(mouseX)-(startPosition.x))
        xSpeed = cos(angle)
        ySpeed = sin(angle)
        xSpeed *= bubbleFlySpeed
        ySpeed *= bubbleFlySpeed
    
        currentBubble.append(FlyingBubble(startPosition.x, startPosition.y, xSpeed, ySpeed, bubbleSize, val))
        nextColor = random.choice(colorsInGame)

#Function to draw bubble
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
        popMatrix()

    for bubble in currentBubble:
        if bubble.Collision():
            bubble.Teleport()
            canShoot = True

        elif bubble.OutOfBounds():
            bubble.Teleport()
            canShoot = True
    
        else:
            bubble.ChangeDirection()
            bubble.Move()
            bubble.Display()

#Function to create new row in the grid
def NewRow():
    global rowIndent
    global colWidth
    global bubbleSize
    global gameOver
    
    #Creating new row
    if not gameOver:
        #Changing rowWidth if it should be indented
        if rowIndent:
            rowWidth = 47
            rowIndent = False
                
        else:
            rowWidth = 30
            rowIndent = True
        
        gridList.pop()
        tempRow = [0] * 16
        for col in range(16):
            tempRow[col] = StatBubble(0, col, (bubbleSize+bubbleSize/7)*col+rowWidth, colWidth, random.choice(colorsInGame))
            
        gridList.insert(0, tempRow)

#Function to check which colors are still in the game
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

#Function to display the Game Over screen
def GameOverScreen():
    #Code for Game Over screen
    
    background(0)
    fill(79, 0, 0)
    textFont(loadFont("TimesNewRomanPSMT-48.vlw"), 60)
    textAlign(CENTER, CENTER)
    text("YOU DIED", width/2, height/2)
    textFont(loadFont("TimesNewRomanPSMT-48.vlw"), 20)
    textAlign(CENTER, CENTER)
    text("(With a score of " + str(score) + ")", width/2, 400)

#Function to decode values into hexes
def ColorAssigner(value):
    if value == 0:
        pass

    elif value == 1:
        #Red = ffef161a
        fill(unhex("ffef161a"))

    elif value == 2:
        #Green = ff00da00
        fill(unhex("ff00da00"))
        
    elif value == 3:
        #Yellow = fffeff00
        fill(unhex("fffeff00"))
        
    elif value == 4:
        #Purple = ffe500e6
        fill(unhex("ffe500e6"))
        
    elif value == 5:
        #Dark Blue = ff1e00fd
        fill(unhex("ff1e00fd"))
        
    elif value == 6:
        #Light Blue = ff02fafa
        fill(unhex("ff02fafa"))

    else:
        raise Exception("Encountered value " + str(value) + " while initializing")
