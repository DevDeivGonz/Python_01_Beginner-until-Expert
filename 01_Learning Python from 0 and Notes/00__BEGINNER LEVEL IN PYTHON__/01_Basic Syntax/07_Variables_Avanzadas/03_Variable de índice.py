
""" 
La variable de índice se utiliza para almacenar el índice actual durante la iteración sobre una estructura
de datos en Python. 
Es particularmente útil cuando necesitas acceder tanto al valor como al índice de los elementos en una estructura de datos,
como una lista, tupla o cadena de texto.
"""

nombres = ["Juan", "María", "Pedro", "Ana"]

for indice, nombre in enumerate(nombres):
    print("El nombre en la posición", indice, "es:", nombre)
    
input("ENTER PARA CONTINUAR: ")

    
numeros = [10, 5, -3, 8, -6, 12]

for indice, numero in enumerate(numeros):
    if numero < 0:
        print("El primer número negativo es:", numero, "y se encuentra en la posición:", indice)
        break
else:
    print("No se encontraron números negativos en la lista.")

input("ENTER PARA CONTINUAR: ")


numeros = [10, 5, -3, 8, -6, 12]

for indice, numero in enumerate(numeros):
    if numero > 0:
        print("El primer número es:", numero, "y se encuentra en la posición:", indice)
        break
else:
    print("No se encontraron números negativos en la lista.")