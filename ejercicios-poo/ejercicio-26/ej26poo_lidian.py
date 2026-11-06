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

# Clase Hija 1 (Vendedor) — Herencia:
# Hereda de Empleado.
# Atributo propio: comision (un importe fijo extra por sus ventas del mes).
# Sobrescribe calcular_sueldo() para sumar la comisión al sueldo base.

class Vendedor(Empleado):

    comision = 0

    def __init__(self, comision):

        self.comision = comision    

        