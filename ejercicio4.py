# Realiza un programa que pida dos números enteros al usuario y devuelva el producto de ambos.

producto = True

while producto == True:
	try:
		num1 = int(input("Introduce un numero entero:"))
		num2 = int(input("Introduce otro numero entero:"))
		print("La multiplicacion de ambos es: ", num1 * num2)
		producto = False
	except ValueError:
		print("Error: El caracter introducido no es un numero entero.")