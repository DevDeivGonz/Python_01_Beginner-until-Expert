# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:56:07 2024

@author: Laptop
"""

"""
Lista de inventarios basica, mini mercado
"""
def limpiar_pantalla():
    print('\n' * 40)
limpiar_pantalla()

# Definición inicial del inventario
inventario = []

# Función para agregar un nuevo producto al inventario
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    
    producto = {
        'nombre': nombre,
        'precio': precio
    }
    inventario.append(producto)
    print(f"Producto '{nombre}' agregado al inventario.")

# Función para actualizar el precio de un producto existente
def actualizar_precio():
    nombre = input("Ingrese el nombre del producto cuyo precio desea actualizar: ")
    nuevo_precio = float(input(f"Ingrese el nuevo precio para '{nombre}': "))
    
    for producto in inventario:
        if producto['nombre'] == nombre:
            producto['precio'] = nuevo_precio
            print(f"Precio del producto '{nombre}' actualizado a ${nuevo_precio:.2f}.")
            return
    print(f"Producto '{nombre}' no encontrado en el inventario.")

# Función para eliminar un producto del inventario
def eliminar_producto():
    nombre = input("Ingrese el nombre del producto que desea eliminar: ")
    
    for producto in inventario:
        if producto['nombre'] == nombre:
            inventario.remove(producto)
            print(f"Producto '{nombre}' eliminado correctamente del inventario.")
            return
    print(f"Producto '{nombre}' no encontrado en el inventario.")

# Función para mostrar todos los productos en el inventario
def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("Inventario del Mini Supermercado:")
        for producto in inventario:
            print(f"Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}")

# Menú principal de la aplicación
while True:
    print("\n=== Gestión de Inventario ===")
    print("1. Agregar Producto")
    print("2. Actualizar Precio")
    print("3. Eliminar Producto")
    print("4. Mostrar Inventario")
    print("5. Salir")
    
    opcion = input("Ingrese el número de la opción que desea ejecutar: ")
    
    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        actualizar_precio()
    elif opcion == '3':
        eliminar_producto()
    elif opcion == '4':
        mostrar_inventario()
    elif opcion == '5':
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor ingrese un número del 1 al 5.")



