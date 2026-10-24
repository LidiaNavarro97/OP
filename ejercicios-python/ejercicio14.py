# Meter en un match / case los ejercicios del 9 al 13, de forma que aparezca un
# menú con las 5 opciones para que el usuario decida que ejercicio o enunciado quiere ejecutar.
from ejercicio9 import metrosCentimetros
from ejercicio10 import areaCirculo
from ejercicio11 import importeRestaurante
from ejercicio12 import calcularIMC
from ejercicio13 import mensajeBienvenida

print("MENÚ DE LOS EJERCICIOS")

print("9. Convertir metros a centímetros")
print("10. Calcular el área de un círculo")
print("11. Calcular el importe total de un restaurante")
print("12. Calcular el IMC")
print("13. Mensaje de bienvenida")

option = int(input("Elige un ejercicio del 1 al 9: "))

match option:

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
