"""
Listas y Diccionarios Anidados

1. ¿Qué Son?

    Listas Anidadas: Son listas que contienen otras listas como elementos. Esto permite crear estructuras de datos más
    complejas que reflejan relaciones jerárquicas o matrices. Por ejemplo, una lista de listas podría representar una
    tabla o una cuadrícula.

"""
def clear_space():
    print("\n"*5)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

clear_space()

"""
Diccionarios Anidados: 

    Son diccionarios que contienen otros diccionarios como valores. Esto es útil para representar 
    datos con múltiples niveles de detalle o para agrupar información relacionada bajo claves comunes.

"""

empleado = {
    "nombre": "Juan",
    "detalles": {
        "edad": 30,
        "departamento": "Ventas"
    }
}


"""



"""

# EJEMPLO = Diccionario de departamentos
departamentos = {
    'Electrónica': {
        'productos': [
            {'nombre': 'Televisor', 'precio': 500.00, 'stock': 10},
            {'nombre': 'Laptop', 'precio': 1000.00, 'stock': 5},
            {'nombre': 'Lavadora', 'precio': 2000.00, 'stock': 20},
        ],
        'gerente': 'Juan Pérez',
    },
    'Hogar': {
        'productos': [
            {'nombre': 'Sofá', 'precio': 300.00, 'stock': 2},
            {'nombre': 'Mesa', 'precio': 150.00, 'stock': 7},
        ],
        'gerente': 'Ana Gómez',
    },
}

# Acceder a los datos
for departamento, detalles in departamentos.items():
    print(f"Departamento: {departamento}")
    print(f"Gerente: {detalles['gerente']}")
    print("Productos:")
    for producto in detalles['productos']:
        print(f"  - {producto['nombre']} (Precio: ${producto['precio']}, Stock: {producto['stock']})")
    print()  # Línea en blanco para separar departamentos


# Ejemplo Avanzado: Sistema de Gestión de Proyecto
#
# Aquí tienes un ejemplo de cómo podrías usar listas y diccionarios anidados para gestionar proyectos en una empresa:

proyectos = {
    "Proyecto A": {
        "equipo": [
            {"nombre": "Juan", "rol": "Desarrollador", "horas": 40},
            {"nombre": "Ana", "rol": "Diseñadora", "horas": 30}
        ],
        "tareas": [
            {"tarea": "Desarrollo", "estado": "En progreso", "responsable": "Juan"},
            {"tarea": "Diseño", "estado": "Completado", "responsable": "Ana"}
        ]
    },
    "Proyecto B": {
        "equipo": [
            {"nombre": "Luis", "rol": "Analista", "horas": 35},
            {"nombre": "Marta", "rol": "Gestora", "horas": 20}
        ],
        "tareas": [
            {"tarea": "Análisis", "estado": "Pendiente", "responsable": "Luis"},
            {"tarea": "Gestión", "estado": "En progreso", "responsable": "Marta"}
        ]
    }
}


clear_space()
clear_space()

# Ahora el mismo ejercicio pero con entradas del usuario (inputs)

# Estructura inicial vacía para los proyectos


# Función para agregar un nuevo proyecto
proyectos = {}


def agregar_proyecto_y_miembro():
    nombre_proyecto = input("Ingrese el nombre del proyecto: ")

    # Verificar si el proyecto ya existe
    if nombre_proyecto in proyectos:
        print(f"El proyecto '{nombre_proyecto}' ya existe.")
    else:
        # Si no existe, agregar el nuevo proyecto
        proyectos[nombre_proyecto] = {
            "equipo": [],
            "tareas": []
        }
        print(f"Proyecto '{nombre_proyecto}' creado.")

    # Agregar un miembro al equipo del proyecto, ya sea nuevo o existente
    nombre = input("Ingrese el nombre del miembro del equipo: ")
    rol = input("Ingrese el rol del miembro del equipo: ")
    horas = int(input("Ingrese el número de horas trabajadas: "))

    miembro = {"nombre": nombre, "rol": rol, "horas": horas}
    proyectos[nombre_proyecto]["equipo"].append(miembro)
    print(f"Miembro '{nombre}' agregado al proyecto '{nombre_proyecto}'.")



# Función para agregar una tarea a un proyecto
def agregar_tarea(nombre_proyecto):
    if nombre_proyecto in proyectos:
        tarea = input("Ingrese el nombre de la tarea: ")
        estado = input("Ingrese el estado de la tarea (Pendiente/En progreso/Completado): ")
        responsable = input("Ingrese el nombre del responsable de la tarea: ")

        tarea_info = {"tarea": tarea, "estado": estado, "responsable": responsable}
        proyectos[nombre_proyecto]["tareas"].append(tarea_info)
        print(f"Tarea '{tarea}' agregada al proyecto '{nombre_proyecto}'.")
    else:
        print(f"No se encontró el proyecto '{nombre_proyecto}'.")


# Función para mostrar todos los proyectos con su equipo y tareas
def mostrar_proyectos():
    if not proyectos:
        print("No hay proyectos disponibles.")
        return

    for proyecto, detalles in proyectos.items():
        print(f"\nProyecto: {proyecto}")
        print("Equipo:")
        if detalles["equipo"]:
            for miembro in detalles["equipo"]:
                print(f"  Nombre: {miembro['nombre']}, Rol: {miembro['rol']}, Horas: {miembro['horas']}")
        else:
            print("  No hay miembros en el equipo.")

        print("Tareas:")
        if detalles["tareas"]:
            for tarea in detalles["tareas"]:
                print(f"  Tarea: {tarea['tarea']}, Estado: {tarea['estado']}, Responsable: {tarea['responsable']}")
        else:
            print("  No hay tareas asignadas.")


# Menú de interacción con el usuario
def menu():
    while True:
        print("\nOpciones:")
        print("1. Agregar Proyecto")
        print("2. Agregar Miembro al Equipo")
        print("3. Agregar Tarea")
        print("4. Mostrar Proyectos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_proyecto_y_miembro()
        elif opcion == "2":
            nombre_proyecto = input("Ingrese el nombre del proyecto al que agregar el miembro: ")
            agregar_miembro_equipo(nombre_proyecto)
        elif opcion == "3":
            nombre_proyecto = input("Ingrese el nombre del proyecto al que agregar la tarea: ")
            agregar_tarea(nombre_proyecto)
        elif opcion == "4":
            mostrar_proyectos()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


# Ejecutar el menú
menu()
