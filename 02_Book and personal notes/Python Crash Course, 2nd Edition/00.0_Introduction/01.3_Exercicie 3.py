
def clear_console():
    print("\n"*3)

my_list = []

print("Welcome")
full_name = input("Enter your full name ")
shift = input("Enter the shift you belong to ")
age = int(input("Enter your age "))
my_list = [{full_name}, {shift}, {age}]
print(f"Welcome {full_name}, you belong to the {shift} shift and your age is {age} years old")

if age < 18:
    print(f"You are underage")
else:
    print(f"You are an adult")

if age > 18:
    print(f"You are an adult")
else:
    print(f"You are underage")

clear_console()

list_products = []

product_purchased = input("Enter the product purchased by you:\n")
cost_product = int(input("Enter what was the cost of the purchased:\n"))
list_products = [{product_purchased}, {cost_product}]
print(f"The products purchased are: {product_purchased} and the total cost is: {cost_product}")