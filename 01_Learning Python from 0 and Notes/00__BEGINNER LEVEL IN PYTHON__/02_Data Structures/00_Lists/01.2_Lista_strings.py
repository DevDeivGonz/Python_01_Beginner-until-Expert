lista_strings = [] # Inicializar una lista vacía

while True:
    string = input("Ingrese un string (o 'salir' para terminar): ")
    if string.lower() == 'salir':
        break

    lista_strings.append(string)

print(f"Lista de strings ingresados: {lista_strings}")


