# Listas y tipos de listas , Pyhton orientado a objetos, ya que cuando se manejan listas, ya 
#se esta usando un lenguaje para que sea orientado a objetos 
#sirven para alojar informacion y copilar almacenamiento 

import os
def limpiar_pantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

my_list = []  # Inicializa una lista vacía

""" LAS LISTAS GUARDAN ELEMENTOS 1 A 1 ORDENADOS"""

# Lista para añadir elementos
print(len(my_list))

my_list = [35, 24, 17, 68, 52, 30, 17]
print(my_list)

my_other_list = [35, 1.71, "Deivid", "Gonzo"]
print(type(my_other_list))

# Accediendo a elementos de la lista
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[2])
print(my_other_list[-3])
print(my_other_list[-2])
print(my_other_list[-1])
print(my_list.count(17))
#print(my_list * my_other_list) error

# Desempaquetando elementos de la lista
age, height, name, last_name = my_other_list
print(name)

my_other_list.append("Gonzo")
print("my_other_list")

my_other_list.insert(1,"Azul")
print(my_other_list)

my_other_list.remove("Gonzo")
print(my_other_list)
my_list.remove(30)
print(my_list)

my_other_list

# Accediendo al elemento en el índice 3 con verificación de longitud
if len(my_other_list) >= 4:
    print(my_other_list[3])
else:
    print("La lista no tiene suficientes elementos para acceder al índice 3.")

my_list = "Hola Python" # esto no es una lista
print(type(my_list))

#CONSTANTES 

my_list = ["Hola Python"] # esto si es una lista
print(my_list)
print(type(my_list))


my_new_list = my_list.copy 

my_list.clear()
print(my_list)
print(my_new_list)

