"""
Ejercicio: Sistema de Gestión de Cuentas Bancarias

Descripción:

Vas a crear un sistema para gestionar cuentas bancarias en un banco. Cada cuenta bancaria debe tener la capacidad de:

    Registrar la Información:
        Nombre del titular.
        Número de cuenta.
        Saldo de la cuenta.

    Realizar Operaciones:
        Depositar dinero en la cuenta.
        Retirar dinero de la cuenta (solo si hay suficiente saldo).

    Mostrar Información:
        Mostrar el nombre del titular y el número de cuenta.
        Mostrar el saldo actual.

    Encapsulación:
        Atributos Privados: Utiliza atributos privados para almacenar el saldo y el número de cuenta, asegurando que no
        se modifiquen directamente desde fuera de la clase.
        Atributos Protegidos: Utiliza atributos protegidos para el nombre del titular, permitiendo acceso desde
        subclases, pero sugiriendo que no debe modificarse directamente desde fuera de la clase.

    Métodos:
        Métodos para realizar depósitos y retiros.
        Métodos para mostrar la información de la cuenta.

Requisitos:

    Implementa una clase CuentaBancaria con atributos y métodos adecuados.
    Asegúrate de manejar los errores, como intentar retirar más dinero del que hay en la cuenta.
    Crea una clase CuentaDeAhorros que herede de CuentaBancaria y añade algún comportamiento adicional, como aplicar
    un interés sobre el saldo.
"""

class Cuenta_bancaria:
    def __init__(self, Nombre_del_titular, Número_de_cuenta, Saldo_cuenta):
        self._Nombre_del_titular = Nombre_del_titular
        self.__Número_de_cuenta = Número_de_cuenta
        self._Saldo_cuenta = Saldo_cuenta

    def Depositar_dinero(self, deposito):
        if deposito > 0:
            self._Saldo_cuenta += deposito
        else:
            print("Cantidad no válida para depositar.")

    def Retirar_dinero(self, retiro):
        if self._Saldo_cuenta <= 0:
            print(f"No se puede retirar dinero ya que no hay dinero.")
        else:
            self._Saldo_cuenta -= retiro

    def mostrar_info(self):
        print(f"El nombre del titular de la cuenta es: {self._Nombre_del_titular},\n"
              f"el numero de la cuenat es: {self.__Número_de_cuenta},\n"
              f"el saldo actual de la cuenta es {self._Saldo_cuenta}")


brandon_cuenta = Cuenta_bancaria('Brandon David Gonzalez', '2899yup92j890', 0 )
print(brandon_cuenta.Depositar_dinero(340000))
print(brandon_cuenta.Retirar_dinero(20000))
print(brandon_cuenta.mostrar_info())
