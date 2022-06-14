# from game import Arena

class Knight:
    def __init__(self, name, symbol, row, col):
        self.name = name
        self.symbol = symbol
        self.row = row
        self.col = col
        self.status = "LIVE"
        self.item = None
        self.attackScore = 1
        self.defenceScore = 1

    def __repr__(self):
        return repr((self.symbol, (self.row, self.col), self.status, self.item, self.attackScore, self.defenceScore))

    # get knight's name
    def getName(self):
        return self.name

    # get knight's symbol
    def getSymbol(self):
        return self.symbol

    # Get Knight's position
    def getPosition(self):
        return self.row, self.col

    # get knight's status
    def getStatus(self):
        return self.status

    # get aquired weapon
    def getItem(self):
        if self.item == None:
            return 'null'
        return self.item

    # get aquired weapon
    def getItemName(self):
        if self.item == None:
            return 'null'
        return self.item.getName()

    # get attack score
    def getAttackScore(self):
        return self.attackScore

    # get defence score
    def getDefenceScore(self):
        return self.defenceScore

    # set knight's name
    def setName(self, name):
        self.name = name

    # set knight's symbol
    def setSymbol(self, symbol):
        self.symbol = symbol

    # set knight's status
    def setStatus(self, status):
        self.status = status

    # set knight's position
    def setPosition(self, row, col):
        self.row, self.col = row, col

    # set knight's item
    def setItem(self, item):
        self.item = item

    # set knight's attack score
    def setAttackScore(self, score):
        self.attackScore = score

    # set knight's defence score
    def setDefenceScore(self, score):
        self.defenceScore = score

        # Knight's moves
    def move(self, direction):
        # print("Move in direction:", direction)
        match direction:
            case 'N':
                self.row = self.row - 1
            case 'E':
                self.col = self.col + 1
            case 'S':
                self.row = self.row + 1
            case 'W':
                self.col = self.col - 1
            case _:
                raise ValueError('Not a valid direction!')
        return self.row, self.col

    # knight attacking
    def attacking(self):
        self.attackScore += self.item.attackScore

    # knight element of suprise
    def elementOfSurprise(self):
        self.attackScore += 0.5

    # knight defending
    def defending(self):
        self.defenceScore += self.item.defenceScore
    
    # knight drops item
    def dropItem(self):
        self.item = None