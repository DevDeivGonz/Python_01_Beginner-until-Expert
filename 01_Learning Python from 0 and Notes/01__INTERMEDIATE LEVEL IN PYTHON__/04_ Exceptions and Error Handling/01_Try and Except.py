"""
The try, except, else, and finally blocks in Python are used for error handling. The try block contains code that might
raise an exception. If an exception occurs, the except block catches and handles it. The else block runs if no
exceptions are raised, and the finally block executes regardless of whether an exception occurred, making it useful for
cleanup operations like closing files or releasing resources.

"""
def exit_():
    print("Thank you for using the MATH-PLUS program.")
    exit()

def addition_numbers():
    try:
        number_add_1 = int(input("Enter the first number"))
        number_add_2 = int(input("Enter the second number"))
        result_addition = number_add_1 + number_add_2
    except ValueError:
        print("Error, enter validated value.")
    else:
        print(f"The result of {number_add_1} + {number_add_2} is: {result_addition}")
    finally: # Executes regardless of whether an exception was raised or not.
        print("Thank you for using the MATH-PLUS program.")
        menu()

def subtract_numbers():
    try:
        number_subs_1 = int(input("Enter the first number"))
        number_subs_2 = int(input("Enter the second number"))
        result_subs = number_subs_1 - number_subs_2
    except ValueError:
        print("Error, enter validated value.")
    else:
        print(f"The result of {number_subs_1} - {number_subs_2} is: {result_subs}")
    finally: # Executes regardless of whether an exception was raised or not.
        print("Thank you for using the MATH-PLUS program.")
        menu()


def multiply_numbers():
    try:
        number_multiplication_1 = int(input("Enter the first number"))
        number_multiplication_2 = int(input("Enter the second number"))
        result_multiplication_1 = number_multiplication_1 * number_multiplication_2
    except ValueError:
        print("Error, enter validated value.")
    else:
        print(f"The result of {number_multiplication_1} * {number_multiplication_2} is: {result_multiplication_1}")
    finally: # Executes regardless of whether an exception was raised or not.
        print("Thank you for using the MATH-PLUS program.")
        menu()

def divide_numbers():
    try: # Contains code that might raise an exception.
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        result = number1 / number2
    except ZeroDivisionError: # Catches and handles the exception.
        print("Error: Cannot divide by zero.")
    except ValueError: # Catches and handles the exception.
        print("Error: Invalid input. Please enter numeric values.")
    else: # Executes if no exception is raised.
        print("The division was successful. Result:", result)
    finally: # Executes regardless of whether an exception was raised or not.
        print("Thank you for using the MATH-PLUS program.")
        menu()


def menu():
    options = {
        1: addition_numbers,
        2: subtract_numbers,
        3: multiply_numbers,
        4: divide_numbers,
        5: exit_
    }

    while True:
        print("Menu:")
        print("1. Addition numbers")
        print("2. Subtraction numbers")
        print("3. Multiplication numbers")
        print("4. Divide numbers")
        print("5. Exit")
        request_user = int(input("Enter your choice: "))

        if request_user in options: # request_user in optionsme significa que si la opcion esta en el diccionario opciones entonces se ejecturara....
            try:
                options[request_user]() # los () llaman a la funcion (def) en el diccionario
            except ValueError:
                print("ERROR, enter a valid request.")
            finally:
                print()
        else:
            print("ERROR, please enter a valid option.")

if __name__ == "__main__":
    menu()
