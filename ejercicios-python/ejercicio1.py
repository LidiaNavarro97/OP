# Escribe un programa que solicite al usuario dos números enteros y muestre la suma de ambos.

suma = True

while suma == True:
	try:
		num1 = int(input("Introduce un número entero:"))
		num2 = int(input("Introduce otro número:"))
		print("La suma de los dos es: ", num1 + num2)
		suma = False
	except ValueError:
		print("Error: El caracter introducido no es un número entero.")