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

    def myAction(self):
        print("This is my action!")

class Cat(action):
    def __init__(self):
        print("placeholder!")

class ActionParser:
    def __init__(self, *Actions):
        self.ActionsList = []
        for action in Actions:
            self.ActionsList.append(action)
        
    def CommandList(self):
        print("\n\n=== LIST OF USEABLE COMMANDS===")
        for Action in self.ActionsList:
            Action.helpMe()
        print("=== END OF LIST ==\n")

    def getInput(self, input):
        if input == "help":
            return self.CommandList()
        else:
            for Action in self.ActionsList:
                if Action.actionName == input:
                    return Action.runAction()
            return print("No action found, try again")

class inputRunner:
    def __init__(self):
        print("placeholder!")

class victoryCondition:
    def __init__(self):
        print("placeholder!")
    
currentGame = gameState()