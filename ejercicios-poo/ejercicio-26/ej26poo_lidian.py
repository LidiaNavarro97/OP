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

    def __init__(self, nombre, sueldo_base, comision):
        super().__init__(nombre, sueldo_base)

        self.comision = comision # guardo la comision del vendedor

    def calcular_sueldo(self): # sobreescribo el metodo padre y suma la comision al sueldo
        return self.sueldo_base + self.comision   

# Clase Hija 2 (Gerente) — Herencia:
# Hereda de Empleado.
# Atributo propio: bono_gestion (un porcentaje o extra fijo por liderar el equipo).
# Sobrescribe calcular_sueldo() para sumar el bono al sueldo base.  

class Gerente(Empleado):

    def __init__(self, nombre, sueldo_base, bono_gestion):
        super().__init__(nombre, sueldo_base)

        self.bono_gestion = bono_gestion # guarda el bono propio del gerente   

    def calcular_sueldo(self):
        return self.sueldo_base + self.bono_gestion # lo vuelvo a sobreescribir
                                                    # devuelvo el sueldo base + bono gestion

# Polimorfismo:
# Crea una lista que contenga objetos mezclados (Empleado, Vendedor, Gerente).
# Empleada: Ana, 1200 eur
# Vendedor: Carlos, 1200 eur, 350 eur
# Gerente: Marta, 2000 eur, 500 eur
# Escribe por pantalla el sueldo de cada empleado

# creo los objetos

empleado1 = Empleado("Ana", 1200)
vendedor1 = Vendedor("Carlos", 1200, 350)
gerente1 = Gerente("Marta", 2000, 500)

# creo una lista con los tres objetos
empelados = [empleado1, vendedor1, gerente1]

# recorro la lista
for empleado in empelados:
    print(f"{empleado.nombre}: {empleado.calcular_sueldo()} euros")