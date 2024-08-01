import random

def attemp_guess():
    guess_list = ["Manzana", "Pera", "Sandia", "Fresa", "Papaya", "Coco", "Limón"]
    palabra_secreta = random.choice(guess_list)
    intentos = 0

    print(f"""
                    Esta es la lista de las palabras que debes adivinar, adivina cual es.
                    {guess_list}.""")
    adivinado = False  # Variable para controlar el estado del juego

    while not adivinado:
        Answer_guess = input("\nIngrese su intento: ").strip().capitalize()
        intentos += 1

        if Answer_guess == palabra_secreta:
            print(f"Felicidades, has adivinado la palabra secreta en {intentos} intentos.")
            adivinado = True  # Salir del bucle cuando se adivina correctamente

        else:
            print(f"Ups, intento inválido, sigue intentando, llevas {intentos} intentos, buena suerte!.")


def menu_adivinasas():
    print("""
    Bienvenido.
    [1]. Para iniciar una partida.
    [2]. Para salir.
    """)

    while True:
        try:
            requested = int(input("Ingrese su opción: "))
        except ValueError:
            print("Por favor ingrese un número válido.")
            continue

        if requested == 1:
            attemp_guess()
        elif requested == 2:
            print("Gracias por elegirnos, lindo día.")
            break
        else:
            print("Opción inválida. Por favor, elija 1 o 2.")


if __name__ == "__main__":
    menu_adivinasas()