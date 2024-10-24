import pandas as pd 
import csv
#sin pandas 
"""
with open("c:/Users/camil/OneDrive/Escritorio/Desde 0/Python/archivos/archivo.txt") as archivo:
    leer = csv.reader(archivo)
    for row in leer:
        print(row)
        
"""

#con pandas 
df = pd.read_csv("c:/Users/camil/OneDrive/Escritorio/Desde 0/Python/archivos/archivo.txt")
# accediendo a los datos de una columna 
print(df["nombre"])
#ahora si la data que estamos tratando no incluye los campos de encabezado como nombre apellido edad que son los títulos que se pueden ver en un documento excel le podemos indicar a pandas cuales son de la siguiente formar names=["name", "apellido", "edad"]
"""
df = pd.read_csv("c:/Users/camil/OneDrive/Escritorio/Desde 0/Python/archivos/archivo.txt", names=["name", "apellido", "edad"])
"""
