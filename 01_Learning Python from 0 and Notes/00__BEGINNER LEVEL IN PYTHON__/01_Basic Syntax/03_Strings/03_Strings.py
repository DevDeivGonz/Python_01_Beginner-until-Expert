## STRINGS ""

my_string = " Mi string"
my_other_string = " Mi otro string"

print (len(my_string))
print (len(my_other_string))

print (my_string + "" + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "Este es un string\ncon tabulacion"
print(my_tab_string)

my_scape_string = "\\Este es un string\\n escaolado" # lo manda a la otra linea
print(my_scape_string) 

# estas dos maneras es mas rapido y facil de hacer esta forma de hacer strings

name, surname, age = "Brais", "Moure", 35
# para hacer strings con format
print ("Mi nimbre es {} {} y mi edad es {}".format(name, surname, age))
# para hacer string sin ,format 
print ("Mi nimbre es %s %s y mi edad es %s"%(name, surname, age))

#formatear cadenas de texto y crear strins mas efectivos y rapidos para entender
print (f"Mi nimbre es {name} {surname} y mi edad es {age}")

#desempaquetado de caracteres
language = "Python"
a, b, c, d, e ,f = language
print (a)   
print (e)

# division en

language_slice = language [1:3]
print(language_slice)

language_slice = language [1]
print(language_slice)

reversed_language = language [:: -1]
print(reversed_language)

#Funciones

print(language.capitalize())
print(language.upper())
print(language.lower())
print ("1".isnumeric())
print(language.title())
print(language.startswith("Py"))

# Tabla de los strings mas usados 


    
"""" 
    
Aquí tienes una tabla con los métodos de strings en Python, incluyendo una descripción breve y un ejemplo para cada uno 


| Método             

| `capitalize()`     | Convierte el primer carácter a mayúscula.                                   
| `"python".capitalize() -> "Python"`                  |

| `upper()`          | Convierte todos los caracteres a mayúsculas.                                
| `"python".upper() -> "PYTHON"`                       |

| `lower()`          | Convierte todos los caracteres a minúsculas.                                
| `"PYTHON".lower() -> "python"`                       |
| `title()`          | Convierte el primer carácter de cada palabra a mayúscula.                   
| `"python is fun".title() -> "Python Is Fun"`         |

| `swapcase()`       | Convierte mayúsculas a minúsculas y viceversa.                              
| `"PyThOn".swapcase() -> "pYtHoN"`                    |

| `replace(old, new)`| Reemplaza todas las ocurrencias de un substring por otro.                  
| `"Hello world".replace("world", "Python") -> "Hello Python"` |

| `isnumeric()`      | Verifica si todos los caracteres son numéricos.                             
| `"123".isnumeric() -> True`                          |

| `isdigit()`        | Verifica si todos los caracteres son dígitos.                               
| `"123".isdigit() -> True`                            |

| `isalpha()`        | Verifica si todos los caracteres son letras.                               
| `"Python".isalpha() -> True`                         |

| `isalnum()`        | Verifica si todos los caracteres son alfanuméricos.                         
| `"Python123".isalnum() -> True`                      |

| `isupper()`        | Verifica si todos los caracteres están en mayúsculas.                       
| `"PYTHON".isupper() -> True`                         |

| `islower()`        | Verifica si todos los caracteres están en minúsculas.                       
| `"python".islower() -> True`                         |

| `istitle()`        | Verifica si la string sigue el formato de título.                          
| `"Python Is Fun".istitle() -> True`                  |

| `startswith(prefix)`| Verifica si la string comienza con el prefijo especificado.                 
| `"python".startswith("py") -> True`                  |

| `endswith(suffix)` | Verifica si la string termina con el sufijo especificado.                   
| `"python".endswith("on") -> True`                    |

| `center(width[, fillchar])`| Centra la string en un campo de ancho especificado.                
| `"python".center(10, '-') -> "--python--"`           |

| `ljust(width[, fillchar])`| Justifica la string a la izquierda en un campo de ancho especificado.
| `"python".ljust(10, '-') -> "python----"`            |

| `rjust(width[, fillchar])`| Justifica la string a la derecha en un campo de ancho especificado.  
| `"python".rjust(10, '-') -> "----python"`            |

| `strip([chars])`   | Elimina los caracteres especificados (o espacios) del inicio y el final.   
| `"  python  ".strip() -> "python"`                   |

| `lstrip([chars])`  | Elimina los caracteres especificados (o espacios) del inicio.              
| `"  python  ".lstrip() -> "python  "`                |

| `rstrip([chars])`  | Elimina los caracteres especificados (o espacios) del final.               
| `"  python  ".rstrip() -> "  python"`                |

| `split([sep[, maxsplit]])`| Divide la string en una lista, usando el separador especificado.     |
`"a,b,c".split(",") -> ['a', 'b', 'c']`              |

| `rsplit([sep[, maxsplit]])`| Divide la string en una lista, usando el separador especificado, empezando desde el final.| 
`"a,b,c".rsplit(",", 1) -> ['a,b', 'c']`             |

| `splitlines([keepends])`| Divide la string en una lista usando los saltos de línea como separadores.|
`"a\nb\nc".splitlines() -> ['a', 'b', 'c']`           |

| `join(iterable)`   | Une una lista de strings en una sola string, usando la string actual como separador.| 
`",".join(['a', 'b', 'c']) -> "a,b,c"`                |

| `find(sub[, start[, end]])`| Devuelve el índice más bajo donde se encuentra el substring.      
| `"python".find("th") -> 2`                           |


| `rfind(sub[, start[, end]])`| Devuelve el índice más alto donde se encuentra el substring.     
| `"python".rfind("o") -> 4`                           |

| `index(sub[, start[, end]])`| Igual que `find`, pero lanza una excepción si no se encuentra.   
| `"python".index("th") -> 2`                          |

| `rindex(sub[, start[, end]])`| Igual que `rfind`, pero lanza una excepción si no se encuentra. 
| `"python".rindex("o") -> 4`                          |

| `count(sub[, start[, end]])`| Devuelve el número de ocurrencias del substring.                 
| `"python".count("o") -> 1`                           |

| `partition(sep)`   | Divide la string en una tupla de tres elementos: antes del separador, el separador, y después del separador.
| `"python".partition("th") -> ('py', 'th', 'on')` |

| `rpartition(sep)`  | Divide la string en una tupla de tres elementos desde el final: antes del separador, el separador, y después del separador.
| `"python".rpartition("o") -> ('pyth', 'o', 'n')` |

| `format(*args, **kwargs)`| Formatea la string usando los argumentos y palabras clave.          
| `"Hello, {}!".format("world") -> "Hello, world!"`    |

| `format_map(mapping)`| Similar a `format`, pero usa un mapeo en lugar de palabras clave.       
| `"{name}".format_map({'name': 'world'}) -> "world"`  |

| `zfill(width)`     | Rellena la string con ceros a la izquierda hasta alcanzar el ancho especificado.
| `"42".zfill(5) -> "00042"`                        |

| `expandtabs(tabsize)`| Expande los tabuladores en la string a espacios.                        
| `"a\tb".expandtabs(4) -> "a   b"`                    |  

"""