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





