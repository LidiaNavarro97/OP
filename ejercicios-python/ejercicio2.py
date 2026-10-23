# Escribe un programa que pida al usuario dos números reales (decimales) y calcule su suma.

suma = True

while suma == True:
	try:
		num1 = float(input("Introduce un numero:"))
		num2 = float(input("Introduce otro numero:"))
		print("La suma de los dos es: ", num1 + num2)
		suma = False
	except ValueError:
		print("Error: El caracter introducido no es un numero.")