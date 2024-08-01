import os
def limpiar_pantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
        


numero1 = [1,2,4,56,67,100, 0]
numero2 = [1,2,4,56,67,100, 10]

# Acceder a elementos
numero1.extend(numero2) # extent  agrega todos los elementos de una lista a otra
print(f"Primer elemento: {numero1}")
print(f"Último elemento: {numero2}")
numero1.append ([-101001, 56, -123]) # apppend agrega un dato que no este en una lista
print(f"{numero1}")
primer_elemento = numero1[0]
z = numero1[7]
print("z:", z) 

# Crear una lista
numeros3 = [10, 20, 30, 40, 50]

# Convertir cada elemento a una cadena y unirlos con una coma y un espacio
numeros3_str = ', '.join(map(str, numeros3))
print("Lista sin corchetes:", numeros3_str)  # Salida: Lista sin corchetes: 10, 20, 30, 40, 50

