class Action:
    def __init__(self, name, abv, description):
        if len(str(abv)) != 3:
            self.abreviation = str(name)[0:2]
            self.abreviation = str(self.abreviation).lower()
        elif len(str(abv)) == 3:
            self.abreviation = str(abv).lower()
        self.actionName = str(name).capitalize()
        self.description = str(description).capitalize()
    
    def retChar(self):
        return(str(self.actionName)[0])

    def helpMe(self):
        return(print(f'{self.actionName} ({self.abreviation}): {self.description}'))

    def runAction(self):
        return(print(f'\n{self.actionName}: {self.description}\n'))

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
        if len(str(input)) == 3:
            for Action in self.ActionsList:
                if Action.abreviation == input:
                    return Action.runAction()
        

soldier = Action("Soulja boy", "soj", "Up in dat ho")
Announce = Action("Announce", "anc", "Announce your presence to the world!")

todaysParser = ActionParser(soldier,Announce)

game = True
while game == True:
    g = input("Input an action! \n")
    todaysParser.getInput(g)