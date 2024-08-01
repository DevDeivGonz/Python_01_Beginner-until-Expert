# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 00:16:47 2024

@author: Laptop
"""

"""
Crea una lista de números enteros del 1 al 20 y luego realiza las siguientes operaciones:

1. Encuentra y muestra el número más grande y el más pequeño de la lista.
2. Calcula y muestra la suma de todos los números en la lista.
3. Filtra y muestra solo los números pares de la lista.
4. Duplica cada elemento de la lista y muestra la nueva lista.
5. Cuenta cuántos números son mayores que 10 en la lista.
"""
import itertools

numbers_list = [1,2,3,4,5,6,7,8,9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

max_number = numbers_list[19]
min_number = numbers_list[0]

print(f"Aqui esta el número más grande y el más pequeño de la lista {max_number} y el numero menor es {min_number}")

# 2.
suma = 0
for numero in range(1, 20 ):
    suma += numero
# la variable  suma muestra la suma y numero los numeros que hay
print("Aqui esta el resultado de las suma de los numeros del 1 al 20: ", suma)

# 3. Filtra y muestra solo los números pares de la lista.

for pares in numbers_list:
    if  pares % 2 == 0:
        print("Aqui estan los numeros pares", pares)

# 4. Duplica cada elemento de la lista y muestra la nueva lista.

duplicated_numbers = []

# Duplicar cada número en la lista
for number in numbers_list:
    duplicated_number = number * 2
    duplicated_numbers.append(duplicated_number)

# Imprimir los números duplicados
print("Aquí están los números duplicados desde el 1 al 20: ", duplicated_numbers)


# 5. Cuenta cuántos números son mayores que 10 en la lista.
count_greater_than_10 = 0

# Iterar sobre cada número en la lista
for number in numbers_list:
    if number > 10:
        count_greater_than_10 += 1

# Imprimir el resultado
print("El número de elementos en la lista que son mayores que 10 es:", count_greater_than_10)