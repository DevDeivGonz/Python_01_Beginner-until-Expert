"""""    DICCIONARIOS    """""

""""" LOS DICCIONARIOS GUARDAN ELEMENTOS CLAVE VALOR  """""


my_dict = dict ()
my_other_dict = {}
print(type(my_dict))

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Deivid",  "Apellido": "Gonzalez","Edad": 21, 1:"Python"}

my_dict = {
            "Nombre": "Deivid",
            "Apellido": "Gonzalez",
            "Edad": 21,
            "Lenguaje": {"Python", "Swift", "Kotlin"}, 
            1:1.71
        }


print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

my_dict["Nombre"] = "Pedro" 
print(my_dict["Nombre"])

my_dict[1]

my_dict["Calle"] = "Calle Deivid" 

print(my_dict)

del my_dict["Calle"] # eliminar datos de un diccionario
print(my_dict)

print("Nombre" in my_dict)
print("Apellido" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]
my_new_dict = dict.fromkeys((my_list))
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso")) # asi se crea o se hace un dicconario nuevo pero no es comun usar este metodo
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, ("Deivid", "Gonzalez"))
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(my_new_dict.values()))
print(tuple(my_new_dict))
print(set(my_new_dict))


