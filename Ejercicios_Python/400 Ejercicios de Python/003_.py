# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 23:06:54 2024

@author: Laptop
"""

"""
3) Hacer un programa que solicite una edad y determine si es mayor de edad.
"""
nombre_apellido = input("Ingrese su nombre y apellido: ")
edad = int(input("Ingrese su edad: "))
if edad <18:
    print(f"Usted es menor de edad {nombre_apellido}")
elif edad >= 18:
    print(f"Usted es mayor de edad {nombre_apellido}")
else: 
    print("Error")
        
    
    
