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

# Classes, Objects, Attributes, Methods and Basic Encapsulation

class Student:
    def __init__(self, name_student, age_student, course_student, average_student):
        self.name_student = name_student
        self.age_student = age_student
        self.course_student = course_student
        self.average_student = average_student

    def display_info(self):
        print(f"This is the student {self.name_student}, her age is {self.age_student},"
              f" her grade is {self.course_student} and her average in all semesters was {self.average_student}.")

    def adult_or_minor(self):
        if self.age_student >= 18:
            print(f" Dear {self.name_student}, you are adult.")
        else:
            print(f" Dear {self.name_student}, you are a minor.")

    def final_notes(self):
        if self.average_student >= 100:
            print(f"Excellent average {self.name_student}, you have the perfect score so far!")
        elif self.average_student >= 90:
            print(
                f"Dear {self.name_student}, amazing congratulations on your excellent grades with "
                f"{self.average_student} this semester, keep it up!")
        elif self.average_student >= 70:
            print(f"Dear {self.name_student}, you have passed the semester with {self.average_student}. "
                  f"However, cheer up for a better semester next time!")
        else:
            print(f"Dear {self.name_student}, unfortunately you have not passed the semester.")


student_marcela_fuentes = Student("Mariana Fuentes", 18,
                                  "9° grade", 78) # Create an instance of Student

student_marcela_fuentes.display_info()
student_marcela_fuentes.final_notes()
print("\n")
camilo_vargas = Student("camilo vargas", 21,
                        "9° grade", 56)
camilo_vargas.adult_or_minor()
camilo_vargas.final_notes()
print("\n")
sofia_vergara = Student("Sofia Vergara", 16,
                        "11° grade", 90)
sofia_vergara.display_info()
sofia_vergara.adult_or_minor()
sofia_vergara.final_notes()
print("\n")
brandon_gonzalez = Student("Brandon David Gonzalez", 22,
                           "11° grade", 100)
brandon_gonzalez.adult_or_minor()
brandon_gonzalez.display_info()
brandon_gonzalez.final_notes()
print("\n")