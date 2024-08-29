# POO

"""
Attributes and Methods
Instance Attributes

    Atributos de instancia: Son variables que pertenecen a cada objeto creado a partir de            
    una clase.  
    Cada objeto puede tener valores diferentes para sus atributos de instancia.

    Definir atributos de instancia en el constructor (__init__):
    """


class Coche:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def describir(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, y su precio es de ${self.precio}"

toyota = Coche('Toyota', '1990', '20000')

print(toyota.describir())


########################################################################3


print("Segundo ejemplo de POO")

class Calculadora:
    def __init__(self, numero): # inicia la clase, init es el cosntructor
        self.numero = numero

    def sumar(self, otro_numero): # otro numero es que le se agrega a la clase para que se sume.
        return self.numero + otro_numero

    def restar(self, otro_numero):
        return self.numero - otro_numero
    
    def multiplicar(self, mult_num):
        return self.numero * mult_num

# Crear una instancia de la clase Calculadora
calc = Calculadora(5)

# Usar métodos del objeto
print(calc.sumar(3))  # Imprime: 8
print(calc.restar(2))  # Imprime: 3
print(calc.multiplicar(45))