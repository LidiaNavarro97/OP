# Sistema de Gestión y resumen de ventas de vehículos.

# Se trata de desarrollorar una aplicación para gestionar el registro de ventas de un
# concesionario de coches desde el año 2024 hasta la actualidad. Tendremos unos datos
# iniciales de ventas para tener volumen y permitiremos que el usuario introduzca nuevos
# registros de ventas (con los datos: Marca, Modelo, AñoVenta, AñoFabricacion y precio) y
# pueda visualizar 3 tipos de resúmenes de ventas.

# MARCAS Y MODELOS
MARCAS_MODELOS = { 
"SEAT": ["Ibiza", "Leon", "Ateca", "Arona"],
"Toyota": ["Corolla", "Yaris", "RAV4", "C-HR"] 
}

#VENTAS
# seria [Marca, Modelo, año_venta, año_fabricacion, precio]
ventas = [
["SEAT", "Ibiza", 2024, 2023, 18000], ["SEAT", "Ibiza", 2024, 2024, 18500], ["SEAT", "Ibiza", 2024, 2024, 19000],
["SEAT", "Ibiza", 2025, 2024, 19500], ["SEAT", "Ibiza", 2025, 2025, 20000], ["SEAT", "Ibiza", 2025, 2025, 20200],
["SEAT", "Ibiza", 2026, 2025, 20500], ["SEAT", "Ibiza", 2026, 2026, 21000], ["SEAT", "Ibiza", 2026, 2026, 21500],
["SEAT", "Leon", 2024, 2024, 24000], ["SEAT", "Leon", 2024, 2024, 24500], ["SEAT", "Leon", 2024, 2023, 23800],
["SEAT", "Leon", 2025, 2025, 25500], ["SEAT", "Leon", 2025, 2025, 26000], ["SEAT", "Leon", 2025, 2024, 25200],
["SEAT", "Leon", 2026, 2026, 27000], ["SEAT", "Leon", 2026, 2026, 27500], ["SEAT", "Leon", 2026, 2025, 26800],
["SEAT", "Ateca", 2024, 2024, 28000], ["SEAT", "Ateca", 2025, 2025, 29500], ["SEAT", "Ateca", 2026, 2026, 31000],
["SEAT", "Arona", 2024, 2024, 21000], ["SEAT", "Arona", 2025, 2025, 22000], ["SEAT", "Arona", 2026, 2026, 23000],
["Toyota", "Corolla", 2024, 2024, 26000], ["Toyota", "Corolla", 2024, 2024, 26500], ["Toyota", "Corolla", 2024, 2023, 25800],
["Toyota", "Corolla", 2025, 2025, 27500], ["Toyota", "Corolla", 2025, 2025, 28000], ["Toyota", "Corolla", 2025, 2024, 27200],
["Toyota", "Corolla", 2026, 2026, 29000], ["Toyota", "Corolla", 2026, 2026, 29500], ["Toyota", "Corolla", 2026, 2025, 28800],
["Toyota", "Yaris", 2024, 2024, 20000], ["Toyota", "Yaris", 2025, 2025, 21000], ["Toyota", "Yaris", 2026, 2026, 22000],
["Toyota", "RAV4", 2024, 2024, 38000], ["Toyota", "RAV4", 2025, 2025, 39500], ["Toyota", "RAV4", 2026, 2026, 41000],
["Toyota", "C-HR", 2024, 2024, 31000], ["Toyota", "C-HR", 2025, 2025, 32500], ["Toyota", "C-HR", 2026, 2026, 34000]
]

# 1) Dar de alta nueva venta:

def altaVenta():

# a) Seleccion de marca   
# pedir al usuario que escriba el nombre de la marca
    print("\n Marcas y modelos disponibles: ")

# aqui los muestro
    for marca in MARCAS_MODELOS:
        print(marca) 

# aqui lo pido 
    marca = input("Introduce la marca: ").capitalize()

# b) Seleccion de modelo
# mostrar los modelos 
    print("\n Modelos disponibles: ")
    print(MARCAS_MODELOS[marca])

    modelo = input("Introduce el modelo: ").capitalize()

# c) Normalizacion y validacion de nombres

# Validacion de marca:
while marca not in MARCAS_MODELOS:
    print("Error: No exite esa marca. ")

    for m in MARCAS_MODELOS:
        print(m)

    marca = input("Escribe una marca valida: ").capitalize()

# Validacion del modelo:
while modelo not in MARCAS_MODELOS[marca]:
    print("Error: No existe ese modelo en esa marca. ") 

    modelo = input("Escribe un modelo valido: ").capitalize()

# d) Validacion de datos numericos (try/except)

# Año de venta
while True:
    try:
        anio_venta = int(input("Introduce el año de venta (2024-2026): "))

        if anio_venta >= 2024 and anio_venta <= 2026:
            break
        else:
            print("Error: el año de venta debe estar entre 2024 y 2026.")

    except ValueError:
        print("Error: debes introducir un número entero.")


# Año de fabricación
while True:
    try:
        anio_fabricacion = int(input("Introduce el año de fabricación (1990-" + str(anio_venta) + "): "))

        if anio_fabricacion >= 1990 and anio_fabricacion <= anio_venta:
            break
        else:
            print("Error: el año de fabricación debe estar entre 1990 y el año de venta.")

    except ValueError:
        print("Error: debes introducir un número entero.")


# Precio
while True:
    try:
        precio = int(input("Introduce el precio del vehículo (1000-100000 €): "))

        if precio >= 1000 and precio <= 100000:
            break
        else:
            print("Error: el precio debe estar entre 1.000 y 100.000 €.")

    except ValueError:
        print("Error: debes introducir un número entero.")

# Añadir la nueva venta a la lista
ventas.append([marca, modelo, anio_venta, anio_fabricacion, precio])

print("Venta registrada correctamente.") 

# 2) Resumen de Ventas por Marca, Modelo y Año de fabricacion

resumen_ventas = {}

for venta in ventas: #recorro ventas
    marca = venta[0]
    modelo = venta[1]
    anio_venta = venta[2]
    precio = venta[4]

    clave = marca + "_" + modelo + "_" + str(anio_venta) #creo la clave del diccionario
    #str convierte el año en texto y lo puede concatenar

    #comprobamos si la clave ya existe
    if clave in resumen_ventas:
        resumen_ventas[clave][0] += 1 #total unidades vendidas
        resumen_ventas[clave][1] += precio # total euros acumlados
    else: #sino existe la creamos
        resumen_ventas[clave] = [1, precio] #uno y otro

print(resumen_ventas)



