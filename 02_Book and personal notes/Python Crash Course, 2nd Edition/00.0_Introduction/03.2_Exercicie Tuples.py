"""

4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.

• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the change.
• The restaurant changes its menu, replacing two of the items with different foods.
  Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

"""
def clear_console():
    print("\n"*4)

foods_buffet = ("Arepas", "Empanadas", "Ajiaco", "Bandeja Paisa", "Sancocho")
print("This is the food there is in the restaurant tonight:\n")
for food in foods_buffet:
    print(food)

clear_console()

"""
Write a Python program that performs the following tasks:

    Prompts the user to enter names separated by commas.
    Splits the input string into individual names.
    Converts the list of names into a tuple.
    Prompts the user to enter an index to retrieve a name from the tuple.
    Prints the name at the specified index.
    Handles any potential errors, such as the user entering an invalid index.
"""



def create_list_employed():
    input_name = input("Enter the first and last name of the employed:\t ")
    user_names = input_name.split(',')
    list_employeds = tuple(user_names)

    for name_user in list_employeds:
        print(name_user)

    input("Press Enter to continue...")
    clear_console()

    while True:
        choise_sub = input("Do you want to follow up here:\n"
                       "\n[1]. Still\n"
                       "\n[2]. Return to main menu\n")
        if choise_sub == "1":
            create_list_employed()
        elif choise_sub == "2":
            display_menu()
        else:
            print("Error. Enter a valided choise.")


def display_menu():
    print("\nMenu:\n")
    print("1. Created a list of employeds.")
    print("2. Exit\n")
    while True:

        choice = input("\nEnter your option:\t ")

        if choice == '1':
            create_list_employed()
        elif choice == '2':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

display_menu()