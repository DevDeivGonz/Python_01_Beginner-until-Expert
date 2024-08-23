"""

1. Listas Anidadas: Concepto y Uso Básico

Las listas anidadas son listas dentro de listas. Son útiles para representar estructuras como matrices, tablas,
o cualquier conjunto de datos multidimensional.

"""

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accediendo a un elemento en una lista anidada
print(matriz[0][1])  # Output: 2 (primera fila, segundo elemento)

# Iterando sobre una lista anidada
for fila in matriz:
    for elemento in fila:
        print(elemento, end=' ,')# end= ' ', hace que las variables corran en una misma fila separadas por un espacio y ,
                                 # Output: 1 2 3 4 5 6 7 8 9


numeros_pares = [
    [2, 4, 6, 8, 10],
    [20, 40, 60, 80, 100],
    [1000, 10000, 100000, 1000000]
]

print(f"\n\n\nSegunda fila de la lista numeros pares, {numeros_pares[1][1]}")
print("\n\n Aqui estan los numeros de las 3 listas de numeros pares\n")
for fila_num in numeros_pares:
    for cada_num in fila_num:

        print(cada_num, end=' ,')

print("\n\n\n\n\n\n")

# ahora veremos listas con diccionarios anidados

# Lista de diccionarios

empleados = [
    {"nombre": "Julian Alvarez", "Departamento": "Soporte Tecnico", "Cuidad": "Bogota", "Salario": 1500000},
    {"nombre": "Sofia Vergara",  "Departamento":      "VENTAS",     "Cuidad": "Bogota", "Salario": 3000000},
    {"nombre": "David Gonzalez", "Departamento": "Soporte Tecnico", "Cuidad": "Bogota", "Salario": 4500000}
]

for empleado in empleados:
    print(f" Nombre: {empleado['nombre']}, {empleado['Departamento']}, {empleado['Cuidad']}, {empleado['Salario']} ")

salario_total = 0
for empleado in empleados:
    salario_total += empleado['Salario']

print(f"Salario total de todos los empleados: {salario_total}")

# ya subiendo el nivel, veremos listas anidadas pero manejando INPUTS

def crear_tabla():

    # Solicitar el número de filas y columnas
    num_filas = int(input("Ingrese el número de filas: "))
    num_columnas = int(input("Ingrese el número de columnas: "))

    tabla = []

    for i in range(num_filas):
        fila = []
        print(f"Ingrese los datos para la fila {i + 1}:")
        for j in range(num_columnas):
            dato = input(f"Columna {j + 1}: ")
            fila.append(dato)
        tabla.append(fila)

    return tabla

def imprimir_tabla(tabla):
    # Imprimir la tabla de manera formateada
    print("\nTabla:")
    for fila in tabla:
        print(" |".join(fila))

# Crear la tabla a partir de la entrada del usuario
tabla = crear_tabla()

# Imprimir la tabla
imprimir_tabla(tabla)

