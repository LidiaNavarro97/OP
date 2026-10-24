# EJERCICIO 18
# SISTEMA DE GESTION PARA FRUTERIA

#datos
productos = ["manzanas", "plátanos", "naranjas", "kiwis", "fresas"]

#tupla de informacion
info_tienda = ("Frutería La Huerta", "Calle Mayor 12", "912345678", 2010)

# diccionario de precios
precios = {
    "manzanas": 1.50,
    "plátanos": 2.10,
    "naranjas": 1.20,
    "kiwis": 3.45,
    "fresas": 2.80
}

#menu
opcion = 0

while opcion != 4:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Gestión de lista de productos")
    print("2. Información de la tienda")
    print("3. Gestión de precios")
    print("4. Salir")

    try: 
        opcion= int(input("Eilge una opción: "))

        match opcion:

            case 1:
            case 2:
            case 3:
            case 4:
            case _: 

    except ValueError:
       print("Error: introduce un número válido o un precio correcto.")        
