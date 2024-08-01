"""
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
pizza names in a list, and then use a for loop to print the name of each pizza.

• Modify your for loop to print a sentence using the name of the pizza
instead of printing just the name of the pizza. For each pizza you should
have one line of output containing a simple statement like I like pepperoni
pizza.

• Add a line at the end of your program, outside the for loop, that states
how much you like pizza. The output should consist of three or more lines
about the kinds of pizza you like and then an additional sentence, such as
I really love pizza!
"""

def clear_space():
    print("\n"*2)

def clear_many_spaces():
    print("\n"*6)

list_pizzas = ["Pepperoni Pizza", "Margherita Pizza", "Meat Pizza", "BBQ Chicken Pizza"]

print("\nThis is the menu today:\n")
for pizza in list_pizzas:
    print(pizza)

clear_space()

for pizza in list_pizzas:
    print("\nI like", pizza, "\n")

print(f"I like this kind of pizzas:\n {list_pizzas}, I really love the pizza")

clear_many_spaces()

"""
4-2. Animals: Think of at least three different animals that have a common characteristic. 
Store the names of these animals in a list, and then use a for loop to print out the name of each animal.

• Modify your program to print a statement about each animal, such as A dog would make a great pet.
• Add a line at the end of your program stating what these animals have in common. 
You could print a sentence such as Any of these animals would make a great pet!
"""

list_animals = ["Lion", "Tiger", "Leopard"]

for animal in list_animals:
    print(animal)

for animal in list_animals:
    print(f"{animal}, have a common characteristic with the others animals, it is are hunters, eat meat by them prey")

clear_space()
"""
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

"""

for number in range(1,21):
    print(number)

clear_space()

""" 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
     (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)
"""


clear_space()



"""
     
4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your 
     list actually starts at one and ends at one million. 
     Also, use the sum() function to see how quickly Python can add a million numbers.
     
"""

million_numbers = list(range(1, 1000001))
print(million_numbers)
print("First 5 numbers:", million_numbers[:10]) # like this you verify the order of queues in the list
print("Last 5 numbers:", million_numbers[-10:])

min_value = min(million_numbers)
max_value = max(million_numbers)
print(f"""
This is the minimum value in the list: {min_value}
This is the maximum value in the list: {max_value}
""")
total_sum = sum(million_numbers)
print(f"This is the result of the sum of all number in the list of 1000000\n {total_sum}")


clear_space()

"""
4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. 
     Use a for loop to print each number."""

for odd_number in range(1, 20, 2):
    print(odd_number)

clear_space()

"""
4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
"""
print("List of the multiples of 3")
for tree in range(3,31):
    if tree % 3 == 0:
        print(tree)

clear_space()

"""
4-8. Cubes: A number raised to the third power is called a cube. For example,the cube of 2 is written as 2**3 in Python. 
     Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), 
     and use a for loop to print out the value of each cube."""

for number_raise in range(1, 11):
    cube = number_raise ** 3
    print(f"{number_raise}**3 : {cube}")
clear_space()
for nr in range(1,16):
    n_raise = nr ** 8
    print(f"{nr} ** 8 : {n_raise}")


"""
4-9. Cube Comprehension: Use a list comprehension to generate a list of the
first 10 cubes.
"""
raise_n = [nr ** 3 for nr in range(1,11)]
print(raise_n)

clear_space()

"""
4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:

• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Use a slice to print the last three items in the list.
"""
manufactory_items = ["Tables", "Apples", "Creppers", "Oranges", "Toyota", "Alicia Kennedy", "2 bools"]
for name_item in manufactory_items[:3]:
    print(name_item)

print(len(manufactory_items))

for n in manufactory_items[3:]:
    print(n)


for nm in manufactory_items[4:]:
    print(nm)

clear_space()

"""
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
(page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite
pizzas are:, and then use a for loop to print the first list. Print the message
My friend’s favorite pizzas are:, and then use a for loop to print the sec-
ond list. Make sure each new pizza is stored in the appropriate list.
"""


friend_pizzas = list_pizzas[:]

list_pizzas.append("Hacker Pizza")
friend_pizzas.append("Developer Pizza")
print(f"This is the original list of pizzas again:\n {list_pizzas}\n")
print(f"This is the NEW list of pizzas again:\n {friend_pizzas}\n")

for pizza_n in list_pizzas:
    print(f"My favorite pizza are: {pizza_n}")

for pizza_f in friend_pizzas:
    print(f"My favorite pizza are: {pizza_f}")

clear_space()

"""
4-12. More Loops: All versions of foods.py in this section have avoided using
for loops when printing to save space. Choose a version of foods.py, and
write two for loops to print each list of foods.
"""

list_pizzas
print("This is the list of the Pizzas today: ")
for pizza in list_pizzas:
    print(pizza)

list_animals
print("This is the list of the Animals in the ZOO today: ")
for animal in list_animals:
    print(animal)
