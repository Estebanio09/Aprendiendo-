####   Funciones

"""Hasta ahora hemos visto muchas funciones integradas de Python. En esta sección, nos enfocaremos en funciones personalizadas. ¿Qué es una función? Antes de comenzar a crear funciones, aprendamos qué es una función y por qué las necesitamos."""

# Definición de una Función

"""Una función es un bloque de código o declaraciones de programación reutilizables diseñados para realizar una tarea determinada. Para definir o declarar una función, Python proporciona la palabra clave def. El siguiente es el formato para definir una función. El bloque de código de la función se ejecuta solo si la función es llamada o invocada."""

# Declarando y Llamando a una Función

"""Cuando creamos una función, la llamamos declarar una función. Cuando comenzamos a usarla, la llamamos llamar o invocar una función. Las funciones pueden ser declaradas con o sin parámetros."""

# Sintaxis
# Declarando una función

"""
def nombre_de_funcion():
    codigo
    codigo
"""

# Llamando a una función

"""
nombre_de_funcion()
"""

# Función sin Parámetros

# Una función puede ser declarada sin parámetros.


def generar_nombre_completo():
    nombre = "Asabeneh"
    apellido = "Yetayeh"
    espacio = " "
    nombre_completo = nombre + espacio + apellido
    print(nombre_completo)


generar_nombre_completo()  # llamando a una función


def sumar_dos_numeros():
    numero_uno = 2
    numero_dos = 3
    total = numero_uno + numero_dos
    print(total)


sumar_dos_numeros()

# Función que Retorna un Valor - Parte 1

"""Una función también puede devolver valores. Si una función no tiene una declaración de retorno, el valor de la función será None. Reescribamos las funciones anteriores usando return. A partir de ahora, obtendremos un valor de una función cuando la llamemos e imprimamos el resultado."""


def generar_nombre_completo():
    nombre = "Asabeneh"
    apellido = "Yetayeh"
    espacio = " "
    nombre_completo = nombre + espacio + apellido
    return nombre_completo


print(generar_nombre_completo())  # Asabeneh Yetayeh


def sumar_dos_numeros():
    numero_uno = 2
    numero_dos = 3
    total = numero_uno + numero_dos
    return total


print(sumar_dos_numeros())  # 5

# Función con Parámetros

"""
En una función, podemos pasar diferentes tipos de datos (números, cadenas, booleanos, listas, tuplas, diccionarios o conjuntos) como parámetro.
"""

"""
Un solo parámetro: Si nuestra función toma un parámetro, debemos llamar a nuestra función con un argumento.
"""

# Sintaxis
# Declarando una función
"""
def nombre_funcion(parámetro):
    código
    código
"""
# Llamando a la función
"""
print(nombre_funcion(argumento))
"""


def saludos(nombre):
    mensaje = nombre + ", ¡bienvenido a Python para Todos!"
    return mensaje


print(saludos("Asabeneh"))


def sumar_diez(num):
    diez = 10
    return num + diez


print(sumar_diez(90))  # 100


def cuadrado_numero(x):
    return x * x


print(cuadrado_numero(2))  # 4


def area_del_circulo(r):
    PI = 3.14
    area = PI * r**2
    return area


print(area_del_circulo(10))  # 314.0


def suma_de_numeros(n):
    total = 0
    for i in range(n + 1):
        total += i
    print(total)


print(
    suma_de_numeros(10)
)  # 55 - None // Llamar a la función hace que el print de la función imprima, pero como no retorna nada en este print es None
print(
    suma_de_numeros(100)
)  # 5050 - None // Llamar a la función hace que el print de la función imprima, pero como no retorna nada en este print es None

"""
Dos parámetros: Una función puede o no tener parámetros. Una función también puede tener dos o más parámetros. Si nuestra función toma parámetros, debemos llamarla con argumentos. Veamos una función con dos parámetros:
"""
# Sintaxis
# Declarando una función
"""
def nombre_funcion(para1, para2):
    código
    código
"""
# Llamando a la función
"""
print(nombre_funcion(arg1, arg2))
"""


def generar_nombre_completo(primer_nombre, apellido):
    espacio = " "
    nombre_completo = primer_nombre + espacio + apellido
    return nombre_completo


print(
    "Nombre completo: ", generar_nombre_completo("Asabeneh", "Yetayeh")
)  # Nombre completo:  Asabeneh Yetayeh


def sumar_dos_numeros(num_uno, num_dos):
    suma = num_uno + num_dos
    return suma


print("Suma de dos números: ", sumar_dos_numeros(1, 9))  # Suma de dos números:  10


def calcular_edad(año_actual, año_de_nacimiento):
    edad = año_actual - año_de_nacimiento
    return edad


print("Edad: ", calcular_edad(2021, 1819))  # 202


def peso_de_objeto(masa, gravedad):
    peso = (
        str(masa * gravedad) + " N"
    )  # El valor debe convertirse en una cadena primero
    return peso


print(
    "Peso de un objeto en Newtons: ", peso_de_objeto(100, 9.81)
)  # Peso de un objeto en Newtons:  981.0 N

# Pasando Argumentos con Clave y Valor

# Si pasamos los argumentos con clave y valor, el orden de los argumentos no importa.

# Sintaxis
# Declarando una función
"""
def nombre_funcion(para1, para2):
    código
    código
"""
# Llamando a la función

# print(nombre_funcion(para1='John', para2='Doe'))  # el orden de los argumentos no importa aquí


def imprimir_nombre_completo(primer_nombre, apellido):
    espacio = " "
    nombre_completo = primer_nombre + espacio + apellido
    return nombre_completo


print(
    imprimir_nombre_completo(apellido="Yetayeh", primer_nombre="Asabeneh")
)  # Asabeneh Yetayeh


def sumar_dos_numeros(num1, num2):
    total = num1 + num2
    return total


print(sumar_dos_numeros(num2=3, num1=2))  # 5  // El orden no importa

# Función que Devuelve un Valor - Parte 2

"""Si no devolvemos un valor con una función, entonces nuestra función devuelve None por defecto. Para devolver un valor, usamos la palabra clave return seguida de la variable que estamos retornando. Podemos devolver cualquier tipo de datos desde una función."""

# Devolviendo una cadena:


def imprimir_nombre(primer_nombre):
    return primer_nombre


print(imprimir_nombre("Asabeneh"))  # Asabeneh


def imprimir_nombre_completo(primer_nombre, apellido):
    espacio = " "
    nombre_completo = primer_nombre + espacio + apellido
    return nombre_completo


print(
    imprimir_nombre_completo(primer_nombre="Asabeneh", apellido="Yetayeh")
)  # Asabeneh Yetayeh

# Devolviendo un número:


def sumar_dos_numeros(num1, num2):
    total = num1 + num2
    return total


print(sumar_dos_numeros(2, 3))  # 5


def calcular_edad(año_actual, año_de_nacimiento):
    edad = año_actual - año_de_nacimiento
    return edad


print("Edad: ", calcular_edad(2019, 1819))  # Edad:  200

# Devolviendo un booleano:


def es_par(n):
    if n % 2 == 0:
        print("par")
        return (
            True  # return detiene la ejecución posterior de la función, similar a break
        )
    return False


print(es_par(10))  # True
print(es_par(7))  # False

# Devolviendo una lista:


def encontrar_numeros_pares(n):
    pares = []
    for i in range(n + 1):
        if i % 2 == 0:
            pares.append(i)
    return pares


print(encontrar_numeros_pares(10))  # [0, 2, 4, 6, 8, 10]

# Función con Parámetros Predeterminados

"""
A veces pasamos valores predeterminados a los parámetros cuando invocamos la función. Si no pasamos argumentos al llamar a la función, se usarán los valores predeterminados.
"""

# Sintaxis
# Declarando una función
"""
def nombre_funcion(parametro=valor):
    código
    código
"""
# Llamando a la función
"""
nombre_funcion()
nombre_funcion(argumento)
"""


def saludos(nombre="Peter"):
    mensaje = nombre + ", ¡bienvenido a Python para Todos!"
    return mensaje


print(saludos())  # Peter, ¡bienvenido a Python para Todos!
print(saludos("Asabeneh"))  # Asabeneh, ¡bienvenido a Python para Todos!


def generar_nombre_completo(primer_nombre="Asabeneh", apellido="Yetayeh"):
    espacio = " "
    nombre_completo = primer_nombre + espacio + apellido
    return nombre_completo


print(generar_nombre_completo())  # Asabeneh Yetayeh
print(generar_nombre_completo("David", "Smith"))  # David Smith


def calcular_edad(año_de_nacimiento, año_actual=2024):
    edad = año_actual - año_de_nacimiento
    return edad


print("Edad: ", calcular_edad(1999))  # Edad:  25


def peso_del_objeto(masa, gravedad=9.81):
    peso = str(masa * gravedad) + " N"  # El valor debe ser convertido a cadena primero
    return peso


print(
    "Peso de un objeto en Newtons: ", peso_del_objeto(100)
)  # 9.81 - gravedad promedio en la superficie de la Tierra
print(
    "Peso de un objeto en Newtons: ", peso_del_objeto(100, 1.62)
)  # Gravedad en la superficie de la Luna

# Número Arbitrario de Argumentos

"""Si no sabemos cuántos argumentos vamos a pasar a nuestra función, podemos crear una función que acepte un número arbitrario de argumentos añadiendo un * antes del nombre del parámetro."""

# Sintaxis
# Declarando una función
"""
def nombre_funcion(*args):
    código
    código
"""
# Llamando a la función
# nombre_funcion(param1, param2, param3, ..)


def sumar_todos_los_numeros(*numeros):
    total = 0
    for num in numeros:
        total += num  # lo mismo que total = total + num
    return total


print(sumar_todos_los_numeros(2, 3, 5))  # 10

# Parámetros Predeterminados y Número Arbitrario de Parámetros en Funciones


def generar_grupos(equipo, *args):
    print(equipo)
    for i in args:
        print(i)


print(generar_grupos("Equipo-1", "Asabeneh", "Brook", "David", "Eyob"))

# Función como Parámetro de Otra Función

# Podemos pasar funciones como parámetros de otras funciones.


def cuadrado_de_un_numero(n):
    return n * n


def hacer_algo(funcion, x):
    return funcion(x)


print(hacer_algo(cuadrado_de_un_numero, 3))  # 9
