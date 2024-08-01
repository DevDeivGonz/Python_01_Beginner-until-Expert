import os
def limpiar_pantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

# Modificar un elemento
lista = [3, 1, 4, 2, 5]
lista[0] = 10
print("Lista modificada:", lista)
