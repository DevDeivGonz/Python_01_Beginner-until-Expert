"""
OPERADORES LOGICOS 

Los operadores lógicos son operadores que se utilizan para combinar declaraciones condicionales y 
realizar evaluaciones lógicas en un programa. Estos operadores permiten tomar decisiones basadas en múltiples condiciones.


"""

# AND 
# Este operador devuelve True si ambas condiciones son verdaderas. Si alguna de las condiciones es falsa, devuelve False.

True and True   # Output: True
True and False  # Output: False

# OR  
# Este operador devuelve True si al menos una de las condiciones es verdadera. Solo devuelve False si ambas condiciones son falsas.

True or True    # Output: True
True or False   # Output: True

# NOT Este operador invierte el valor de la condición. Si la condición es verdadera, not devuelve False, y si la condición es falsa, not devuelve True.

not True   # Output: False
not False  # Output: True


# Definimos algunas variables para usar en los ejemplos
age = 20
is_student = True
has_discount_coupon = False
salary = 3500
credit_score = 700

# Operadores de comparación y lógicos básicos
# Ejemplo 1: Verificar si una persona puede recibir un descuento
if age < 18 or age > 65 or (is_student and not has_discount_coupon):
    print("You get a discount!")  # Output: You get a discount!
else:
    print("No discount available.")

# Ejemplo 2: Verificar si una persona puede solicitar una tarjeta de crédito
# La persona debe tener al menos 18 años, un salario mayor a 3000 y un puntaje de crédito mayor a 600
if age >= 18 and salary > 3000 and credit_score > 600:
    print("You are eligible to apply for a credit card.")  # Output: You are eligible to apply for a credit card.
else:
    print("You are not eligible to apply for a credit card.")

# Ejemplo 3: Verificar si una persona puede acceder a un beneficio
# La persona debe ser mayor de edad y (ser estudiante o tener un cupón de descuento)
if age >= 18 and (is_student or has_discount_coupon):
    print("You can access the benefit.")  # Output: You can access the benefit.
else:
    print("You cannot access the benefit.")

# Ejemplo 4: Verificar si una persona puede recibir un préstamo
# La persona debe tener un salario mayor a 4000, o un puntaje de crédito mayor a 700, pero no debe ser estudiante
if (salary > 4000 or credit_score > 700) and not is_student:
    print("You can receive a loan.")  # Output: You can receive a loan.
else:
    print("You cannot receive a loan.")

# Ejemplo 5: Verificar si una persona puede participar en una promoción
# La persona debe tener un puntaje de crédito mayor a 600 y no debe tener un cupón de descuento
if credit_score > 600 and not has_discount_coupon:
    print("You can participate in the promotion.")  # Output: You can participate in the promotion.
else:
    print("You cannot participate in the promotion.")

# Ejemplo avanzado: combinación de múltiples condiciones
# Verificar si una persona puede obtener una hipoteca
# La persona debe tener un salario mayor a 3000, un puntaje de crédito mayor a 650, ser mayor de 21 años, y no ser estudiante
if salary > 3000 and credit_score > 650 and age > 21 and not is_student:
    print("You are eligible for a mortgage.")  # No output because age > 21 condition fails
else:
    print("You are not eligible for a mortgage.")




""" ¿Cómo no se deben usar los operadores lógicos?
No confundir operadores lógicos con operadores de comparación:

Los operadores lógicos (and, or, not) deben ser utilizados para combinar condiciones, no para realizar comparaciones directas entre valores. Por ejemplo, usar and en lugar de & para operaciones bit a bit:
"""

# Incorrecto
result = 5 and 3  # Esto no hace lo que probablemente esperas
# Correcto
result = 5 & 3  # Esto realiza una operación bit a bit AND
# No usar operadores lógicos con valores no booleanos de manera ambigua:

# Aunque en Python se pueden usar valores no booleanos con operadores lógicos (ya que Python considera algunos valores como False y otros como True), esto puede llevar a código confuso e inesperado.

# Evitar ambigüedades
value = 0 or 10  # Output: 10 (0 es considerado False)
# Mejor ser explícito
is_valid = (value != 0) or (value > 5)  # Output: True
# No encadenar demasiadas condiciones sin usar paréntesis:

# Cuando se combinan muchas condiciones, es mejor usar paréntesis para asegurarse de que la lógica sea clara y correcta.

# Incorrecto y difícil de leer
if a == 1 and b == 2 or c == 3 and d == 4:
    ...
# Correcto y claro
if (a == 1 and b == 2) or (c == 3 and d == 4):
    ...
    