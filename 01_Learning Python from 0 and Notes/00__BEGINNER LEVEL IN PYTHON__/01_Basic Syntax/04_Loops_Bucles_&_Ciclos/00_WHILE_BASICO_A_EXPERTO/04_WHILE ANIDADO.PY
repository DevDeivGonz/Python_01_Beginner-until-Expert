"""
El uso de bucles anidados (anidados) implica colocar un bucle dentro de otro. En el caso de bucles while anidados, esto significa que hay un while dentro de otro while. 

Los bucles anidados son útiles para trabajar con estructuras de datos multidimensionales, como listas de listas (matrices), 
o para realizar operaciones repetitivas dentro de otras operaciones repetitivas.

"""
import os 
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")
    limpiar_pantalla()

   
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

i = 0
while i < len(matriz):  # Bucle exterior recorre las filas
    j = 0
    while j < len(matriz[i]):  # Bucle interior recorre las columnas
        print(f"Elemento en [{i}][{j}]: {matriz[i][j]}")
        j += 1  # Incrementa j para recorrer las columnas
    i += 1  # Incrementa i para recorrer las filas


""" 
Cuándo Usarlo
Estructuras de Datos Multidimensionales: Cuando trabajas con matrices o listas de listas.
Problemas de Combinación: Para generar todas las combinaciones de elementos entre dos o más conjuntos.
Operaciones Repetitivas Anidadas: Cuando necesitas realizar una serie de operaciones repetitivas dentro de otra serie de operaciones repetitivas.

Cuándo No Usarlo
Complejidad: Si el uso de bucles anidados aumenta significativamente la complejidad del código, lo que lo hace difícil de entender o mantener.
Rendimiento: En casos donde el rendimiento es crucial, ya que los bucles anidados pueden llevar a un crecimiento exponencial en el tiempo de ejecución.
Alternativas Más Simples: Si existe una alternativa más simple y eficiente, como el uso de funciones de biblioteca optimizadas (por ejemplo, en numpy para operaciones con matrices en Python).

"""
input("ENTER PARA CONTINUAR")


print(""" 
Calcular la Suma de Cada Fila de una Matriz
Supongamos que tenemos una matriz (una lista de listas) y queremos calcular la suma de todos los elementos de cada fila.
""")

# Matriz de ejemplo
# Matriz de ejemplo
matriz = [
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
]

# Variable para almacenar las sumas de cada fila
suma_filas = []

i = 0
while i < len(matriz):  # Bucle exterior recorre las filas
    suma_fila = 0
    j = 0
    while j < len(matriz[i]):  # Bucle interior recorre las columnas
        suma_fila += matriz[i][j]  # Suma los elementos de la fila actual
        j += 1  # Incrementa j para recorrer las columnas
    suma_filas.append(suma_fila)  # Agrega la suma de la fila actual a la lista de sumas
    i += 1  # Incrementa i para recorrer las filas

# Imprimir la suma de cada fila
for indice, suma in enumerate(suma_filas):
    print(f"Suma de la fila {indice}: {suma}")

input("ENTER PARA CONTINUAR")

multiplicacion_filas = []
i = 0
while i < len(matriz):
    multiplicacion_fila = 0
    j = 0
    while j < len(matriz[i]):
        multiplicacion_filas * matriz[i][j]
        j += 1
    multiplicacion_filas.append(multiplicacion_fila)
    i += 1
    
for indice, multiplicacion in enumerate(multiplicacion_filas):
    print(f"Multiplicación de la fila {indice}: {multiplicacion}")
    
input("ENTER PARA CONTINUAR")
    
matriz = [
    [2, 42, 4, 4, 4, 45, 2783923],
    [3, 31, 10, 6778],
    [4, 5, 67, 2]
]

multiplicacion_filas = []
i = 0
while i < len(matriz):
    multiplicacion_fila = 1  # Inicializar en 1 para la multiplicación
    j = 0
    while j < len(matriz[i]):
        multiplicacion_fila *= matriz[i][j]  # Multiplicar los elementos
        j += 1
    multiplicacion_filas.append(multiplicacion_fila)
    i += 1

for indice, multiplicacion in enumerate(multiplicacion_filas):
    print(f"Multiplicación de la fila {indice}: {multiplicacion}")

input("ENTER PARA CONTINUAR")

