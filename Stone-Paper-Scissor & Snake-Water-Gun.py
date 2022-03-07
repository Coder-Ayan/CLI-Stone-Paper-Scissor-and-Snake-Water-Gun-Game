# Importing modules
from random import randint
from time import sleep

# CNV = Chosen Number to Value
def CNV(game, cn):
    if game == 1:
        if cn == 1:
             return 'stone'
        elif cn == 2:
             return 'paper'
        elif cn == 3:
             return 'scissor'
    elif game == 2:
        if cn == 1:
             return 'snake'
        elif cn == 2:
             return 'water'
        elif cn == 3:
             return 'gun'

# rerun function
def rerun():
    # Taking try again input(yes/no)
    run = input("Do you want to try again (yes/no): ")

    # Run Cases
    if run == 'yes':
        start()
    elif run == 'no':
        exit()
    else:
        print("Your input is wrong.")
        rerun()


# play function
def play(game_no):
    # Computer is choosing...
    print("Computer is choosing...")
    comp = randint(1, 3)
    # Pause code for 3 seconds
    sleep(3)
    print("Computer has choosen.\n")

    # Stone, Paper, Scissor game
    if game_no == 1:
        # Taking player choice input
        print("Enter 1 for stone,")
        print("Enter 2 for paper,")
        print("Enter 3 for scissor.")
        player = input("Enter your choice: ")

        # When player's choice is not 1 or 2 or 3
        if player != '1' and player != '2' and player != '3':
            print("Your input is wrong")
            rerun()

        # Changing data type of player: str to int
        player = int(player)

        # Printing that who has chosen what
        print("\nYour choice is", CNV(game_no, player))
        print("Computer's choice is", CNV(game_no, comp))

        # Cases
        # Player's choice and computer's choice when same
        if player == comp:
            return "The match was tie."
        # Stone - Paper
        elif (player == 1) and (comp == 2):
            return "You loss"
        # Stone - Scissor
        elif (player == 1) and (comp == 3):
            return "You won"
        # Paper - Stone
        elif (player == 2) and (comp == 1):
            return "You won"
        # Paper - Scissor
        elif (player == 2) and (comp == 3):
            return "You loss"
        # Scissor - Paper
        elif (player == 3) and (comp == 1):
            return "You loss"
        # Scissor - Stone
        elif (player == 3) and (comp == 2):
            return "You won"

    # Snake, Water, Gun game
    if game_no == 2:
        # Taking player choice input
        print("Enter 1 for snake,")
        print("Enter 2 for water,")
        print("Enter 3 for gun.")
        player = input("Enter your choice: ")

        # When player's choice is not 1 or 2 or 3
        if player != '1' and player != '2' and player != '3':
            print("Your input is wrong")
            rerun()

        # Changing data type of player: str to int
        player = int(player)

        # Printing that who has chosen what
        print("\nYour choice is", CNV(game_no, player))
        print("Computer's choice is", CNV(game_no, comp))

        # Cases
        # Player's choice and computer's choice when same
        if player == comp:
            return "The match was tie."
        # Snake - Water
        elif (player == 1) and (comp == 2):
            return "You won"
        # Snake - Gun
        elif (player == 1) and (comp == 3):
            return "You loss"
        # Water - Snake
        elif (player == 2) and (comp == 1):
            return "You loss"
        # Water - Gun
        elif (player == 2) and (comp == 3):
            return "You won"
        # Gun - Snake
        elif (player == 3) and (comp == 1):
            return "You won"
        # Gun - Water
        elif (player == 3) and (comp == 2):
            return "You loss"


def start():
    while True:
        print("Enter 1 to play Stone, Paper, Scissor.")
        print("Enter 2 to play Snake, Water, Gun.")

        game = input("Which game do you want to play?: ")

        if (game != '1' and game != '2'):
            print("Your input is wrong.")
            rerun()

        game = int(game)

        print(play(game))

        rerun()

if __name__ == "__main__":
    start()