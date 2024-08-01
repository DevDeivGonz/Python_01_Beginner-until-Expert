def clear_space():
    print("\n" * 3)

"""
The loop or BUCKLE FOR is a indefinite BUCKLE, that it used for buckle with a determinate repetitions.

When writing your own for loops that you can choose any name you want for the temporary variable that will be associated with
each value in the list. However, it’s helpful to choose a meaningful name that represents a single item from the list. For example,
here’s a good way to start a for loop for a list of cats, a list of dogs, and a general list of items:

for cat in cats:

for dog in dogs:

for item in list_of_items:

"""
# for using for variables
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!") # the method title() become the first index become in an upper
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

winners_COP_world = ["Germany", "Italy", "Argetina", "France", "Spain", "Brazil"]
for country in winners_COP_world:
    print(country,"Was the World Champion\n")

clear_space()

# for using with numbers

for value in range(-1, 6): #range count de numbers, in this cause count from 0 until 6
    print(value)

clear_space()

numbers = list(range(1,11)) # like this is how to do a list with range
print(numbers)
even_numbers = list(range(2, 45, 2)) # the first number begin to count from 3 and count each 2 times for the last item
print(even_numbers)

odd_numbers = list(range(3,45,2))
print(odd_numbers)

tableof_5 = list(range(5,55, 5))
print(tableof_5)

clear_space()

# table of 2 elevated itself
squares = []
for value in range(2, 50, 2):
 square = value ** 2
 squares.append(square)
 print(squares)

 clear_space()

 # Simple Statistics with a List of Numbers

 digits = [1,2,3,4,5,6,7,8,9,0]
 min(digits)
 max(digits)
 sum(digits)

# List Comprehensions

squares = [value**2 for value in range(1, 11)]
print(squares)

table_table_3 = [ tree_table * 3 for tree_table in range(1, 11)]
print(table_table_3)

music = [song for song in ["Metal", "Rock", "Pop", "Rap"]]
print(music)
print(music[:1])
clear_space()

names = ["alice", "bob", "carol"]
capitalized_names = [name.capitalize() for name in names] # method in Python is a string method used to convert the first character of a string to uppercase


