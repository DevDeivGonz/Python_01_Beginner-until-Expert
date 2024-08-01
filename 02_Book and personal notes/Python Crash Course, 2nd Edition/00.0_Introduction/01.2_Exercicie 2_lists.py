def clear_space():
    print("\n"*5)


print("""
3-8. Seeing the World: Think of at least five places in the world you’d like to
visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly,
just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the
actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse alphabetical order without chang-
ing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse() to change the order of your list. Print the list to show that its
order has changed.
• Use reverse() to change the order of your list again. Print the list to show
it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the
list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse alphabetical order.
Print the list to show that its order has changed.
""")

clear_space()

list_places = ["Turn eiffel", "Stadium Santiago Bernabeut", "The Palace Topkapi Palace ", "Google Center", "Replay´s Aquarium of Canada", "The Museum of Science"]
print(list_places, "\n")
print(sorted(list_places))
print(list_places, "\n")
reverse_list = sorted(list_places, reverse = True)
print(f"This list in reverse alphabetical order without changing the order of the original list {reverse_list}\n\n")
print("This is the original list\n", list_places, "\n\n")
list_places.reverse()
print("This the list using reverse method:\n", list_places, "\n")
list_places.reverse()
print("This the list used for second time the reverse method:\n", list_places, "\n")
list_places.sort()
print(f"This is the list, however to change the list in alphabetical order: \n {list_places}\n")
list_places.sort(reverse = True) # used for change any order in the variables or lists.
print(f"This is the list, however to change for second time the list in alphabetical order: \n {list_places}\n")
