#A partir del ejercicio 26, con los atributos públicos, añadir la gestión de los departamentos
# nacional, internacional y nuevos productos de la empresa. 
 
#Estos departamentos tienen un nombre de departamento, un gerente y 
#un número indeterminado de empleados y vendedores. 

#Haz un ejemplo con estos datos y imprime por pantalla la información global 
#del departamento, con su gerente, empleados y la nómina total del departamento:

# CLASE DEPARTAMENTO

class Departamento:

    def __init__(self, nombre, gerente):

        self.nombre = nombre
        self.gerente = gerente
        self.empleados = []  # lista donde guardo empleados y vendedores

    # para añadir empleados o vendedores al departamento
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    # Calcular la nomina total del departamento
    def calcular_nomina(self):

        nomina = self.gerente.calcular_sueldo()

        for empleado in self.empleados:
            nomina += empleado.calcular_sueldo()

        return nomina

    # Mostrar toda la informacion del departamento
    def mostrar_informacion(self):

        print(f"Departamento {self.nombre}")

        print(f"Gerente: {self.gerente.get_nombre()}")
        print(f"Sueldo gerente: {self.gerente.calcular_sueldo()} €")

        print("\nEmpleados y vendedores:")

        for empleado in self.empleados:
            print(f"{empleado.get_nombre()}: {empleado.calcular_sueldo()} €")

        print(f"\nNomina total del departamento: {self.calcular_nomina()} €")

# DEPARTAMENTO NACIONAL 

departamento_nacional = Departamento("Nacional", gerente1)
departamento_nacional.agregar_empleado(empleado1)
departamento_nacional.agregar_empleado(vendedor1)


# DEPARTAMENTO INTERNACIONAL 

gerente_internacional = Gerente("John", 2500, 850)

departamento_internacional = Departamento("Internacional", gerente_internacional)

vendedor_internacional1 = Vendedor("Sarah", 1500, 600)
vendedor_internacional2 = Vendedor("Pierre", 1500, 550)

departamento_internacional.agregar_empleado(vendedor_internacional1)
departamento_internacional.agregar_empleado(vendedor_internacional2)


# DEPARTAMENTO NUEVOS PRODUCTOS 

gerente_nuevos_productos = Gerente("Marta", 2000, 450)

empleado_nuevos_productos = Empleado("Jaime", 1200)
vendedor_nuevos_productos = Vendedor("Secundino", 1200, 350)

departamento_nuevos_productos = Departamento("Nuevos Productos", gerente_nuevos_productos)

departamento_nuevos_productos.agregar_empleado(empleado_nuevos_productos)
departamento_nuevos_productos.agregar_empleado(vendedor_nuevos_productos)


# muestro los tres departamentos

departamento_nacional.mostrar_informacion()
departamento_internacional.mostrar_informacion()
departamento_nuevos_productos.mostrar_informacion()        