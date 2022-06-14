

# add constructors to the item class for attack and defence 
class Item:
    def __init__(self, name, symbol, row, col, attackScore=0, defenceScore=0):
        self.name = name
        self.symbol = symbol
        self.row = row
        self.col = col
        self.equipped = False
        self.defenceScore = defenceScore
        self.attackScore = attackScore

    def __repr__(self):
        return repr((self.symbol, (self.row, self.col), self.equipped, self.attackScore, self.defenceScore))

    # Get item position
    def getPosition(self):
        return self.row, self.col

    # Get item's name
    def getName(self):
        return self.name
    
    # Get item attack scores
    def getAttackScores(self):
        return self.attackScore
    
    # Get item defence scores
    def getDefenceScores(self):
        return self.defenceScore

    # Get the item's symbol
    def getSymbol(self):
        return self.symbol

    # Get item status
    def getStatus(self):
        return self.equipped

    # Set item position
    def setPosition(self, row, col):
        self.row, self.col = row, col
    
    # Check if item is equipped
    def setStatus(self, status):
        self.equipped = status

    # TODO: Add setters for defence and attack scores, and for name and symbol