from random import *

class meeple:
    def __init__(self, name, xStart, yStart):
        self.xLocation = xStart
        self.yLocation = yStart
        ##self.health = 6
        self.name = name

    def myLocation(self):
        print(f'{self.name}s current position is X: {self.xLocation} And Y : {self.yLocation}')

class board:
    def __init__(self, xMax, yMax):
        self.xMax = xMax
        self.yMax = yMax

class player:
    def __init__(self, name):
        self.name = name

class inputReader:
    def __init__(self, player, meeple, board, gameState):
        self.numberOfPlayers = 1
        self.thePlayer = player
        self.theMeeple = meeple
        self.theBoard = board
        self.theGame = gameState
        self.resetVictory()
        self.theMeeple.myLocation()

    def winCheck(self):
        if self.winningX == self.theMeeple.xLocation and self.winningY == self.theMeeple.yLocation:
            return self.theGame.winGame()
        elif self.winningX != self.theMeeple.xLocation or self.winningY != self.theMeeple.yLocation:
            return

    def actions(self, input):
        if input.lower() == 'move left' and self.theMeeple.xLocation >= 2:
            self.theMeeple.xLocation -= 1
            self.winCheck()
            return self.theMeeple.myLocation()
        elif input.lower() == 'move left' and self.theMeeple.xLocation == 1:
            return print("Illegal manuever: Cannot move past left bounds")

        if input.lower() == 'move right' and (self.theBoard.xMax - 1) >= self.theMeeple.xLocation:
            self.theMeeple.xLocation += 1
            self.winCheck()
            return self.theMeeple.myLocation()
        elif input.lower() == 'move right' and self.theMeeple.xLocation == self.theBoard.xMax:
            return print("Illegal manuever: Cannot move past left bounds")

        if input.lower() == 'move down' and self.theMeeple.yLocation >= 2:
            self.theMeeple.yLocation -= 1
            self.winCheck()
            return self.theMeeple.myLocation()
        elif input.lower() == 'move down' and self.theMeeple.yLocation == 1:
            return print("Illegal manuever: Cannot move below bottom bounds")

        if input.lower() == 'move up' and (self.theBoard.yMax - 1) >= self.theMeeple.yLocation:
            self.theMeeple.yLocation += 1
            self.winCheck()
            return self.theMeeple.myLocation()
        elif input.lower() == 'move up' and self.theMeeple.yLocation == self.theBoard.yMax:
            return print("Illegal manuever: Cannot move above top bounds")

    def resetVictory(self):
        self.winningX = randrange(1,self.theBoard.xMax)
        self.winningY = randrange(1,self.theBoard.yMax)
        self.theMeeple.yLocation = 2
        self.theMeeple.xLocation = 2
        return

class gameState:
    def __init__(self):
        self.gameLoop = True
        self.curPlayer = player(input("Tell me your name! \n"))
        self.curBoard = board(3,3)
        self.curMeeple = meeple(str(self.curPlayer.name),2,2)
        self.curReader = inputReader(self.curPlayer, self.curMeeple, self.curBoard, self)
        self.runGame()
    
    def runGame(self):
        while(self.gameLoop == True):
            g = input("Input an action! \n")
            self.curReader.actions(str(g))

    
    def winGame(self):
        input("Congrats on winning! \nPress any key to start a new game\n\n")
        self.curReader.resetVictory()
    
currentGame = gameState()