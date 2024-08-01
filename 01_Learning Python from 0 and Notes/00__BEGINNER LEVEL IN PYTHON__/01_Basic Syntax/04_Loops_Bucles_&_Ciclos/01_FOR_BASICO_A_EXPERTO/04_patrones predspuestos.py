numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares = []
for numero in numeros:
    if numero % 2 != 0:
        impares.append(numero)
print(impares)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)