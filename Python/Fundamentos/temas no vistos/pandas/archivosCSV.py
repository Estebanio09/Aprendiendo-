import pandas as pd
import csv

# sin pandas
"""
with open("c:/Users/camil/OneDrive/Escritorio/Desde 0/Python/archivos/archivo.txt") as archivo:
    leer = csv.reader(archivo)
    for row in leer:
        print(row)
        
"""

# con pandas
df = pd.read_csv(
    "c:/Users/camil/OneDrive/Escritorio/Desde 0/Python/archivos/archivo.txt"
)
df2 = pd.read_csv(
    "c:/Users/camil/OneDrive/Escritorio/Desde 0/Python/archivos/archivo.txt"
)
# accediendo a los datos de una columna
"""
print(df["nombre"])
"""
# ahora si la data que estamos tratando no incluye los campos de encabezado como nombre apellido edad que son los títulos que se pueden ver en un documento excel le podemos indicar a pandas cuales son de la siguiente formar names=["name", "apellido", "edad"]
"""
df = pd.read_csv("c:/Users/camil/OneDrive/Escritorio/Desde 0/Python/archivos/archivo.txt", names=["name", "apellido", "edad"])
"""

# ordenar los datos: en este caso los organizaremos por sus edades esto nos devuelve una copia organizada la cual podemos almacenar en una variable // data.sort_values(valor por el cual organizar)
# ascending=False con nos muestra los valores de mayor a menor
df_organizado = df.sort_values("edad", ascending=False)

# concatenando dos dataframe pd.concat([iterable de lo que vamos a concatenar en formato lista])
df_concatenados = pd.concat([df, df2])

# acceder a los datos de arriba a abajo con head() y de abajo a arriba con tail()
# head()
primeros_tres_datos = df.head(3)
print(primeros_tres_datos)
# tail()
ultimos_tres_datos = df.tail(3)
print(ultimos_tres_datos)

# acceder a la cantidad de filas y columnas con shape // primero las filas después las columnas

info_data = df.shape
print(info_data)  #  (5, 3)
filas = df.shape[0]
print(filas)  # 5
columnas = df.shape[1]
print(columnas)  # 3
filas, columnas = df.shape  # desempaquetar

# obteniendo estadísticas del dataframe
df_info = df.describe()
print(df_info)
"""
count   5.000000
mean   45.800000
std    29.626002
min    24.000000
25%    27.000000
50%    39.000000
75%    42.000000
max    97.000000
"""

# acceder a datos específicos del data frame con loc[indice]

elemento_especifico = df.loc[1]
print(elemento_especifico)
"""
nombre        robertto
apellido     demencial
edad                42
Name: 1, dtype: object
"""
elemento_especifico = df.loc[1, "edad"]
print(elemento_especifico)  # 42

# accediendo con iloc[]
elemento_iloc = df.iloc[1, 2]
print(elemento_iloc)  # 42

# accediendo a todas la filas (row) de una columna
apellidos = df.iloc[:, 1]
apellidos_con_loc = df.loc[:, "apellido"]
print(apellidos)
"""
0         dalto
1     demencial
2         dalto
3        zosten
4     galactica
Name: apellido, 
"""
print(apellidos_con_loc)
"""
0         dalto
1     demencial
2         dalto
3        zosten
4     galactica
"""
# accediendo a los datos de una fila
fila_2 = df.loc[1, :]
print(fila_2)
"""
nombre        robertto
apellido     demencial
edad                42
"""
fila_3 = df.loc[2, :]
print(fila_3)
"""
nombre      camila
apellido     dalto
edad            24
"""
fila_4 = df.iloc[3, :]
print(fila_4)
"""
nombre      nicolas
apellido     zosten
edad             27
"""
# accediendo con una condicional en este caso que traiga los mayores de 30

mayores_de_30 = df.loc[df["edad"] > 30, :]
print(mayores_de_30)
"""
     nombre    apellido  edad
0     lucas       dalto    97
1  robertto   demencial    42
4   maquina   galactica    39
"""