class Operacion:
    def __init__(self):
        self.valores = []  # Inicializa una lista vacía para almacenar los valores
        # Usa un bucle para capturar cinco valores
        for valor_ingresado in range(5):
            valor = int(input(f"Ingrese valor {valor_ingresado + 1}: "))
            self.valores.append(valor)  # Agrega cada valor a la lista

        # Imprime todos los valores capturados
        print("Valores ingresados:", self.valores)
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()
        self.potenciar()

    def sumar(self):
        suma = sum(self.valores)
        print(f"La suma de los valores es {suma}")

    def restar(self):
        if len(self.valores) > 1:
            resta = self.valores[0]
            for valor in self.valores[1:]:
                resta -= valor
            print(f"La resta de los valores es {resta}")
        else:
            print("No hay suficientes valores para restar")

    def multiplicar(self):
        if self.valores:
            multi = 1
            for valor in self.valores:
                multi *= valor
            print(f"El producto de los valores es {multi}")
        else:
            print("No hay valores para multiplicar")

    def dividir(self):
        if len(self.valores) > 1:
            divi = self.valores[0]
            for valor in self.valores[1:]:
                if valor != 0:
                    divi /= valor
                else:
                    print("Error: División por cero no permitida")
                    return
            print(f"La división de los valores es {divi}")
        else:
            print("No hay suficientes valores para dividir")

    def potenciar(self):
        if len(self.valores) > 1:
            potencia = self.valores[0] ** self.valores[1]
            print(f"La potenciación de {self.valores[0]} elevado a {self.valores[1]} es igual a: {potencia}")
        else:
            print("No hay suficientes valores para calcular la potenciación")

# Crear una instancia de la clase
operacion1 = Operacion()
