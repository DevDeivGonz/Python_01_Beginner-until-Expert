# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:28:06 2024

@author: Laptop
"""

""" 
10) Hacer un programa que muestre el siguiente dibujo.
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
"""

print("""
      * * * * * * * * * *
      * * * * * * * * * *
      * * * * * * * * * *
      * * * * * * * * * *
      * * * * * * * * * *
      """)
      
print("SEGUNDA FORMA AVANZADA")
filas = 5 # define el número de filas en el dibujo.
columnas = 10 # define el número de asteriscos en cada fila.

for _ in range(filas):
    print('* ' * columnas) # imprime cada fila, multiplicando el string '* ' por el número de columnas.
    
chi = 5  # Número de filas
ño = 10  # Número de columnas

print("____________________________________________________\n")
chi = 6 # Número de filas
ño = 3  # Número de columnas
for _ in range(chi):
    print('* ' * ño)
    
    