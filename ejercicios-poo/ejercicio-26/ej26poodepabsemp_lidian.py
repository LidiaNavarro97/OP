# A partir del ejercicio: ej26poodepabs.py, 
# añadir la clase empresa que contiene un nombre de empresa y una lista de departamentos. 
# Implementar los métodos: 
# ► agregar un nuevo departamento 
# ► transferir a un empleado de un departamento a otro 
# ► calcular nómina global de la empresa 
# ► imprimir la información de todos los departamentos

from abc import ABC, abstractmethod


# EMPLEADO (CLASE ABSTRACTA)
class Empleado(ABC):

    def __init__(self, nombre, sueldo_base):

        self.__nombre = nombre
        self.__sueldo_base = sueldo_base

    # GET Y SET DEL NOMBRE

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):

        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio")

        self.__nombre = nombre

    # GET Y SET DEL SUELDO BASE

    def get_sueldo_base(self):
        return self.__sueldo_base

    def set_sueldo_base(self, sueldo_base):

        if sueldo_base <= 0 or sueldo_base >= 200000:
            raise ValueError("El sueldo base debe ser mayor que 0 y menor de 200.000€")

        self.__sueldo_base = sueldo_base

    # METODO ABSTRACTO

    @abstractmethod
    def calcular_sueldo(self):
        pass


# EMPLEADO BASE NORMAL
class EmpleadoBase(Empleado):

    def calcular_sueldo(self):
        return self.get_sueldo_base()


# VENDEDOR
class Vendedor(Empleado):

    def __init__(self, nombre, sueldo_base, comision):
        super().__init__(nombre, sueldo_base)

        self.__comision = comision

    # GET Y SET DE COMISION

    def get_comision(self):
        return self.__comision

    def set_comision(self, comision):

        if comision >= self.get_sueldo_base() * 0.50:
            raise ValueError("La comision debe ser inferior al 50% del sueldo base")

        self.__comision = comision

    def calcular_sueldo(self):
        return self.get_sueldo_base() + self.get_comision()


# GERENTE
class Gerente(Empleado):

    def __init__(self, nombre, sueldo_base, bono_gestion):
        super().__init__(nombre, sueldo_base)

        self.__bono_gestion = bono_gestion

    # GET Y SET DE BONO GESTION

    def get_bono_gestion(self):
        return self.__bono_gestion

    def set_bono_gestion(self, bono_gestion):

        if bono_gestion >= self.get_sueldo_base() * 0.50:
            raise ValueError("El bono debe ser inferior al 50% del sueldo base")

        self.__bono_gestion = bono_gestion

    def calcular_sueldo(self):
        return self.get_sueldo_base() + self.get_bono_gestion()


# DEPARTAMENTO
class Departamento:

    def __init__(self, nombre, gerente):

        self.nombre = nombre
        self.gerente = gerente
        self.empleados = []

    # para añadir empleados y vendedores
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    # CALCULAR NOMINA TOTAL
    def calcular_nomina(self):

        nomina = self.gerente.calcular_sueldo()

        for empleado in self.empleados:
            nomina += empleado.calcular_sueldo()

        return nomina

    # MOSTRAR INFORMACION DEL DEPARTAMENTO
    def mostrar_informacion(self):

        print(f"\nDepartamento {self.nombre}")

        print(f"Gerente: {self.gerente.get_nombre()}")
        print(f"Sueldo gerente: {self.gerente.calcular_sueldo()} €")

        print("\nEmpleados y vendedores:")

        for empleado in self.empleados:
            print(f"{empleado.get_nombre()}: {empleado.calcular_sueldo()} €")

        print(f"\nNomina total del departamento: {self.calcular_nomina()} €")


# EMPRESA
class Empresa:

    def __init__(self, nombre):

        self.nombre = nombre
        self.departamentos = []

    # AGREGAR UN NUEVO DEPARTAMENTO
    def agregar_departamento(self, departamento):
        self.departamentos.append(departamento)

    # TRANSFERIR UN EMPLEADO DE UN DEPARTAMENTO A OTRO
    def transferir_empleado(self, empleado, departamento_origen, departamento_destino):

        if departamento_origen in self.departamentos and departamento_destino in self.departamentos:

            if empleado in departamento_origen.empleados:

                departamento_origen.empleados.remove(empleado)
                departamento_destino.agregar_empleado(empleado)

                print(f"{empleado.get_nombre()} ha sido transferido correctamente")

            else:
                print("El empleado no pertenece al departamento de origen")

        else:
            print("Los departamentos no pertenecen a esta empresa")

    # CALCULAR NOMINA GLOBAL DE LA EMPRESA
    def calcular_nomina_global(self):

        nomina = 0

        for departamento in self.departamentos:
            nomina += departamento.calcular_nomina()

        return nomina

    # MOSTRAR INFORMACION DE TODOS LOS DEPARTAMENTOS
    def mostrar_departamentos(self):

        print(f"EMPRESA {self.nombre}")

        for departamento in self.departamentos:
            departamento.mostrar_informacion()

        print(f"\nNOMINA GLOBAL DE LA EMPRESA: {self.calcular_nomina_global()} €")


#DEPARTAMENTO NACIONAL ---

empleado1 = EmpleadoBase("Ana", 1200)
vendedor1 = Vendedor("Carlos", 1200, 350)
gerente1 = Gerente("Marta", 2000, 500)

departamento_nacional = Departamento("Nacional", gerente1)

departamento_nacional.agregar_empleado(empleado1)
departamento_nacional.agregar_empleado(vendedor1)


#DEPARTAMENTO INTERNACIONAL ---

gerente_internacional = Gerente("John", 2500, 850)

vendedor_internacional1 = Vendedor("Sarah", 1500, 600)
vendedor_internacional2 = Vendedor("Pierre", 1500, 550)

departamento_internacional = Departamento("Internacional", gerente_internacional)

departamento_internacional.agregar_empleado(vendedor_internacional1)
departamento_internacional.agregar_empleado(vendedor_internacional2)


#DEPARTAMENTO NUEVOS PRODUCTOS

gerente_nuevos_productos = Gerente("Marta", 2000, 450)

empleado_nuevos_productos = EmpleadoBase("Jaime", 1200)
vendedor_nuevos_productos = Vendedor("Secundino", 1200, 350)

departamento_nuevos_productos = Departamento("Nuevos Productos", gerente_nuevos_productos)

departamento_nuevos_productos.agregar_empleado(empleado_nuevos_productos)
departamento_nuevos_productos.agregar_empleado(vendedor_nuevos_productos)


#CREAR EMPRESA
empresa = Empresa("LIDIA EMPRESA S.L.")

# AGREGAR LOS DEPARTAMENTOS A LA EMPRESA
empresa.agregar_departamento(departamento_nacional)
empresa.agregar_departamento(departamento_internacional)
empresa.agregar_departamento(departamento_nuevos_productos)


#TRANSFERIR EMPLEADO
empresa.transferir_empleado(vendedor1, departamento_nacional, departamento_internacional)


# Mostrar la informacion de la empresa
empresa.mostrar_departamentos()
