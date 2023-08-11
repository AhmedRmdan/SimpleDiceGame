import time
import numpy as np

PROBABILITIES = {2: 0.4704, 3: 0.3303, 4: 0.24075, 5: 0.1908}
MINIMUM_DEPOSIT = 10


def get_dice_odds(odd=2):
    return np.random.binomial(n=1, p=PROBABILITIES.get(odd, 0.4704))


for DollarSign in range(1, 5):
    print("$" * DollarSign)

print("Welcome to Vegas!")

for DollarSign in range(5, 8):
    print("$" * DollarSign)
print(
    """



"""
)
print(
    """    Please choose a game to play: 
        [1] DICE
        [0] EXIT """
)

PlayerBalance = 0

GameChoiceInput = input("Game: ").strip().casefold()
if GameChoiceInput == "exit" or GameChoiceInput == "0":
    quit()

while GameChoiceInput == "1" or GameChoiceInput == "dice":  # previous if
    print("Dice, A classic!\n")
    print("How much money would you like to deposit?")
    ChipsDeposit = input("   $")
    if ChipsDeposit.isalpha():
        print("Deposit can only be numbers")

    else:
        ChipsDeposit = float(ChipsDeposit)
        PlayerBalance += ChipsDeposit
        print(f"      Your current balance is ${PlayerBalance}\n")

        if PlayerBalance < MINIMUM_DEPOSIT:
            print("Sorry, minimum deposit is $10")

        else:
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
                PlayerBalance -= DiceBet

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

                else:
                    print("\nERROR: Multiplier must be 2X to 5X\n")

            else:
                print("\nBet amount cannot exceed player balance!\n")

        else:
            print("\nHouse always win.. GAME OVER!\n")

else:
    print("Please choose a valid option")


# CHATGPT Points:
# The code you provided has some issues and could be improved. Here's a review of the code:

# 1. Inconsistent indentation: The code has inconsistent indentation, which can make it harder to read and understand. It's important to maintain consistent indentation for better code readability.

# 2. Unclear variable names: Some variable names in the code are not descriptive enough. For example, `odd`, `DiceOdds`, `GameChoiceInput`, and `DiceRiskChoice` could be named more clearly to improve code readability.

# 3. Magic numbers: The code contains some hard-coded values like probabilities (0.4704, 0.3303, 0.24075, 0.1908), multipliers (2, 3, 4, 5), and balance requirements ($10). It would be better to assign these values to named constants or variables with descriptive names to improve code readability and maintainability.

# 4. Redundant condition: The condition `(DiceBet) <= PlayerBalance` is unnecessary because `DiceBet` is already converted to a float, so the comparison can be done directly as `DiceBet <= PlayerBalance`. The same applies to the condition `(DiceRiskChoice) == int(2)` and similar comparisons.

# 5. Lack of input validation: The code assumes that the user always enters valid input. It would be better to add input validation to handle cases where the user enters unexpected input, such as non-numeric characters when entering the bet amount.

# 6. Repetitive code: The code could be refactored to reduce repetition. For example, the logic for calculating odds and checking the result could be extracted into a separate function to avoid duplication.

# 7. Use of `quit()` function: The `quit()` function is used to exit the program, but it's generally not recommended to use it in production code. Instead, you could use a loop or a flag variable to control the flow of the program.

# 8. Lack of error handling: The code does not handle potential errors, such as invalid input or exceptions that might occur during execution. Adding appropriate error handling would make the code more robust.

# 9. Lack of modularity: The code could benefit from better organization and modularization. Breaking down the code into smaller functions with specific responsibilities can improve readability, reusability, and maintainability.

# Overall, the code could be improved by addressing the issues mentioned above.
# ---------------
# Tell me more
# ------------
# Certainly! Here are some additional details about the improvements made to the code:

# 1. Input Validation: The updated code includes input validation for the bet amount entered by the user. It checks if the input contains only numeric characters and handles cases where the user enters non-numeric input. This helps prevent errors and ensures that the code works correctly.

# 2. Random Odds Calculation: The code now uses the `numpy.random.binomial` function to calculate the odds for the dice game. It takes the desired multiplier (risk) as an input and retrieves the corresponding probability from the `PROBABILITIES` dictionary. This approach provides a more flexible and accurate way to calculate the odds.

# 3. Named Constants: The code defines named constants, such as `PROBABILITIES` and `MINIMUM_DEPOSIT`, to store hard-coded values. This makes the code more readable and maintainable because the purpose of these values is clear.

# 4. Functions for Reusability: The code has been refactored into functions to improve reusability. For example, the `print_dollar_signs` function is responsible for printing a sequence of dollar signs, and the `get_dice_odds` function calculates the odds based on the chosen multiplier. By encapsulating specific functionalities into functions, the code becomes more modular and easier to maintain.

# 5. Loop Control: The code now uses a `while` loop with a condition to control the flow of the program. This allows the player to continue playing the dice game until they choose to exit. The loop breaks when the player enters "exit" or "0" as the game choice, ensuring a smooth and controlled program execution.

# 6. Error Handling: Although comprehensive error handling has not been implemented in the code, it handles some potential errors, such as invalid input for the bet amount. By validating user input and handling specific cases, the code becomes more robust and user-friendly.

# 7. Improved User Interface: The code includes additional prints and formatting to create a more engaging and user-friendly interface. It provides clear instructions, prompts, and information to guide the player through the game and display the results.

# These improvements aim to enhance the readability, maintainability, and functionality of the code. However, it's essential to consider your specific requirements and further tailor the code to meet your needs.
