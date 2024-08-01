"""

In Python, while and for are two control structures used to create loops, that is,
to repeatedly execute a block of code. However, there are important differences between them.

WHILE
The while statement executes a block of code as long as a condition is true.
The condition is evaluated before each iteration of the loop, and if it is True, the block of code is executed. If it is False, the loop stops.

"""

# Import the os module to clear the console (optional)
import os

print("WHILE AND ITS USES FROM BASIC TO ADVANCED")

# Function to clear the console
def clear_console():
    print("\n" * 4)

# Initialize a counter variable
counter = 0

# While loop: Executes as long as the condition is True
while counter < 100:
    print(counter)  # Print the current value of counter
    counter += 3**2  # Increment the counter by 3 squared (9)

# Reinitialize the counter variable
counter = 0

# Another while loop with different increment
while counter < 100:
    print(counter)
    counter += 5**2  # Increment the counter by 5 squared (25)

# Clear the console
clear_console()

# Initialize a new counter variable
count = 0

# Another while loop with a different increment
while count <= 20:
    print(count)
    count += 2*2  # Increment the counter by 2 multiplied by 2 (4)


# its better (for) for counts numbers but it is an alternative.
