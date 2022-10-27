import random
import time

#Variables
gridList = [[0]*16 for i in range(16)]
colorsInGame = [1, 2, 3, 4, 5, 6]
position = PVector(302, 617)
bubbleFlySpeed = 10
currentBubble = []
canShoot = True
gameOver = False
score = 69
rowIndent = False
nextColor = 1



#Flying Bubble class
class FlyingBubble:
    def __init__(self, tempX, tempY, tempSpeedX, tempSpeedY, tempW, val):
        self.x = tempX
        self.y = tempY
        self.speedX = tempSpeedX
        self.speedY = tempSpeedY
        self.w = tempW
        self.directionX = 1
        self.val = val
    
    #Function to detect if flying bubble is out of bounds    
    def OutOfBounds(self):
        global bubbleFlySpeed
        if self.y < (30 + bubbleFlySpeed/2):
            return True

        else:
            return False

    #Function to detect if flying bubble hit stationary bubble
    def Hit(self):
        global gridList
        global bubbleFlySpeed
        # return False
        for row in gridList:
            for statBubble in row:
                if statBubble != 0:
                    distX = self.x - statBubble.x
                    distY = self.y - statBubble.y
                    distance = sqrt((distX*distX) + (distY*distY))
                    
                    if distance <= (30 + bubbleFlySpeed/2):
                        return True
                
        return False

    #Function to bounce off walls
    def ChangeDirection(self):
        if self.x < 27 or self.x > 575: 
            self.directionX *= -1

    #Function to move bubble
    def Move(self):
        self.x += self.speedX * self.directionX
        self.y += self.speedY
    
    #Function to display bubble
    def Display(self):
        ColorAssigner(self.val)
        stroke(1)
        ellipse(self.x, self.y, self.w, self.w)
        
    #Function to teleport bubble to nearest grid point
    def Teleport(self):
        currentBubble.remove(self)

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
    clear()
    
    Start()

#Loop
def draw():
    global canShoot
    global gameOver
    background(255)
    Initialize()
    DrawBubble()
    if mousePressed:
        if canShoot:
            canShoot = False
            FireBubble()
        
    if keyPressed:
        if key == " ":
            canShoot = True
        if key == "w":
            NewRow()
            time.sleep(0.1)
            
    if gameOver:
        GameOverScreen()
        if keyPressed:
            if key == "p":
                gameOver = False
                Start()



#Function to fill the grid at the start of a game
def Start():
    global rowWidth
    global rowIndent

    for row in range(9):
        if rowIndent:
            rowWidth = 47
            rowIndent = False
            
        else:
            rowWidth = 30
            rowIndent = True

        for col in range(16):
            gridList[row][col] = StatBubble(row, col, 35*col+rowWidth, 35*row+30, random.choice(colorsInGame))


    for row in range(9, 16):
        for col in range(16):
            gridList[row][col] = 0

#Function to initialize the game
def Initialize():    
    strokeWeight(10)
    stroke(unhex("ffc1c0ff"))
    fill(255)
    rect(4, 4, 595, 641)
    
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

    for row in gridList:
        for statBubble in row:
            if statBubble != 0:
                ColorAssigner(statBubble.val)
                ellipse(statBubble.x, statBubble.y, 30, 30)

#Function to fire bubble
def FireBubble():
    global currentBubble
    global canShoot
    global nextColor

    val = nextColor
    nextColor = random.choice(colorsInGame)
    xSpeed = 0
    ySpeed = 0
    mx = mouseX
    my = mouseY
    if my < 590 and my >= 10 and mx < 594 and mx >= 10:
        angle = atan2(float(mouseY)-(position.y), float(mouseX)-(position.x))
        xSpeed = cos(angle)
        ySpeed = sin(angle)
        xSpeed *= bubbleFlySpeed
        ySpeed *= bubbleFlySpeed
    
        currentBubble.append(FlyingBubble(position.x, position.y, xSpeed, ySpeed, 30, val))

#Function to draw bubble
def DrawBubble():
    global currentBubble
    global canShoot
    global nextColor

    if canShoot:
        pushMatrix()
        translate(position.x, position.y)
        stroke(1)
        ColorAssigner(nextColor)
        ellipse(0, 0, 30, 30)
        popMatrix()

    for bubble in currentBubble:
        if bubble.Hit():
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
    
    #Checking if player is GameOver
    global gameOver
    for col in range(16):
        if gridList[15][col].val != 0:
            gameOver = True
            break
    
    #Creating new row
    if not gameOver:
        gridList.pop()
        tempRow = [0] * 16
        for col in range(16):
            tempRow[col] = StatBubble(0, col, 35*col+rowWidth, 35*0+30, random.choice(colorsInGame))
            
        gridList.insert(0, tempRow)
    
        if rowIndent:
            rowIndent = False
            
        else:
            rowIndent = True

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

#Function to display the Game Over screen
def GameOverScreen():
    #Code for Game Over screen
    for fade in range(79):
        background(0)
        fill(fade, 0, 0)
        textFont(loadFont("TimesNewRomanPSMT-48.vlw"), 60)
        textAlign(CENTER, CENTER)
        text("YOU DIED", width/2, height/2)
        textFont(loadFont("TimesNewRomanPSMT-48.vlw"), 20)
        textAlign(CENTER, CENTER)
        text("(With a score of " + str(score) + ")", width/2, 400)
