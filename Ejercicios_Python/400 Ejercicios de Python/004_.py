# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 23:53:49 2024

@author: Laptop
"""

"""
4). Hacer un programa que cuente desde el 1 al 100 y los imprima uno a uno
"""
import itertools

print("Primero metodo para contar: ")
for numero in range(0, 101 ):
    print(numero)
    
    
print("segunda forma de contar: ")
print("______________________________________________-")
contador = itertools.count(start=1) # Esto crea un iterador contador que comenzará en
                                    # y generará una secuencia infinita de números 
                                    # incrementados en 1.
for _ in range(100):# indica que el bucle se ejecutará 100 veces. La variable _ se usa                     
                    # comúnmente en Python para indicar que el valor de la variable no 
                    # es importante.
    print(next(contador)) # next(contador) se llama para obtener el siguiente número 
                          # de la secuencia generada por contador y lo imprime.
                          
                          
print("Ahora con numero pares: ")
print("______________________________________________-")

contador = itertools.count(start=-24) # inicia a contar desde -24
for _ in range(50): # hasta 50
    print(next(contador))
    
print("Tercera forma de contar: ")
print("______________________________________________-")
    
suma = 0
for numero in range(1, 101):
    suma += numero
print(f"La suma de los números del 1 al 100 es: {suma}")

resta = 0 
for numero in range (1, 50):
    resta -= numero
print(f"La resta desde el 1 al 50 es: {resta}")
    
    
    
    