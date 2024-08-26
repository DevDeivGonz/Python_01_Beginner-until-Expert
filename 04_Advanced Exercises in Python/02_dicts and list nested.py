objetos = {
    'alimentos': [
        {'producto': 'manzana', 'precio': 2300},
        {'producto': 'banano', 'precio': 4500},
    ],
    'electrodomesticos': [
        {'producto': 'Portatil HP 2020', 'precio': 2890000},
        {'producto': 'Lavadora', 'precio': 3490000},
        {'producto': 'TV samsung', 'precio': 2000000},
    ]
}

for categoria, productos in objetos.items():
    print(f"Aquí está el inventario de {categoria}:")
    for producto in productos:
        print(f"Producto: {producto['producto']}, Precio: {producto['precio']}")
    print()  # Línea en blanco para separar categorías


porque_si = 1
while porque_si < 20:
    print(porque_si, end=', ')  # Usa un espacio como separador
    porque_si += 1