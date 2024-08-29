import math

class ValoresUsuario:
    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0
        self.resultado = 0
    
    def ingresar_valores(self):
        self.valor1 = float(input("Ingrese primer valor: "))
        self.valor2 = float(input("Ingrese segundo valor: "))

class Operacion_Matematica(ValoresUsuario):
    def __init__(self):
        super().__init__()

    def sumar(self):
        self.resultado = self.valor1 + self.valor2
        print(f"La suma de {self.valor1} y {self.valor2} es {self.resultado}")
        
    def restar(self):
        self.resultado = self.valor1 - self.valor2
        print(f"La resta de {self.valor1} y {self.valor2} es {self.resultado}")
        
    def multiplicar(self):
        self.resultado = self.valor1 * self.valor2
        print(f"La multiplicación de {self.valor1} y {self.valor2} es {self.resultado}")
        
    def dividir(self):
        if self.valor2 != 0:
            self.resultado = self.valor1 / self.valor2
            print(f"La división de {self.valor1} entre {self.valor2} es {self.resultado}")
        else:
            print("No se puede dividir entre 0, elija otro valor")
        
    def potenciar(self):
        self.resultado = self.valor1 ** self.valor2
        print(f"{self.valor1} elevado a {self.valor2} es {self.resultado}")

    def radicar(self):
        if self.valor1 >= 0:
            self.resultado = self.valor1 ** (1 / self.valor2)
            print(f"La raíz {self.valor2}-ésima de {self.valor1} es {self.resultado}")
        else:
            print("No se puede calcular la raíz de un número negativo")
    
    def logaritmo(self):
        if self.valor1 > 0 and self.valor2 > 0:
            self.resultado = math.log(self.valor1, self.valor2)
            print(f"El logaritmo de {self.valor1} en base {self.valor2} es {self.resultado}")
        else:
            print("El valor del logaritmo debe ser mayor que 0")
    
    def convertir(self):
        print(f"\nValor ingresado en:")
        print(f"Decimal: {self.valor1}")
        print(f"Binario: {bin(int(self.valor1))}")
        print(f"Fraccionario: {self.valor1}")
        print()

    def salir_(self):
        print("Saliendo del programa...")
        exit()

def menu():
    operacion = Operacion_Matematica()
    while True:
        print("\nMenú de operaciones:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Potenciación")
        print("6. Radicación")
        print("7. Logaritmo")
        print("8. Convertir valor")
        print("9. Salir")
        
        opcion = int(input("Seleccione una opción: ")) 

        if opcion == 1:
            operacion.ingresar_valores()
            operacion.sumar()
        elif opcion == 2:
            operacion.ingresar_valores()
            operacion.restar()
        elif opcion == 3:
            operacion.ingresar_valores()
            operacion.multiplicar()
        elif opcion == 4:
            operacion.ingresar_valores()
            operacion.dividir()
        elif opcion == 5:
            operacion.ingresar_valores()
            operacion.potenciar()
        elif opcion == 6:
            operacion.ingresar_valores()
            operacion.radicar()
        elif opcion == 7:
            operacion.ingresar_valores()
            operacion.logaritmo()
        elif opcion == 8:
            operacion.ingresar_valores()
            operacion.convertir()
        elif opcion == 9:
            operacion.salir_()
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el menú
menu()
