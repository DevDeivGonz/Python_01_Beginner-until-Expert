"""

Ejercicio:

    Sistema de Gestión de Inventario para una Tienda
    Descripción del Problema.

    Estás creando un sistema para gestionar el inventario de una tienda. Este sistema debe permitir agregar productos,
    registrar ventas, y consultar el estado del inventario.

Requisitos del Ejercicio

    Agregar Productos:
        Permite al usuario ingresar información sobre nuevos productos, incluyendo:
            Nombre del producto
            Categoría (por ejemplo, Electrónica, Ropa, Alimentos)
            Precio unitario
            Cantidad en inventario

    Registrar Ventas:
        Permite al usuario registrar una venta, especificando:
            Nombre del producto
            Cantidad vendida
        Actualiza la cantidad en inventario del producto correspondiente.

    Consultar Inventario:
        Muestra una lista de todos los productos con su información:
            Nombre
            Categoría
            Precio unitario
            Cantidad disponible en inventario

    Mostrar Productos por Categoría:
        Permite al usuario consultar los productos filtrados por categoría.

    Eliminar Productos:
        Permite al usuario eliminar un producto del inventario por nombre.

    Actualizar Información de Productos:
        Permite al usuario actualizar el precio unitario y la cantidad en inventario de un producto.

"""
inventario_general = {}


def Agregar_Productos():
    producto = input("Ingrese el nombre del producto para validar si está en el inventario o sino agregarlo:\t")

    if producto in inventario_general:
        print("El producto ya está agregado, intente con otro.")
        menu_principal()
    else:

        print(f"El producto {producto} no esta registrado, por favor agregelo.")

        # Si el producto no está en el inventario, se procede a agregarlo
        nombre_producto = input("Ingrese el nombre del producto:\t")
        categoria = input("Ingrese la categoría del producto (por ejemplo, Electrónica, Ropa, Alimentos):\t")
        precio = float(input("Ingrese el precio unitario del producto:\t"))
        cantidad = int(input("Ingrese la cantidad en inventario:\t"))

        inventario_general[producto] = {
            'Nombre del producto': nombre_producto,
            'Categoría': categoria,
            'Precio unitario': precio,
            'Cantidad en inventario': cantidad
        }

        print(f"Se ha agregado el producto a la lista de productos:\n"
              f"Nombre del producto: {nombre_producto},\n"
              f"Categoría: {categoria},\n"
              f"Precio unitario: {precio},\n"
              f"Cantidad en inventario: {cantidad}")

        while True:
            solicitud_agregar_producto = input("Desea agregar otro producto al inventario? | [Si] para seguir | [No] para volver al menu princial.")
            if solicitud_agregar_producto == "Si":
                Agregar_Productos()
            elif solicitud_agregar_producto == "No":
                menu_principal()
                break
            else:
                print("Error, imgrese un valor valido")

def Registrar_Ventas():
    print("Registro de ventas por productos.\n\n")
    #
    nombre_producto_vendido = input("Ingrese el nombre del producto que fue vendido:\t")

    if nombre_producto_vendido in inventario_general:
        cantidad_vendida = int(input(f"Ingrese la cantidad vendida de {nombre_producto_vendido}:\t"))

        if cantidad_vendida <= inventario_general[nombre_producto_vendido]['Cantidad en inventario']:
            inventario_general[nombre_producto_vendido]['Cantidad en inventario'] -= cantidad_vendida
            print(f"Venta registrada: {cantidad_vendida} unidades de {nombre_producto_vendido}.")
        else:
            print("Error: La cantidad vendida excede la cantidad disponible en inventario.")
    else:
        print("Error: El producto no está en el inventario.")

    while True:
        solicito_Registrar_Ventas = input("Desea agregar otro producto vendido? | [Si] para seguir | [No] para volver al menu princial.")
        if solicito_Registrar_Ventas == "Si":
            Registrar_Ventas()
        elif solicito_Registrar_Ventas == "No":
            menu_principal()
            break
        else:
            print("Error, imgrese un valor valido")
            Registrar_Ventas()

def Consultar_Inventario():
    if not inventario_general:
        print("El inventario está vacío. No hay productos para mostrar.")
        menu_principal()

        print("Aquí está el inventario general de productos agregados:\n")
        print("Nombre del producto    |    Categoría    |    Precio unitario    |    Cantidad en inventario |")
        print("-" * 94)
        for producto, detalles_producto in inventario_general.items():
            nombre_producto = detalles_producto['Nombre del producto']
            categoria = detalles_producto['Categoría']
            precio = detalles_producto['Precio unitario']
            cantidad = detalles_producto['Cantidad en inventario']

            print(f"{nombre_producto:<22} | {categoria:<17} | {precio:<22} | {cantidad:<12} ")
    menu_principal()


def Mostrar_Productos_por_Categoría():
    categoria_buscada = input("Ingrese la categoría que desea consultar (por ejemplo, Electrónica, Ropa, Alimentos):\t")
    productos_en_categoria = []

    for producto, detalles in inventario_general.items():
        if detalles['Categoría'].lower() == categoria_buscada.lower():
            productos_en_categoria.append(detalles)

    if productos_en_categoria:
        print(f"Productos en la categoría '{categoria_buscada}':")
        for detalles in productos_en_categoria:
            print(f"Nombre: {detalles['Nombre del producto']}, Precio: {detalles['Precio unitario']}, Cantidad: {detalles['Cantidad en inventario']}")
    else:
        print(f"No se encontraron productos en la categoría '{categoria_buscada}'.")

    menu_principal()

def Actualizar_Información_de_Productos():
    nombre_producto = input("Ingrese el nombre del producto que desea actualizar:\t")

    if nombre_producto in inventario_general:
        print(f"Información actual de {nombre_producto}:")
        print(f"Precio actual: {inventario_general[nombre_producto]['Precio unitario']}")
        print(f"Cantidad en inventario: {inventario_general[nombre_producto]['Cantidad en inventario']}")

        nuevo_precio = float(input("Ingrese el nuevo precio unitario (deje en blanco para no actualizar):\t") or inventario_general[nombre_producto]['Precio unitario'])
        nueva_cantidad = int(input("Ingrese la nueva cantidad en inventario (deje en blanco para no actualizar):\t") or inventario_general[nombre_producto]['Cantidad en inventario'])

        inventario_general[nombre_producto]['Precio unitario'] = nuevo_precio
        inventario_general[nombre_producto]['Cantidad en inventario'] = nueva_cantidad

        print(f"Información actualizada para {nombre_producto}.")
    else:
        print("El producto no existe en el inventario.")

    menu_principal()

def Eliminar_Productos():
    nombre_producto = input("Ingrese el nombre del producto que desea eliminar:\t")

    if nombre_producto in inventario_general:
        del inventario_general[nombre_producto]
        print(f"El producto '{nombre_producto}' ha sido eliminado del inventario.")
    else:
        print("El producto no existe en el inventario.")

    menu_principal()

def Salir():
    print("Gracias por elegirnos")
    print("\n\n\n\nSeliendo.......\n\n\n\n\n")
    exit()

def menu_principal():
    print("""
    
    Bienvendio a LogiGO.
    
    Esta es la gestion de inventarios.
    
    Menu:
    
    [1]. Agregar Productos.
    [2]. Registrar Ventas.
    [3]. Consultar Inventario.
    [4]. Mostrar Productos por Categoría.
    [5]. Actualizar Información de Productos.
    [6]. Eliminar Productos.
    [7]. Salir.
    
    """)

    eleccion_usuario = int(input("Ingrese si opcion:\t"))
    if eleccion_usuario == 1:
        Agregar_Productos()
    elif eleccion_usuario == 2:
        Registrar_Ventas()
    elif eleccion_usuario == 3:
        Consultar_Inventario()
    elif eleccion_usuario == 4:
        Mostrar_Productos_por_Categoría()
    elif eleccion_usuario == 5:
        Actualizar_Información_de_Productos()
    elif eleccion_usuario == 6:
        Eliminar_Productos()
    elif eleccion_usuario == 7:
        Salir()
    else:
        print("Opcion no valida, por favor intente de nuevo")
        menu_principal()

menu_principal()
