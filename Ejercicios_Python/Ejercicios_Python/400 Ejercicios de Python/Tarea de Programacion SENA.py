# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:20:01 2024

@author: Laptop
"""

""" 
1. Elaborar un programa que muestre  los números pares comprendidos entre 10 y 20 inclusive.
"""

for i in range(9,21):
    if i % 2 == 0:
        print(i)
        

""" 
2. Elaborar un programa que muestre  los números impares comprendidos entre 20 y 10 inclusive
(orden descendente)."""

contador_impares = 0

for i in range(1, 20):
    if i % 2 != 0:  # Verifica si el número es impar
        contador_impares += 1
    

print("La cantidad de números impares en el rango de 1 a 20 es:", contador_impares)

""" 
3. Elaborar un programa que calcule la suma de los números múltiplos de 3 a partir del número 9 y finaliza en el número 45.

4. Elaborar un programa que sume y muestre por pantalla todos los números naturales del 1 hasta el 5, ambos incluidos. Lo mismo pero de 1 a 50; lo mismo pero de 1 a 500.

5. Elaborar un programa que sume el número 5 y sus múltiplos hasta el 100 inclusive y muestre el  resultado por pantalla.

6. Elaborar un programa que calcule el promedio de edades de hombres, mujeres y de todo un grupo de n alumnos.

7. Elaborar un programa que lea 50 calificaciones de un grupo de alumnos. Calcule y escriba el porcentaje de reprobados. Tomando en cuenta que la calificación mínima aprobatoria es de 70.

8. Elaborar un programa que permita a un profesor de una materia conocer la cantidad de sus alumnos que no tienen derecho al examen de nivelación.

9. Elaborar un programa que lea las calificaciones obtenidas en las 5 unidades por cada uno de los 40 alumnos y escriba la cantidad de ellos que no tienen derecho al examen de nivelación.

10. Elaborar un programa que lea por cada alumno de DISEÑO su número de control y su calificación en cada una de las 5 unidades de la materia. Al final que escriba el número de control del alumno que obtuvo mayor promedio. Suponga que los alumnos tienen diferentes promedios."""