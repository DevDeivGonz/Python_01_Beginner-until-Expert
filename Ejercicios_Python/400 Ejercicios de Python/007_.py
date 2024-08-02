# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:02:25 2024

@author: Laptop
"""

"""
7) Hacer un programa que cuente del 1 al 100 inclusive e imprima los números que son
divisibles por 2 y por 5.

"""

for i in range(1,101):
    if i % 2 == 0 and i % 5 == 0: 
        print(i)
# El operador % se usa para verificar si un número i es divisible por 2 y por 5. Si i   % 2 es igual a 0, significa que i es divisible por 2 sin ningún resto. Del mismo modo, si i % 5 es igual a 0, significa que i es divisible por 5 sin ningún resto.
        

for i in range(1,51):
    if i % 2 == 0:
        print(i)

print("\n____________________________________________")
for i in range(1,71):
    if i % 7 == 0:
        print(i)