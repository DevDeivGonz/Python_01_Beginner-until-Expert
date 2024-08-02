# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 14:36:11 2024

@author: Laptop
"""
import math

def calcular_angulos_y_area(a, b, c):
    # Calcular los ángulos usando el teorema del coseno
    alpha = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    beta = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    gamma = 180 - alpha - beta
    
    # Calcular el semiperímetro
    s = (a + b + c) / 2
    
    # Calcular el área usando la fórmula de Herón
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return alpha, beta, gamma, area


##########################################################################################################################################################################


def Triángulo():
    # Pedir al usuario que ingrese las longitudes de los lados del triángulo
    a = float(input("Ingrese la longitud del lado a: "))
    b = float(input("Ingrese la longitud del lado b: "))
    c = float(input("Ingrese la longitud del lado c: "))
    
    # Calcular los ángulos y el área del triángulo
    alpha, beta, gamma, area = calcular_angulos_y_area(a, b, c)
    
    # Imprimir los resultados
    print(f"Ángulo alpha: {alpha} grados")
    print(f"Ángulo beta: {beta} grados")
    print(f"Ángulo gamma: {gamma} grados")
    print(f"Área del triángulo: {area} unidades cuadradas")
    
    continuar = input("""
          
          ¿DESEA CONTINUAR?, 
          
          [SI] PARA CONTINUAR
          [NO] PARA VOLVER AL MENÚ PRINCIPAL: """).lower()
          
    while True:
        if continuar == "si":
            Triángulo()
        elif continuar == "no":
            menu_principal()
            break
        else:
            print("ERROR. Elija una opción válida")

# Las demás funciones de las figuras geométricas pueden permanecer sin cambios

# El resto del código sigue igual




def Rectángulo():
    pass

def Cuadrado():
    pass

def Rombo():
    pass

def Círculo():
    pass

def Elipse():
    pass

def Trapecio():
    pass

def Paralelogramo():
    pass

def Pentágono():
    pass

def Hexágono():
    pass

def Heptágono():
    pass

def Octógono():
    pass

def Nonágono():
    pass

def Decágono():
    pass

def Dodecágono():
    pass

def Polígono():
    pass

def Estrella():
    pass

def Corazón():
    pass

def Espiral():
    pass


def menu_principal():
    
        print("""
        Menu de figuras Geometricas.
        
        [1] Triángulo
        [2] Rectángulo
        [3] Cuadrado
        [4] Rombo
        [5] Círculo
        [6] Elipse
        [7] Trapecio
        [8] Paralelogramo
        [9] Pentágono
        [10] Hexágono
        [11] Heptágono
        [12] Octógono
        [13] Nonágono
        [14] Decágono
        [15] Dodecágono
        [16] Polígono
        [17] Estrella
        [18] Corazón
        [19] Espiral
        _________________________________________
        
        [20] Salir
        _________________________________________
        """)
        while True:
            
            opcion = int(input("Elija una opción: "))
            
            if opcion == 1:
                Triángulo()
            elif opcion == 2:
                Rectángulo()
            elif opcion == 3:
                Cuadrado()
            elif opcion == 4:
                Rombo()
            elif opcion == 5:
                Círculo()
            elif opcion == 6:
                Elipse()
            elif opcion == 7:
                Trapecio()
            elif opcion == 8:
                Paralelogramo()
            elif opcion == 9:
                Pentágono()
            elif opcion == 10:
                Hexágono()
            elif opcion == 11:
                Heptágono()
            elif opcion == 12:
                Octógono()
            elif opcion == 13:
                Nonágono()
            elif opcion == 14:
                Decágono()
            elif opcion == 15:
                Dodecágono()
            elif opcion == 16:
                Polígono()
            elif opcion == 17:
                Estrella()
            elif opcion == 18:
                Corazón()
            elif opcion == 19:
                Espiral()
            elif opcion == 20:
                print("GRACIAS POR ELEGIRNOS, QUE TENGA UN EXCELENTE DIA!....")
                break
            else:
                print("ERROR. Inserte una opción válida.")

if __name__ == "__main__":
    menu_principal()
    
    
    
    
    