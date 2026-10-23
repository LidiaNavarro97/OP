# Escribe un programa que calcule el importe total a pagar en un restaurante. 
# El programa deberá pedir al usuario el coste de la comida y el porcentaje de propina que
# quiere dejar, y luego devolver el importe total.

comida = float(input("Introduce el coste de la comida: "))
propina = float(input("Introduce el porcentaje de propina que quieras dejar: "))

porcentajePropina = comida * propina / 100
total = comida + porcentajePropina 

print("El importe de la propina es: ", porcentajePropina)
print("El importe total es: ", total)