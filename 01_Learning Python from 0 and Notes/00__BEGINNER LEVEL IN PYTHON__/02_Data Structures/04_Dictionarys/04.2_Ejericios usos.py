dict_helados = {
    1: "helado chocolate",
    2: "helado vainilla",
    3: "helado fresa",
}

for key, value in dict_helados.items():
    print(f"{key}, {value}")

helados_usuario = {}

requerimiento_usuario = input("Ingrese su helado favorito")
helados_usuario["1."] = requerimiento_usuario
requerimiento_usuario = input("Ingrese su segundo helado favorito")
helados_usuario["2."] = requerimiento_usuario

print(helados_usuario)

helados_bodega = {
    "helado_fresa": { "iD": 182929929, "producto": "Helado fresa", "Precio": 12000},
}

print(helados_bodega)