# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 23:40:36 2024

@author: Laptop
"""

"""
5). Hacer un programa que solicite un color por teclado e imprima “Puede pasar “ si el
color ingresado es verde , “Precaución “ si es amarillo , “No pasar “ si es rojo o “Color
inválido” si es cualquier otro.
"""

while True:

    color = input("Ingrese el color que ve en el semaforo: ").lower()
    
    if color == "verde":
        print("Puede pasar :)")
    elif color == "amarillo":
        print("Precaución :/")
    elif color == "rojo":
        print("No pasar :(")
        break
    elif color != ("verde" and "amarillo") or "rojo":
        print("Color inválido xC ") 
    else:
        print("ERROR....... ") 