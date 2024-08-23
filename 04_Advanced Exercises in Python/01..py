import os

# Definición de la clase Tarea
class Tarea:
    def __init__(self, descripcion, prioridad, tiempo_limite, departamento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.tiempo_limite = tiempo_limite
        self.departamento = departamento

    def __str__(self):
        return f"Descripción: {self.descripcion}, Prioridad: {self.prioridad}, Tiempo límite: {self.tiempo_limite}, Departamento: {self.departamento}"

# Lista global para almacenar las tareas
lista_tareas_pendientes = []

def cargar_tareas():
    """Carga las tareas desde un archivo de texto."""
    if os.path.exists("tareas.txt"):
        with open("tareas.txt", "r") as file:
            for line in file:
                descripcion, prioridad, tiempo_limite, departamento = line.strip().split("|")
                tarea = Tarea(descripcion, prioridad, tiempo_limite, departamento)
                lista_tareas_pendientes.append(tarea)

def guardar_tareas():
    """Guarda las tareas en un archivo de texto."""
    with open("tareas.txt", "w") as file:
        for tarea in lista_tareas_pendientes:
            file.write(f"{tarea.descripcion}|{tarea.prioridad}|{tarea.tiempo_limite}|{tarea.departamento}\n")

def agregar_tarea():
    """Solicita al usuario los datos de una nueva tarea y la agrega a la lista."""
    descripcion = input("Ingrese la descripción de la tarea: ")
    prioridad = input("Ingrese la prioridad (Alta, Media, Baja): ")
    tiempo_limite = input("Ingrese el tiempo límite: ")
    departamento = input("Ingrese el departamento: ")
    tarea = Tarea(descripcion, prioridad, tiempo_limite, departamento)
    lista_tareas_pendientes.append(tarea)
    print("Tarea agregada exitosamente.")

def ver_tareas_pendientes():
    """Muestra todas las tareas pendientes."""
    if not lista_tareas_pendientes:
        print("No hay tareas pendientes.")
    else:
        for idx, tarea in enumerate(lista_tareas_pendientes, start=1):
            print(f"{idx}. {tarea}")

def eliminar_tarea():
    """Elimina una tarea según el número especificado por el usuario."""
    ver_tareas_pendientes()
    try:
        num_tarea = int(input("Ingrese el número de la tarea que desea eliminar: ")) - 1
        if 0 <= num_tarea < len(lista_tareas_pendientes):
            del lista_tareas_pendientes[num_tarea]
            print("Tarea eliminada exitosamente.")
        else:
            print("Número de tarea no válido.")
    except ValueError:
        print("Entrada no válida. Debe ingresar un número.")

def menu():
    """Muestra el menú principal y maneja las opciones del usuario."""
    opciones = {
        1: agregar_tarea,
        2: ver_tareas_pendientes,
        3: eliminar_tarea,
        4: salir
    }

    while True:
        print("""
        1. Agregar tarea.
        2. Ver tareas pendientes.
        3. Eliminar tarea.
        4. Salir
        """)
        try:
            opcion = int(input("Ingrese su opción: "))
            if opcion in opciones:
                opciones[opcion]()
            else:
                print("Opción no válida, ingrese una opción válida.")
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")
        finally:
            guardar_tareas()  # Guardar tareas en el archivo después de cada acción

def salir():
    """Termina el programa."""
    print("Saliendo...")
    exit()

if __name__ == "__main__":
    cargar_tareas()  # Cargar tareas al iniciar
    menu()
