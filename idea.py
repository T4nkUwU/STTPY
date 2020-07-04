class input:
    def __init__(self, meeple, *names):
        self.callNames = []
        self.condition = True
        for i in names:
            self.callNames.append(str(names[i]))
        
    def runMove(self):
        if self.condition == True:
            return print("You did it!")
        elif self.condition == False:
            return self.throwError()

    def throwError(self):
        return print("Error")

class moveLeft(input, meeple):
    def __init__(self):
        input.__init__(meeple, "Move Left", "move left", "ml")


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