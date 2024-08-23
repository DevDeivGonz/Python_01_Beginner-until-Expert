"""

1. ¿Qué Son las Listas de Comprensión?

    Las listas de comprensión permiten crear listas nuevas de manera compacta y clara. En lugar de usar un bucle for
    para construir una lista, puedes usar una sola línea de código.

"""

print('Crear una lista de números pares del 1 al 20')
numeros_pares = [x for x in range(1, 21) if x % 2 == 0]
print(numeros_pares)  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print("Las tablas de multiplicar del 1 al 10 x 10")
matriz = [[i * j for j in range(1, 11)] for i in range(1, 11)]
print(matriz)

"""
[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30], 
[4, 8, 12, 16, 20, 24, 28, 32, 36, 40], 
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50], 
[6, 12, 18, 24, 30, 36, 42, 48, 54, 60], 
[7, 14, 21, 28, 35, 42, 49, 56, 63, 70], 
[8, 16, 24, 32, 40, 48, 56, 64, 72, 80], 
[9, 18, 27, 36, 45, 54, 63, 72, 81, 90], 
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]]

"""



# Crear una lista de los cuadrados de los números del 0 al 9
cuadrados = [x**2 for x in range(3, 10)]
print(cuadrados)  # Output: [9, 16, 25, 36, 49, 64, 81]

tabla_mult_2 = [num*2 for num in range(1, 15)]
print(tabla_mult_2)

################################################


lista_3_5_7_9 = {
    "Tabla del 3": [num3 * 3 for num3 in range(1,11)],
    "Tabla del 5": [num5 * 5 for num5 in range(1,11)],
    "Tabla del 7": [num7 * 7 for num7 in range(1,11)],
    "Tabla del 9": [num9 * 9 for num9 in range(1,11)],
}

print(f"\n\n Aqui estan las tablas del 3, 5, 7 y 9.")
for numero_por_su_tabla, tabla in lista_3_5_7_9.items():
    print(f"{numero_por_su_tabla}: {tabla}\n")

# Filtrar y Transformar
print("Crear una lista de cuadrados de números impares del 1 al 20")
cuadrados_impares = [x**2 for x in range(1, 21) if x % 2 != 0]
print(cuadrados_impares)  # Output: [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]

print("Crear una lista de números y etiquetarlos como 'par' o 'impar'")
etiquetas = ['par' if x % 2 == 0 else 'impar' for x in range(1, 11)]
print(etiquetas)  # Output: ['impar', 'par', 'impar', 'par', 'impar', 'par', 'impar', 'par', 'impar', 'par']


