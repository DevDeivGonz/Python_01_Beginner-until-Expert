# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 12:19:05 2024

@author: Laptop
"""

"""
Hacer un programa que solicite por teclado dos número y muestre la suma , la resta ,la 
multiplicación y la división de esos números 

"""
def suma():
    num1 = int(input("Ingrese el numero 1: "))
    num2 = int(input("Ingrese el numero 2: "))
    resultado = num1 + num2 
    print(f" La suma de {num1} y {num2} es de : {resultado}")
    continuar = input("""
          
          ¿DESEA CONTINUAR?, 
          
          [SI] PARA CONTINUAR
          [NO] PARA VOLVER AL MENÚ PRINCIPAL: """).lower()
    
    while True:
        if continuar == "si":
            suma()
        elif continuar == "no":
            menu_principal()
            break
        else:
            print("ERROR. Elija una opción válida")

def resta():
    num1 = int(input("Ingrese el numero 1: "))
    num2 = int(input("Ingrese el numero 2: "))
    resultado = num1 - num2 
    print(f" La reta de {num1} y {num2} es de : {resultado}")
    continuar = input("""
          
          ¿DESEA CONTINUAR?, 
          
          [SI] PARA CONTINUAR
          [NO] PARA VOLVER AL MENÚ PRINCIPAL: """).lower()
    
    while True:
        if continuar == "si":
            resta()
        elif continuar == "no":
            menu_principal()
            break
        else:
            print("ERROR. Elija una opción válida")
            
def multiplicacion():
    num1 = int(input("Ingrese el numero 1: "))
    num2 = int(input("Ingrese el numero 2: "))
    resultado = num1 * num2 
    print(f" La multiplicacion de {num1} y {num2} es de : {resultado}")
    continuar = input("""
          
          ¿DESEA CONTINUAR?, 
          
          [SI] PARA CONTINUAR
          [NO] PARA VOLVER AL MENÚ PRINCIPAL: """).lower()
    
    while True:
        if continuar == "si":
            multiplicacion()
        elif continuar == "no":
            menu_principal()
            break
        else:
            print("ERROR. Elija una opción válida")

def division():

    num1 = int(input("Ingrese el numero 1: "))
    num2 = int(input("Ingrese el numero 2: "))
    if num1 == 0 or num2 == 0:
       print("No se puede dividir por 0, eliga solo numeros enteros. ")
    else: 
        resultado = num1 / num2 
        print(f" La division de {num1} y {num2} es de : {resultado}")
        continuar = input("""
              
              ¿DESEA CONTINUAR?, 
              
              [SI] PARA CONTINUAR
              [NO] PARA VOLVER AL MENÚ PRINCIPAL: """).lower()
    
    
        while True:
            if continuar == "si":
                division()
            elif continuar == "no":
                menu_principal()
                break
            else:
                print("ERROR. Elija una opción válida")

def menu_principal():
    print("""
          Calculadora básica de Python
          
          Eliga una opción
          
          [1] Suma
          [2] Resta
          [3] Multiplicación
          [4] División
          [5] Salir
          """)
          
    while True:
        opcion = int(input("Elija una opción: "))
        
        if opcion == 1:
            suma()
        elif opcion == 2:
            resta()
        elif opcion == 3:
            multiplicacion()
        elif opcion == 4:
            division()
        elif opcion == 5:
            print("Gracias por elegirnos, tenga un excelente día.")
            break
        else:
            print("ERROR. Eliga una opcion valida. ")
            


if __name__ == "__main__": #siempre llamara al menu principal, sin esto no correra el codigo
   menu_principal()
