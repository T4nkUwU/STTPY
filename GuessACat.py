#from random import *
#import math
from os import system, name

class gameState:
    def __init__(self):
        print("placeholder!")

class player:
    def __init__(self, name):
        self.name = str(name)
            
class board:
    def __init__(self, xMax, yMax):
        self.xMax = int(xMax)
        self.yMax = int(yMax)

class action:
    def __init__(self, name, description):
        self.actionName = str(name).capitalize()
        self.description = str(description).capitalize()

class ActionParser:
    def __init__(self, *Actions):
        self.ActionsList = []
        self.alphabet = ''
        for action in Actions:
            self.ActionsList.append(action)
            self.alphabet += str(action.actionName)[0]
        ##self.ActionTable = []
        ##for i in self.ActionsList:
        ##    if 
        
    def CommandList(self):
        print("\n\n=== LIST OF USEABLE COMMANDS===")
        for Action in self.ActionsList:
            Action.helpMe()
        print("=== END OF LIST ==\n")

    def getInput(self, input):
        if input == "help":
            return self.CommandList()
        # if len(str(input)) == 3:
        #     for Action in self.ActionsList:
        #         if Action.abreviation == input:
        #             return Action.runAction()
        elif len(str(input)) > 3:
            for Action in self.ActionsList:
                    if Action.actionName == input:
                        return Action.runAction()

class inputRunner:
    def __init__(self):
        print("placeholder!")

class victoryCondition:
    def __init__(self):
        print("placeholder!")

# class meeple:
#     def __init__(self, name, xStart, yStart):
#         self.xLocation = xStart
#         self.yLocation = yStart
#         self.health = 6
#         self.name = name

#     def myLocation(self):
#         print(f'{self.name}s current position is X: {self.xLocation} And Y : {self.yLocation}')

# class board:
#     def __init__(self, xMax, yMax):
#         self.xMax = xMax
#         self.yMax = yMax

# class player:
#     def __init__(self, name):
#         self.name = name

# class inputReader:
#     def __init__(self, player, meeple, board, gameState):
#         self.numberOfPlayers = 1
#         self.thePlayer = player
#         self.theMeeple = meeple
#         self.theBoard = board
#         self.theGame = gameState
#         self.resetVictory()
#         self.theMeeple.myLocation()

#     def winCheck(self):
#         if self.winningX == self.theMeeple.xLocation and self.winningY == self.theMeeple.yLocation:
#             return self.theGame.winGame()
#         elif self.winningX != self.theMeeple.xLocation or self.winningY != self.theMeeple.yLocation:
#             return

#     def actions(self, input):
#         if input.lower() == 'move left' and self.theMeeple.xLocation >= 2:
#             self.theMeeple.xLocation -= 1
#             self.winCheck()
#             return self.theMeeple.myLocation()
#         elif input.lower() == 'move left' and self.theMeeple.xLocation == 1:
#             return print("Illegal manuever: Cannot move past left bounds")

#         if input.lower() == 'move right' and (self.theBoard.xMax - 1) >= self.theMeeple.xLocation:
#             self.theMeeple.xLocation += 1
#             self.winCheck()
#             return self.theMeeple.myLocation()
#         elif input.lower() == 'move right' and self.theMeeple.xLocation == self.theBoard.xMax:
#             return print("Illegal manuever: Cannot move past left bounds")

#         if input.lower() == 'move down' and self.theMeeple.yLocation >= 2:
#             self.theMeeple.yLocation -= 1
#             self.winCheck()
#             return self.theMeeple.myLocation()
#         elif input.lower() == 'move down' and self.theMeeple.yLocation == 1:
#             return print("Illegal manuever: Cannot move below bottom bounds")

#         if input.lower() == 'move up' and (self.theBoard.yMax - 1) >= self.theMeeple.yLocation:
#             self.theMeeple.yLocation += 1
#             self.winCheck()
#             return self.theMeeple.myLocation()
#         elif input.lower() == 'move up' and self.theMeeple.yLocation == self.theBoard.yMax:
#             return print("Illegal manuever: Cannot move above top bounds")

#     def resetVictory(self):
#         system('cls')
#         self.winningX = randrange(1,self.theBoard.xMax)
#         self.winningY = randrange(1,self.theBoard.yMax)
#         self.theMeeple.yLocation = int(math.ceil(self.theBoard.yMax/2))
#         self.theMeeple.xLocation = int(math.ceil(self.theBoard.yMax/2))
#         return

# class gameState:
#     def __init__(self):
#         self.gameLoop = True
#         self.curPlayer = player(input("Tell me your name! \n"))
#         self.curBoard = board(7,7)
#         self.curMeeple = meeple(str(self.curPlayer.name),int(math.ceil(self.curBoard.xMax/2)),int(math.ceil(self.curBoard.yMax/2)))
#         self.curReader = inputReader(self.curPlayer, self.curMeeple, self.curBoard, self)
#         self.runGame()
    
#     def runGame(self):
#         while(self.gameLoop == True):
#             g = input("Input an action! \n")
#             self.curReader.actions(str(g))

    
#     def winGame(self):
#         input("Congrats on winning! \nPress any key to start a new game\n\n")
#         self.curReader.resetVictory()
    
currentGame = gameState()