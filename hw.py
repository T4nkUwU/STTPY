class meeple:
    def __init__(self, location, board):
        self.location = location
        self.health = 6
        self.board = board

    def myLocation(self):
        print(str(self.location))

    def actionFunction(self, action):
        if action.lower() == 'move left' and self.location >= 2:
            self.location -= 1
            self.myLocation()
        elif self.location == 1:
            print("Illegal manuever!")

        if action.lower() == 'move right' and (self.board.xMax - 1) >= self.location:
            self.location += 1
            self.myLocation()
        elif self.location == self.board.xMax:
            print("Illegal manuever!")


class board:
    def __init__(self, xMax, yMax):
        self.xMax = xMax
        self.yMax = yMax



newBoard = board(7,1)
redMeeple = meeple(3, newBoard)
gameLoop = True

while(gameLoop == True):
    g = input("Input an action! \n")
    redMeeple.actionFunction(g)
 #       if action == ("Move Right"): 
 #           print("Character Moves Right")
 #           redMeeple.location += 1
 #           redMeeple.myLocation()
