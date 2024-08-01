# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 23:49:37 2024

@author: Laptop
"""

"""
Tienes una lista de palabras. Realiza las siguientes operaciones:

1. Encuentra y muestra la palabra más larga en la lista.
2. Cuenta y muestra cuántas palabras tienen más de 5 caracteres.
3. Crea una nueva lista que contenga solo las palabras que comienzan con una vocal (a, e, i, o, u) y muestra esta lista.
4. Ordena la lista de palabras en orden alfabético y muestra la lista ordenada.
"""
def limpiar_pantalla():
    print('\n' * 40)
limpiar_pantalla()


list_words = ["papas", "atun", "aguacate", "mais", "frijoles", "lentejas", "zanahorias", "esparragos", "tomate", "maní", "sal"]

print("1. Encuentra y muestra la palabra más larga en la lista.")

palabra_mas_larga = max(list_words, key=len) # max() devuelve el elemento más grande de una secuencia y key=len para especificar que queremos comparar los elementos en función de su longitud.
print("La palabras mas larga es: ", palabra_mas_larga)

# segundo ejemplo 
palabra_mas_corta = min(list_words, key=len)
print("La palabras mas corta es: ", palabra_mas_corta)

print("\n2. Cuenta y muestra cuántas palabras tienen más de 5 caracteres.\n")

contador_palabras_mayor_5 = 0
palabras_mayor_5 = []

# Recorre cada palabra en la lista
for word in list_words:
    # Verifica si la longitud de la palabra es mayor que 5
    if len(word) > 5:
        # Incrementa el contador
        contador_palabras_mayor_5 += 1
        # Agrega la palabra a la lista de palabras que cumplen la condición
        palabras_mayor_5.append(word)

# Muestra el resultado
print("El número de palabras con más de 5 caracteres es: ", contador_palabras_mayor_5)
print("Las palabras que tienen más de 5 caracteres son: ", palabras_mayor_5)

input("Enter para continuar")
limpiar_pantalla()
    
print("Hola otra vez")
print("Holaaaaaaaaaaa")


lista_2 = []

words = input("Ingrese su lista de compras: ")
palabras = words.split()

for word in palabras:
    try:
        word = word.strip()
        lista_2.append(word)
    except ValueError:
        print(f"Advertencia: '{word}' no está en el inventario.")

print(f"Aquí está la lista de su carrito de compras: {lista_2}")
