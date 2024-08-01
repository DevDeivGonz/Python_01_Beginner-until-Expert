# Función print()
mensaje = "Hola, mundo!"
print(mensaje)

# Función len()
lista = [1, 2, 3, 4, 5]
longitud = len(lista)
print("Longitud de la lista:", longitud)

# Función input()
nombre = input("Ingrese su nombre: ")
print("Hola,", nombre)

# Función range()
numeros = range(1, 6)  # Genera los números del 1 al 5
for num in numeros:
    print(num)

# Función str()
numero = 42
cadena = str(numero)
print("El número convertido a cadena:", cadena)

# Función int()
cadena = "123"
numero = int(cadena)
print("La cadena convertida a entero:", numero)

# Función float()
cadena = "3.14"
numero = float(cadena)
print("La cadena convertida a número flotante:", numero)

# Función list()
tupla = (1, 2, 3)
lista = list(tupla)
print("La tupla convertida a lista:", lista)

# Función sorted()
lista = [3, 1, 4, 1, 5, 9, 2]
lista_ordenada = sorted(lista)
print("Lista ordenada:", lista_ordenada)

# Función zip()
nombres = ["Alice", "Bob", "Charlie"]
edades = [30, 25, 35]
datos = zip(nombres, edades)
for nombre, edad in datos:
    print(nombre, "tiene", edad, "años.")


# Función max()
numeros = [3, 7, 2, 8, 5]
maximo = max(numeros)
print("El máximo de la lista es:", maximo)

# Función min()
minimo = min(numeros)
print("El mínimo de la lista es:", minimo)

# Función sum()
suma = sum(numeros)
print("La suma de los números en la lista es:", suma)

# Función abs()
valor_absoluto = abs(-42)
print("El valor absoluto de -42 es:", valor_absoluto)

# Función round()
numero_decimal = 3.14159
redondeado = round(numero_decimal, 2)
print("El número decimal redondeado a dos decimales es:", redondeado)

# Función pow()
potencia = pow(2, 3)
print("2 elevado a la 3 es:", potencia)

# Función enumerate()
paises = ["España", "Francia", "Italia"]
for indice, pais in enumerate(paises):
    print("País", indice + 1, ":", pais)

# Función reversed()
reversa = reversed(numeros)
print("Lista en orden inverso:", list(reversa))

# Función any()
valores = [False, False, True, False]
algun_true = any(valores)
print("¿Hay algún valor True en la lista?", algun_true)

# Función all()
todos_true = all(valores)
print("¿Todos los valores en la lista son True?", todos_true)

# Función len()
cadena = "Hola mundo"
longitud = len(cadena)
print("La longitud de la cadena es:", longitud)

# Función sorted()
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
ordenados = sorted(numeros)
print("Lista ordenada:", ordenados)

# Función zip()
nombres = ["Juan", "María", "Pedro"]
edades = [30, 25, 35]
for nombre, edad in zip(nombres, edades):
    print(nombre, "tiene", edad, "años")

# Función filter()
def es_par(numero):
    return numero % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = filter(es_par, numeros)
print("Números pares:", list(pares))

# Función map()
def duplicar(numero):
    return numero * 2

numeros = [1, 2, 3, 4, 5]
dobles = map(duplicar, numeros)
print("Dobles de los números:", list(dobles))

# Función join()
palabras = ["Hola", "mundo", "Python"]
frase = " ".join(palabras)
print("Frase unida:", frase)

# Función split()
texto = "Python es un lenguaje de programación"
palabras = texto.split()
print("Palabras separadas:", palabras)

# Función format()
nombre = "Juan"
edad = 30
print("Hola, me llamo {} y tengo {} años".format(nombre, edad))

# Función isinstance()
x = 5
print("¿x es de tipo entero?", isinstance(x, int))

# Función range()
for i in range(5):
    print("Número:", i)
