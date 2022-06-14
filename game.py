from operator import attrgetter

BOARD_DIMENSION = 8
# TODO: 
global Board
Board = [ [ {'knight': [], 'item': []} for i in range(BOARD_DIMENSION)] for j in range(BOARD_DIMENSION)]

class Game:
    def __init__(self):
        pass

    # Initialize the board.
    def initBoard(self, knights, items):
        for i in knights:
            row, col = i.getPosition()
            Board[row][col]['knight'].append(i)
        for j in items:
            row, col = j.getPosition()
            Board[row][col]['item'].append(j)

    # Update board position
    def updateKnightBoardPosition(self, currentPosition, newPosition, piece):
        [currentRow, currentCol] = currentPosition
        [newRow, newCol] = newPosition

        Board[currentRow][currentCol]['knight'].remove(piece) # Clear the current board position.
        Board[newRow][newCol]['knight'].append(piece) # Add move knight to new position.
        Board[newRow][newCol]['knight'].sort(key=lambda knight: knight.getSymbol())

    # Move knights on the board
    def moveAndUpdateKnight(self, movingKnight, direction):

        # Obtain the current position of the moving knight
        currentRow, currentCol = movingKnight.getPosition()

        # move the knight and get his new position
        newRow, newCol = movingKnight.move(direction)

        # check if the move has put the knight out of bounds
        if newRow >= BOARD_DIMENSION or newRow < 0 or newCol >= BOARD_DIMENSION or newCol < 0:
            print(f'{movingKnight.getName()} went out of the arena and drowned!')
            self.drownedOrDead(currentRow, currentCol, 'DROWNED', movingKnight)
            movingKnight.setPosition(None, None)
            Board[currentRow][currentCol]['knight'].remove(movingKnight)

        else:
            # Get lists of pieces at the destination tile.
            knightInDestTile = Board[newRow][newCol]['knight']
            itemsInDestTile = Board[newRow][newCol]['item']
            
            # check if destination tile is empty
            if (not knightInDestTile) and (not itemsInDestTile): 
                # update board
                self.updateKnightBoardPosition([currentRow, currentCol], [newRow, newCol], movingKnight)
            
            # destination tile has items but no knights
            elif(not knightInDestTile) and (itemsInDestTile): 
                item = itemsInDestTile[0]
                
                # check if moving knight has an item
                if (movingKnight.getItem() == 'null'): 
                    # Equip knight with available item
                    self.equipKnight(movingKnight, item)
                
                # Update board
                self.updateKnightBoardPosition([currentRow, currentCol], [newRow, newCol], movingKnight)
                    
            # destination tile has knight but no items
            elif (knightInDestTile) and (not itemsInDestTile): 
                defendingKnight = knightInDestTile[0]

                # check if knight is alive
                if(defendingKnight.getStatus() == 'LIVE'): 

                    winnerKnight = self.knightsEncouter(movingKnight, defendingKnight)

                    if winnerKnight.getItem() == 'null':
                        
                        # Get the item.
                        item = Board[newRow][newCol]['item'][0]

                        # Equip knight with available item
                        self.equipKnight(winnerKnight, item)

                    # update board.
                    self.updateKnightBoardPosition([currentRow, currentCol], [newRow, newCol], winnerKnight)

                else:
                    # update board
                    self.updateKnightBoardPosition([currentRow, currentCol], [newRow, newCol], movingKnight)

            else: # destination has knight and items.
                defendingKnight = knightInDestTile[0]
                item = itemsInDestTile[0]

                # Check if attacking knight has an item and if item on tile is equipped
                if movingKnight.getItem() == 'null' and item.getStatus() == False:
                    # Equip knight with available item
                    self.equipKnight(movingKnight, item)

                # Check if knight on tile is ALIVE
                if(defendingKnight.getStatus() == 'LIVE'):
                
                    winnerKnight = self.knightsEncouter(movingKnight, defendingKnight)
                    
                    # update board.
                    self.updateKnightBoardPosition([currentRow, currentCol], [newRow, newCol], winnerKnight)

                else:
                    # update board
                    self.updateKnightBoardPosition([currentRow, currentCol], [newRow, newCol], movingKnight)

    # Equip a knight.
    def equipKnight(self, knight, item):
        knight.setItem(item)
        item.setStatus(True)
        # remove equipped item from item's list
        row, col = item.getPosition()
        Board[row][col]['item'].remove(item)
        Board[row][col]['item'].sort(key=attrgetter('attackScore', 'defenceScore'), reverse=True)
    

    # Fight outcome of knights.
    def knightsEncouter(self, attacker, defender):
        # check if attacking knight an item
        if attacker.getItem() != 'null': 
            attacker.attacking()
        
        # Element of surprise
        attacker.elementOfSurprise() 
        
        # check if defending knight has an item
        if defender.getItem() != 'null': 
            defender.defending()

        # get their scores
        attackerScore = attacker.getAttackScore()
        defenderScore = defender.getDefenceScore()
        
        # compare their scores
        if attackerScore > defenderScore:
            row, col = defender.getPosition()
            self.drownedOrDead(row, col, 'DEAD', defender)
            return attacker
        else:
            row, col = attacker.getPosition()
            self.drownedOrDead(row, col, 'DEAD', attacker)
            return defender

    # Set knight status to drowned or dead
    def drownedOrDead(self, row, col, status, knight):
        knight.setStatus(status)
        knight.setAttackScore(0)
        knight.setDefenceScore(0)
        knight.setSymbol(knight.getSymbol().lower())
        item = knight.getItem()
        if item != 'null':
            item.setStatus(False)
            item.setPosition(row, col)
            Board[row][col]['item'].append(item)
            Board[row][col]['item'].sort(key=attrgetter('attackScore', 'defenceScore'), reverse=True)
        knight.dropItem()
        knight.setPosition(None, None)

    # Print the arena.
    def printBoard(self):
        i = 0
        print(" _ _ _ _ _ _ _ _")
        while i < BOARD_DIMENSION:
            j = 0
            while j < BOARD_DIMENSION:
                knightTile = Board[i][j]['knight'] 
                itemTile = Board[i][j]['item']

                if (not knightTile) and (not itemTile):
                    print('|_', end='')
                elif (knightTile) and (not itemTile):
                    print('|' + knightTile[0].symbol, end='')
                elif (not knightTile) and (itemTile):
                    print('|' + itemTile[0].symbol, end='')
                else:
                    print('|' + knightTile[0].symbol, end='')
                j+=1
            print('|')
            i+=1


    def play(self, pieces, filename):
        [red, blue, green, yellow] = pieces
        with open(filename, 'r') as inputFile:
            if inputFile.mode == 'r':
                for line in inputFile.readlines():
                    line = line.strip()
                    [knight, direction] = line.split(':')
                    match knight:
                        case 'R':
                            self.moveAndUpdateKnight(red, direction)
                        case 'B':
                            self.moveAndUpdateKnight(blue, direction)
                        case 'G':
                            self.moveAndUpdateKnight(green, direction)
                        case 'Y':
                            self.moveAndUpdateKnight(yellow, direction)
                        case _:
                            raise ValueError('Not a valid input!')
