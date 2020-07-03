class meeple:
    def __init__(self, xStart, yStart, board):
        self.xLocation = xStart
        self.yLocation = yStart
        self.health = 6
        self.board = board

    def myLocation(self):
        print("Your current board position is X:" + str(self.xLocation) + " And Y : " + str(self.yLocation))

    def actionFunction(self, action):
        if action.lower() == 'move left' and self.xLocation >= 2:
            self.xLocation -= 1
            return self.myLocation()
        elif action.lower() == 'move left' and self.xLocation == 1:
            return print("Illegal manuever: Cannot move past left bounds")

        if action.lower() == 'move right' and (self.board.xMax - 1) >= self.xLocation:
            self.xLocation += 1
            return self.myLocation()
        elif action.lower() == 'move right' and self.xLocation == self.board.xMax:
            return print("Illegal manuever: Cannot move past left bounds")

        if action.lower() == 'move down' and self.yLocation >= 2:
            self.yLocation -= 1
            return self.myLocation()
        elif action.lower() == 'move down' and self.yLocation == 1:
            return print("Illegal manuever: Cannot move below bottom bounds")

        if action.lower() == 'move up' and (self.board.yMax - 1) >= self.yLocation:
            self.yLocation += 1
            return self.myLocation()
        elif action.lower() == 'move up' and self.yLocation == self.board.yMax:
            return print("Illegal manuever: Cannot move above top bounds")

class board:
    def __init__(self, xMax, yMax):
        self.xMax = xMax
        self.yMax = yMax


newBoard = board(7,1)
redMeeple = meeple(3,1, newBoard)

gameLoop = True

while(gameLoop == True):
    g = input("Input an action! \n")
    redMeeple.actionFunction(g)