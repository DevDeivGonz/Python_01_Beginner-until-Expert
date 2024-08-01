""" 
Escribe un programa que solicite al usuario ingresar una contraseña. 
El programa deberá seguir solicitando la contraseña hasta que el usuario ingrese la contraseña correcta. Una vez que la contraseña correcta sea ingresada, 
el programa deberá imprimir un mensaje de éxito y finalizar.

Este ejercicio te ayudará a comprender cómo usar while not para crear un bucle que continúe ejecutándose hasta que se cumpla una condición específica, 
en este caso, hasta que el usuario ingrese la contraseña correcta.
"""

import os 
def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')    
    else:
        os.system('clear')
        
user = input("Ingrese su Usuario ")
password = "Tigre"
password_true = input("Ingrese su Contraseña ")


while not password != password_true:
    print("Contraseña Incorrecta")
    password_true = input("Ingrese su Contraseña")  
    break
limpiar_pantalla()       
print(f"Contraseña correcta\nGracias por elegirnos {user}, le deseamos un excelente dia :)")

    

            