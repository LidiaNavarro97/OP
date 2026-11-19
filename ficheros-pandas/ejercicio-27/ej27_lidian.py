import pandas as pd

ARCHIVO = "Ej 27 Pandas 1.xlsx"
HOJA = "Alumnos"
datos = {}

excel = pd.ExcelFile(ARCHIVO) #abrir el libro de excel 
df = pd.read_excel(excel, sheet_name= HOJA, index_col= None) #leer la hoja
df = df.fillna("") #rellenar los datos vacios, nos permite rellenar los valores nulos
print(df)

# Opcion 1: Con "records"
datos[HOJA] = df.to_dict(orient="records") #convierto el dataframe a diccionario
print(datos)

for alumnos in datos[HOJA]:
    for clave, valor in alumnos.items():
        print(f"{clave}: {valor}")
    print("---")        

# Parte 2:    
# Opcion 2: Con "dict"
datos_dict = df.to_dict(orient="dict") #
print(datos_dict)

for columna, filas in datos_dict.items(): #diccinario de columnas
    for indice, valor in filas.items(): #filas es otro diccionario
        print(f"{columna} (fila {indice}): {valor}")
    print("---")

# Opcion 3: Con "index"
datos_index = df.to_dict(orient="index") # diccionario de diccionarios
print(datos_index)

for indice, alumno in datos_index.items(): #cada indice con su alumno
    for columna, valor in alumno.items(): #columnas y valores de ese alumno
        print(f"{columna}: {valor}")
    print("---")    

# Opcion 4: Con "list"
datos_list = df.to_dict(orient="list") #diccionario de listas
print(datos_list)

for columna, lista_valores in datos_list.items(): #dicc, columna y su lista de valores
    for valor in lista_valores: # es una lista, se recorre directamente
        print(f"{columna}: {valor}")
    print("---")    


# Parte 3:    

# Ahora el id_persona será el índice
df_indice = pd.read_excel(excel, sheet_name=HOJA, index_col=0)
df_indice = df_indice.fillna("") # rellenamos los vacíos 
print(df_indice) # id_persona aparece a la izq en vez de 0,1,2...

# hacerlo con el orient="dict"
datos_dict_id = df_indice.to_dict(orient="dict") # diccionario de diccionarios
print(datos_dict_id)

for columna, alumnos in datos_dict_id.items(): #diccionario de columnas
    for id_persona, valor in alumnos.items(): # las claves ahora son los id_persona
        print(f"{columna} ({id_persona}): {valor}")
    print("---")  


# hacerlo con el orient="index"
datos_index_id = df_indice.to_dict(orient="index") # diccionario de diccionarios
print(datos_index_id)

for id_persona, datos_alumno in datos_index_id.items(): #la clave principal es el id de cada alum
    print(f"Alumno: {id_persona}")

    for columna, valor in datos_alumno.items(): #colum y valores de ese alumno
        print(f" {columna}: {valor}")
    print("---")    