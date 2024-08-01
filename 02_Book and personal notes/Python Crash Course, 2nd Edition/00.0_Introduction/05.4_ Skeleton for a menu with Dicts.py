
def option_one():
    print("Option 1 selected.")
    # Add functionality for Option 1

def option_two():
    print("Option 2 selected.")
    # Add functionality for Option 2

def option_three():
    print("Option 3 selected.")
    # Add functionality for Option 3

def exit_program():
    print("Exiting the program. Goodbye!")
    exit()  # Exit the program

def display_menu():
    """Displays the menu and handles user input."""
    menu_options = {
        1: {"description": "Option 1", "function": option_one},
        2: {"description": "Option 2", "function": option_two},
        3: {"description": "Option 3", "function": option_three},
        0: {"description": "Exit", "function": exit_program}
    }

    while True:
        print("Menu:")
        for key, value in menu_options.items():
            print(f"{key}. {value['description']}")

        user_choice = int(input("Please choose an option (1-3, 0 to exit): "))

        if user_choice in menu_options:
            menu_options[user_choice]["function"]()
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    display_menu()
