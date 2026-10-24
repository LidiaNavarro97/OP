#  Añadir al ejercicio anterior una opción para salir del programa y 
# un bucle del que sólo saldrá el programa cuando el usuario seleccione dicha opción de salida.

from ejercicio9 import metrosCentimetros
from ejercicio10 import areaCirculo
from ejercicio11 import importeRestaurante
from ejercicio12 import calcularIMC
from ejercicio13 import mensajeBienvenida

option = -1 #le pongo un valor distinto de 0 para q el bucle empiece

while option != 0: #el menu se repite mientras lo q elija sea distinto de 0

    print("MENÚ DE LOS EJERCICIOS")

    print("9. Convertir metros a centímetros")
    print("10. Calcular el área de un círculo")
    print("11. Calcular el importe total de un restaurante")
    print("12. Calcular el IMC")
    print("13. Mensaje de bienvenida")
    print("0. Salir del programa")

    option = int(input("Elige un ejercicio del 1 al 9 (0 para salir): "))

    match option:
        case 0: # como option vale 0, si elige este el while termina
            print("Has salido del programa")
        case 9:
            metrosCentimetros()
        case 10:
            areaCirculo()
        case 11:
            importeRestaurante()
        case 12:
            calcularIMC()
        case 13:
            mensajeBienvenida()
        case _: #en cualquier otro caso...
            print("Opción no válida")