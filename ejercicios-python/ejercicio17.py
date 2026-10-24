# Tienes una lista de datos de ventas donde cada registro es una tupla con el formato: 
# ("producto", cantidad, precio_unitario). 
# Los datos los metes directamente en el programa, pongamos 5 tuplas o lineas de la compra, 
# ejemplo de tupla: manzanas, cantidad 3 kilos y precio 2,7 eur. 
# El programa debe hacer lo siguiente: 
# Convierta el nombre del producto a mayúsculas.
# Calcule el total gastado en cada producto (cantidad * precio) y 
# redondee el resultado final a 2 decimales usando la función round().
# Muestre por pantalla el total de esa compra y el total de la suma de todas las cantidades.


# Lista de datos de ventas
ventas = [ # producto, cantidad y precio unitario
    ("manzanas", 3, 2.7),
    ("peras", 2, 1.8),
    ("platanos", 5, 1.5),
    ("naranjas", 4, 2.2),
    ("uvas", 1, 3.5)
]

total_compra = 0
total_cantidades = 0

# recorro la lista 
for venta in ventas:
    producto = venta[0].upper() #obtiene la posicion 0, osea el producto y lo pone mayuscula
    cantidad = venta[1] #obtiene la posicion 1, osea la cantidad
    precio_unitario = venta[2] #obtiene la posicion 2, osea el precio unitario

    total_producto = round(cantidad * precio_unitario, 2) #gasto de ese producto
    total_compra = total_compra + total_producto #cojo lo q llevo acumulado y le sumo el precio del producto
    total_cantidades = total_cantidades + cantidad # igual pero sumando las cantidades de frutas

    print("Producto:", producto)
    print("Cantidad:", cantidad)
    print("Precio unitario:", precio_unitario, "€")
    print("Total del producto:", total_producto, "€")
    print() #dejo una linea en blanco para que no este pegado

print("Total de la compra: ", round(total_compra, 2), "€")
print("Total de la suma de todas las cantidades: ", total_cantidades)

