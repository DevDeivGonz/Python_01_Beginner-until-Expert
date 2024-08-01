def mostrar_menu_principal():
    print("\nBienvenido al menú de operadores en Python")
    print("1. Operadores matemáticos")
    print("2. Operadores lógicos")
    print("3. Operadores de comparación")
    print("4. Salir")

def mostrar_submenu(tema, opciones):
    print(f"\nBIENVENIDO A {tema}")
    for key, value in opciones.items():
        print(f"{key}. {value['nombre']}")
    print("5. Volver al menú principal")
    print("6. Terminar por hoy (FIN)")

def submenu(tema, opciones):
    while True:
        mostrar_submenu(tema, opciones)
        opcion = input("Seleccione una opción: ")
        if opcion in opciones:
            print(opciones[opcion]['descripcion'])
        elif opcion == '5':
            break  # Volver al menú principal
        elif opcion == '6':
            print("Terminando por hoy...")
            exit()  # Terminar el programa
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def menu_principal():
    operadores = {
        '1': {
            'nombre': 'Operadores matemáticos',
            'tema': 'OPERADORES MATEMÁTICOS',
            'opciones': {
                '1': {'nombre': 'Suma (+)', 'descripcion': 'Suma (+): Este operador se usa para sumar dos números. Ejemplo: 2 + 3 = 5'},
                '2': {'nombre': 'Resta (-)', 'descripcion': 'Resta (-): Este operador se usa para restar un número de otro. Ejemplo: 5 - 2 = 3'},
                '3': {'nombre': 'Multiplicación (*)', 'descripcion': 'Multiplicación (*): Este operador se usa para multiplicar dos números. Ejemplo: 3 * 4 = 12'},
                '4': {'nombre': 'División (/)', 'descripcion': 'División (/): Este operador se usa para dividir un número entre otro. Ejemplo: 10 / 2 = 5'},
            }
        },
        '2': {
            'nombre': 'Operadores lógicos',
            'tema': 'OPERADORES LÓGICOS',
            'opciones': {
                '1': {'nombre': 'AND', 'descripcion': 'AND: Este operador devuelve True si ambas condiciones son verdaderas. Ejemplo: True and False = False'},
                '2': {'nombre': 'OR', 'descripcion': 'OR: Este operador devuelve True si al menos una de las condiciones es verdadera. Ejemplo: True or False = True'},
                '3': {'nombre': 'NOT', 'descripcion': 'NOT: Este operador invierte el valor de la condición. Ejemplo: not True = False'},
            }
        },
        '3': {
            'nombre': 'Operadores de comparación',
            'tema': 'OPERADORES DE COMPARACIÓN',
            'opciones': {
                '1': {'nombre': 'Igual a (==)', 'descripcion': 'Igual a (==): Este operador compara si dos valores son iguales. Ejemplo: 5 == 5 es True'},
                '2': {'nombre': 'Diferente de (!=)', 'descripcion': 'Diferente de (!=): Este operador compara si dos valores son diferentes. Ejemplo: 5 != 3 es True'},
                '3': {'nombre': 'Mayor que (>)', 'descripcion': 'Mayor que (>): Este operador compara si el valor de la izquierda es mayor que el de la derecha. Ejemplo: 5 > 3 es True'},
                '4': {'nombre': 'Menor que (<)', 'descripcion': 'Menor que (<): Este operador compara si el valor de la izquierda es menor que el de la derecha. Ejemplo: 3 < 5 es True'},
            }
        }
    }

    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")
        if opcion in operadores:
            submenu(operadores[opcion]['tema'], operadores[opcion]['opciones'])
        elif opcion == '4':
            print("Saliendo del programa...")
            break  # Salir del programa
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Ejecutar el menú principal
menu_principal()
