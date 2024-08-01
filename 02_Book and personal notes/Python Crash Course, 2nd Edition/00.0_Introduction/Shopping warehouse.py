def clear_console():
    print("\n"*5)

variable = "string", "int 123", "float 12.99", "bool V, F"

banano = "muchos bananos"
print(banano)

numero_gay = 1232334
print(numero_gay)

ventas = ["venta 1: 12.000", "venta 2: 34.000", "venta 3: 23.000"]

print(f"Ventas del dia {ventas}")

numero_1 = int(input("Ingrese el primer numero:\t"))
numero_2 = int(input("Ingrese el segundo numero:\t"))

resultado_suma = numero_1 + numero_2

print(f"La suma de {numero_1} y {numero_2}: {resultado_suma}")
result_resta = numero_1 - numero_2
print(f"La resta de {numero_1} y {numero_2}: {result_resta}")
result_mult = numero_1 * numero_2
print(f"La multiplicacion de {numero_1} y {numero_2}: {result_mult}")

if numero_1 or numero_2 == 0:
    print("Error: Division by zero!")
else:
    result_division = numero_1 / numero_2
    print(f"The result of {numero_1} / {numero_2}:", result_division)


clear_console()

# Prompt the user to enter products separated by spaces or commas
productos_input = input("Ingrese los productos separados por espacios o comas: ")

# Split the input string into a list of products
productos = productos_input.split()

# Initialize an empty list to store processed values
processed_productos = []

# Iterate over each item in productos
for producto in productos:
    if producto.isdigit():
        # Convert to integer if it's a digit and append to processed_productos
        processed_productos.append(int(producto))
    else:
        # Keep as a string and append to processed_productos
        processed_productos.append(producto)

# Print the result to see the processed values
print("Productos procesados:", processed_productos)
