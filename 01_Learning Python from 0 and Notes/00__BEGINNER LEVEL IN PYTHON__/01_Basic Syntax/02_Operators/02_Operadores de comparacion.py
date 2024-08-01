"""
OPERADORES DE COMPARACION 



""" 

# Operadores comparativos

print(3 > 4)
print(3 <  4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

print("Hola " > "Python")
print("Hola "<  "Python")
print(len("aaa ") >= len("abaaa")) # Ordenazion alfabetica
print("Hola " <= "Python")
print("Hola " == "Hola")  
print("Hola " != "Python")

# Operadores Logicos

print(3 > 4  and "Hola" > "Python")
print(3 > 4  or "Hola" > "Python")
print(3 < 4  and "Hola" < "Python")
print(3 < 4  or "Hola" < "Python")
print(3 < 4  or ("Hola" > "Python" and 4 == 4))
print (not (3 > 4 ))

#print(3 > 4  not "Hola" > "Python")

# Tabla de verdad para el operador AND
print("Tabla de verdad para AND:")
print("True and True  =", True and True)
print("True and False =", True and False)
print("False and True =", False and True)
print("False and False=", False and False)
print()

# Tabla de verdad para el operador OR
print("Tabla de verdad para OR:")
print("True or True  =", True or True)
print("True or False =", True or False)
print("False or True =", False or True)
print("False or False=", False or False)
print()

# Tabla de verdad para el operador NOT
print("Tabla de verdad para NOT:")
print("not True  =", not True)
print("not False =", not False)

# Tabla de verdad para el operador de igualdad (==)
print("Tabla de verdad para ==")
print("True == True   =", True == True)
print("True == False  =", True == False)
print("False == True  =", False == True)
print("False == False =", False == False)
print()

# Tabla de verdad para el operador de desigualdad (!=)
print("Tabla de verdad para !=")
print("True != True   =", True != True)
print("True != False  =", True != False)
print("False != True  =", False != True)
print("False != False =", False != False)
print()

# Tabla de verdad para combinaciones de operadores lógicos
print("Tabla de verdad para combinaciones de operadores lógicos:")
print("True and (True or False) =", True and (True or False))
print("False or (True and True) =", False or (True and True))
print("(True and False) or (False and True) =", (True and False) or (False and True))
print("not (True and False) =", not (True and False))

# Tabla de verdad para el operador de mayor que (>)
print("Tabla de verdad para >")
print("3 > 2  =", 3 > 2)
print("2 > 3  =", 2 > 3)
print("2 > 2  =", 2 > 2)
print()

# Tabla de verdad para el operador de menor que (<)
print("Tabla de verdad para <")
print("3 < 2  =", 3 < 2)
print("2 < 3  =", 2 < 3)
print("2 < 2  =", 2 < 2)
print()

# Tabla de verdad para el operador de mayor o igual que (>=)
print("Tabla de verdad para >=")
print("3 >= 2  =", 3 >= 2)
print("2 >= 3  =", 2 >= 3)
print("2 >= 2  =", 2 >= 2)
print()

# Tabla de verdad para el operador de menor o igual que (<=)
print("Tabla de verdad para <=")
print("3 <= 2  =", 3 <= 2)
print("2 <= 3  =", 2 <= 3)
print("2 <= 2  =", 2 <= 2)
print()

# Tabla de verdad para el operador de pertenencia (in)
lista = [1, 2, 3, 4, 5]
print("Tabla de verdad para 'in'")
print("1 in lista  =", 1 in lista)
print("6 in lista  =", 6 in lista)
print()

# Tabla de verdad para el operador de no pertenencia (not in)
print("Tabla de verdad para 'not in'")
print("1 not in lista  =", 1 not in lista)
print("6 not in lista  =", 6 not in lista)
print()

# Tabla de verdad para el operador de identidad (is)
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("Tabla de verdad para 'is'")
print("x is y  =", x is y)
print("x is z  =", x is z)
print()

# Tabla de verdad para el operador de no identidad (is not)
print("Tabla de verdad para 'is not'")
print("x is not y  =", x is not y)
print("x is not z  =", x is not z)
print()