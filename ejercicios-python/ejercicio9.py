# Crea un programa que convierta metros a centímetros. El programa deberá
# pedir al usuario que introduzca una cantidad en metros y devolver la cantidad en centímetros


def metrosCentimetros():

    cantidadMetros = float(input("Introduce una cantidad en metros: "))

    cantidadCentimetros = cantidadMetros * 100 

    print("La cantidad en centímetros es: ", cantidadCentimetros)