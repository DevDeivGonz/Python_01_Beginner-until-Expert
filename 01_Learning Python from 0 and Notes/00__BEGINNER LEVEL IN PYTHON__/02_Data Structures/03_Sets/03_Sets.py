"""   SETS   """

""" LOS SETS GUARDAN ELEMENTOS QUE NI ESTAN REPETIDOS   """
# esuna estructura que almacena datos desordenados y que no almacena datos repetidos

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #inicialmente es un diccionario

my_other_set = {"Deiv", "Gonz", 21} 
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Deiv")
print(my_other_set) # un set no es una estructura ordenada

my_other_set.add("Gonz") # la forma de gaurdar elementos es dezorrdenada
print(my_other_set) # un set no admite repetidos

print("Deiv" in my_other_set)
print("Deivi" in my_other_set)

my_other_set.remove("Deiv")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set 
# print(my_other_set) Name Error

my_set = {"Deiv", "Gonz", 21} 
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Python", "C#", "Rust"}
my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript"}))

print(my_new_set.difference(my_set))






