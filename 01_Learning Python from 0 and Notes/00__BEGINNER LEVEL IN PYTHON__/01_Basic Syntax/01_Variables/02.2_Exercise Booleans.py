"""
In this exercise, you will create a simple guessing game where the user has to guess a secret number.
The program will provide hints indicating whether the guessed number is greater or less than the secret number.
The game will continue until the user guesses the correct number or chooses to exit.
"""
import random
import os  # Import the os module to clear the screen

secret_number = random.randint(1, 20)  # Generates a random secret number between 1 and 50
guessed_correctly = False

print("""
       Welcome to the guessing game. 
       
       You need to guess the number you believe is correct.
       
       Keep trying until you get it right, but if you give up type 'exit' to end the game.
       
       GOOD LUCKKKKKKKKKK !!!!!
       """)

while not guessed_correctly:
    user_guess = input("Enter your guess: ")

    if user_guess.lower() == "exit":
        print("Thanks for playing.")
        break

    if not user_guess:
        print("Please enter a value.")
        continue

    try:
        guess = int(user_guess)
    except ValueError:
        print("Please enter a valid value.")
        continue

    if guess < secret_number:
        print("Your guess is lower than the correct number.")
    elif guess > secret_number:
        print("Your guess is higher than the correct number.")
    else:
        print(f"Congratulations, you guessed the correct number: {secret_number}")
        guessed_correctly = True

    if not guessed_correctly:
        print("Try again.")

# Function to clear the screen
def clear_screen():
    print("\n" * 4 )
