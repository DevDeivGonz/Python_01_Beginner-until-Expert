import random
import string

def generar_usuario(nombre_usuario, id_usuario):
    # Generar nombre completo aleatorio
    nombres = ['Juan', 'María', 'Carlos', 'Laura', 'Ana', 'Pedro', 'Sofía', 'Luis', 'Elena', 'Diego']
    apellidos = ['García', 'Martínez', 'López', 'Hernández', 'González', 'Pérez', 'Rodríguez', 'Sánchez', 'Fernández', 'Ruiz']
    nombre_completo = random.choice(nombres) + ' ' + random.choice(apellidos)
    
    return nombre_usuario, nombre_completo, id_usuario

def imprimir_usuario(usuario):
    nombre_usuario, nombre_completo, id_usuario = usuario
    print("\nUsuario:")
    print("Nombre de usuario:", nombre_usuario)
    print("Nombre completo:", nombre_completo)
    print("ID de usuario:", id_usuario)

# Solicitar al usuario que ingrese su nombre de usuario e ID
nombre_usuario = input("Ingrese su nombre de usuario: ")
id_usuario = input("Ingrese su ID de usuario: ")

# Generar el usuario y mostrarlo
usuario = generar_usuario(nombre_usuario, id_usuario)
imprimir_usuario(usuario)

# Guardar los datos ingresados en un archivo o en variables para su uso posterior
datos_usuario = {
    "nombre_usuario": nombre_usuario,
    "id_usuario": id_usuario
}

# Puedes acceder a los datos del usuario utilizando las variables datos_usuario["nombre_usuario"] y datos_usuario["id_usuario"]
print("\nDatos guardados:")
print("Nombre de usuario:", datos_usuario["nombre_usuario"])
print("ID de usuario:", datos_usuario["id_usuario"])
