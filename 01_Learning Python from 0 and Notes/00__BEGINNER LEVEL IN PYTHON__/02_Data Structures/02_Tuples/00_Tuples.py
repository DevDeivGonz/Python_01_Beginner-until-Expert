#### TUPLESSSS !!!!!!
""" 
Tuplas:

LAS TUPLAS GUARDAN ELEMENTOS PERO QUE NO SE PUEDEN RETOCAR

Inmutables: Las tuplas no se pueden modificar una vez creadas. 
No se pueden agregar, eliminar o cambiar elementos dentro de una tupla.
Definidas por paréntesis: Las tuplas se definen utilizando paréntesis (). 
Los elementos se separan por comas.
Acceso por índice: Se puede acceder a los elementos de una tupla utilizando 
su índice entre corchetes [].

Almacenar datos que no cambian, como constantes, configuraciones o resultados de funciones.
Representar colecciones de elementos con un orden fijo que no se modificará.
Pasar datos de forma segura entre funciones o módulos, ya que no se pueden modificar accidentalmente.
 

# Crear una tupla inmutable
my_tuple = (1, 2, 3, 4, 5)

# Intentar modificar la tupla (genera un error)
my_tuple[0] = 10

# Acceder a un elemento por índice
first_element = my_tuple[0]  # first_element = 1


Listas:

Mutables: Las listas sí se pueden modificar después de su creación. 
Se pueden agregar, eliminar o cambiar elementos dentro de una lista.
Definidas por corchetes: Las listas se definen utilizando corchetes [].
Los elementos se separan por comas.
Acceso por índice: Se puede acceder a los elementos de una lista utilizando su
índice entre corchetes [].

Almacenar datos dinámicos que pueden cambiar con el tiempo, como listas de compras, listas de tareas o registros de datos.
Implementar algoritmos que requieren manipulación de listas, como ordenamiento, filtrado o búsqueda.
Modelar estructuras de datos jerárquicas, como árboles o grafos.

# Crear una lista mutable
my_list = [1, 2, 3, 4, 5]

# Agregar un elemento a la lista
my_list.append(6)

# Eliminar un elemento por índice
my_list.remove(3)

# Cambiar un elemento por índice
my_list[2] = 10

# Acceder a un elemento por índice
first_element = my_list[0]  # first_element = 1


"""

# es un conjunto de valores, no es lo mimso que una lista ya que 
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.71, "Deivid", "Gonzalez", "De Colombia")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) error
#print(my_tuple[-6]) error


print(my_tuple.count("Deivid"))
print(my_tuple.index("Gonzalez"))
print(my_tuple.index("De Colombia"))


# my_tuple [5]= 1.80 es un error // object does not support item assignment 

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

#tupla mutable o quiero una lista?

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Gonzalez"
my_tuple.insert(1, "Azul")
my_print = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

#tuples con valores inmutables

# del my_tuple [2 tYPEeRROR: "TPLE" ojject doesn´t support item sellection]

del my_tuple
# rint(my_tuple) NameError







