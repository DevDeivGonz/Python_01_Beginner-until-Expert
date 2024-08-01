def Crear_tarea():
    print("se haran muchas tareas")
    menu_principal()


def Editar_tarea():
    print("Se editaran muchas tareas")
    menu_principal()


def Revisar_tareas_pendientes():
    print("Se revisaran muchas tareas pendientes en el sistema")
    menu_principal()


def Revisar_tareas_completadas():
    print("Se revisaran todas las tareas completadas")


def salir():
    print("Ha selecionado finalizar todo, que tenga un excelente dia.")
    exit()


def menu_principal():
    print("""
    Bienvenido al menu de tareas asignadas.

    [1] Crear tarea.
    [2] Editar tarea.
    [3] Revisar tareas pendientes.
    [4] Revisar tareas completadas.
    [5] Salir
    """)

    menu = {
        1: {"description": "Crear tarea.", "function": Crear_tarea},
        2: {"description": "Editar tarea.", "function": Editar_tarea},
        3: {"description": "Revisar tareas pendientes.", "function": Revisar_tareas_pendientes},
        4: {"description": "Revisar tareas completadas.", "function": Revisar_tareas_completadas},
        5: {"description": "Salir", "function": salir},
    }

    while True:
        user_answer = int(input("Ingrese su opcion\n"))

        if user_answer in menu:
            menu[user_answer]["function"]()
        else:
            print("Opcion invalida.")


__name__ == "__menu_principal__"
menu_principal()