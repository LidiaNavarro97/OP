# Pedir dos números enteros y hacer la división real.

def divisionReal():
        
    num1 = int(input("Introduce el primer número entero: "))
    num2 = int(input("Introduce el segundo número entero: "))

    if num2 == 0: #compruebo si el divisor es 0

        #lanzo la excepcion de la division
        raise ZeroDivisionError("No se puede dividir entre cero.")

    resultado = num1 / num2

    print("El resultado de la división es:", resultado)