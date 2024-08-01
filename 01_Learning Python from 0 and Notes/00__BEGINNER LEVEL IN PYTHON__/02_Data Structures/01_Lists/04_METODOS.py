import os
def limpiar_pantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
        
print("Se usa extend")

lista_carnes = ["Cerdo", "Res", "Pollo"]
lista_verduras = ["Apio", "Alberjas", "Frijol verde"]
precio_carnes = [50000]
precio_verduras = [ 40000]

lista_carnes.extend(precio_carnes) # de esta manera, se agregan dos listas para cuando se llamen no aparezca uno sino las dos, ya que aqui se une la lista_carnes y la lista_verduras como una sola lista
lista_verduras.extend(precio_verduras)
print(f"Aqui esta la lista de carnes y su precio total: \n, {lista_carnes}, \nAqui esta la lista de verduras y su precio total: , {lista_verduras}")

input("PASE CON ENTER")
limpiar_pantalla()

print("USANDO .append")
lista_carnes.append(lista_verdurasta_) # Usando .append()
print("Aquí esta la lista de los alimentos comprados: ", lista_carnes) # Usando .append()

input("PASE CON ENTER")
limpiar_pantalla()

lista_chi = [1, 2, 3,]
lista_ño = [4 , 5, 6, 7, 8, 9, 10]
# Usando +=
lista_chi += lista_ño
print("Con +=:", lista_chi) # tambien hace lo mismo que los anteriores, suma una lista con otra lista para que quede unidas

#################################################
input("PASE CON ENTER")
limpiar_pantalla()
#################################################

