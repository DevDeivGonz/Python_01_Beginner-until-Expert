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
