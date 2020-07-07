class Action:
    def __init__(self, name, abv, description):
        if len(str(abv)) != 3:
            self.abreviation = str(name)[0:2]
            self.abreviation = str(self.abreviation).lower()
        elif len(str(abv)) == 3:
            self.abreviation = str(abv).lower()
        self.actionName = str(name).capitalize
        self.description = str(description).capitalize
    
    def retChar(self):
        return(str(self.actionName)[0])

class ActionParser:
    def __init__(self):
        self.Announce = Action("Announce", "anc", "Announce your presence to the world!")

soldier = Action("Soulja boy", "soj", "Up in dat ho")
g = input("Input an action! \n")