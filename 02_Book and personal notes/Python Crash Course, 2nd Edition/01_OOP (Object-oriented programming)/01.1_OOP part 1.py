"""

What is Object-Oriented Programming (OOP)?

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects,"
which can contain data and code. The data is in the form of fields (often known as attributes or properties),
and the code is in the form of procedures (often known as methods). OOP aims to implement real-world entities like inheritance,
polymorphism, encapsulation, and abstraction in programming.

Key Concepts of OOP

    Class:
    A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects can use.

    Object:
    An object is an instance of a class. When a class is defined, no memory is allocated until an object of that class is created.

    Attributes:
    Attributes are the data stored inside an object and represent the state or quality of the object.

    Methods:
    Methods are the functions defined inside a class that describe the behaviors of the objects.

    Encapsulation:
    Encapsulation is the mechanism of restricting access to some of an object's components and preventing the accidental
    modification of data. This is typically done by making attributes private and providing public methods to access and modify them.

    Inheritance:
    Inheritance is the mechanism by which one class can inherit attributes and methods from another class. This allows
    for code reuse and the creation of a hierarchy of classes.

    Polymorphism:
    Polymorphism allows for using a single interface to represent different underlying data types. This is often implemented
    through method overriding, where a subclass provides a specific implementation of a method that is already defined in its superclass.

    Abstraction:
    Abstraction involves hiding the complex implementation details of a system and exposing only the necessary and
    relevant parts to the user.


"""

def clear_console():
  print("\n"*6)

class Car: # se define el nombre de la clase
  # Constructor Method (__init__):
  def __init__(self, mark, year_model, cost, id_identification_product): # inicia el method y se denomina sus valores preterminados
    self.mark = mark # se defines los valores dentro de la function def __init__(self)
    self.year_model = year_model
    self.cost = cost
    self.id_identification_product = id_identification_product

car_1 = Car("Mercedes", 2020, 25000, "2990099292")
print(f"""
  The car {car_1.mark.upper()},the year model is {car_1.year_model},
  his cost is ${car_1.cost} and the ID number is {car_1.id_identification_product}.""")

car_2 = Car("BMW", 2021, 55000, "18992002002")
print(f"""
  The car {car_2.mark.upper()},the year model is {car_2.year_model},
  his cost is ${car_2.cost} and the ID number is {car_2.id_identification_product}.""")

car_3 = Car("Audi", 2022, 53000, "8282910901010")
print(f"""
  The car {car_3.mark.upper()},the year model is {car_3.year_model},
  his cost is ${car_3.cost} and the ID number is {car_3.id_identification_product}.""")

car_4 = Car("Toyota", 2021, 30000, "82829201010")
print(f"""
  The car {car_4.mark.upper()},the year model is {car_4.year_model},
  his cost is ${car_4.cost} and the ID number is {car_4.id_identification_product}.""")

class Productos_plasticos:
  def __init__(self, nombre_producto, id_producto, precio_producto, medidas_producto, cantidades_disponibles_producto):
    self.nombre_producto = nombre_producto
    self.id_producto = id_producto
    self.precio_producto = precio_producto
    self.medidas_producto = medidas_producto
    self.cantidades_disponibles_producto = cantidades_disponibles_producto

bolsa_negra = Productos_plasticos("Bolsa negra", "1999022", 5500, "22cm x 20cm", 34)
print(f"""
Este es el producto {bolsa_negra.nombre_producto}, su iD es el {bolsa_negra.id_producto}, su precio es {bolsa_negra.precio_producto},
sus medidas son {bolsa_negra.medidas_producto} y la cantidad disponible de este producto en las bodegas es de {bolsa_negra.cantidades_disponibles_producto} por unidad.""")

