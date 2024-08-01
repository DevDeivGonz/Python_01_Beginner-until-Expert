""""
Escribe un programa que determine si una persona es elegible para votar en una elección:

Condiciones:

La persona debe tener al menos 18 años de edad.
La persona debe ser ciudadana del país donde se realiza la elección.
La persona no debe haber sido condenada por un delito grave.
"""

print("Bienvenido al registro de votaciones 2024")
nombres_apellidos = input("Ingrese su nombre y apellido con el que esta registrado con su documento de identidad")
edad = int(input("Ingrese su edad"))
pais = input("Ingrese de que pais es")
antecedemtes = input("Ingrese si tiene antecedentes penales")

if edad >= 18 and pais == "Colombia" and antecedemtes == "No":
    print(f"Bienvenido {nombres_apellidos}, usted es elegible para votar")
else:
    print(f"Bienvenido {nombres_apellidos}, usted no es elegible para votar")

