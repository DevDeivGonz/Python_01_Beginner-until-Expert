print("Welcome! Here we will calculate the area of geometric shapes. Please use '.' for decimals.")

# Rectangle Area Calculation
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area_rectangle = length * width
print(f"The area of the rectangle is: {area_rectangle}")

# Square Area Calculation
side_a = float(input("Enter the length of side A of the square: "))
side_b = float(input("Enter the length of side B of the square: "))
area_square = side_a * side_b
print(f"The area of the square is: {area_square}")

# Triangle Area Calculation
base = float(input("Enter the base length of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area_triangle = base * height / 2
print(f"The area of the triangle is: {area_triangle}")
