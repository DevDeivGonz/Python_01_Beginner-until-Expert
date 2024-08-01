import os
def limpiar_pantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

# Crear una lista
lista = [3, 1, 4, 2, 5]
print(f"Lista original: {lista}")

input("PASE CON ENTER")
limpiar_pantalla()

lista_usuario = []
nombre_apellido = input("Ingrese su nombre y apellido: ")

# Convertir el nombre y apellido en una lista de caracteres
lista_usuario.append(nombre_apellido)
print("Su Nombre y apellido es: ", lista_usuario)

input("PASE CON ENTER")
limpiar_pantalla()


