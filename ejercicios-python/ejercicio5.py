# Diseña un programa que solicite dos números reales y muestre el resultado de multiplicarlos entre sí.

producto = True

while producto == True:
    try:
        num1 = float(input("Introduce un numero real: "))
        num2 = float(input("Introduce otro numero real: "))
        print("La multiplicacion de ambos es: ", num1 * num2)
        producto = False
    except ValueError:
        print("Error: El caracter introducido no es un numero real.")