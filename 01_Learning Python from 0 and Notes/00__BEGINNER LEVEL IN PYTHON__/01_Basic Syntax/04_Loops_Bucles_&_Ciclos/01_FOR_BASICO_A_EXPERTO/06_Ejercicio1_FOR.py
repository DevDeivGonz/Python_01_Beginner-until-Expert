# -*- coding: utf-8 -*-


"""
Created on Thu Jun 13 15:37:22 2024

@author: Laptop
"""
"""
Escribe un programa en Python que simule una visita a una tienda de frutas. Define una lista llamada frutas que contenga al menos cuatro tipos diferentes de frutas que te gustaría comprar. Utiliza un bucle for para recorrer la lista de frutas e imprimir un mensaje para cada fruta que indique que estás comprando esa fruta específica.
"""

listafrutas = []

# Solicitar al usuario que ingrese las frutas que desea comprar
print("Ingrese las frutas que desea comprar (separadas por coma):")
entrada = input()
frutas = entrada.split(",")  # Dividir la entrada por comas para obtener una lista de frutas

# Iterar sobre la lista de frutas e imprimir un mensaje para cada una
for fruta in frutas:
    listafrutas.append(fruta.strip())  # Agregar cada fruta a listafrutas, eliminando espacios extra

# Imprimir la lista de frutas compradas
print("Las frutas que usted compró son:", listafrutas)



