# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:04:00 2024

@author: Laptop
"""

"""
 1. Crear una lista vacía: Inicializa una lista vacía y asigna el resultado a una variable llamada mi_lista.

2. Agregar elementos: Agrega los siguientes elementos a la lista mi_lista: 
   "manzana", "banana", "cereza".

3. Acceder a elementos: Imprime el segundo elemento de la lista mi_lista.

4. Modificar elementos: Cambia el primer elemento de la lista mi_lista a "pera".

5. Eliminar elementos: Elimina el tercer elemento de la lista mi_lista.

6. Longitud de la lista: Calcula y muestra la cantidad de elementos que tiene 
   mi_lista.

7. Iteración: Utiliza un bucle for para imprimir cada elemento de mi_lista en una línea 
   separada.

8. Concatenación: Crea una segunda lista llamada otra_lista con los elementos   
   "naranja", "uva". Luego, concatena otra_lista a mi_lista.

9. Ordenamiento: Ordena mi_lista en orden ascendente.

10. Búsqueda: Verifica si "banana" está presente en mi_lista y muestra el
    resultado.
"""
def limpiar_pantalla():
    print("\n"*50)


print("1. Crear una lista vacía: Inicializa una lista vacía y asigna el resultado a una variable llamada mi_lista.")

mi_lista = ["manzanas", "pescados", "Bananas", "Atun"]
print(mi_lista)

input("ENTER PARA CONTINUAR")
limpiar_pantalla()

print("2. Agregar elementos: Agrega los siguientes elementos a la lista mi_lista: manzana, banana, cereza.")

lista_2 = ["manzana", "banana", "cereza"]

mi_lista.extend(lista_2)

print(mi_lista)

input("ENTER PARA CONTINUAR")
limpiar_pantalla()

print("3. Acceder a elementos: Imprime el segundo elemento de la lista mi_lista.")

print("Aqui esta el segundo elemento de la lista: ", mi_lista[1])

input("ENTER PARA CONTINUAR")
limpiar_pantalla()

print("4. Modificar elementos: Cambia el primer elemento de la lista mi_lista a pera.")

mi_lista[0] = "pera"
print(mi_lista)
