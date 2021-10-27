import random
import time


#Variables
ColorsInGame = [1, 2, 3, 4, 5, 6]
position = PVector(302, 617)
bubbles = []
bubbleFlySpeed = 10
bubble = 1
gameOver = False
score = 69
rowIndent = False

#Making the grid
gridList = [[0]*16 for i in range(16)]



#Setup
def setup():
    size(800, 650)
    smooth()
    clear()
    
    Start()
    

 
#Loop
def draw():
    global bubble
    global gameOver
    background(255)
    Initialize()
    DrawBubble()
    print(bubbles)
    if mousePressed:
        FireBubble()
        
    if keyPressed:
        if key == " ":
            bubble += 1
        if key == "w":
            NewRow()
            time.sleep(0.1)
            
    if gameOver:
        GameOverScreen()
        if keyPressed:
            if key == "p":
                gameOver = False
                Start()





#Bubble class
class Bubble:
    def __init__(self, tempX, tempY, tempSpeedX, tempSpeedY, tempW):
        self.x = tempX
        self.y = tempY
        self.w = tempW
        self.speedX = tempSpeedX
        self.speedY = tempSpeedY
        self.directionX = 1
    
    
    
    #Function to detect if bubble is out of bounds    
    def OutOfBounds(self):
        if self.y < 15:
            return True
    
    
    
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
        fill(unhex("ffe500e6"))
        stroke(1)
        ellipse(self.x, self.y, self.w, self.w)
        
    





#Functions


#Function to fill the grid at the start of a game
def Start():
    for row in range(9):
        for val in range(16):
            gridList[row][val] = random.randint(1, 6)
            
    for row in range(9, len(gridList)):
        for val in range(16):
            gridList[row][val] = 0
      
      

#Function to initialize the game
def Initialize():
    global rowIndent
    
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
    for row in range(16):
        
        if rowIndent:
            global rowWidth
            rowWidth = 47
            rowIndent = False
            
        else:
            global rowWidth
            rowWidth = 30
            rowIndent = True
        
        
        for val in range(16):
            if gridList[row][val] == 0:
                pass
        
            elif gridList[row][val] == 1:
                #Red = ffef161a
                fill(unhex("ffef161a"))
                circle(35*val+rowWidth, 35*row+30, 30)
            
            elif gridList[row][val] == 2:
                #Green = ff00da00
                fill(unhex("ff00da00"))
                circle(35*val+rowWidth, 35*row+30, 30)
                
            elif gridList[row][val] == 3:
                #Yellow = fffeff00
                fill(unhex("fffeff00"))
                circle(35*val+rowWidth, 35*row+30, 30)
                
            elif gridList[row][val] == 4:
                #Purple = ffe500e6
                fill(unhex("ffe500e6"))
                circle(35*val+rowWidth, 35*row+30, 30)
                
            elif gridList[row][val] == 5:
                #Dark Blue = ff1e00fd
                fill(unhex("ff1e00fd"))
                circle(35*val+rowWidth, 35*row+30, 30)
                
            elif gridList[row][val] == 6:
                #Light Blue = ff02fafa
                fill(unhex("ff02fafa"))
                circle(35*val+rowWidth, 35*row+30, 30)
            
            else:
                raise Exception("Encountered value " + str(gridList[row][val]) + " while initializing")
    



#Function to fire bubble
def FireBubble():
    global bubble
    global bubbles
    xSpeed = 0
    ySpeed = 0
    mx = mouseX
    my = mouseY
    if my < 590 and my >= 10 and mx < 594 and mx >= 10:
        if bubble > 0:
            bubble -= 1
            angle = atan2(float(mouseY)-(position.y), float(mouseX)-(position.x));
            xSpeed = cos(angle)
            ySpeed = sin(angle)
            xSpeed *= bubbleFlySpeed
            ySpeed *= bubbleFlySpeed
        
            
            bubbles.append(Bubble(position.x, position.y, xSpeed, ySpeed, 30))



#Function to draw bubble
def DrawBubble():
    pushMatrix()
    translate(position.x, position.y)
    stroke(1)
    fill(unhex("ffe500e6"))
    circle(0, 0, 30)
    popMatrix()
    
    for currentBubble in bubbles:
        if currentBubble.OutOfBounds():
            bubbles.remove(currentBubble)
        
        else:
            currentBubble.ChangeDirection()
            currentBubble.Move()
            currentBubble.Display()
        


#Function to detect collision
def Collision(x1, y1, x2, y2):
    if val != 0:
        distX = x1 - x2
        distY = y1 - y2
        distance = sqrt((distX*distX) + (distY*distY))
        
        if distance <= 50:
            return True
        
        else:
            return False
        


#Function to create new row in the grid
def NewRow():
    global rowIndent
    
    #Checking if player is GameOver
    global gameOver
    for val in range(16):
        if gridList[15][val] != 0:
            gameOver = True
            break
    
    #Creating new row
    if not gameOver:
        gridList.pop()
        tempRow = [0] * 16
        for val in range(16):
            tempRow[val] = random.choice(ColorsInGame)
            
        gridList.insert(0, tempRow)
    
        if rowIndent:
            rowIndent = False
            
        else:
            rowIndent = True



#Function to check which colors are still in the game
def CheckColorsInGame():
    CurrentColorsInGame = []
    
    for row in range(16):
        for val in range(16):
            if gridList[row][val] == 0:
                pass

            elif not CurrentColorsInGame.contains(gridList[row][val]):
                CurrentColorsInGame.append(gridList[row][val])
        
        ColorsInGame.clear()
        ColorsInGame.extend(CurrentColorsInGame)



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
