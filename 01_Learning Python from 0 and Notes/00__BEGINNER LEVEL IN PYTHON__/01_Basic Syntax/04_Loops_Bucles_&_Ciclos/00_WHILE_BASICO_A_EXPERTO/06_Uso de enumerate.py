""" 
SE PUEDE USAR TANTO EN WHILE COMO EN FOR
"""


import os 
def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

lista = ["Papel", "Lapiz", "Carton"]

for i, valor in enumerate(lista):
    print(f"Índice: {i}, Valor: {valor}")
    
input("ENTER PARA CONTINUAR")
limpiar_pantalla()
#######################################################################################3

lista = ["Papel", "Lapiz", "Carton"]

for indice, valor in enumerate(lista):
    for _ in range(indice + 1):  # Repetir la operación según el índice + 1
        print(f"Procesando {valor} (Índice: {indice})")

articulos = ["Papel", "Lapiz", "Carton"]

articulos_con_precios = {}

for indice, articulo in enumerate(articulos):
    precio = (indice + 1) * 1.50  # Ejemplo de lógica para calcular el precio
    articulos_con_precios[articulo] = precio

print(articulos_con_precios)

input("ENTER PARA CONTINUAR")
limpiar_pantalla()
#######################################################################################3

print("PRECIOS HOY COLOMBIA")
articulos_con_precios = {
    "Papel": 2550,
    "Lapiz": 1200,
    "Carton": 500
}

for articulo, precio in articulos_con_precios.items():
    print(f"Artículo: {articulo}, Precio: {precio}")

input("ENTER PARA CONTINUAR")
limpiar_pantalla()
#######################################################################################3

print("USO INTERMEDIO DE ENUMERATE\nLISTA DE OBJETOS")
productos = [("CAMISETA ADDIDAS", 89.000), ("PANTALOS LEVIS", 250.500), ("CALCETINES 3x1", 15.000)]

total = 0 
""""¿Qué es total y por qué se inicializa en 0?
    total es una variable que se utiliza para acumular el precio total de la compra. Se inicializa en 0 porque al principio no se ha comprado ningún producto, 
    por lo que el precio total es 0. 
    Luego, durante la iteración, se suman los precios individuales de cada producto al precio total.
"""

for indice, (producto, precio) in enumerate (productos, start=1): # ¿Qué es indice? 
    #indice es una variable que representa el índice de cada elemento de la lista productos durante la iteración con enumerate. 
    #Este índice comienza desde el valor especificado en el parámetro start, que en este caso es 1. Es un contador que aumenta en cada iteración y se utiliza para 
    #llevar un registro del orden de los productos en la lista.
    print(f"Producto {indice}: {producto} - Precio: ${precio}")
    total += precio # total += precio es un ejemplo de operador de asignación compuesta en Python. En esta línea de código, 
                    # se agrega el valor de precio al valor actual de total. 
print(f"\nEL PRECIO TOTAL DE LA COMPRA ES: ${total}")