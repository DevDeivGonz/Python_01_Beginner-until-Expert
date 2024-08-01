"""   

append(): Agrega un elemento al final de la lista.

extend(): Extiende la lista agregando los elementos de otra lista al final.

insert(): Inserta un elemento en una posición específica.

remove(): Elimina la primera ocurrencia de un elemento específico.

pop(): Elimina y devuelve el elemento en la posición dada (o el último si no se especifica).

index(): Devuelve el índice de la primera ocurrencia de un elemento.

count(): Devuelve el número de veces que aparece un elemento en la lista.

sort(): Ordena los elementos de la lista in situ.

reverse(): Invierte el orden de los elementos de la lista in situ.

clear(): Elimina todos los elementos de la lista.

copy(): Retorna una copia superficial de la lista.

len(): Retorna la longitud (número de elementos) de la lista, los cuenta, sea palabras, caracteres, unidades en listas, sets, duplas o diccionarios, cuenta la longitud de cuantos hay 

min(): Retorna el elemento mínimo de la lista.

max(): Retorna el elemento máximo de la lista.

sum(): Retorna la suma de todos los elementos de la lista.

any(): Retorna True si algún elemento de la lista es verdadero, False de lo contrario.

all(): Retorna True si todos los elementos de la lista son verdaderos, False de lo contrario.

sorted(): Retorna una nueva lista ordenada a partir de los elementos de la lista original.

index(): Retorna el índice del primer elemento que sea igual al valor especificado.

count(): Retorna el número de veces que aparece un elemento en la lista.
    

"""

# Crear una lista
lista = [3, 1, 4, 2, 5]
print("Lista original:", lista)

# Acceder a elementos
primer_elemento = lista[0]
ultimo_elemento = lista[-1]
print("Primer elemento:", primer_elemento)
print("Último elemento:", ultimo_elemento)

# Slicing (Corte)
sublista = lista[1:4]
print("Sublista:", sublista)

# Modificar un elemento
lista[0] = 10
print("Lista modificada:", lista)

# Modificar un rango de elementos
lista[1:3] = [20, 30]
print("Lista modificada por rango:", lista)

# Método append()
lista.append(6)
print("Después de append:", lista)

# Método extend()
lista.extend([7, 8])
print("Después de extend:", lista)

# Método insert()
lista.insert(1, 'a')
print("Después de insert:", lista)

# Método remove()
lista.remove('a')
print("Después de remove:", lista)

# Método pop()
elemento = lista.pop()
print("Elemento eliminado con pop:", elemento)
print("Después de pop:", lista)

# Método index()
indice = lista.index(4)
print("Índice del elemento 4:", indice)

# Método count()
cuenta = lista.count(2)
print("Número de veces que aparece 2:", cuenta)

# Método sort()
lista.sort()
print("Después de sort:", lista)

# Método reverse()
lista.reverse()
print("Después de reverse:", lista)

# Método clear()
lista.clear()
print("Después de clear:", lista)

# Concatenación
lista1 = [1, 2]
lista2 = [3, 4]
lista3 = lista1 + lista2
print("Después de concatenar:", lista3)

# Repetición
lista_repetida = lista1 * 2
print("Después de repetir:", lista_repetida)

# Slicing (Corte)
sublista = lista3[1:3]
print("Sublista:", sublista)

# Comprensión de listas
cuadrados = [x**2 for x in lista3]
print("Cuadrados:", cuadrados)

# Función len()
longitud = len(lista3)
print("Longitud de la lista:", longitud)


# Creación de una lista
lista = [3, 1, 4, 2, 5]
print("Lista original:", lista)

# Acceso a elementos
primer_elemento = lista[0]
ultimo_elemento = lista[-1]
print("Primer elemento:", primer_elemento)
print("Último elemento:", ultimo_elemento)

# Modificación de un elemento
lista[0] = 10
print("Lista modificada:", lista)

# Agregar un elemento al final
lista.append(6)
print("Después de append:", lista)

# Extender la lista con otra lista
lista.extend([7, 8])
print("Después de extend:", lista)

# Insertar un elemento en una posición específica
lista.insert(1, 'a')
print("Después de insert:", lista)

# Eliminar un elemento específico
lista.remove('a')
print("Después de remove:", lista)

# Eliminar y devolver el último elemento
elemento = lista.pop()
print("Elemento eliminado con pop:", elemento)
print("Después de pop:", lista)

# Obtener el índice de un elemento
indice = lista.index(4)
print("Índice del elemento 4:", indice)

# Contar el número de veces que aparece un elemento
cuenta = lista.count(2)
print("Número de veces que aparece 2:", cuenta)

# Ordenar la lista
lista.sort()
print("Después de sort:", lista)

# Invertir el orden de la lista
lista.reverse()
print("Después de reverse:", lista)

# Limpiar la lista
lista.clear()
print("Después de clear:", lista)


import statistics

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Encontrar la mediana de la lista
median_number = statistics.median(numbers_list)

print("La mediana es:", median_number)

"""Si quieres implementar la búsqueda de la mediana sin usar la biblioteca statistics, puedes hacerlo manualmente ordenando la lista y luego encontrando el valor medio:"""

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Ordenar la lista
sorted_list = sorted(numbers_list)

# Encontrar la mediana
n = len(sorted_list)
if n % 2 == 1:
    median_number = sorted_list[n // 2]
else:
    median_number = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2

print("La mediana es:", median_number)
