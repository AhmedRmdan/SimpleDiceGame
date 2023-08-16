import time
import numpy as np
import json


PROBABILITIES = {2: 0.4704, 3: 0.3303, 4: 0.24075, 5: 0.1908}
DEFAULT_BALANCE = 100
PLAYER_BALANCE_FILE = "player_balance.json"


def get_balance():
    """Restores saved player balance"""
    with open(PLAYER_BALANCE_FILE, "r+") as f_obj:
        stored_balance = json.load(f_obj)
        stored_balance = float(stored_balance)
    return stored_balance


def check_balance():
    """Checks for player balance and get the stored one if available,
    else will give default balance (100)"""
    with open(PLAYER_BALANCE_FILE) as file:
        if file:
            PlayerBalance = get_balance()
        else:
            PlayerBalance = DEFAULT_BALANCE
    return float(PlayerBalance)


PlayerBalance = check_balance()
PlayerBalance = float(PlayerBalance)


def get_dice_odds(odd=2):
    """Generates odds for player's risk choices"""
    return np.random.binomial(n=1, p=PROBABILITIES.get(odd, 0.4704))


def store_balance():
    """Stores player's balance in a file"""
    with open(PLAYER_BALANCE_FILE, "w") as f_obj:
        json.dump(float(PlayerBalance), f_obj)


for DollarSign in range(1, 5):
    print("$" * DollarSign)

print("Welcome to Vegas!")

for DollarSign in range(5, 8):
    print("$" * DollarSign)


print("\n\n\n")

print(
    """    Please choose a game to play: 
        [1] DICE
        [0] EXIT """
)


GameChoiceInput = input("Game: ").strip().casefold()
if GameChoiceInput == "exit" or GameChoiceInput == "0":
    quit()


while GameChoiceInput == "1" or GameChoiceInput == "dice":  # previous if
    print("Dice, A classic!\n")
    time.sleep(1)
    print("You have $100 to start your joruney")
    print("The casino takes it's cut %20 from every bet.")
    time.sleep(1)
    print("If you lose all your money, game will be over.")
    print(f"      Your current balance is ${PlayerBalance}\n")
    print("Let's win!\n")
    print("$" * 10)

    while PlayerBalance > 0:
        print("\nHow much would you like to bet?\n")
        print("     ***Enter 0 or exit to quit playing\n")

        DiceBet = input(" $")
        if DiceBet.isalpha():
            quit()
        elif DiceBet == "0":
            quit()

        DiceBet = float(DiceBet)
        if DiceBet <= PlayerBalance:  # previous while
            print("$" * 10)
            print("\nChoose your multiplier(2-5), aka Risk.")
            DiceRiskChoice = int(input(f"Your ${DiceBet} X "))

            if DiceRiskChoice in range(2, 6):
                MaxPotentialWin = float(DiceBet) * DiceRiskChoice
                UserPotentialWin = MaxPotentialWin - (MaxPotentialWin * 10 / 100)

                print("$" * 10)
                print(f"\nPotential winnings are ${UserPotentialWin}\n")
                print("$" * 10)

                odds = get_dice_odds(DiceRiskChoice)

                if odds == 1:
                    PlayerBalance += UserPotentialWin

                    print("\nBetting...\n")
                    time.sleep(3)
                    print("\n$ $ $     W I N    $ $ $\n")
                    print("$" * 10)
                    print(f"\n      Current Balance: ${PlayerBalance}\n")
                    print("$" * 10)

                else:
                    PlayerBalance -= float(DiceBet)

                    print("\nBetting...\n")
                    time.sleep(3)
                    print("\n      YOU LOST!    \n")
                    print("$" * 10)
                    print(f"\n      Current Balance: ${PlayerBalance}\n")
                    print("$" * 10)
                store_balance()

            else:
                print("\nERROR: Multiplier must be 2X to 5X\n")

        else:
            print("\nBet amount cannot exceed player balance!\n")

    else:
        print("\nHouse always win.. GAME OVER!\n")
        break

else:
    print("Please choose a valid option")
