def clear_space():
    print("\n"*6)

""" Asi se hacen listas anidadas, muy parecidas a las matrices"""

lista_anidada = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Accediendo a un elemento específico
print(lista_anidada[1][2])  # Output: 6

lista_anidada_2 = [
    [2, 4, 6, 8, 10],
    [1, 3, 5, 7, 9],
    [30, 70, 110, 150, 1900]
]

for lista in lista_anidada_2:
    for numero in lista:
        print(f'Fila {lista} y numero {numero}')

clear_space()

# ahora veremos listas anidadas usando inputs

# fila_valores = int(input("Ingrese las filas que desea para la lista:\t")) # determina el numero de filas horizontales que habran
# columnas_por_fila = int(input("Ingrese cuantas columnas desea por fila:\t")) # determina el numero de columnas que habran en las filas
fila_valores = 4 # determina el numero de filas horizontales que habran
columnas_por_fila = 3 # determina el numero de columnas que habran en las filas

tabla_valores = []

for valor in range(fila_valores):
    fila_valores = []
    for columna in range(columnas_por_fila):
        valor = input(f"Ingrese dato en la posicion [{valor}][{columna}]:\t")
        fila_valores.append(valor)
    tabla_valores.append(fila_valores)

print(f"\nTabla creada: ")
for fila_valores in tabla_valores:
    print(fila_valores)









