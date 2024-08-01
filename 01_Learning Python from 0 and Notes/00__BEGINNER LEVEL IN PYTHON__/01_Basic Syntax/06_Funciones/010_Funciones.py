""" FUNCIONES """

""" FUNCIONES ARREGLAN PROBLEMAS Y NOS AYUDA A EVITAR ERRORES"""

def my_function ():
    print("Esto es una funcion")
    
my_function() 
my_function() 
my_function() 

def multh_numbers (first_number, second_number, third_number):
    print(first_number * second_number * third_number)

multh_numbers(5, 5, 5) # muestra el resultado de la operacion 
multh_numbers(0.34,-34, 4345) # pueden ponerse numeros enteros, reales y decimales

def sum_two_values (first_number, second_number):
    print("Aqui va la suma incorpotada", first_number + second_number)
    
sum_two_values(53434343434, 734334343343)
sum_two_values(222, 222)



def sum_two_values_with_return (first_number, second_number):
    my_sum = first_number + second_number
    return my_sum

my_result = sum_two_values (15, 5)
my_result = sum_two_values_with_return (10, 5)
print(sum_two_values_with_return(10, 5))


def print_name(name, surname):
    print(f"{name} {surname}")
    
print_name(surname = "Gonzalez", name = "Deivid")

def print_name_with_default(name, apellido, alias = "sin alias"):
    print(f"{name} {apellido} {alias}")

print_name_with_default("Deivid", "Gonzalez", "GonzoDev")

def print_text(*texts):
    for text in texts:
       print(text.upper())
    
print_text("Hola", "Python", "GonzoDev")
print_text("Hola")

    
    
    
    
    