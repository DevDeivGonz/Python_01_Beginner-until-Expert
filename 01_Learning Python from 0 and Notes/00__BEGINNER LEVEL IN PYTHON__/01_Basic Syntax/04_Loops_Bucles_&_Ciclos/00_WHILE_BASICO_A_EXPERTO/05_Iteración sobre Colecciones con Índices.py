lista = [1, 2, 3, 4, 5]
i = 0
while i < len(lista):
    print(lista[i])
    i += 1

input("ENTER PARA CONTINUAR")

lista = [1, 2, 3, 4, 5]
for i, elemento in enumerate(lista):
    print(f"Índice: {i}, Elemento: {elemento}")

input("ENTER PARA CONTINUAR")

lista_1 = ["Papel", "Lapiz", "Carton"]

i = 0 

while i < len(lista_1):
    print(lista_1[i])
    i += 1

# Resumen:
# i = 0: Empieza desde el primer elemento de la lista.
# i = 1: Empieza desde el segundo elemento de la lista.
# i = -1: Accede al último elemento de la lista pero puede causar un bucle infinito si no se maneja adecuadamente.