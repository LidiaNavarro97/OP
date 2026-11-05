# Queremos modelar el cálculo del sueldo mensual de los empleados de una tienda:
# Clase Base (Empleado):
# Atributos: nombre y sueldo_base.
# Método: calcular_sueldo(), que por defecto devuelve únicamente el sueldo_base.

class Empleado:

    def __init__(self, nombre, sueldo_base):

        self.nombre = nombre
        self.sueldo_base = sueldo_base

    def calcular_sueldo(self):
        return self.sueldo_base 