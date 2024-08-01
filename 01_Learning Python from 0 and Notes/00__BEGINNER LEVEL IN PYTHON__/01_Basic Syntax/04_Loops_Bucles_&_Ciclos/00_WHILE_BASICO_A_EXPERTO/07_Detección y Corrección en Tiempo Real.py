"""  
Se utiliza para verificar continuamente una condición hasta que se cumpla, generalmente con una función de verificación que devuelve True cuando la condición se cumple.
""" 

import time

# Función que simula la verificación del estado del sensor
def verificar_sensor():
    # Aquí iría la lógica para verificar el estado del sensor
    # En este ejemplo, se simula que el sensor se activa aleatoriamente
    import random
    return random.choice([True, False])

sensor_activado = False
while not sensor_activado:
    sensor_activado = verificar_sensor()  # Función que verifica el estado del sensor
    if sensor_activado:
        print("Sensor activado. Procesando datos...")
    else:
        time.sleep(1)  # Esperar un segundo antes de verificar nuevamente



