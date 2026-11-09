# A partir del ejercicio 26, cambiar los atributos para que sean privados y se hagan las
# siguientes validades al modificar dichos atributos:
# - nombre: no puede estar vacio
# - sueldo base: mayor que cero y menor de 200.000 eur
# - comisión: menor del 50% del sueldo base
# - bono: menor del 50% del sueldo base
# Los hacemos privados con el método tradicional de acceso con: get y set
# Hacemos una prueba en código, subiendo en 100 eur la comisión e intentando poner un
# sueldo base negativo


# EMPLEADO
class Empleado:

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


# creo los objetos

empleado1 = Empleado("Ana", 1200)
vendedor1 = Vendedor("Carlos", 1200, 350)
gerente1 = Gerente("Marta", 2000, 500)

# CREO UNA LISTA CON LOS TRES OBJETOS
empleados = [empleado1, vendedor1, gerente1]

# recorro la lista
for empleado in empleados:
    print(f"{empleado.get_nombre()}: {empleado.calcular_sueldo()} euros")


# Subimos la comision 100 euros a Carlos
vendedor1.set_comision(vendedor1.get_comision() + 100)

print(f"Nueva comision de Carlos: {vendedor1.get_comision()} €")


# Intentamos poner un sueldo base negativo

try:
    vendedor1.set_sueldo_base(-500)

except ValueError as error:
    print(f"Error: {error}")


