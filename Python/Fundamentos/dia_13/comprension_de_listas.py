#### Comprensión de Listas

"""
La comprensión de listas en Python es una forma compacta de crear una lista a partir de una secuencia. Es una manera corta de crear una nueva lista. La comprensión de listas es considerablemente más rápida que procesar una lista usando un bucle for."""

"""
[i for i in iterable if expression]
"""

#Si deseas convertir una cadena en una lista de caracteres, puedes usar varios métodos. Veamos algunos de ellos:

# Primera forma
language = 'Python'
lst = list(language)  # cambiando la cadena a lista
print(type(lst))      # list
print(lst)            # ['P', 'y', 't', 'h', 'o', 'n']

# Segunda forma: comprensión de listas
lst = [i for i in language]
print(type(lst))      # list
print(lst)            # ['P', 'y', 't', 'h', 'o', 'n']

#Si deseas generar una lista de números:

# Generando números
numbers = [i for i in range(11)]  # para generar números del 0 al 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# También es posible hacer operaciones matemáticas durante la iteración
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# También es posible crear una lista de tuplas
numbers = [(i, i * i) for i in range(11)]
print(numbers)  # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

#La comprensión de listas puede combinarse con expresiones if:

# Generando números pares
even_numbers = [i for i in range(21) if i % 2 == 0]  # generar lista de números pares del 0 al 21
print(even_numbers)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Generando números impares
odd_numbers = [i for i in range(21) if i % 2 != 0]  # generar números impares del 0 al 21
print(odd_numbers)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Filtrando números positivos pares de la lista
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)  # [4, 6, 8, 10]

#Aplanando una lista tridimensional:

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

#### Función Lambda

"""Una función lambda es una pequeña función anónima que no tiene nombre. Puede tomar cualquier cantidad de argumentos, pero solo puede tener una expresión. Las funciones lambda son similares a las funciones anónimas en JavaScript. Son útiles cuando queremos escribir una función anónima dentro de otra función.
"""

#Creando una Función Lambda

"""Para crear una función lambda usamos la palabra clave lambda, seguida de un parámetro o varios, y luego una expresión. La función lambda no usa la palabra clave return, pero devuelve de manera implícita el resultado de la expresión."""

"""
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(arg1, arg2, arg3))
"""

def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))  # 5

#Ahora cambiamos la función anterior a una función lambda:

add_two_nums = lambda a, b: a + b
print(add_two_nums(2, 3))  # 5

#Función lambda auto-invocada:

print((lambda a, b: a + b)(2, 3))  # 5

square = lambda x: x ** 2
print(square(3))  # 9

cube = lambda x: x ** 3
print(cube(3))    # 27

#Múltiples variables:

multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3))  # 22

# Función Lambda Dentro de Otra Función
# Es posible usar una función lambda dentro de otra función.

def power(x):
    return lambda n: x ** n

cube = power(2)(3)  # La función power ahora necesita 2 argumentos, en paréntesis separados
print(cube)         # 8

two_power_of_five = power(2)(5)
print(two_power_of_five)  # 32





