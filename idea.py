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