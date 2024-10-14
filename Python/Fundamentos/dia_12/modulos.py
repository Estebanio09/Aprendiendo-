#### ¿Qué es un Módulo?
# Un módulo es un archivo que contiene un conjunto de códigos o funciones que se pueden incluir en una aplicación. Un módulo puede ser un archivo que contenga una sola variable, una función o una base de código grande.

# Creación de un Módulo
# Para crear un módulo, escribimos nuestro código en un script de Python y lo guardamos como un archivo .py. Crea un archivo llamado mymodule.py dentro de tu carpeta de proyecto. Escribamos algo de código en este archivo:

# archivo mymodule.py


def generate_full_name(firstname, lastname):
    return firstname + " " + lastname


# Crea un archivo main.py en tu directorio de proyecto e importa el archivo mymodule.py.

# Importando un Módulo
# Para importar el archivo usamos la palabra clave import seguida del nombre del archivo solamente.
# archivo main.py
import mymodule

print(mymodule.generate_full_name("Asabeneh", "Yetayeh"))  # Asabeneh Yetayeh

# Importar Funciones desde un Módulo
# Podemos tener muchas funciones en un archivo e importarlas todas de manera diferente.

# archivo main.py
from mymodule import generate_full_name, sum_two_nums, person, gravity

print(generate_full_name("Asabneh", "Yetayeh"))
print(sum_two_nums(1, 9))
mass = 100
weight = mass * gravity
print(weight)
print(person["firstname"])

# Importar Funciones de un Módulo y Renombrarlas
# Durante la importación, podemos cambiar el nombre del módulo.

# archivo main.py
from mymodule import (
    generate_full_name as fullname,
    sum_two_nums as total,
    person as p,
    gravity as g,
)

print(fullname("Asabneh", "Yetayeh"))
print(total(1, 9))
mass = 100
weight = mass * g
print(weight)
print(p)
print(p["firstname"])

# Importar Módulos Incorporados
"""Al igual que en otros lenguajes de programación, también podemos importar módulos utilizando la palabra clave import. Vamos a importar algunos módulos comunes que usaremos con frecuencia. Algunos de los módulos incorporados comunes son: math, datetime, os, sys, random, statistics, collections, json, re."""

# Módulo OS
"""Usando el módulo os de Python, es posible realizar automáticamente muchas tareas del sistema operativo. El módulo os en Python proporciona funciones para crear, cambiar el directorio de trabajo actual, eliminar un directorio (carpeta), obtener su contenido, y cambiar e identificar el directorio actual."""

# Importar el módulo
import os

# Crear un directorio
# os.mkdir("nombre_del_directorio")

# Cambiar el directorio actual
# os.chdir("ruta")

# Obtener el directorio de trabajo actual
# os.getcwd()

# Eliminar un directorio
# os.rmdir("nombre_del_directorio")

# Módulo Sys
"""El módulo sys proporciona funciones y variables utilizadas para manipular diferentes partes del entorno de ejecución de Python. La función sys.argv devuelve una lista de argumentos pasados a un script de Python desde la línea de comandos. El elemento en el índice 0 de esta lista es siempre el nombre del script, y en el índice 1 está el argumento pasado desde la línea de comandos."""

# Ejemplo de un archivo script.py:
import sys

# print(sys.argv[0], argv[1],sys.argv[2])  # Esta línea imprimiría: nombre_del_archivo argumento1 argumento2
# print('Bienvenido {}. ¡Disfruta el reto de {}!'.format(sys.argv[1], sys.argv[2]))

# Ahora, para verificar cómo funciona este script, escribí en la línea de comandos:
# Bienvenido Asabeneh. ¡Disfruta el reto de 30DaysOfPython!
# Para salir de sys
# sys.exit()

# Para conocer el número entero más grande que soporta
# sys.maxsize

# Para conocer la ruta del entorno
# sys.path

# Para conocer la versión de Python que estás usando
# sys.version

# Módulo Statistics
"""El módulo statistics proporciona funciones para realizar estadísticas matemáticas con datos numéricos. Algunas de las funciones estadísticas más comunes en este módulo son: mean, median, mode, stdev, entre otras."""

from statistics import *  # Importar todas las funciones del módulo statistics

edades = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]

print(mean(edades))  # 21.09090909090909
print(median(edades))  # 22
print(mode(edades))  # 20
print(stdev(edades))  # 6.106628291529549

##Módulo Math
# Este módulo contiene muchas operaciones y constantes matemáticas.

import math
print(math.pi)           # 3.141592653589793, constante pi
print(math.sqrt(2))      # 1.4142135623730951, raíz cuadrada
print(math.pow(2, 3))    # 8.0, función exponencial
print(math.floor(9.81))  # 9, redondeo hacia abajo
print(math.ceil(9.81))   # 10, redondeo hacia arriba
print(math.log10(100))   # 2, logaritmo en base 10

'''
Ahora, hemos importado el módulo math, que contiene muchas funciones que nos pueden ayudar a realizar cálculos matemáticos. Para comprobar qué funciones tiene el módulo, podemos usar help(math) o dir(math). Esto mostrará las funciones disponibles en el módulo. Si solo queremos importar una función específica del módulo, lo hacemos de la siguiente manera:
'''

from math import pi
print(pi)

#También es posible importar múltiples funciones al mismo tiempo:

from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(log10(100))         # 2

#Pero si queremos importar todas las funciones del módulo math, podemos usar *:

from math import *
print(pi)                  # 3.141592653589793, constante pi
print(sqrt(2))             # 1.4142135623730951, raíz cuadrada
print(pow(2, 3))           # 8.0, exponencial
print(floor(9.81))         # 9, redondeo hacia abajo
print(ceil(9.81))          # 10, redondeo hacia arriba
print(log10(100))          # 2

#Cuando importamos, también podemos cambiar el nombre de la función:

from math import pi as PI
print(PI)  # 3.141592653589793

#Módulo String
#El módulo string es útil para muchos propósitos. El siguiente ejemplo muestra algunos usos del módulo string.

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

#Módulo Random
'''
Ya estás familiarizado con la importación de módulos. Hagamos una importación más para familiarizarnos aún más. Importemos el módulo random, que nos da un número aleatorio entre 0 y 0.9999... El módulo random tiene muchas funciones, pero en esta sección solo utilizaremos random y randint.
'''
from random import random, randint
print(random())   # no toma ningún argumento; devuelve un valor entre 0 y 0.9999
print(randint(5, 20)) # devuelve un número entero aleatorio entre [5, 20] inclusive
