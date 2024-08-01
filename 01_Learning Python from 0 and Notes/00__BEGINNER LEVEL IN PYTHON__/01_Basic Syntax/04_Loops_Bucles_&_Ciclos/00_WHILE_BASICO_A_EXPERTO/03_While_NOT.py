
import os

print("USAGE OF WHILE NOT")


# Function to clear the screen
def clear_console():
    print("\n" * 6)


def main_menu():
    print("""WELCOME TO THE MAIN MENU
          \nPLEASE CHOOSE AN OPTION
          \n""")
    print("1. Data entry validated negatively")
    print("2. Wait until an inverse condition is met")
    print("3. Iterate until a desired state is reached")
    print("4. Processing lists or data structures")
    print("5. Exit")

    while True:
        try:
            option = int(input("Enter an option: "))
        except ValueError:
            print("Invalid input. Enter a valid option.")
            continue  # Return to the beginning of the loop to request new input

        if option == 1:
            submenu_negative_numbers()
        elif option == 2:
            submenu_wait_condition()
        elif option == 3:
            submenu_iteration_state()
        elif option == 4:
            submenu_processing_lists_data()
        elif option == 5:
            print("Thank you for choosing us, see you next time!")
            break  # Exit the while loop
        else:
            print("Invalid option. Try again.")


def submenu_negative_numbers():
    number = 0
    while True:
        clear_console()
        print("""Negatively validated data entry.
              \nWhen you want to ask the user to enter data until they provide valid input,
              you can use while not to execute the code block while the user's input is not valid.
        \nNEGATIVELY VALIDATED DATA ENTRY.
        \nSelect an option:
        \n""")
        print("1. Enter a positive number")
        print("2. Return to the main menu")

        try:
            option = int(input("\nSelect an option: "))
        except ValueError:
            print("Invalid input. Try again.")
            continue

        if option == 1:
            while not number > 0:
                try:
                    number = int(input("Enter a positive number: "))
                    if number <= 0:
                        print("The entered number is not valid. Try again.")
                except ValueError:
                    print("Invalid input. Try again.")

            print(f"Well done! You entered a positive number: {number}")
        elif option == 2:
            main_menu()  # Return to the main menu
            break
        else:
            print("Invalid option. Try again.")


def submenu_wait_condition():
    # Code for the second submenu goes here
    # Wait until the user does not enter "exit"
    response = ""
    print("""Wait until an inverse condition is met
          \nSometimes, it can be more natural to think in terms of what we don't want to happen instead of what we want 
          to happen. In those cases, while not can be useful to execute a code block until a specific condition becomes true.
          """)
    print("1. Enter a positive number")
    print("2. Return to the main menu")

    try:
        option = int(input("\nSelect an option: "))
    except ValueError:
        print("Invalid input. Try again.")

    if option == 1:
        while not response == 'exit':
            response = input("Type 'exit' to end the program: ")
            if not response == 'exit':
                print("Incorrect response. Try again.")
    else:
        main_menu()
        clear_console()


def submenu_iteration_state():
    print("""Iterate until a desired state is reached
          \nSometimes, it can be more natural to think in terms of what we don't want to happen instead of what we want 
          to happen. In those cases, while not can be useful to execute a code block until a specific condition becomes true.
          """)
    print("1. Wait until an inverse condition is met")
    print("2. Return to the main menu")

    try:
        option = int(input("\nSelect an option: "))
    except ValueError:
        print("Invalid input. Try again.")

    counter = 0
    target_number = 10

    if option == 1:
        while not counter == target_number:
            print(f"Counter: {counter}")
            counter += 1
    else:
        main_menu()
        clear_console()

    # Code for the third submenu goes here
    main_menu()


def submenu_processing_lists_data():
    print("""Processing lists or data structures: 
          \nYou can use while not to traverse a list or a data structure until it is completely processed or 
          a specific exit condition is met.
          """)
    print("1. Processing lists or data structures")
    print("2. Return to the main menu")

    try:
        option = int(input("\nSelect an option: "))
    except ValueError:
        print("Invalid input. Try again.")

    numbers = [1, 2, 3, 4, 5, -1, 6, 7, 8, 9, 10]
    index = 0

    if option == 1:
        while not numbers[index] < 0:
            print(f"Number at index {index}: {numbers[index]}")
            index += 1

        print("A negative number has been found")
    else:
        main_menu()


if __name__ == "__main__":
    main_menu()
