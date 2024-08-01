import random

def generar_datos():
    # Esta función genera y devuelve datos aleatorios
    return random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100

def procesar_datos(datos):
    # Esta función procesa los datos recibidos como entrada
    print(f"Procesando datos: {datos}")  # Simplemente imprime los datos procesados

while True:
    datos = generar_datos()  # Función que genera datos aleatorios
    procesar_datos(datos)  # Función que procesa los datos
    if random.random() < 0.01:  # Simulación de condición de parada rara
        print("Condición rara alcanzada, deteniendo simulación.")
        break
