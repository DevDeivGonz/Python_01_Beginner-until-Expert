"""
Descripción:

    Vas a crear un sistema sencillo para gestionar empleados en una empresa. Cada empleado tiene un nombre, un salario,
    y una antigüedad en años. El sistema debe permitir agregar empleados, calcular aumentos salariales basados en la
    antigüedad, y listar a todos los empleados que cumplan ciertas condiciones.
"""

class Empleado: # la clase
    def __init__(self, nombre_empleado, salario_empleado, anos_trabajado_del_empleado ): # constructor de la clase
        self.nombre_empleado = nombre_empleado # atributos
        self.salario_empleado = salario_empleado # atributos
        self.anos_trabajado_del_empleado = anos_trabajado_del_empleado # atributos

    def calcular_aumentos_salariales(self):
        if self.anos_trabajado_del_empleado >= 10: # se encapsula el atributo 'anos_trabajado_del_empleado'.
            self.salario_empleado += 5000000
            print(f"Ahora el empleado {self.nombre_empleado} tiene un salario de ${self.salario_empleado}")
        elif self.anos_trabajado_del_empleado >= 5:
            self.salario_empleado += 3000000
            print(f"Ahora el empleado {self.nombre_empleado} tiene un salario de ${self.salario_empleado}")
        elif self.anos_trabajado_del_empleado >= 2:
            self.salario_empleado += 1500000
            print(f"Ahora el empleado {self.nombre_empleado} tiene un salario de ${self.salario_empleado}")
        else:
            print(
                f"El empleado {self.nombre_empleado} no puede recibir un aumento de salario, ya que aún no ha superado los dos años "
                f"de estancia laboral en la empresa, por lo tanto el salario ${self.salario_empleado} seguirá siendo el mismo.")


empleado_gonzalez29992 = Empleado('Brandon David Gonzalez', 2500000,
                                  2)
empleado_8289299 = Empleado('Sofia Vergara', 2400000, 1)

print(empleado_gonzalez29992.calcular_aumentos_salariales()) # se calcula los salarios llamando el metodo calcular_aumentos_salariales
                                                            # de la clase Empleado
print(empleado_8289299.calcular_aumentos_salariales())
