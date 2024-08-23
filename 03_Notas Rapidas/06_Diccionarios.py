
# Los diccionarios son colecciones de pares clave-valor. Permiten almacenar y acceder a datos de forma rápida mediante claves únicas.

user_info = {} # Crear un diccionario vacío

# Agregar información al diccionario usando inputs
user_info["name"] = input("Enter your name: ")
user_info["age"] = int(input("Enter your age: "))
user_info["city"] = input("Enter your city: ")

print("User information:", user_info)

for key, value, in user_info.items(): # siempre que se vayan a poner key y value en un bucle se pone items() al final
    print(f"Information is {key}, and the important ticket is {value}")

"""

        Métodos Comunes

get(key, default): Retorna el valor para la clave, o el valor por defecto si la clave no está presente.
keys(): Retorna una vista de las claves del diccionario.
values(): Retorna una vista de los valores del diccionario.
items(): Retorna una vista de los pares clave-valor.
update(other_dict): Actualiza el diccionario con pares clave-valor de otro diccionario.
pop(key): Elimina y retorna el valor para la clave especificada.
popitem(): Elimina y retorna un par clave-valor arbitrario.
clear(): Elimina todos los pares clave-valor del diccionario.

"""
