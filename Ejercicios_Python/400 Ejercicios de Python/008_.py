# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:10:51 2024

@author: Laptop
"""

"""
8) Hacer un programa que imprima una tabla de multiplicar del 2 al 9 . Cada uno debe
mostrar sus valores multiplicados del 1 al 9 inclusive
"""

# Imprimir tablas de multiplicar del 2 al 9

for i in range(2, 10):  # Bucle exterior para las tablas del 2 al 9
    print(f"Tabla del {i}:")  # Encabezado de cada tabla
    for j in range(1, 10):  # Bucle interior para los multiplicadores del 1 al 9
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
    print("__________________________________")  # Línea en blanco para separar las tablas
    
input("ENTER PARA CONTINUAR")

for i in range(1, 16):
    print(f"Tabla de potenciacion de {i}: ")
    for j in range(1,16):
        resultado = i ** j
        print(f"{i}**{j} = {resultado} ")
    print("___________________________________\n") 

input("ENTER PARA CONTINUAR")
    
for i in range(1,10):
    print(f"TABLA DE DIVISIONES DE {i}: ")
    for j in range(1,10):
        resultado = i / j 
        print(f" {i} / {j} = {resultado}")
    print("___________________________________\n") 

    

