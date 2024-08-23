"""

Resumen

    append(): Añade un elemento al final.
    extend(): Añade varios elementos al final.
    insert(): Inserta un elemento en una posición específica.
    remove(): Elimina la primera ocurrencia de un valor.
    pop(): Elimina y devuelve un elemento de una posición específica.
    index(): Encuentra el índice de un valor.
    count(): Cuenta las ocurrencias de un valor.
    sort(): Ordena la lista en su lugar.
    reverse(): Invierte el orden de los elementos.
    copy(): Crea una copia superficial de la lista.

"""
lista_productos = ["Jabon", "Detergente", "Shampoo"]
print(lista_productos)

lista_productos.append("Mayoneza")
print(lista_productos)

new_lista = ["Pepinillos", "Tomates", "Arroz"]

lista_productos.extend(new_lista)
print(lista_productos)

new_jabones = ["Jabones de limon", "Jabones de limon", "Jabones de limon", "Jabones de limon", "Jabones de limon"]
lista_productos.extend(new_jabones)
print(lista_productos)

print(f"Hay {lista_productos.count('Jabones de limon')} jabones de limon")

lista_productos.sort()
print(f"{lista_productos}")

lista_productos.reverse()
print(f"{lista_productos}")

