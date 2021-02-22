import random
import time


#Variables
ColorsInGame = [1, 2, 3, 4, 5, 6]
position = PVector(290, 630)
bubbles = []
bubbleFlySpeed = 5
fireSpeed = 1
hit = False
x = 0
y = 0    
ang = 0
bubble = 1

#Making the grid
gridList = [[0]*16 for i in range(16)]



#Setup
def setup():
    size(800, 650)
    smooth()
    clear()
    
    Start()
    Initialize()
    


 
#Loop
def draw():
    global bubble
    background(255)
    Initialize()
    DrawBubble()
    if mousePressed:
        Fire()
        
    if keyPressed:
        if key == " ":
            bubble += 1
        

    
            


#Shoot bubble class
class Bubble:
    def __init__(self, tempX, tempY, tempSpeedX, tempSpeedY, tempW):
        self.x = tempX
        self.y = tempY
        self.w = tempW
        self.speedX = tempSpeedX
        self.speedY = tempSpeedY
        
    def move(self):
        self.x += self.speedX
        self.y += self.speedY
        
    def display(self):
    
        fill(unhex("ffe500e6"))
        stroke(1)
        ellipse(self.x, self.y, self.w, self.w)
        
    
        
        




#Functions


def OuterBubbles():
    pass



def Fire():
    global bubble
    global bubbles
    if bubble > 0:
        bubble -= 1
        xSpeed = 0
        ySpeed = 0
        mx = mouseX
        my = mouseY
        if my < 590 and my >= 10 and mx < 575 and mx >= 10:
            angle = atan2(float(mouseY)-(position.y-15), float(mouseX)-(position.x-15));
            xSpeed = cos(angle)
            ySpeed = sin(angle)
            xSpeed *= bubbleFlySpeed
            ySpeed *= bubbleFlySpeed
        
            
            bubbles.append(Bubble(position.x-15, position.y-15, xSpeed, ySpeed, 30))


#Drawing shoot bubble
def DrawBubble():
    pushMatrix()
    translate(position.x, position.y)
    stroke(1)
    fill(unhex("ffe500e6"))
    circle(-15, -15, 30)
    popMatrix()
    
    for currentBubble in bubbles:
        currentBubble.move()
        currentBubble.display()


#Initializing at the start of a game
def Start():
    for row in range(9):
        for val in range(16):
            gridList[row][val] = random.randint(1,6)
      


def Initialize():
    
    strokeWeight(10)
    stroke(unhex("ffc1c0ff"))
    fill(255)
    rect(4,4,580,640)
    
    strokeWeight(1)
    x = 10
    while x < 580:
        stroke(-(x+590>>1 & 1))
        line(x, 590, x+5, 590)
        x+=6
        
    fill(unhex("ffc1c0ff"))
    strokeWeight(1)
    stroke(unhex("ffc1c0ff"))
    rect(575,0,224,649)
    
    strokeWeight(1.3)    
    stroke(0)
    fill(0)
    for row in range(16):
            for val in range(16):
                if gridList[row][val] == 0:
                    pass
            
                elif gridList[row][val] == 1:
                    #Red = ffef161a
                    fill(unhex("ffef161a"))
                    circle(30*val+30+val*5, 30*row+30+row*5, 30)
                
                elif gridList[row][val] == 2:
                    #Green = ff00da00
                    fill(unhex("ff00da00"))
                    circle(30*val+30+val*5, 30*row+30+row*5, 30)
                    
                elif gridList[row][val] == 3:
                    #Yellow = fffeff00
                    fill(unhex("fffeff00"))
                    circle(30*val+30+val*5, 30*row+30+row*5, 30)
                    
                elif gridList[row][val] == 4:
                    #Purple = ffe500e6
                    fill(unhex("ffe500e6"))
                    circle(30*val+30+val*5, 30*row+30+row*5, 30)
                    
                elif gridList[row][val] == 5:
                    #Dark Blue = ff1e00fd
                    fill(unhex("ff1e00fd"))
                    circle(30*val+30+val*5, 30*row+30+row*5, 30)
                    
                elif gridList[row][val] == 6:
                    #Light Blue = ff02fafa
                    fill(unhex("ff02fafa"))
                    circle(30*val+30+val*5, 30*row+30+row*5, 30)
                
                else:
                    raise Exception("Encountered value " + str(gridList[row][val]) + " while initializing")
    
            
        

            

def NewRow():
    #Checking if player is GameOver
    GameOver = False
    for val in range(16):
        if gridList[15][val] != 0:
            GameOverScreen()
            GameOver = True
            break
    
    if not GameOver:
        gridList.pop()
        tempRow = [0] * 16
        for val in range(16):
            tempRow[val] = random.choice(ColorsInGame)
            
        gridList.insert(0, tempRow)

    


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



def GameOverScreen():
    print("Game Over")
    #Code for Game Over screen
    
            
