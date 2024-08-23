def clean_space():
    print("\n"* 5)
"""

Listas:

    Definición:
    .Una lista es una colección ordenada de elementos que es mutable, lo que significa que se puede cambiar
    después de su creación.

    Sintaxis: Se define usando corchetes [].

"""

lista_basica_num = [128, 182929, 2892020, 8282382832]
print(f"Lista basica {lista_basica_num}")

clean_space()

import re
"""
lista_numbers = []
print("Ingreso de valores int/floeat/numericos a listas.\n")
input_numbers = input("Ingrese los números separados por espacios (sin comas u otros caracteres):\t") # Ingresar números como cadena de texto

input_numbers_clean = re.sub(r'[^\d\s]', '', input_numbers) # Limpiar la entrada eliminando comas y otros caracteres no deseados
""" 
        # r'[^\d\s]': ---> Esta expresión regular busca cualquier carácter que no sea un dígito (\d) o un espacio (\s).
        # re.sub(...): --> Reemplaza esos caracteres no deseados con una cadena vacía (''), limpiando así la entrada del
        #  usuario para que solo queden números y espacios.
"""

try: # Dividir la cadena limpia en partes y convertir cada parte en entero
    lista_numbers = [int(num) for num in input_numbers_clean.split() if num]
    print(f"Aquí está la lista de números introducida:\n {lista_numbers}")
except ValueError:
    print("Error: Asegúrate de que todos los valores sean enteros válidos separados por espacios.")
"""
clean_space()

""" Asi se ponen valores numeros en las listas, pero se deben usar List of Comprehension """

calificaciones = []

notas_estudiante = (input("Ingrese las nots del estudiante:\t"))
notas_estudiante_limpiar = re.sub(r'[^\d\s]', '', notas_estudiante)
""" 
    . r'[^\d\s]': ---> Esta expresión regular busca cualquier carácter que no sea un dígito (\d) o un espacio (\s).
    . re.sub(...): --> Reemplaza esos caracteres no deseados con una cadena vacía (''), limpiando así la entrada del
      usuario para que solo queden números y espacios.
"""
try:
    calificaciones = [int(calificacion) for calificacion in notas_estudiante_limpiar.split() if calificacion]
except ValueError:
    print("Error, ingrese una calificacion valida.")

print(f"Aqui estan las notas del estudiante:\n {calificaciones}")