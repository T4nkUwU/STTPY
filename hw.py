class meeple:
    def __init__(self, location):
        self.location = location
        self.health = 6

    def myLocation(self):
        print(str(self.location))

    def actionFunction(self, action):
        if action.lower() == 'move left':
            self.location -= 1
            self.myLocation()

        if action.lower() == 'move right':
            self.location += 1
            self.myLocation()


board = 6
redMeeple = meeple(3)
g = input("Input your first action! \n")
redMeeple.actionFunction(g)
 #       if action == ("Move Right"): 
 #           print("Character Moves Right")
 #           redMeeple.location += 1
 #           redMeeple.myLocation()
