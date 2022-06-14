import json
import argparse

from knight import Knight
from item import Item
from game import Game

def main():
    
    # Read input file from command line
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input', help = 'An input file containing a valid set a of move.')

    args = parser.parse_args()

    inputFile = args.input

    print("\n\n\n!!!!!!!!!!WELCOME TO BATTLING KNIGHTS!!!!!!!!!!\n\n\n")

    # Instatiate knight objects
    red = Knight('red', 'R', 0, 0)
    blue = Knight('blue', 'B', 7, 0)
    green = Knight('green', 'G', 7, 7)
    yellow = Knight('yellow', 'Y', 0, 7)

    # Instatiate item objects
    # TODO: Overide the constructor for attack and defence
    axe = Item('axe', 'A', 2, 2, attackScore=2, defenceScore=0)
    dagger = Item('dagger', 'D', 2, 5, attackScore=1, defenceScore=0)
    magicStaff = Item('magic_staff', 'M', 5, 2, attackScore=1, defenceScore=1)
    helmet = Item('helmet', 'H', 5, 5, attackScore=0, defenceScore=1)

    # Instatiate a game object.
    game = Game()

    # Add knights and items to the arena
    game.initBoard([red, blue, green, yellow], [axe, dagger, magicStaff, helmet])

    # Play a game.
    game.play([red, blue, green, yellow], inputFile)

    # print final status of the board.
    game.printBoard()

    # create a dictionary of data in preparation to saving in a json file.
    data = {
        red.getName(): [red.getPosition(), red.getStatus(), red.getItemName(), red.getAttackScore(), red.getDefenceScore()],
        blue.getName(): [blue.getPosition(), blue.getStatus(), blue.getItemName(), blue.getAttackScore(), blue.getDefenceScore()],
        green.getName(): [green.getPosition(), green.getStatus(), green.getItemName(), green.getAttackScore(), green.getDefenceScore()],
        yellow.getName(): [yellow.getPosition(), yellow.getStatus(), yellow.getItemName(), yellow.getAttackScore(), yellow.getDefenceScore()],
        axe.getName(): [axe.getPosition(), axe.getStatus()],
        dagger.getName(): [ dagger.getPosition(), dagger.getStatus()],
        helmet.getName(): [ helmet.getPosition(), helmet.getStatus()],
        magicStaff.getName(): [ magicStaff.getPosition(), magicStaff.getStatus()],
    }

    # write data to a json file.
    with open("final_state.json", "w") as outfile:
        json.dump(data, outfile, indent=4)

if __name__ == "__main__":
    main()