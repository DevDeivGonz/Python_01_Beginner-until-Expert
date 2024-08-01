"""
What is a Dictionary in Python?

A dictionary in Python is an unordered collection of items.
Each item is a key-value pair, where the key is a unique identifier used to access the corresponding value.
Dictionaries are mutable, which means you can change them by adding, modifying, or removing key-value pairs.

"""

def clear_space():
    print("\n"*5)

# Creating a dictionary using curly braces
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}
"""
# Creating a dictionary using the dict() function
my_dict = dict(name='Alice', age=25, city='New York')
"""

print(my_dict['name'])  # Output: Alice
print(my_dict['age'])  # Output: 25
print(my_dict["city"])

purchaseds = {
    "rexoma": 25000,
    "fabuloso": 13000,
    "presto-barber": 4500,
    "computer HP-279k": 2590000
}

print(f"Aqui estan sus compras: {purchaseds}")

clear_space()

# Creating a dictionary
student = {
    'name': 'Alice',
    'age': 25,
    'courses': ['Math', 'CompSci']
}

# Accessing values
print(student['name'])   # Output: Alice
print(student['courses'])  # Output: ['Math', 'CompSci']

# Adding a new key-value pair
student['email'] = 'alice@example.com'

# Modifying an existing key-value pair
student['age'] = 26

# Using the get() method
print(student.get('name'))  # Output: Alice
print(student.get('phone', 'Not Found'))  # Output: Not Found

# Using the update() method
student.update({'name': 'Alicia', 'age': 27})
print(student)  # Output: {'name': 'Alicia', 'age': 27, 'courses': ['Math', 'CompSci'], 'email': 'alice@example.com'}

# Using the pop() method
email = student.pop('email')
print(email)  # Output: alice@example.com
print(student)  # Output: {'name': 'Alicia', 'age': 27, 'courses': ['Math', 'CompSci']}

# Iterating over key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")

# Output:
# name: Alicia
# age: 27
# courses: ['Math', 'CompSci']

# ////////////////////////////////////////////////////////////

# proyect ALIENS

clear_space()

alien_0 = {'color': 'green',
           'points': 50,
           "damage": +243,
           "experience": "level 12"
}

print("the alien 0 and his skills: ")
print(alien_0['color'])
print(alien_0['points'])
print(alien_0["damage"])
print(alien_0["experience"])

# key-value adding new items in the dict
alien_0['x_position'] = 0 # adding new items in a dicts
alien_0['y_position'] = 25 # adding new items in a dicts
alien_0["Weapon"] = "sword" # like this you can add items
print(alien_0)

#///////////////////////////////////////////////////////////////////////7/777

clear_space()

# ///////////////////////////////////////////////////////////////////////
# dict for inventory using input

inventory = {}
"""
while True:
    product = input("Enter the purchased and their cost(or 'done' to finish): ")
    if product.lower() == 'done':
        break
    value_per_product = input("Enter a value: ")
    inventory[product] = value_per_product

print("\nThe dictionary you created is:")
for key, value in inventory.items():
    print(f"{key}: ${value}")

search_key = input("\nEnter a key to search for its value: ")
if search_key in inventory:
    print(f"The value for '{search_key}' is: {inventory[search_key]}")
else:
    print(f"'{search_key}' not found in the dictionary.")
    
"""
# //////////77////////////////////////////////////////////////////////////////////////

# other examples using dicts

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
z = car.values()

print(x) #before the change

car["color"] = "white" # with this method you can add more items in the dict

print(f"this is the dict:\n{x} and their values {z}")
for key, value in car.items(): # using method will return each item in a dictionary, as tuples in a list.
    print(f"This is thekey {key} and this is the value {value}.") #after the change

if "model" in car:
  print("Yes, 'model' is one of the keys in the cer dictionary")


clear_space()

def clear_space():
    print("\n"*5)

# nested dictionarys and their methods of how to do it

clientes_frecuentes = {

    "usuario_1" : {

        "name" : "juliana",
        "Emil": "19967kap@gmail.com",
        "year" : 2004,

    },

    "usuario_2" : {

        "name" : "felipe",
        "Emil": "189papasarroz@gmail.com",
        "year" : 1999,
    },

    "usuario_3" : {

        "name" : "Magnus",
        "Emil": "maguns19983qp@gmail.com",
        "year" : 1999,
    }
}


for key, value in clientes_frecuentes.items(): # Separately printing keys and values
    print(f"{key}:")
    for sub_key, sub_value in value.items():
        print(f"  {sub_key}: {sub_value}")


clear_space()

#copy a dict

backup_of_clientes_frecuentes = clientes_frecuentes.copy()
print(backup_of_clientes_frecuentes)

clear_space()


# dicts using INPUTS
def add_user_to_dict():
    dict_of_names = {}

    while True:
        add_more = input("Do you want to add a new user? (yes/no):\n").lower()
        if add_more == "no":
            break

        user_id = input("Enter user ID (e.g., user_1):\n")
        name = input("Enter your name:\n")
        last_name = input("Enter your last name:\n")
        age = int(input("Enter your age:\n"))

        dict_of_names[user_id] = {
            "name": name,
            "last_name": last_name,
            "age": age
        }

    return dict_of_names

# Recopilar datos del usuario
users = add_user_to_dict()

# Imprimir el diccionario para verificar
for user_id, user_info in users.items():
    print(f"{user_id}:")
    for key, value in user_info.items():
        print(f"  {key}: {value}")

clear_space()


