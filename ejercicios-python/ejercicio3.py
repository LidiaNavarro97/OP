# Crea un programa que pida dos números enteros y muestre el resultado de restar el segundo número al primero.

resta = True

while resta == True:
	try:
		num1 = int(input("Introduce un numero entero:"))
		num2 = int(input("Introduce otro numero entero:"))
		print("La resta de ambos numeros es: ", num2 - num1)
		resta = False
	except ValueError:
		print("Error: El caracter introducido no es un numero entero.")