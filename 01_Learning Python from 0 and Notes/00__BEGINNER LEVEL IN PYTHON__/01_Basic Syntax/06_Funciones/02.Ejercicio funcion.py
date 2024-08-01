import os
def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Uso
def nombre_de_la_funcion(parametros):
    # Código de la función
    return resultado

# Ejemplo Intermedio
def suma(a, b):
    return a + b

# Llamada a la función
resultado = suma(3, 5)
print("La suma es:", resultado)


input("ENTER PARA CONTINUAR")
limpiar_pantalla()

def resta():
    valor_num1 = int(input("Ingrese el primer número para restar: "))
    valor_num2 = int(input("Ingrese el segundo número para restar: "))
    valor_num3 = int(input("Ingrese el tercer número para restar: "))
    resultado = valor_num1 - valor_num2 - valor_num3
    return resultado

resultado = resta()
print(f"La resta es: {resultado}")





