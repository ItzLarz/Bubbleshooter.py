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
            

ColorsInGame = ("red", "green", "yellow", "blue", "purple")


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
            Grid.gridList[row][val] = random.randint(1,5)
            
    #Code for initializing squares
    
    
    
            

def NewRow():
    Grid.gridList.pop()
    tempList= [0] * 9
    for val in range(9):
        tempList[val] = random.randint(1,5)
        
    Grid.gridList.insert(0, tempList)
        
    if Grid().GameOverCheck:
        GameOverScreen()
        
        
        
        
    #Code for initializing squares
    
    
    
def GameOverScreen():
    pass
    
            
