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


# Muestro cada dato por separado indicandole la posicion dentro de la lista
print("\nDETALLE DE LOS PRODUCTOS")

for producto in productos:
    print("Nombre:", producto[0])
    print("Unidades disponibles:", producto[1])
    print("Precio:", producto[2], "€")
    print()

# append añade un nuevo elemento al final
productos.append(["teclado", 6, 29.95])

print("Lista después de añadir el producto:")
print(productos)



#DICCIONARIO DE LISTAS
catalogo = {
    "moviles": ["Samsung Galaxy", "iPhone", "Xiaomi Redmi"],
    "ordenadores": ["Portatil HP", "Portatil Lenovo"],
    "accesorios": ["Auriculares", "Teclado", "Raton"]
}

# muestro el diccionario completo
print("CATÁLOGO DE LA TIENDA")
print(catalogo)

# recorrer con un for el diccionario con items()
# NO ME SALE

# añado una nueva categoría con sus productos
catalogo["tablets"] = ["iPad", "Samsung Galaxy Tab"]

# añado un producto a una categoría existente
catalogo["accesorios"].append("Cargador")

print("Catálogo actualizado:")
print(catalogo)


#RECORRER UNA CADENA DE CARACTERES
texto = "teclado"

for letra in texto:
    print(letra * 2)

# DICCIONARIO CON VALUES
precios = {
    "movil": 299.99,
    "portatil": 799.50,
    "tablet": 249.90
}

# recorro solamente los precios
for precio in precios.values():
    print(f"Precio: {precio} €")