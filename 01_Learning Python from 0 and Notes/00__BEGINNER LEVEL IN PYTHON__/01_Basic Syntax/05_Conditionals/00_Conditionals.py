""" CONDITIONALS """

my_condition = False

if my_condition: ## es lo mismo que if my_condition == True
    print("Se ejecuta la condicion del if")
    
print("La ejecucion continua")

my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condicion del segundo if")
    
if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10")
elif my_condition  ==1:
    print("es igual a 1")
    
else:
     print("Es menor que 10 o igual que 20")
        
    
print("La ejecucion continua")