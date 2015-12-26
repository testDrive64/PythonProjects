"""
# Planung:
#  1. Spiel type waehlen
#  2. Runden anzahl
#  3. Gesamte Runden bis alle boote gefunden wurden
#  4. Boote koennen gesetzt werden
#  5. Boot arten
#          - 2 x 2 - Felder Boot
#          - 1 x 3 - Felder Boot
#          - 1 x 4 - Felder Boot
"""

from random import randint

def print_menu():
    print "Hauptmenu:"
    print "1. New Game"
    print "2. Quit"
    choice = int(raw_input("> "))
    while choice is not 1 and choice is not 2:
        choice = int(raw_input("Type 1 or 2: "))
    choice = menu_point(choice)
    game_option(choice)

def menu_point(choice):
    if choice == 1:
        print "1. Human vs Human"
        print "2. Human vs Comp."
        print "3. Round per Player:"
        gameType = int(raw_input("New Game> "))

        return gameType

    elif choice == 2:
        print "Programm stops"
        break
    else:
        print "Wrong input!"

def game_option(gameType):

    print roundsPPlayer
    # field size
    fieldSizeCol = int(raw_input("Columns: "))
    fieldSizeRow = int(raw_input("Rows   : "))

    # place from the boats
    print "Place for the boats: "
    boat1 = int(raw_input("Boat1 (2-field): "))
    boat2 = int(raw_input("Boat2 (2-field): "))
    boat3 = int(raw_input("Boat3 (3-field): "))
    boat4 = int(raw_input("Boat4 (4-field): "))

    # default Round / Player
    roundsPPlayer = 3

    if gameType == 1:
        build_board(fieldSizeRow, filedSizeCol)

        start_game(2, roundsPPlayer, boat1, boat2, boat3, boat4)
    elif gameType == 2:
        start_game(1, roundsPPlayer, boat1, boat2, boat3, boat4)
    elif gameType == 3:
        print "Type Round / Player: "
        roundsPPlayer = int(raw_input("> "))
        menu_point(1)
    else:
        print "Wrong input!"

def build_board(fieldSizeRow, fieldSizeCol) :
    # define the game field
    board = []
    for x in range(fieldSizeRow):
        board.append(["O"] * fieldSizeCol)
    print_board(board)


# print the game field to the screen
def print_board(board):
    for row in board:
        print " ".join(row)

# start game play
print "Let's play Battleship!"
print_board(board)

# define a boat
def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
# just for production
# show the place from the boats
print ship_row
print ship_col

# play round per player
for turn in range(4):
    print "Turn", turn + 1
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        # Print (turn + 1) here!
        print_board(board)

    if turn == 3:
        print "Game Over"
        break
