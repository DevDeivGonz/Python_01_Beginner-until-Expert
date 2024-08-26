print("lista de comprension basica")
numeros_impares = [numero for numero in range(1, 21) if numero % 2 != 0] # lista de comprension basica
print(f"{numeros_impares}")

nombres = ['ana maria', ' beatriz rojas', 'ximena anaiz vela']
all_names = [name for name in nombres]
print(all_names)

edades_estudiantes = [edad for edad in range(10, 45) if 18 < edad <=40]
print(f'\n\n{edades_estudiantes}')

numeros_random = []  # Lista para almacenar los números ingresados

for _ in range(4):  # El bucle se repetirá 4 veces
    numero = int(input('Ingrese un número: '))
    numeros_random.append(numero)  # Agregar el número a la lista

# Filtrar los números divisibles por 3 usando comprensión de lista
mostrar_todo = [num for num in numeros_random if num % 3 == 0]

print("Números divisibles por 3:", mostrar_todo)