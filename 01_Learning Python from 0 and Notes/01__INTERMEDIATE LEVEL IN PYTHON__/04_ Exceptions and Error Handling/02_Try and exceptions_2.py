def addition_numbers():
    try:
        number_add_1 = int(input("Enter the first number: "))
        number_add_2 = int(input("Enter the second number: "))
        result_addition = number_add_1 + number_add_2
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    else:
        print(f"The result of {number_add_1} + {number_add_2} is: {result_addition}")
    finally:
        print("Thank you for using the MATH-PLUS program.")

def subtract_numbers():
    try:
        number_subs_1 = int(input("Enter the first number: "))
        number_subs_2 = int(input("Enter the second number: "))
        result_subs = number_subs_1 - number_subs_2
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    else:
        print(f"The result of {number_subs_1} - {number_subs_2} is: {result_subs}")
    finally:
        print("Thank you for using the MATH-PLUS program.")


# asi se usarian los try y exceptios pero con los conditionals y con el bucle while

def menu():
    while True:
        print("Menu:")
        print("1. Addition numbers")
        print("2. Subtract numbers")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            try:
                addition_numbers()
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                print()

        elif choice == 2:
            try:
                subtract_numbers()
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                print()

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("ERROR: Please enter a valid option.")

if __name__ == "__main__":
    menu()
