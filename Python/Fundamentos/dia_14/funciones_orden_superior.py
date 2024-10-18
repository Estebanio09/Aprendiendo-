#Funciones de Orden Superior
#En Python, las funciones son tratadas como ciudadanos de primera clase, lo que te permite realizar las siguientes operaciones con ellas:

"""
Una función puede tomar una o más funciones como parámetros.
Una función puede ser devuelta como resultado de otra función.
Una función puede ser modificada.
Una función puede ser asignada a una variable.
En esta sección, cubriremos:

Manejo de funciones como parámetros.
Devolver funciones como valor de retorno desde otra función.
Uso de cierres (closures) y decoradores en Python.
"""

#Función como Parámetro

def sum_numbers(nums):  # función normal
    return sum(nums)    # una función triste que usa la función incorporada sum :<

def higher_order_function(f, lst):  # función como parámetro
    summation = f(lst)
    return summation

result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15

#Función como Valor de Retorno

def square(x):          # función cuadrado
    return x ** 2

def cube(x):            # función cubo
    return x ** 3

def absolute(x):        # función valor absoluto
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type):  # función de orden superior que devuelve una función
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3

#Puedes ver en el ejemplo anterior que la función de orden superior devuelve diferentes funciones según el parámetro pasado.

#Cierres en Python
"""
Python permite que una función anidada acceda al ámbito exterior de la función que la engloba. Esto es conocido como un Cierre (Closure). En Python, un cierre se crea al anidar una función dentro de otra función encapsuladora y luego devolver la función interna. Veamos un ejemplo de cómo funcionan los cierres en Python.
"""

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))   # 15
print(closure_result(10))  # 20

#Decoradores en Python
"""
Un decorador es un patrón de diseño en Python que permite al usuario añadir nuevas funcionalidades a un objeto existente sin modificar su estructura. Los decoradores son usualmente llamados antes de la definición de la función que deseas decorar.
"""
#Creación de Decoradores
"""
Para crear una función decoradora, necesitamos una función externa con una función interna que actúe como wrapper (envoltura).
"""

# Función normal
def greeting():
    return 'Welcome to Python'

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

g = uppercase_decorator(greeting)
print(g())  # WELCOME TO PYTHON

#Implementación del Ejemplo con un Decorador

'''Esta función decoradora es una función de orden superior
que toma una función como parámetro'''

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def greeting():
    return 'Welcome to Python'

print(greeting())  # WELCOME TO PYTHON

#Aplicando Múltiples Decoradores a una Sola Función

'''Estas funciones decoradoras son funciones de orden superior
que toman funciones como parámetros.'''

# Primer Decorador
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Segundo Decorador
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string_decorator
@uppercase_decorator  # el orden es importante - .upper() no funciona con listas
def greeting():
    return 'Welcome to Python'

print(greeting())  # ['WELCOME', 'TO', 'PYTHON']

#Aceptando Parámetros en Funciones Decoradoras
"""La mayoría de las veces necesitamos que nuestras funciones acepten parámetros, por lo que puede ser necesario definir un decorador que acepte parámetros."""

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("Vivo en {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("Soy {} {}. Me encanta enseñar.".format(first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh", 'Finlandia')
#Soy Asabeneh Yetayeh. Me encanta enseñar.
#Vivo en Finlandia

#Funciones Incorporadas de Orden Superior
"""Algunas de las funciones de orden superior integradas en Python que cubriremos son map(), filter(), y reduce(). Las funciones lambda pueden pasarse como parámetros, y el mejor caso de uso para estas funciones lambda es en funciones como map, filter y reduce."""

#Función map() en Python
#La función map() es una función incorporada que toma una función y un iterable como parámetros.
# sintaxis
"""map(función, iterable)"""

numbers = [1, 2, 3, 4, 5]  # iterable

def square(x):
    return x ** 2

numbers_squared = map(square, numbers)
print(list(numbers_squared))  # [1, 4, 9, 16, 25]

# Aplicación con una función lambda
numbers_squared = map(lambda x: x ** 2, numbers)
print(list(numbers_squared))  # [1, 4, 9, 16, 25]

numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))  # [1, 2, 3, 4, 5]

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))  # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Aplicación con una función lambda
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))  # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

#Función filter() en Python
"""La función filter() llama a la función especificada, que devuelve un valor booleano para cada elemento del iterable especificado (lista). Filtra los elementos que cumplen con el criterio de filtrado"""

"""filter(función, iterable)"""

# Filtrar solo los números pares
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    return num % 2 == 0

even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # [2, 4]

# Filtrar solo los números impares
numbers = [1, 2, 3, 4, 5]  # iterable

def is_odd(num):
    return num % 2 != 0

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))  # [1, 3, 5]

#Filtrar nombres largos:

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def is_name_long(name):
    return len(name) > 7

long_names = filter(is_name_long, names)
print(list(long_names))  # ['Asabeneh']

#Función reduce() en Python
"""La función reduce() se define en el módulo functools, y debemos importarla desde este módulo. Al igual que map() y filter(), toma dos parámetros: una función y un iterable. Sin embargo, no devuelve otro iterable, sino un valor único."""

from functools import reduce

numbers_str = ['1', '2', '3', '4', '5']  # iterable

def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)  # 15
