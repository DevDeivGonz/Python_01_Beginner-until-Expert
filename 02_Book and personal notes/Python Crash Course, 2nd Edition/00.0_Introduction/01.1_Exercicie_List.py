def clear_per_space():
    print("\n"*4)

print("""3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner. """)

list_invited_dinner = ["Ricardo Chaves", "James Rodriguez", "Ronaldo Nazario", "Chespirito"]
print(f"Those are the invites of my dinner tonight\n {list_invited_dinner}")
print(f"I invited {list_invited_dinner[0]}\n I invited {list_invited_dinner[1]} \n I invited {list_invited_dinner[2]} \n I invited {list_invited_dinner[3]}")

clear_per_space()

print("""3-5. Changing Guest List:\n You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.""")

list_invited_dinner.insert(4, "Daniel Muñoz")
print(f"This is the new invited for make the dinner tonight with me, and it is {list_invited_dinner[4]}")

clear_per_space()

print("""\n• 
Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list. 
""")

print(f"This is the list {list_invited_dinner} and now this is the end item, {list_invited_dinner.pop()}")

clear_per_space()

print(""" 3-6. More Guests: 
. You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people 
  that you found a bigger dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
Introducing Lists 43
\n
""")

list_invited_dinner.insert (0, "Camilo Zuñiga")
middle_index = len(list_invited_dinner) // 2
list_invited_dinner.insert(middle_index, "Paolo Maldini") # Insert an element in the middle of the list
list_invited_dinner.append("Diego Milito")

print(f"here is the new list of guests; {list_invited_dinner}")

clear_per_space()

print("""
3-7. 
. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space 
  for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, 
  print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. 
  Print your list to make sure you actually have an empty list at the end of your program. \n \n""")


print(f"This is the numbers of guests {len(list_invited_dinner)}, however we only can choose 2 guests, and are:")

not_invited_1 = list_invited_dinner.pop(0)
not_invited_2 = list_invited_dinner.pop(0)
not_invited_3 = list_invited_dinner.pop(0)
not_invited_4 = list_invited_dinner.pop(0)
not_invited_5 = list_invited_dinner.pop(-1)


print(f"""\n \nBy this middle I notified you the list of the guests that not are invited for this dinner tonight, 
         apologize for the disadvantages, have a blessed day.
         1. {not_invited_1} 
         2. {not_invited_2}
         3. {not_invited_3}
         4. {not_invited_4}
         5. {not_invited_5}
\n \n""")

print(f"Good evening dear {list_invited_dinner[0]}, it's our pleasure to let you know that you are invited tonight.")
print(f"Good evening dear {list_invited_dinner[1]}, it's our pleasure to let you know that you are invited tonight.")
print("Final guest list:", list_invited_dinner)

del list_invited_dinner[:] # use this method for clear
print("This list was clear", list_invited_dinner)

clear_per_space()


print("""
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
through 3-7 (page 42), use len() to print a message indicating the number
of people you are inviting to dinner.
""")

