import os

def clear_console():
    print("\n"*40)
clear_console()


mess = "message"
print(f"Here are {mess}")

name = "ada lovelace"
print(name.title())
print(mess.title()) # other way to print a strings

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

Albert_mess = "this is the magnificent of the universe, you will never find out the end of this extended universe."

print(f"Hello, {Albert_mess}")

input("ENTER TO CONTINUE\n")
clear_console()

number_1 = int(input("Enter the number 1: "))
number_2 = int(input("Enter the number 2: "))
result_sum = number_1 + number_2
result_substracs = number_1 - number_2
result_multiplication = number_1 * number_2
result_divide = number_1 / number_2

print(f"The addition of {number_1} and {number_2} is : {result_sum}")
print(f"The substraction of {number_1} and {number_2} is : {result_substracs}")
print(f"The multiplication of {number_1} and {number_2} is : {result_multiplication}")
print(f"The division of {number_1} and {number_2} is : {result_divide}")

input("ENTER TO CONTINUE\n")
clear_console()

def decimal_to_binary():
    number = int(input("Enter the decimal number to convert to binary: "))
    original_number = number  # Keep track of the original number
    binary_representation = ''

    if number == 0:
        return original_number, "0"

    while number > 0:
        remainder = number % 2
        binary_representation = str(remainder) + binary_representation
        number = number // 2

    return original_number, binary_representation



# Call the function and print the results
decimal_number, binary_result = decimal_to_binary()
print(f"The decimal number is: {decimal_number}")
print(f"The binary representation is: {binary_result}")

input("ENTER TO CONTINUE\n")
clear_console()

favorite_language = input("Enter your personal words\t")
favorite_language = favorite_language.rstrip()

print(favorite_language.rstrip()) # Removes trailing whitespace (spaces, tabs, newlines) or specified characters from the right end of a string.
print(favorite_language.lstrip()) # Removes leading whitespace or specified characters from the left end of a string.
print(favorite_language.strip())  # Removes leading and trailing whitespace or specified characters from both ends of a string.

"""
2-7. Stripping Names: Use a variable to represent a person’s name, and include
some whitespace characters at the beginning and end of the name. Make sure
you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip().
"""
person_name = input("\nEnter your full name\t")
person_name.lstrip()
print(f"\nThis is your personal information {person_name.lstrip()}")

input("Enter to CONTINUE ")

# Read the input from the user
user_input = input("Enter the list of your personal market: ")

# Split the input string by spaces
parts = user_input.split()

# Process the parts
result = []
for part in parts:
    if part.isdigit():
        # Convert to integer if it's a digit
        result.append(int(part))
    else:
        # Keep as a string if it's not a digit
        result.append(part)

# Print the result to see the processed values
print(result)


