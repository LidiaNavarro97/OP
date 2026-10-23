# Escribe un programa que calcule el área de un círculo. El programa deberá
# pedir al usuario que introduzca el radio del círculo y, 
# utilizando la fórmula Área = Pi * radio^2
import math #para poder utilizar pi

def areaCirculo():

    radioCirculo = float(input("Introduce el radio del circulo: "))

    area = math.pi * radioCirculo ** 2 #el ^ se utiliza con **

    print("El area de un circulo es: ", area)