import random

random_num = random.randint(1, 15)  # Generate a random number between 1 and 15
print(f"The random number generated is: {random_num}")

# Iterate over the range from 1 to random_num (inclusive)
for number in range(1, random_num + 1):
    print(number)

names = ["alice", "bob", "carol"]
capitalized_names = [name.capitalize() for name in names]
print(capitalized_names)  # Output: ["Alice", "Bob", "Carol"]

