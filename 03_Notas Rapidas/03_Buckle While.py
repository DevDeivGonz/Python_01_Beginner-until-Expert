def clear_space():
    print("\n\n\n")

count = 0
while count < 5:
    print(count)
    count += 1

clear_space()

numbers = 1
while numbers < 21:
    print(numbers)
    numbers *= 2

clear_space()

def review_numbers():
    print("Hello, in building....")
    menu()
def create_new_numbers():
    print("Hello, in building....")
    menu()

def exit_():
    print("Hello, bye bye....")
    exit()

def menu():
    print("""
        1. Review numbers
        2. Create new numbers
        3. Exit
    """)
    answer = int(input("Enter a choise"))
    while True:
        if answer == 1:
            review_numbers()
        elif answer == 2:
            create_new_numbers()
        elif answer == 3:
            exit_()
            break
        else:
            print("ERROR, enter a valid choose.")

if __name__ == "__main__":
    menu()

