"""
ALGORITMO TRIANGULO

Realizar un el código de programación (con cualquier lenguaje de programación) que permita caracterizar un triangulo de acuerdo a sus lados y ángulos (EL USUARIO SOLAMENTE COLOCA LOS LADOS), haciendo uso de los operadores lógicos "y" y "o".

1. Portada
2. Código
3. Pantallazos de su funcionamiento

Equilátero  | Si los tres lados son iguales.

Isósceles   | dos lados son iguales.

Escaleno    | Si todos los lados son diferentes.
    
"""
import math
def limpiar_pantalla():
    print("\n" * 30)   


                                                                                  
print(""" 
      
    BUEN DIA PARA TODOS                                     
                                                                                     
                                                                                    
    MI NOMBRE ES BRANDON DAVID GONZALEZ LOPEZ                          
                                                                                   
                                                                                    
    PERTENECIENTE A LA FICHA 2823506-G1                             
                                                                                    
                                                                                   
    ESTA ES LA PRESENTACION DEL TALLER 5°                            
                                                                                    
                                                                                   
    El siguiente programa indicará si el triángulo es equilátero, isósceles o escaleno.                                                                               
     """)

input("INSERTE ENTER PARA CONTINUAR: ")
limpiar_pantalla()

while True:


    lado1 = float(input("Ingrese la longitued del primer lado  "))
    lado2 = float(input("Ingrese la loguntud del segudo lado  "))
    lado3 = float(input("Ingrese la longitud del tercer lado  "))
    
    if not ((lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)):
        print("Los lados ingresados no forman un triángulo.")
    else:
        # Clasificación por tipo de triángulo según lados
        if lado1 == lado2 and lado2 == lado3: 
            # Debe ser Equilátero si tres lados son iguales.
            print("Es un triángulo Equilátero")
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3: 
            # Debe ser Isósceles si dos lados son iguales.
            print("Es un triángulo Isósceles")
        else:
            # Debe ser Escaleno si todos los lados son diferentes.
            print("Es un triángulo Escaleno")
    
    
        cos_alpha = (lado2**2 + lado3**2 - lado1**2) / (2 * lado2 * lado3)
        cos_beta = (lado1**2 + lado3**2 - lado2**2) / (2 * lado1 * lado3)
        cos_gamma = (lado1**2 + lado2**2 - lado3**2) / (2 * lado1 * lado2)

        # Conversión de ángulos a grados
        alpha = math.degrees(math.acos(cos_alpha))
        beta = math.degrees(math.acos(cos_beta))
        gamma = math.degrees(math.acos(cos_gamma))

        # Clasificación por tipo de triángulo según ángulos
        if alpha == 90 or beta == 90 or gamma == 90:
            tipo_angulo = "Rectángulo"
        elif alpha > 90 or beta > 90 or gamma > 90:
            tipo_angulo = "Obtusángulo"
        else:
            tipo_angulo = "Acutángulo"

        # Salida de resultados
        print(f"El triángulo es de agulo {tipo_angulo}.")
    
    
    
        print("____________________________________________________")
    respuesta = input("¿Desea continuar? (SI/NO): ").upper() 
    # upper() Convertir la respuesta a mayúsculas

    if respuesta == "NO":
        limpiar_pantalla()
        print("____________________________________________________")
        print("Aquí esta el codigo corregido profesora, buena tarde.")
        print("____________________________________________________")
        break
    
    limpiar_pantalla()


    

    
    
    
    
    