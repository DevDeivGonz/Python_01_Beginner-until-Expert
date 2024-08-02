""" 
EJERCICIO PENDIENTE, EL ERROR ESTA EN Marcar_Envios_Enviados():

ARREGLARLO
"""
1
#############################################################
# aqui estan las listas definidas para usarlas en varias funciones
lista_usuarios = []
envios = []
####################################################
import os
def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
#################################################################################################333

def Agregar_Producto():
    productos = []
    while True:
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        numero_productos_enBodega = int(input("Ingrese el numero de este producto en bodega: "))
        numero_envios_pendientes = int(input("Ingrese el numero de envios pendientes: "))
                      
        producto = {
                       "1. Nombre del producto": nombre_producto, 
                       "2. Precio": precio, 
                       "3. Numero de los productos en Bodega": numero_productos_enBodega, 
                       "4. Numero_envios_pedientes": numero_envios_pendientes
        }
        
        productos.append(producto)
        
        continuar = input("¿Desea agregar otra tarea? (sí/no): ")
        if continuar.lower() == "sí":
            Agregar_Tarea()
            break
        else:
            menu_principal()
    return producto

############################################################################################3
def Lista_de_productos():
    print("La lista de los productos es: ")
    print(envios)
    continuar = input("¿Desea seguir viendo las listas?, ingrese (si). \n¿Desea volver al menú principal?, ingrese (salir). \n ")
    if "si" in continuar.lower():
        Lista_de_productos()
    elif "salir" in continuar.lower():
        menu_principal()
    else:
        print("ERROR.\nPor favor ingrese una opcion valida. ")
        

        

def Marcar_Envios_Enviados():
    print("Aquí están los envíos pendientes:")
    for envio in envios:
        if envio.get("Número de envíos pendientes", 0) > 0:
            print(envio)
    
    continuar = input("¿Desea seguir viendo los envíos pendientes? Ingrese 'si'.\n¿Desea volver al menú principal? Ingrese 'salir'.\n")
    if "si" in continuar.lower():
        Marcar_Envios_Enviados()
    elif "salir" in continuar.lower():
        return
    else:
        print("ERROR.\nPor favor ingrese una opción válida.")
        Marcar_Envios_Enviados()

        
        
        
def Eliminar_envio_Creado():
    while True:
        eliminar_datos = input("INGRESE EL DATO QUE DESEA ELIMINAR: ")
        if eliminar_datos in envios:
            envios.remove(eliminar_datos)
            print(f"El dato {eliminar_datos} ha sido eliminado de la lista Productos")
            break
        else: 
            print(f"El dato {eliminar_datos} no existe en la lista")
        continuar = input("¿Desea seguir viendo los envíos pendientes?, ingrese (si). \n¿Desea volver al menú principal?, ingrese (salir). \n ")
        if "si" in continuar.lower():
            Marcar_Envios_Enviados()
        elif "salir" in continuar.lower():
            menu_principal()
        else:
            print("ERROR.\nPor favor ingrese una opción válida. ")
            Marcar_Envios_Enviados()

def menu_principal():
    """print("Bienvenido al Gestor de Tareas")
    nombres_apellidos = input("Ingrese su Nombre y Apellido")
    email = input("Ingrese su correo electronico")
    lista_usuarios.append({" Nombres y Apellidos": nombres_apellidos, "EMAIL": email})
    input("Pulse ENTER PARA CONTINUAR")""" 
    
    
    print("1. Agregar producto ")
    print("2. Ver todos los productos ingresados")
    print("3. Marcar Envíos Enviados ")
    print("4. Eliminar envio creado ")
    print("5. Salir del Programa ")
    
    while True:
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            limpiar_pantalla()
            Agregar_Producto() 
        elif opcion == "2":
            limpiar_pantalla()
            Lista_de_productos()
        elif opcion == "3":
            limpiar_pantalla()
            Marcar_Envios_Enviados()
        elif opcion == "4":
            limpiar_pantalla()
            Eliminar_envio_Creado()
        elif opcion == "5":
            limpiar_pantalla()
            print("Gracias por elegirnos\nQue tenga un excelente dia!")
            break
        else:
            print("Entrada inválida. Ingrese una opción válida.")

if __name__ == "__main__":
    menu_principal()


"""  

import os

lista_usuarios = []
envios = []

def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def Agregar_Producto():
    productos = []
    while True:
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        numero_productos_enBodega = int(input("Ingrese el número de este producto en bodega: "))
        numero_envios_pendientes = int(input("Ingrese el número de envíos pendientes: "))
        
        producto = {
            "Nombre del producto": nombre_producto, 
            "Precio": precio, 
            "Número de productos en Bodega": numero_productos_enBodega, 
            "Número de envíos pendientes": numero_envios_pendientes
        }
        
        productos.append(producto)
        
        continuar = input("¿Desea agregar otro producto? (sí/no): ")
        if continuar.lower() != "sí":
            break
    
    return productos

def Marcar_Envios_Enviados():
    print("Aquí están los envíos pendientes:")
    for envio in envios:
        if envio.get("Número de envíos pendientes", 0) > 0:
            print(envio)
    
    continuar = input("¿Desea seguir viendo los envíos pendientes? Ingrese 'si'.\n¿Desea volver al menú principal? Ingrese 'salir'.\n")
    if "si" in continuar.lower():
        Marcar_Envios_Enviados()
    elif "salir" in continuar.lower():
        return
    else:
        print("ERROR.\nPor favor ingrese una opción válida.")
        Marcar_Envios_Enviados()

def menu_principal():
    limpiar_pantalla()
    while True:
        print("Menú Principal")
        print("1. Agregar Producto")
        print("2. Marcar Envíos Enviados")
        print("3. Ver todos los productos ingresados")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            productos = Agregar_Producto()
            envios.extend(productos)
        elif opcion == "2":
            Marcar_Envios_Enviados()
        elif opcion == "3":
            print("Todos los productos ingresados:")
            for envio in envios:
                print(envio)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


menu_principal()

"""