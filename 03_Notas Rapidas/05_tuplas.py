def clear_space():
    print("\n\n\n\n")

coordinates = (10, 20, 30) # Crear una tupla
print(coordinates[1])  # Output: 20  Acceder a un elemento

clear_space()

"""
Métodos Comunes

count(item): Cuenta el número de veces que un elemento aparece en la tupla.
index(item): Retorna el índice de la primera aparición del elemento.
"""

# Crear una tupla de números usando inputs
tupla_inputs = (int(input("Enter first number: ")),
                int(input("Enter second number: ")),
                int(input("Enter third number: ")),
                int(input("Enter fourth number: ")))

print("The tuple of numbers is:", tupla_inputs)

clear_space()

usuario_1 = (input("Ingrese los nombres y apellidos del empleado."),
            input("Ingrese el numero de identidad"),
            input("Ingrese fecha de nacimiento"),
            (input("Ingrese el ID correspondiente")))

print(f"El usuario 1 es: {usuario_1}")
