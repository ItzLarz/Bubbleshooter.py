import random
import time

#Classes
class Grid:
    #Making the grid
    gridList = [[0]*16 for i in range(17)]
    
    #Checking if the user is Game Over
    def GameOverCheck():
        GameOver = False
        for val in Grid.gridList[16]:
            if val != 0:
                GameOver = True
                
        return GameOver
            
#Variables
ColorsInGame = [1, 2, 3, 4, 5, 6]



#Setup
def setup():
    size(800, 650)
    
    noSmooth()
    clear()
    
    strokeWeight(10)
    stroke(unhex("ffc1c0ff"))
    rect(5,5,580,640)
    
    fill(unhex("ffc1c0ff"))
    strokeWeight(1)
    stroke(unhex("ffc1c0ff"))
    rect(580,0,219,649)
    
    # y = 0
    # x = 0
    # while y < height:
    #     while x < width:
    #         stroke(-(x+y>>1 & 1))
    #         line(x+59, y, x+5, y)
    #         x += 6
            
    #     y += 2
    x = 10
    while x < 580:
        stroke(-(x+590>>1 & 1))
        line(x, 590, x+5, 590)
        x+=6
    
    
    stroke(0)
    Initialize()
    
    
                
#Loop
def draw():
  if keyPressed == True:
    NewRow()
    time.sleep(0.15)
    

    

#nice

#Functions


#Initializing at the start of a game
def Initialize():
    for row in range(9):
        for val in range(16):
            Grid.gridList[row][val] = random.randint(1,6)
      
                  
    #Code for initializing squares
    for row in range(9):
        for val in range(16):
            if Grid.gridList[row][val] == 1:
                #Red = ffef161a
                fill(unhex("ffef161a"))
                square(30*val+15+val*5, 30*row+15+row*5, 30)
            
            elif Grid.gridList[row][val] == 2:
                #Green = ff00da00
                fill(unhex("ff00da00"))
                square(30*val+15+val*5, 30*row+15+row*5, 30)
                
            elif Grid.gridList[row][val] == 3:
                #Yellow = fffeff00
                fill(unhex("fffeff00"))
                square(30*val+15+val*5, 30*row+15+row*5, 30)
                
            elif Grid.gridList[row][val] == 4:
                #Purple = ffe500e6
                fill(unhex("ffe500e6"))
                square(30*val+15+val*5, 30*row+15+row*5, 30)
                
            elif Grid.gridList[row][val] == 5:
                #Dark Blue = ff1e00fd
                fill(unhex("ff1e00fd"))
                square(30*val+15+val*5, 30*row+15+row*5, 30)
                
            elif Grid.gridList[row][val] == 6:
                #Light Blue = ff02fafa
                fill(unhex("ff02fafa"))
                square(30*val+15+val*5, 30*row+15+row*5, 30)
            
            else:
                raise Exception("Encountered value " + str(Grid.gridList[row][val]) + " while initializing")
            
                                    
    
            

def NewRow():
    #Checking if player is GameOver
     GameOver = False
     for val in range(16):
         if Grid.gridList[15][val] != 0:
             GameOverScreen()
             GameOver = True
             break
    
    if not GameOver:
        Grid.gridList.pop()
        tempRow = [0] * 16
        for val in range(16):
            tempRow[val] = random.choice(ColorsInGame)
            
        Grid.gridList.insert(0, tempRow)
        
    
        #Code for initializing squares
        
        for row in range(17):
            for val in range(16):
                if Grid.gridList[row][val] == 0:
                    pass
            
                elif Grid.gridList[row][val] == 1:
                    #Red = ffef161a
                    fill(unhex("ffef161a"))
                    square(30*val+15+val*5, 30*row+15+row*5, 30)
                
                elif Grid.gridList[row][val] == 2:
                    #Green = ff00da00
                    fill(unhex("ff00da00"))
                    square(30*val+15+val*5, 30*row+15+row*5, 30)
                    
                elif Grid.gridList[row][val] == 3:
                    #Yellow = fffeff00
                    fill(unhex("fffeff00"))
                    square(30*val+15+val*5, 30*row+15+row*5, 30)
                    
                elif Grid.gridList[row][val] == 4:
                    #Purple = ffe500e6
                    fill(unhex("ffe500e6"))
                    square(30*val+15+val*5, 30*row+15+row*5, 30)
                    
                elif Grid.gridList[row][val] == 5:
                    #Dark Blue = ff1e00fd
                    fill(unhex("ff1e00fd"))
                    square(30*val+15+val*5, 30*row+15+row*5, 30)
                    
                elif Grid.gridList[row][val] == 6:
                    #Light Blue = ff02fafa
                    fill(unhex("ff02fafa"))
                    square(30*val+15+val*5, 30*row+15+row*5, 30)
                
                else:
                    raise Exception("Encountered value " + str(Grid.gridList[row][val]) + " while initializing")
    
    


def CheckColorsInGame():
    CurrentColorsInGame = []
    
    for row in range(17):
            for val in range(16):
                if Grid.gridList[row][val] == 0:
                    pass

                elif not CurrentColorsInGame.contains(Grid.gridList[row][val]):
                     CurrentColorsInGame.append(Grid.gridList[row][val])





def GameOverScreen():
    print("Game Over")
    #Code for Game Over screen
    
            
