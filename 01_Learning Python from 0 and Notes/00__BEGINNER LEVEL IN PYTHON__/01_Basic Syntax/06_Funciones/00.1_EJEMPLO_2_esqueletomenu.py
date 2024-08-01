import os

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')    
    else:
        os.system('clear')
        
def main_menu():
    print("""BIENVENIDO AL MENU PRINCIPAL 
          \nPOR FAVOR ELIGA UNA OPCION
          \n""")
    print("1. Entrada de datos validada negativamente")
    print("2. Espera hasta que se cumpla una condición inversa")
    print("3. Iteración hasta que se alcance un estado deseado")
    print("4. Procesamiento de listas o estructuras de datos")
    print("5. Salir")
    
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError:
            print("Entrada inválida. Ingrese una opción válida.")
            continue
        
        if opcion == 1:
            submenu_numeros_negativos()
        elif opcion == 2:
            submenu_espera_condicion()
        elif opcion == 3:
            submenu_interaccion_estado()
        elif opcion == 4:
            submenu_procesamiento_listas_datos()
        elif opcion == 5:
            print("¡Gracias por elegirnos, nos veremos en otra oportunidad!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def submenu_numeros_negativos():
    numero = 0
    while True:
        limpiar_pantalla()
        print("""Entrada de datos validada negativamente.
        \nSeleccione una opción:
        \n""")
        print("1. Ingresar un número positivo")
        print("2. Regresar al menú principal")
        
        try:
            opcion = int(input("\nSeleccione una opcion: "))
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")
            continue
        
        if opcion == 1:
            while not numero > 0:
                # Lógica de validación de número positivo
                pass
        elif opcion == 2:
            main_menu()
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def submenu_espera_condicion():
    respuesta = ""
    print("""Espera hasta que se cumpla una condición inversa
    """)
    print("1. Ingresar un número positivo")
    print("2. Regresar al menú principal")
    
    try:
        opcion = int(input("\nSeleccione una opcion: "))
    except ValueError:
        print("Entrada inválida. Intente de nuevo.")
        
    if opcion == 1: 
        while not respuesta == 'salir':
            # Lógica de espera hasta condición inversa
            pass
    else:
        main_menu()
        limpiar_pantalla()

def submenu_interaccion_estado():
    print("""Iteración hasta que se alcance un estado deseado
    """)
    print("1. Ingresar: Iteración hasta que se alcance un estado deseado")
    print("2. Regresar al menú principal")
    
    try:
        opcion = int(input("\nSeleccione una opcion: "))
    except ValueError:
        print("Entrada inválida. Intente de nuevo.")
        
    contador = 0
    numero_objetivo = 10
        
    if opcion == 1: 
        while not contador == numero_objetivo:
            # Lógica de iteración hasta estado deseado
            pass
    else:
        main_menu()
        limpiar_pantalla()

    main_menu()

def submenu_procesamiento_listas_datos():
    print("""Procesamiento de listas o estructuras de datos: 
    """)
    print("1. Ingresar: Procesamiento de listas o estructuras de datos")
    print("2. Regresar al menú principal")
    
    try:
        opcion = int(input("\nSeleccione una opcion: "))
    except ValueError:
        print("Entrada inválida. Intente de nuevo.")
        
    numeros = [1, 2, 3, 4, 5, -1, 6, 7, 8, 9, 10]
    indice = 0
    
    if opcion == 1:
        while not numeros[indice] < 0:
            # Lógica de procesamiento de listas
            pass

        print("Se ha encontrado un número negativo")
    else:
        main_menu()

if __name__ == "__main__":
    main_menu()
