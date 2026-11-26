import sys # pa leer argumentos al ejecutar el programa
from datetime import date
import pandas as pd
 
ARCHIVO_ENTRADA = "PR01_Datos.xlsx" # el excel original
ARCHIVO_SALIDA = "PR01_Datos_actualizado.xlsx" # no tocamos el original
CURSO_ACTIVO = "2025-2026"
DOMINIO = "@g.educaand.es"
GRUPOS_VALIDOS = ("DAW1", "DAW2") # tupla que no cambia nunca
 
# Lectura y Escritura 

def cargar_datos(ruta):
    """Lee todas las hojas del Excel y devuelve un dict {hoja: lista de dicts}."""

    # sheet_name=None le dice a pandas: "léeme TODAS las hojas".
    hojas = pd.read_excel(ruta, sheet_name=None) # dict {nombre_hoja: DataFrame}
    datos = {} # aquí iremos guardando el resultado

    # .items() nos da cada pareja (nombre_de_hoja, tabla) para recorrerlas
    for nombre_hoja, df in hojas.items():
        # Cambiamos los NaN de pandas por None 
        df = df.astype(object).where(df.notna(), None) # astype permite mezclar números y None en la misma columna
        #(orient="records") convierte la tabla en lista de diccionarios
        datos[nombre_hoja] = df.to_dict(orient="records") # una fila = un diccionario
    return datos
 
 
def guardar_datos(datos, ruta):
    """Convierte cada lista de dicts en DataFrame y escribe todas las hojas."""

    # ExcelWriter deja escribir varias hojas en el mismo archivo.
    # Con with el archivo se cierra solo al terminar el bloque
    with pd.ExcelWriter(ruta) as escritor:
        for nombre_hoja, filas in datos.items():
            # pd.DataFrame(lista_de_dicts) crea la tabla y las claves pasan a ser columnas
            tabla = pd.DataFrame(filas)
            # index=False evita que pandas añada una columna extra con 0,1,2,3...
            tabla.to_excel(escritor, sheet_name=nombre_hoja, index=False)
 
  