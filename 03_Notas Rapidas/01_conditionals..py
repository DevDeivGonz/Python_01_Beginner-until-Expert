# review conditionals
import random

number_random = random.randint(1, 41)

if number_random == 20:
    print(f"The number {number_random} is equal to 20")

elif number_random < 20:
    print(f"The number {number_random} is less than 20")

elif number_random > 20:
    print(f"The number {number_random} is greatest than 20")

