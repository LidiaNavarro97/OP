# Crea un programa que calcule el IMC (Índice de Masa Corporal) del usuario.
# El programa deberá pedir al usuario su peso (en kilogramos) y su altura (en metros), 
# y luego calcular su IMC usando la fórmula: IMC = Peso / Altura^2

def calcularIMC():

    peso = float(input("Indique su peso en kg: "))
    altura = float(input("Indique su altura en metros: "))

    imc = peso / altura ** 2

    print("Indice de masa corporal: ", imc)