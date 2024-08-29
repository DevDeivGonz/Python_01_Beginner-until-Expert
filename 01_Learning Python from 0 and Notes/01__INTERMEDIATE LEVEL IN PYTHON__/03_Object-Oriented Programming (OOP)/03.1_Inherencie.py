# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:41:03 2024

@author: Laptop
"""

# Clase base para operaciones
class Operacion:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def calcular(self):
        raise NotImplementedError("Este método debe ser implementado en la subclase")

# Subclase para suma
class Suma(Operacion):
    def calcular(self):
        return self.valor1 + self.valor2

# Subclase para resta
class Resta(Operacion):
    def calcular(self):
        return self.valor1 - self.valor2
"""
herencia hace que las subclases puedan manejar la misma clase padre, pero diferentes atributos o metodos con super(), pero con poliformismo se usan los mismos atributos de la clase padre
"""
# Subclase para multiplicación
class Multiplicacion(Operacion):
    def calcular(self):
        return self.valor1 * self.valor2

# Subclase para división
class Division(Operacion):
    def calcular(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "Error: División por cero"

def ejecutar_calculadora():
    while True:
        print("\nSeleccione una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == '5':
            break

        valor1 = float(input("Ingrese el primer valor: "))
        valor2 = float(input("Ingrese el segundo valor: "))

        if opcion == '1':
            operacion = Suma(valor1, valor2)
        elif opcion == '2':
            operacion = Resta(valor1, valor2)
        elif opcion == '3':
            operacion = Multiplicacion(valor1, valor2)
        elif opcion == '4':
            operacion = Division(valor1, valor2)
        else:
            print("Opción no válida")
            continue

        resultado = operacion.calcular()
        print(f"El resultado es: {resultado}")

# Ejecutar la calculadora
ejecutar_calculadora()
