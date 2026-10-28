# En esta tarea teneis que incluir vuestras prácticas sobre lista de listas 
# y diccionario de listas, con ejemplos vuestros propios y sobre esos ejemplos 
# poneis opciones de imprimir, añadir elementos, recorrer con un for, etc


#  LISTA DE LISTAS
productos = [
    ["movil", 5, 299.99],
    ["portatil", 3, 799.50],
    ["tablet", 8, 249.90],
    ["auriculares", 10, 39.99]
]

# Mostrar todos los productos recorriendolo con un for
print("LISTA DE PRODUCTOS")

for producto in productos:
    print(producto)

print("---------------------------------")

# Muestro cada dato por separado indicandole la posicion dentro de la lista
print("DETALLE DE LOS PRODUCTOS")

for producto in productos:
    print("Nombre:", producto[0])
    print("Unidades disponibles:", producto[1])
    print("Precio:", producto[2], "€")
    print()

print("---------------------------------")

# append añade un nuevo elemento al final
print("AÑADIR UN PRODUCTO NUEVO: ")
productos.append(["teclado", 6, 29.95])

print("Lista después de añadir el producto:")
print(productos)

print("---------------------------------")

#DICCIONARIO DE LISTAS
catalogo = {
    "moviles": ["Samsung Galaxy", "iPhone", "Xiaomi Redmi"],
    "ordenadores": ["Portatil HP", "Portatil Lenovo"],
    "accesorios": ["Auriculares", "Teclado", "Raton"]
}

# muestro el diccionario completo
print("CATÁLOGO DE LA TIENDA")
print(catalogo)

print("---------------------------------")

# recorrer con un for el diccionario con items()
print("MOSTRAR PRODUCTO Y PRECIO CON ITEMS")
productos1 = {"movil": 250, "tablet": 100, "portatil": 500}

for producto, precios in productos1.items():
    print(f"{producto} -> {precios}€")

print("---------------------------------")

print("MOSTRAR PRODUCTO Y PRECIO SIN ITEMS")
productos2 = {"movil": 250, "tablet": 100, "portatil": 500}

for producto in productos2:
    print(f"{producto} -> {productos2[producto]}")

print("---------------------------------")

# añado una nueva categoría con sus productos
print("AÑADO NUEVA CATEGORÍA Y PRODUCTOS")
catalogo["tablets"] = ["iPad", "Samsung Galaxy Tab"]

# añado un producto a una categoría existente
print("AÑADO UN PRODUCTO NUEVO A UNA CATEGORIA EXISTENTE")
catalogo["accesorios"].append("Cargador")

print("---------------------------------")

print("Catálogo actualizado:")
print(catalogo)

print("---------------------------------")

#RECORRER UNA CADENA DE CARACTERES
print("RECORRO UNA CADENA DE CARACTÉRES: ")
texto = "teclado"

for letra in texto:
    print(letra * 2)

print("---------------------------------")

# DICCIONARIO CON VALUES
print("RECORRER EL DICCIONARIO CON VALUES:")
precios = {
    "movil": 299.99,
    "portatil": 799.50,
    "tablet": 249.90
}

# recorro solamente los precios
for precio in precios.values():
    print(f"Precio: {precio} €")