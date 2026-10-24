# EJERCICIO 17c: Escribe un programa en Python que inicialice una lista llamada frutas 
#con los elementos "manzana", "platano" y "naranja". 
#El programa debe presentar de forma continua un menú dentro de un bucle while 
#con las siguientes opciones numéricas: 
#1. Ver lista completa: Muestra la lista completa por pantalla. 
#2. Ver un elemento por índice: Pide una posición al usuario y muestra el elemento guardado en dicho índice. 
#3. Añadir elemento: Pide el nombre de una nueva fruta y la añade al final de la lista. 
#4. Modificar elemento: Pide la posición que se desea cambiar y 
#el nuevo nombre para actualizar ese valor en la lista. 
#5. Borrar elemento: Pide el índice del elemento que se quiere eliminar y lo quita de la lista. 
#6. Salir: Muestra un mensaje de despedida y finaliza la ejecución del programa.

#lista inicial
frutas = ["manzana", "platano", "naranja"]

opcion = -1

while opcion != 6: #repite el menu hasta que elija 6 que es salir
    print("--- MENÚ ---")
    print("1. Ver lista completa")
    print("2. Ver un elemento por índice")
    print("3. Añadir elemento")
    print("4. Modificar elemento")
    print("5. Borrar elemento")
    print("6. Salir")

    try:
        opcion = int(input("Elige una opción: "))

        match opcion:
            case 1:
                print("Lista de frutas:", frutas)

            case 2:
                indice = int(input("Introduce el índice de la fruta: "))

                if 0 <= indice < len(frutas): #len te dice cuantas frutas hay en la lista
                    print("Fruta:", frutas[indice])
                else:
                    print("Error: índice fuera de rango.")

            case 3:
                fruta = input("Introduce el nombre de la nueva fruta: ")
                frutas.append(fruta) #añade esa nueva fruta al final de la lista
                print("Fruta añadida correctamente.")

            case 4:
                indice = int(input("Introduce el índice que quieres modificar: "))

                if 0 <= indice < len(frutas):
                    nuevaFruta = input("Introduce el nuevo nombre: ")
                    frutas[indice] = nuevaFruta #sustituye la fruta que ocupa esa posicion
                    print("Fruta modificada correctamente.")
                else:
                    print("Error: índice fuera de rango.")

            case 5:
                indice = int(input("Introduce el índice que quieres borrar: "))

                if 0 <= indice < len(frutas):
                    frutas.pop(indice) #borra el elementento que ha indicado con el indice
                    print("Fruta borrada correctamente.")
                else:
                    print("Error: índice fuera de rango.")

            case 6:
                print("Adiossssss Secun!!")

            case _:
                print("Error: opción no válida.")

    except ValueError:
        print("Error: debes introducir un número válido.")

    print() # para meter un espacio entre los menu