import random
import time

class Grid:
    gridList = [[0]*9 for i in range(17)]
    
    def GameOver():
        GameOver = False
        for val in Grid.gridList[16]:
            if val != 0:
                GameOver = True
                
        return GameOver
            

ColorsInGame = ("red", "green", "yellow", "blue", "purple")


def setup():           
    print(Grid.gridList)
    NewRow()
    print(Grid.gridList)
                
                
def draw():
    pass
    

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
        
    if Grid().GameOver:
        pass
        
        #Code for Game Over screen
        
        
    #Code for initializing squares
            
