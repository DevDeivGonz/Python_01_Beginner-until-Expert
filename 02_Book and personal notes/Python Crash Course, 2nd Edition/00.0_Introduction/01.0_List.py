def clear_console():
    print("\n"*40)
def space_per_space():
    print("\n" * 3)


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

space_per_space()

"""
3-1. Names: Store the names of a few of your friends in a list called names. Print
each person’s name by accessing each element in the list, one at a time.
"""
friends = ["Ricardo", "Yudith", "Sofia", "Santiago"]
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])

space_per_space()

"""
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
printing each person’s name, print a message to them. The text of each message 
should be the same, but each message should be personalized with the
person’s name.
"""
print(f"Hello {friends[0]} Chavez, welcome to this program.")
print(f"Hello {friends[1]} Garcia, welcome to this program.")
print(f"Hello {friends[2]} Vergara, welcome to this program.")
print(f"Hello {friends[3]} Ayure, welcome to this program.")


space_per_space()

"""
3-3. Your Own List: Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
Honda motorcycle.”
"""
list_motorcycle = ["Honda", "Yamaha", "Gixxer", "Apache"]
print(list_motorcycle, "\nThis is the list of the motorcycles that exist in the inventary so far" + "\n"*2)
print(f"""I like {list_motorcycle[0]} for his designer, but his part are a lot cost,\n on another hand, I like {list_motorcycle[1]} but the whole
motorcycle is not worth the price,\n the motorcycle {list_motorcycle[2]} is my favorite so far, fast, economic and not so expensive in the cost,
and now we talk abot of {list_motorcycle[3]}, is so cool for beginners but not enought for me.""")

space_per_space()
list_motorcycle[0] = 'Ducati' # change the value of the list with this way
print(list_motorcycle)

space_per_space()

#using append() method
list_motorcycle.append("Suzuki")
list_motorcycle.append("Toyota")
list_motorcycle.append("lamborghini")
print(f"{list_motorcycle},\n this is the list but modified. " + "\n"*2)
print("adding elements in a list\n")

list_motorcycle.insert(5, "Mercedes") # whit this way you can insert any element but with the index that you delight choose
print(f"This is the new list: {list_motorcycle}")

space_per_space()
#using "del" method
del list_motorcycle[1] # deleted Yamaha
del list_motorcycle[5] # deleted Toyota
print(f"This is the new and evolved list: {list_motorcycle}")

space_per_space()

# using method pop() # remove the last item in a list
print(f"This is the last version of the list motorcycles {list_motorcycle}\n")
list_motorcycle.pop()
print(f"This is the new and evolved list using pop():\n {list_motorcycle}")
last_sell = list_motorcycle.pop()
print(f"The last selling in the warehouse of Motorcycles was {last_sell}")

space_per_space()

# using method remove(), remove a data manually with the name of the data
print("Using remove() method")
print(f"This is the last version of the list motorcycles {list_motorcycle}\n")
list_motorcycle.remove("Apache")
print(f"This is the new and evolved list using remove():\n {list_motorcycle}")

space_per_space()
# using method sort() # to order the numbers from smallest to largest number
print("Using sort() method")
list_motorcycle.sort()
number_motorcycles = [453340000, 34900, 1000000]
number_motorcycles.sort()
print(f"This is the list by order alphabetic {list_motorcycle} and their costs {number_motorcycles}")

space_per_space()

#using reverse method
print("Using reverse() method")
list_motorcycle.reverse()
number_motorcycles.reverse()
print(f"This is the reverese since of the list {list_motorcycle} and {number_motorcycles}")

space_per_space()

# using extend method
list_motorcycle.extend(["Honda", "Toyota", "Hummers", "Kawasaki"]) # for join 2 list and become to one list
print(f"This is the new list of the motorcycles, since we recevied new items, these are: {list_motorcycle} ")

space_per_space()

# using copy() method, Creates a shallow copy of the list.
print(list_motorcycle)
newList_of_vehicles = list_motorcycle.copy()
print(f"This the back up of the list of motorcycles {newList_of_vehicles}\n")
newList_of_vehicles.extend(["BMW", "Aston Martin", "Alfa Romero"])
print(f"This is the update list in the inventary.\n {newList_of_vehicles}")

space_per_space()

# Using the method count(), Returns the number of occurrences of a specified element in the list.
list_sells_vehicles = [2330, 10089, 2399, 1890, 289000, 2390, 2390, 2000, 7000, 2000, 50090, 289000, 2390, 2390]
count_of_sells = list_sells_vehicles.count(2390)
print("Count of sells for the value of $2330:", count_of_sells)

# using sorted() method, Only order or sort the sense of the list in one time, is not temporary as sort()
print("\nThis is the order of each sell\n", sorted(list_sells_vehicles), "\n")
print(f"This is the original sort of the lists {list_sells_vehicles}, and \n {newList_of_vehicles}")


