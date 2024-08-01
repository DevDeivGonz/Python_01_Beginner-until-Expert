# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:54:43 2024

@author: Laptop
"""

# Ejemplo de uso de tuplas en diferentes situaciones

# Coordenadas geográficas
coordenada_punto = (40.7128, -74.0060)  # Latitud y longitud de la ciudad de Nueva York


# Datos personales
datos_personales = ("Juan Pérez", "01-01-1980", "México")

# Meses del año
meses_del_anio = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                  "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

# Productos en un inventario (nombre, precio, stock)
producto1 = ("Camiseta", 15.99, 50)
producto2 = ("Pantalón", 29.99, 30)
producto3 = ("Zapatos", 49.99, 20)

# Acceso a los elementos de las tuplas
nombre_producto1, precio_producto1, stock_producto1 = producto1
nombre_producto2, precio_producto2, stock_producto2 = producto2
nombre_producto3, precio_producto3, stock_producto3 = producto3

# Mostrar información
print("Coordenadas de Nueva York: Latitud {}, Longitud {}".format(coordenada_punto[0], coordenada_punto[1]))
print("Nombre: {}, Fecha de Nacimiento: {}, País: {}".format(datos_personales[0], datos_personales[1], datos_personales[2]))

print("\nMeses del Año:")
for mes in meses_del_anio:
    print(mes)

print("\nInformación de Productos:")
print("Producto: {}, Precio: {}, Stock: {}".format(nombre_producto1, precio_producto1, stock_producto1))
print("Producto: {}, Precio: {}, Stock: {}".format(nombre_producto2, precio_producto2, stock_producto2))
print("Producto: {}, Precio: {}, Stock: {}".format(nombre_producto3, precio_producto3, stock_producto3))
