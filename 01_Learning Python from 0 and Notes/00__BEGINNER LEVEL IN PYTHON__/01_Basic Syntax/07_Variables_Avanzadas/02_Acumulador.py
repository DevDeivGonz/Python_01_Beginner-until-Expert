import os

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    

print("""  
      Un acumulador en programación se utiliza para sumar o acumular valores a lo largo de un programa. 
      Es una variable que se inicializa con un valor específico y luego se actualiza en cada iteración de un bucle o en 
      distintos puntos del programa según sea necesario.
      """)

acumulador = 0
for i in range(1, 6):
    acumulador += i
print("La suma de los números del 1 al 5 es:", acumulador)

input("ENTER PARA CONTINUAR: ")
limpiar_pantalla()

diccionario = {"a": 1, "b": 2, "c": 3, "maton": 23, "Manzanas": 13}
acumulador = 1
for valor in diccionario.values():
    acumulador *= valor
print("La multiplicacion de los valores del diccionario es:", acumulador)

input("ENTER PARA CONTINUAR: ")
limpiar_pantalla()

elevado_alados = {"a": 1, "b": 2, "c": 2, "maton": 2, "Manzanas": 2, "zanahorias": 2, "h": 2, "w": 2}
acumulador = 1
for atencion in elevado_alados.values(): # values() es un método en Python que se usa comúnmente en diccionarios para obtener una vista de los valores almacenados 
                                         # en el diccionario.
                                         # Esto significa que devuelve un objeto iterable que proporciona acceso a todos los valores en el diccionario, 
                                         # pero no a las claves asociadas.
    acumulador *= atencion
print(f"Esta es la tabla del 2**2 8 veces, el resultado es: {acumulador}")

