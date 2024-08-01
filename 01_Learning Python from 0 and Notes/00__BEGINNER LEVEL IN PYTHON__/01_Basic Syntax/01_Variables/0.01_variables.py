# variables 

""" 

Variables and Data Types in Python
Variables

A variable is a name assigned to a value that is stored in memory. It is created using the = operator.

"""

""" int (Integers) """

age = 30

# Basic operations:

a = 10
b = 3
sum = a + b # 13
difference = a - b # 7
product = a * b # 30
quotient = a // b # 3 (integer division)
remainder = a % b # 1
power = a ** b # 1000 (10^3)

# Advanced Example:

large_number = 123456789012345678901234567890
bitwise_and = a & b # 2 (AND bit by bit)
bitwise_or = a | b # 11 (OR bit by bit)

""" float (Floating Point Numbers) """

price = 19.99

# Basic Operations:

a = 5.7
b = 2.3
sum = a + b # 8.0
difference = a - b # 3.4
product = a * b # 13.11
quotient = a / b # 2.4782608695652173

# Advanced Example:

import math
result = math.sqrt(16.0) # 4.0
rounded = round(2.34567, 2) # 2.35

""" str (Text Strings) """

# Basic Example:

name = "Alice"

# Basic Operations:

greeting = "Hello, " + name # "Hello, Alice"
length = len(name) # 5
character = name[0] # 'A' # 'A'

# Advanced Example:

multiline = """This is a 
multiline string."""
formatted = f"{name} is {age} years old." # "Alice is 30 years old."
split_str = "Alice, Bob, Charlie".split(", ") # ['Alice', 'Bob', 'Charlie']


""" bool (Boolean) """

# Truth values: True or False.
# Basic example:

is_active = True

# Basic operations:

a = True
b = False
conjunction = a and b # False
disjunction = a or b # True
negation = not a # False

# Advanced Example:

comparison = (5 > 3) # True
is_equal = (5 == 5) # True
combined = (5 > 3) and (5 == 5) # True

#######################################################################################################################################################################################

my_str_variable = "my string variable"
print (my_str_variable)

my_int_variable = 5
print (my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

#concatenation of variables in a print 
print(type(print (print (my_str_variable, str(my_int_to_str_variable), my_bool_variable))))
print(type(print ("My Text string xd")))
print("this is the value of:", my_bool_variable)

#Some System Functions 

print(len(my_int_to_str_variable))

#variables in a single line ! beware of abusing this syntax!
name, surname, alias, age = "Brains", "Moure", "MoureDev", 35
print("My name is:", name, surname, ",My age is:", age, "And my alias is", 35)

# Inputs
""""
#name = input("What is your name? ")
#age = input("How old are you? ")
print(name)
print(age)
"""""

# we change its type
name = 35
age = "Brians"
print(name)
print(age)

# Force the type?
address: str = "My address"
address = True 
address = 5
print (type(address))

#42intput asks for data 