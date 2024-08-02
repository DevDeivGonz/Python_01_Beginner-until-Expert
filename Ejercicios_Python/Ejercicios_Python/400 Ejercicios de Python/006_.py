# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 00:22:03 2024

@author: Laptop
"""

"""
6) Hacer un programa que cuente del 1 al 100 inclusive e imprima sólo los números pares
"""
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
    
print("_____________________________________")

for i in range(0,101):
    if i %5 == 0:
        print(i)
        
print("_____________________________________")

for i in range(20, -1, -1): # asi se cuenta de reversa.
    print(i)

print("_____________________________________")

for i in range(50, -1, -5): # asi se cuenta de reversa, -1 es donde va a llegar y termina de contar, el -5 se refiere a la frecuencia a la que va a contar, aqui contará de 5 en 5.
    print(i)

        
        