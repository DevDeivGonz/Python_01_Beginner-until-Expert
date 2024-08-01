# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:27:31 2024

@author: Laptop
"""

"""
uso de listas de multiples entradas en un input.
"""

def sumar_valores_desde_input():
    entrada = input("Ingrese los valores separados por coma (Ejemplo: 234, 345, 34, 23): ")
    
    # Dividir la entrada por comas y eliminar espacios adicionales
    valores_texto = entrada.split(',')
    
    # Convertir los valores de texto a números enteros
    valores_enteros = []
    for valor_texto in valores_texto:
        try:
            valor_entero = int(valor_texto.strip())  # strip() para eliminar espacios alrededor
            valores_enteros.append(valor_entero)
        except ValueError:
            print(f"Advertencia: '{valor_texto}' no es un número válido.")

    # Sumar los valores enteros
    suma = sum(valores_enteros)
    print(f"La suma de los valores ingresados es: {suma}")

# Llamar a la función para que el usuario ingrese los valores y se realice la suma
sumar_valores_desde_input()
