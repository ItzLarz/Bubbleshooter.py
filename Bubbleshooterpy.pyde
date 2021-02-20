import random
import time

#Grid class
class Grid:
    #Making the grid
    gridList = [[0]*9 for i in range(17)]
    
    #Checking if the user is Game Over
    def GameOverCheck():
        GameOver = False
        for val in Grid.gridList[16]:
            if val != 0:
                GameOver = True
                
        return GameOver
            

ColorsInGame = [1, 2, 3, 4, 5, 6]


def setup():
    size(800, 600)
    
    strokeWeight(10)
    stroke(unhex("ffc1c0ff"))
    rect(5,5,580,590)
    
    fill(unhex("ffc1c0ff"))
    strokeWeight(1)
    stroke(unhex("ffc1c0ff"))
    rect(580,0,219,599)
    
    
                
                
def draw():
    pass
    
#Initializing at the start of a game
def Initialize():
    for row in range(9):
        for val in range(9):
            Grid.gridList[row][val] = random.randint(1,6)
            
    #Code for initializing squares
    
    
    
    
    
    
    for row in range(9):
        for val in range(9):
            if Grid.gridList[row][val] == 1:
                #Red = ffef161a
            
            elif Grid.gridList[row][val] == 2:
                #Green = ff0f00bf
                
            elif Grid.gridList[row][val] == 3:
                #Yellow = fffeff00
                
            elif Grid.gridList[row][val] == 4:
                #Purple = ffe500e6
                
            elif Grid.gridList[row][val] == 5:
                #Dark Blue = ff1e00fd
                
            elif Grid.gridList[row][val] == 6:
                #Light Blue = ff02fafa
            
            else:
                raise Exception("Encountered value" + Grid.gridList[row][val] + "while initializing")
            
                                    
    
            

def NewRow():
    #Checking if player is GameOver
    GameOver = False
    for val in range(9):
        if Grid.gridList[15][val] != 0:
            GameOverScreen()
            GameOver = True
            break
    
    if !GameOver:
        Grid.gridList.pop()
        tempList= [0] * 9
        for val in range(9):
            tempList[val] = random.choice(ColorsInGame)
            
        Grid.gridList.insert(0, tempList)
        
    
        #Code for initializing squares
    
    
    
def GameOverScreen():
    pass
    #Code for Game Over screen
    
            
