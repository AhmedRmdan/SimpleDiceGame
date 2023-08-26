"""A simple text-based dice game where you start with a 100$ aiming to profit.
game ends when you lose all your money.
this project is for my personal practice only"""
import json
from time import sleep
from numpy import random
import pyfiglet as pf
import termcolor

PROBABILITIES = {2: 0.4704, 3: 0.3303, 4: 0.24075, 5: 0.1908}
DEFAULT_BALANCE = 100
PLAYER_BALANCE_FILE = "player_balance.json"


def get_balance():
    """Restores saved player balance"""
    with open(PLAYER_BALANCE_FILE, "r+", encoding="utf-8") as f_obj:
        stored_balance = json.load(f_obj)
        stored_balance = float(stored_balance)
    return stored_balance


def check_balance():
    """Checks for player balance and get the stored one if available,
    else will give default balance (100)"""
    with open(PLAYER_BALANCE_FILE, encoding="utf-8") as file:
        if file:
            player_balance = get_balance()

        else:
            player_balance = DEFAULT_BALANCE
    return float(player_balance)


player_balance = check_balance()
player_balance = float(player_balance)


def get_dice_odds(odd=2):
    """Generates odds for player's risk choices"""
    return random.binomial(n=1, p=PROBABILITIES.get(odd, 0.4704))


def store_balance():
    """Stores player's balance in a file"""
    with open(PLAYER_BALANCE_FILE, "w", encoding="utf-8") as f_obj:
        json.dump(float(player_balance), f_obj)


dollar_sign = termcolor.colored(pf.figlet_format("$"), "green")


print(dollar_sign)
print("Welcome to Vegas!")
print(dollar_sign)


print(termcolor.colored(pf.figlet_format("Dice"), "yellow"))
print(
    f"""    Please choose a game to play: 
        [1] DICE
        {termcolor.colored('[0] EXIT','red')} """
)


game_choice_input = input("Game: ").strip().casefold()
if game_choice_input in ("exit", "0"):
    raise SystemExit()


while game_choice_input in ("1", "dice"):  # previous if
    print("Dice, A classic!\n")
    sleep(1)
    if player_balance == DEFAULT_BALANCE:
        print("You have $100 to start your joruney")
    print(
        f"The casino takes it's cut, {termcolor.colored('10%','red')} from every bet."
    )
    sleep(1)
    print("If you lose all your money, game will be over.")
    print(
        f"      Your current balance is ${termcolor.colored(player_balance,'green')}\n"
    )
    print("Let's win!\n")
    print("$" * 10)

    while player_balance > 0:
        print("\nHow much would you like to bet?\n")
        print("     ***Enter 0 or exit to quit playing\n")

        dice_bet = input(" $")
        if dice_bet.isalpha():
            raise SystemExit()
        if dice_bet == "0":
            raise SystemExit()

        dice_bet = float(dice_bet)
        if dice_bet <= player_balance:  # previous while
            print("$" * 10)
            print("\nChoose your multiplier(2-5), aka Risk.")
            dice_risk_choice = int(
                input(f"Your ${termcolor.colored(dice_bet,'green')} X ")
            )

            if dice_risk_choice in range(2, 6):
                max_potential_win = float(dice_bet) * dice_risk_choice
                user_potential_win = max_potential_win - (max_potential_win * 10 / 100)

                print("$" * 10)
                print(
                    f"\nPotential winnings are ${termcolor.colored(user_potential_win,'green')}\n"
                )
                print("$" * 10)

                odds = get_dice_odds(dice_risk_choice)

                if odds == 1:
                    player_balance += user_potential_win

                    print("\nBetting...\n")
                    sleep(3)
                    print(termcolor.colored("\n$ $ $     W I N    $ $ $\n", "green"))
                    print("$" * 10)
                    print(
                        f"\n      Current Balance: ${termcolor.colored(player_balance,'green')}\n"
                    )
                    print("$" * 10)

                else:
                    player_balance -= float(dice_bet)

                    print("\nBetting...\n")
                    sleep(3)
                    print(termcolor.colored("\n      YOU LOST!    \n", "red"))
                    print("$" * 10)
                    print(
                        f"\n      Current Balance: ${termcolor.colored(player_balance,'red')}\n"
                    )
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
