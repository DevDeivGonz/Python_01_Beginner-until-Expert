flag = True  # Se inicializa la bandera en True
while flag:  # Se inicia un bucle while con la condición de que la bandera sea True
    accion = input("¿Deseas continuar? (sí/no): ")  # Se solicita al usuario una acción
    if accion == 'no':  # Si la acción ingresada es 'no'
        flag = False  # Se cambia el valor de la bandera a False, lo que detiene el bucle
