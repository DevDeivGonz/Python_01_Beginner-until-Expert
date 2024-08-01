import random

# Function to clear the console
def clear_console():
    print("\n" * 6)

# Function for the guessing game
def guessing_game():
    random_number = random.randint(1, 20)  # Generate a random number between 1 and 20
    attempts = 0  # Initialize the number of attempts

    while True:
        try:
            guess = int(input("Guess the number: "))
            attempts += 1  # Increment the number of attempts

            if guess == random_number:
                print(f"CONGRATULATIONS, YOU GUESSED THE NUMBER IN {attempts} ATTEMPTS")
                break
            elif guess > random_number:
                print(f"THE NUMBER {guess} IS LOWER")
            else:
                print(f"THE NUMBER {guess} IS HIGHER")
        except ValueError:
            print("ERROR. PLEASE ENTER A VALID NUMERIC VALUE")

# Main function to run the game
def main():
    print("GUESSING GAME USING WHILE LOOP")
    print("""WELCOME, GUESS THE NUMBER YOU THINK IT IS,
          REMEMBER IT'S BETWEEN 1 AND 20.
          !!! GOOD LUCK !!!
          """)
    input("PRESS ENTER TO CONTINUE")
    clear_console()

    while True:
        guessing_game()
        response = input("""\n
                        DO YOU WANT TO CONTINUE?
                        PRESS ENTER TO CONTINUE
                        TYPE 'exit' TO END THE GAME
                        """).strip().lower()  # Remove spaces and convert to lowercase

        if response == 'exit':
            clear_console()
            print("HAVE A GREAT DAY")
            break  # Exit the main loop

# Check if the script is being run directly or imported as a module
if __name__ == "__main__":
    main()
