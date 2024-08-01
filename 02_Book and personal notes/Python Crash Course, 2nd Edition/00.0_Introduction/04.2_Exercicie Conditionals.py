def clear_console():
    print("\n"*6)

"""
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. 
Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

• Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)


alien_color = "Green"
choise_1 = input("Guess what the color of the alien:\t")
if choise_1 == alien_color:
    print("Excellent, your right, now you have 5 points.")
elif choise_1 != alien_color:
    print("Upss, you have falied")
else:
    print("Error, try again.")
clear_console()


5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
write an if-else chain. 

• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
• Write one version of this program that runs the if block and another that runs the else block.



choise_2 = input("What is the color of the Alien\t")
if choise_2 != "Green":
    print("Gratulations, you have won 10 points. ")
elif choise_2 == "Green":
    print("Excellent, your right, now you have 5 points.")
else:
    print("Error, try again.")


5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-
else chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed
for the appropriate color alien.  

while True:
    print("\nMenu:")
    print("1. Play the Alien Color Game")
    print("2. Exit")

    choice = input("\nEnter your option (1 or 2): ")

    if choice == '1':
        while True:
            choise_5 = input("What is the color of the Alien?\t").lower()  # Convert input to lowercase for consistency

            if choise_5 == "green":
                print("Congratulations, you have won 5 points.")
            elif choise_5 == "yellow":
                print("Excellent, you are right. Now you have 10 points.")
            elif choise_5 == "red":
                print("Excellent, you are right. Now you have 15 points.")
                break
            else:
                print("Error, try again.")

    elif choice == '2':
        print("Exiting the program. Goodbye!")
        break  # Exit the main loop and end the program

    else:
        print("Invalid choice. Please select 1 or 2.")
"""

"""
5-8. Hello Admin: Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user:
• If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for
logging in again.
"""

list_users = ["Andres", "Fabian", "Thiago", "Admin", "Augustín"]
for user in list_users:
    print(f"Hello dear {user}, a greeting for you!.")
    if user == "Admin":
        print("Would you like to see a status report?")
    elif user != "Admin":
        print(f"Hello {user}, thank you for logging in again.")
    else:
        print("ERROR")

"""
5-10. Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
current_users containing the lowercase versions of all existing users.)
"""


current_users = ["deivgonz777", "KingDeiv123", "KingG0ONZ", "HunterBitches", "senasdo123@"] # List of current usernames
new_users = ["papaps7882", "pretadorXXX", "venecoMAN", "achuchi@1234", "eliasimeon777@"] # List of new usernames to check

current_users_lower = [user.lower() for user in current_users] # Convert current users to lowercase for case-insensitive comparison
for new_user in new_users: # Check each new user
    if new_user.lower() in current_users_lower:
        print(f"The username '{new_user}' is already taken. Please choose a different username.")
    else:
        print(f"The username '{new_user}' is available.")

for not_available_user in current_users_lower:
    print(f"This user is not available: {not_available_user}")

"""
5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if-elif-else chain inside the loop to print the proper ordinal end-
ing for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
7th 8th 9th", and each result should be on a separate line.

"""

# List of numbers from 1 to 9
numbers = list(range(1, 10))

for number in numbers:
    if number % 10 == 1 and number != 11:
        suffix = "st"
    elif number % 10 == 2 and number != 12:
        suffix = "nd"
    elif number % 10 == 3 and number != 13:
        suffix = "rd"
    else:
        suffix = "th"
    print(f"{number}{suffix}")  # Print the number with its ordinal suffix
