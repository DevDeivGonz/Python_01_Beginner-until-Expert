
"""
Encapsulation

Encapsulation is the concept of bundling the data (attributes) and methods (functions) that operate on the data into a
single unit or class.
It also restricts direct access to some of the object's components, which is a means of preventing accidental interference
and misuse of the data.

Step-by-Step:

    Private Attributes:
        In Python, you can define private attributes by prefixing the attribute name with double underscores __.
        These attributes cannot be accessed directly from outside the class.

    Getter and Setter Methods:
        To access and modify private attributes, you use getter and setter methods.
        These methods provide controlled access to the private attributes.

Example:

"""
"""
1. Encapsulación

La encapsulación es el concepto de agrupar los datos (atributos) y los métodos (funciones) que operan sobre esos datos en una única unidad o clase. También restringe el acceso directo a algunos componentes del objeto, lo que previene la interferencia accidental y el mal uso de los datos.
Paso a Paso:

    Atributos Privados:
        En Python, puedes definir atributos privados anteponiendo doble guion bajo __ al nombre del atributo.
        Estos atributos no pueden ser accedidos directamente desde fuera de la clase.

    Métodos Getter y Setter:
        Para acceder y modificar los atributos privados, se utilizan métodos getter y setter.
        Estos métodos proporcionan acceso controlado a los atributos privados.

"""

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad  # Atributo privado

    # Método getter para nombre
    def obtener_nombre(self):
        return self.__nombre

    # Método setter para nombre
    def establecer_nombre(self, nombre):
        self.__nombre = nombre

    # Método getter para edad
    def obtener_edad(self):
        return self.__edad

    # Método setter para edad
    def establecer_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad debe ser un valor positivo")

# Ejemplo de uso
persona = Persona("Juan", 25)
print(persona.obtener_nombre())  # Accediendo al nombre usando el getter
persona.establecer_edad(30)  # Modificando la edad usando el setter
print(persona.obtener_edad())

"""
2. Herencia

La herencia permite que una clase (subclase) herede atributos y métodos de otra clase (superclase). 
Esto promueve la reutilización de código y establece una jerarquía natural.

Paso a Paso:

    Superclase:
        Define la clase padre con atributos y métodos comunes.

    Subclase:
        Define una clase hija que hereda de la superclase.
        La subclase puede extender o sobrescribir los atributos y métodos de la superclase.

"""

# Superclase
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("Algún sonido genérico")

# Subclase
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Llamar al constructor de la superclase
        self.raza = raza

    def hacer_sonido(self):  # Sobrescribir el método hacer_sonido
        print("¡Guau!")

# Ejemplo de uso
perro = Perro("Buddy", "Golden Retriever")
print(perro.nombre)  # Atributo heredado
print(perro.raza)  # Atributo específico de la subclase
perro.hacer_sonido()  # Método sobrescrito

"""
3. Polimorfismo

El polimorfismo permite que los métodos hagan cosas diferentes según el objeto sobre el que actúan, aunque compartan el mismo nombre. Esto se logra a menudo mediante la sobrescritura de métodos.
Paso a Paso:

    Sobrescritura de Métodos:
        Una subclase proporciona una implementación específica de un método que ya está definido en su superclase.
        La firma del método permanece igual, pero la implementación puede diferir.

    Uso del Polimorfismo:
        El polimorfismo permite llamar al mismo método en diferentes objetos y que cada objeto responda de manera distinta.

"""

class Pájaro:
    def hacer_sonido(self):
        print("Pío")

class Gato:
    def hacer_sonido(self):
        print("Miau")

# Ejemplo de uso
animales = [Pájaro(), Gato()]

for animal in animales:
    animal.hacer_sonido()  # Diferentes salidas para diferentes objetos

"""

4. Abstracción

La abstracción implica ocultar los detalles complejos de implementación y exponer solo las partes necesarias y relevantes de un objeto. Esto se hace a menudo usando clases abstractas e interfaces.
Paso a Paso:

    Clase Abstracta:
        Una clase abstracta no puede ser instanciada y está destinada a ser subclaseada.
        Puede tener métodos abstractos, que son métodos declarados pero que no contienen implementación.

    Implementación de Subclase:
        Las subclases heredan de la clase abstracta y proporcionan implementaciones concretas para los métodos abstractos.

"""

from abc import ABC, abstractmethod

# Clase abstracta
class Forma(ABC):
    @abstractmethod
    def area(self):
        pass  # Método abstracto sin implementación

# Subclase
class Círculo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio * self.radio

# Subclase
class Rectángulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

# Ejemplo de uso
formas = [Círculo(5), Rectángulo(4, 6)]

for forma in formas:
    print(forma.area())  # Llama al método area específico de cada forma

"""
Resumen:

    Encapsulación: Protege el estado del objeto manteniendo los atributos privados y proporcionando métodos públicos para acceder y modificarlos.
    Herencia: Permite que una clase herede atributos y métodos de otra clase.
    Polimorfismo: Permite que el mismo método se comporte de manera diferente según el objeto sobre el que actúa.
    Abstracción: Oculta detalles complejos de implementación y expone solo las partes necesarias al usuario.

"""