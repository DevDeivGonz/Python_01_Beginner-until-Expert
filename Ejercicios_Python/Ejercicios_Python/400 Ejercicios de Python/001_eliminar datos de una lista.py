import os

def limpiar_pantalla():
    if os.system("cls"):
        os.system("clear")
    else:
        os.system("cls")
"""
papas = "Valor de papas"
amigos = "Valor de amigos"
pepas = "Valor de pepas"
farmacos = "Valor de farmacos"

envios = {"papas": papas, 
           "amigos": amigos, 
           "pepas": pepas, 
           "farmacos": farmacos}
print(envios)
del envios["amigos"]
print(envios)"""

input("Enter para seguir")
limpiar_pantalla()

productos = []

tipo_producto = input("INGRESE TIPO DE MERCANCIA: ")
precio = int(input("INGRESE EL PRECIO: $"))
peso = int(input("INGRESE EL PESO DEL PRODUCTO: "))
productos = ["Tipo de producto", tipo_producto, "Precio del producto",  precio, "Peso del producto",  peso]
print(productos)

eliminar_datos = input("INGRESE EL DATO QUE DESEA ELIMINAR")

if eliminar_datos in productos:
    productos.remove(eliminar_datos)
    print(f"El dato {eliminar_datos} ha sido eliminado de la lista Productos")
else: 
    print(f"El dato {eliminar_datos} no existe en la lista")