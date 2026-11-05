# Clase Hija 1 (Vendedor) — Herencia:
# Hereda de Empleado.
# Atributo propio: comision (un importe fijo extra por sus ventas del mes).
# Sobrescribe calcular_sueldo() para sumar la comisión al sueldo base.

from empleado import Empleado

class Vendedor(Empleado):

    comision = 0

    def __init__(self, comision):

        self.comision = comision
        