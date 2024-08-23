def clear_space():
    print("\n\n\n\n")

list_productos = ["papas", "azucar", "maiz"]
print(list_productos)

"""
    Métodos Comunes
    
    append(item): Agrega un elemento al final de la lista.
    extend(iterable): Extiende la lista agregando todos los elementos del iterable.
    insert(index, item): Inserta un elemento en una posición específica.
    remove(item): Elimina la primera aparición del elemento.
    pop(index): Elimina y retorna el elemento en la posición dada.
    sort(): Ordena los elementos de la lista en su lugar.
    reverse(): Invierte el orden de los elementos de la lista.
    clear(): Elimina todos los elementos de la lista.
"""

list_numbers = []

while True: # aqui el input seran los que quieramos hasta pulsar done, asi se terminara la iteracion
    user_input = input("Enter a number to add to the list (or 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    try:
        number = int(user_input)
        list_numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")

print("Final list:", list_numbers)

clear_space()

second_list_numbers = []

for _ in range(7): # Agregar números a la lista con entradas o inputs limitados, en este caso solo se puede ingresar 7 inputs,
                   # ya que range declara cuantas veces se repetira.

    num = int(input("Enter a number: "))
    second_list_numbers.append(num)

print("The numbers you entered are:", second_list_numbers)
