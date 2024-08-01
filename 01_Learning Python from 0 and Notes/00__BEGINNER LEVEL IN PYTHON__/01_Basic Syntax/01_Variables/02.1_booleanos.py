"""
BOOLEANS

Booleans in Python are values that can be True or False. These values can be the result of evaluations
of expressions using comparison and logical operators. In the following, I will explain in detail and with examples how these operators work and how they are used in control structures such as while loops.
"""

import random

# Generate a random integer number between 1 and 10 (including both ends)
random_number = random.randint(1, 10)
print(f"The random number generated is: {random_number}")

# Generate a random integer number between 50 and 100
random_number_2 = random.randint(50, 100)
print(f"Another random number generated is: {random_number_2}")

###################################################################

import os
import random

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

import random

# Generate a random secret number between 1 and 100
secret_number = random.randint(1, 100)
guessed_correctly = False

print("Welcome to the guessing game!")
print("I have a secret number between 1 and 100.")
print("Try to guess it or type 'exit' to end the game.")

while not guessed_correctly:
    # Prompt the user to enter a number.
    user_input = input("Enter your guess: ")

    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        print("Thanks for playing. See you next time!")
        break

    # Try converting the input to an integer
    try:
        user_guess = int(user_input)
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Verify the user's guess
    if user_guess < secret_number:
        print("The secret number is greater than your guess.")
    elif user_guess > secret_number:
        print("The secret number is less than your guess.")
    else:
        print(f"Congratulations! You guessed the secret number that was {secret_number}.")
        guessed_correctly = True

    # Message to try again if not guessed correctly
    if not guessed_correctly:
        print("Try again.")

input("Press ENTER to exit...")

##############################################################################################################

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

input("Press ENTER to continue...")

clear_screen()
