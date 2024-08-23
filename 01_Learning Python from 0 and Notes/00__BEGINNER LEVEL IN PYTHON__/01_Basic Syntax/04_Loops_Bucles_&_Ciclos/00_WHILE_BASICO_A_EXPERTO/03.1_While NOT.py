""" 
Escribe un programa que solicite al usuario ingresar una contraseña. 
El programa deberá seguir solicitando la contraseña hasta que el usuario ingrese la contraseña correcta. Una vez que la contraseña correcta sea ingresada, 
el programa deberá imprimir un mensaje de éxito y finalizar.

Este ejercicio te ayudará a comprender cómo usar while not para crear un bucle que continúe ejecutándose hasta que se cumpla una condición específica, 
en este caso, hasta que el usuario ingrese la contraseña correcta.
"""

password = "Tigre"
intentos = 2

##############################################################

user = input("Ingrese su Usuario ")
password_true = input("Ingrese su Contraseña ")


while password != password_true:
        intentos -= 1
        if intentos == 0:
            print("Has agotado tus intentos.")
            break
        print("Contraseña Incorrecta, intenta de nuevo.")
        password_true = input("Ingrese su Contraseña ")


while password_true == password:
    print(f"Contraseña correcta\nGracias por elegirnos {user}, le deseamos un excelente dia :)")
    break
    

            