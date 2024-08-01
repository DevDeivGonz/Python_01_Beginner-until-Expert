"""
What is a Tuple?

    A tuple is an immutable sequence in Python. Unlike lists, once a tuple is created, its elements cannot be modified, added, or removed.
    Tuples are defined using parentheses () and can contain multiple items.

"""

def clear_space():
    print("\n"*6)

tuple_1 = (1,2,3,4,5,6)
print(tuple_1)
clear_space()

"""
center_work = input("Enter your warehouse of work: ")
user_id = int(input("Enter your ID employed: "))

user_info = (center_work, user_id)
print(f"Hello Dear employed, this is your employed information:\n {user_info}")
"""
clear_space()

print("this is the second example:\n")
# List of users, each represented by a tuple
users = [
    (1, 'Alice', 'Admin'),
    (2, 'Bob', 'User'),
    (3, 'Charlie', 'Moderator')
]

# Accessing data
for user_id, name, role in users:
    print(f"User ID: {user_id}, Name: {name}, Role: {role}")

clear_space()

products_purchased = [
    (1089922 , "Computer X129", 2000),
    (1199982, "Refrigerator", 345),
    (1031221, "cooker", 350),
    (1348899, "Sofa set", 1450)

]

for id_user, name_product, price in products_purchased:
    print(f"""This is the list of products:\n
              ID {id_user}, name of the product purchased is {name_product},
              this is the price of the product ${price}.
""")
    
