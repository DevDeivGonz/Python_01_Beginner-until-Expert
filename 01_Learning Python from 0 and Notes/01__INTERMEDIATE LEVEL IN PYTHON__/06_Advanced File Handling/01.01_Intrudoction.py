
"""

Conceptos Básicos
    1. Archivos en Python
        En Python, trabajar con archivos implica leer y escribir datos en archivos del sistema de archivos. Los archivos pueden ser de texto (como .txt, .csv, .json) o binarios (como imágenes o archivos .exe).

    2. Modos de Apertura de Archivos
        Cuando abres un archivo en Python, debes especificar el modo en el que quieres abrirlo.

    Los modos más comunes son:

        'r' (lectura): Abre el archivo para leer su contenido. Este es el modo predeterminado si no especificas ninguno.
        Si el archivo no existe, se genera un error (FileNotFoundError).
        'w' (escritura): Abre el archivo para escribir. Si el archivo ya existe, se trunca (se borra su contenido).
        Si no existe, se crea un nuevo archivo.
        'a' (adjuntar): Abre el archivo para agregar contenido al final del archivo sin truncar el contenido existente.
        Si el archivo no existe, se crea un nuevo archivo.
        'b' (binario): Abre el archivo en modo binario. Se utiliza junto con otros modos (por ejemplo, 'rb' para leer
        en modo binario).

"""
with open("hola_python.txt", "r") as archivo: #  Abrir el archivo en modo lectura

    contenido = archivo.read() # Leer el contenido del archivo
    print(contenido) # Imprimir el contenido



