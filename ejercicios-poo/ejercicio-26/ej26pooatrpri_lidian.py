# A partir del ejercicio 26, cambiar los atributos para que sean privados y se hagan las
# siguientes validades al modificar dichos atributos:
# - nombre: no puede estar vacio
# - sueldo base: mayor que cero y menor de 200.000 eur
# - comisión: menor del 50% del sueldo base
# - bono: menor del 50% del sueldo base
# Los hacemos privados con el método tradicional de acceso con: get y set
# Hacemos una prueba en código, subiendo en 100 eur la comisión e intentando poner un
# sueldo base negativo

#EMPELADO
class Empleado:

    def __init__(self, nombre, sueldo_base):

        self.__nombre = nombre
        self.__sueldo_base = sueldo_base

    # GET Y SET DEL NOMBRE

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):

        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio")

        self.__nombre = nombre

    # GET Y SET DEL SUELDO BASE

    @property
    def sueldo_base(self):
        return self.__sueldo_base

    @sueldo_base.setter
    def sueldo_base(self, sueldo_base):

        if sueldo_base <= 0 or sueldo_base >= 200000:
            raise ValueError("El sueldo base debe ser mayor que 0 y menor de 200.000€")

        self.__sueldo_base = sueldo_base

    def calcular_sueldo(self):
        return self.sueldo_base


#VENDEDOR
class Vendedor(Empleado):

    def __init__(self, nombre, sueldo_base, comision):
        super().__init__(nombre, sueldo_base)

        self.__comision = comision # guardo la comision del vendedor

    #GET Y SET DE COMISION

    @property
    def comision(self):
        return self.__comision

    @comision.setter
    def comision(self, comision):

        if comision >= self.sueldo_base * 0.50:
            raise ValueError("La comision debe ser inferior al 50% del sueldo base")

        self.__comision = comision

    def calcular_sueldo(self): # sobreescribo el metodo padre y suma la comision al sueldo
        return self.sueldo_base + self.comision  


#GERENTE
class Gerente(Empleado):

    def __init__(self, nombre, sueldo_base, bono_gestion):
        super().__init__(nombre, sueldo_base)

        self.__bono_gestion = bono_gestion # guarda el bono propio del gerente   

    # GET Y SET DE BONO GESTION

    @property
    def bono_gestion(self):
        return self.__bono_gestion

    @bono_gestion.setter
    def bono_gestion(self, bono_gestion):

        if bono_gestion >= self.sueldo_base * 0.50:
            raise ValueError("El bono debe ser inferior al 50% del sueldo base")

        self.__bono_gestion = bono_gestion


    def calcular_sueldo(self):
        return self.sueldo_base + self.bono_gestion
                                                    

empleado1 = Empleado("Ana", 1200)
vendedor1 = Vendedor("Carlos", 1200, 350)
gerente1 = Gerente("Marta", 2000, 500)

# creo una lista con los tres objetos
empelados = [empleado1, vendedor1, gerente1]

# recorro la lista
for empleado in empelados:
    print(f"{empleado.nombre}: {empleado.calcular_sueldo()} euros") 



#Prueba del enunciado

vendedor1.comision = vendedor1.comision + 100 #subimos la comision 100€ a carlos
print(f"Nueva comision de Carlos: {vendedor1.comision} €")

# Intento poner un sueldo base negativo

try:
    vendedor1.sueldo_base = -500

except ValueError as error:
    print(f"Error: {error}")

