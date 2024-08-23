"""
Encapsulación y Datos Privados

    En Python, puedes definir atributos privados para una clase utilizando un guion bajo (_) o doble guion bajo (__) al
    comienzo del nombre del atributo. Aquí te explico la diferencia:

    Atributos con un guion bajo (_):
    Esto indica que el atributo es "protegido", lo que es más una convención que una restricción real.
    Significa que no deberías acceder a este atributo desde fuera de la clase, pero Python no impide
    que lo hagas.

    Atributos con doble guion bajo (__):
    Esto crea un nombre "mangling" o un cambio de nombre que hace más difícil (pero no imposible) acceder a estos
    atributos desde fuera de la clase. Python cambia el nombre del atributo internamente para incluir el nombre de
    la clase, lo que evita colisiones de nombres en clases derivadas.

"""

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular      # Atributo protegido
        self.__saldo = saldo         # Atributo privado

    def mostrar_saldo(self):
        return f"El saldo de {self._titular} es {self.__saldo}."

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("Cantidad no válida para depositar.")

cuenta = CuentaBancaria("Carlos", 1000)
print(cuenta.mostrar_saldo())  # Correcto

# Acceso a atributos protegidos y privados:

print(cuenta._titular)          # Acceso permitido, pero no recomendado
# print(cuenta.__saldo)        # Esto dará error
print(cuenta.depositar(5000))
print(cuenta._CuentaBancaria__saldo)  # Acceso posible, pero no recomendado
