import os
import pandas as pd

ARCHIVO = "Ej 27 Pandas 1.xlsx"
HOJA = "Alumnos"
datos = {}

excel = pd.ExcelFile(ARCHIVO) #abrir el libro de excel 
df = pd.read_excel(excel, sheet_name= HOJA, index_col= None) #leer la hoja
df.fillna() #rellenar los datos vacios, nos permite rellenar los valores nulos
print(df)

# Opcion 1: Con "records"
datos[HOJA] = df.to_dict(orient="records") #convierto el dataframe a diccionario
print(datos)

for alumnos in datos[HOJA]:
    for clave, valor in alumnos.items():
        print(f"{clave}: {valor}")
    print("---")        
    
# Opcion 2: Con "dict"
datos[HOJA] = df.to_dict(orient="dict") #
print(datos)

for columna, filas in datos[HOJA]:
    for indice, valor in filas.items():
        print(f"{indice}: {valor}")
    print("---")
