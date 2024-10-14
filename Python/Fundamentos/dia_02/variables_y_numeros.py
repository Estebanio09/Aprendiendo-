### Variables ### 

#Aquí hay algunos ejemplos de nombres de variables válidos:

"""
firstname
lastname
age
country
city
first_name
last_name
capital_city
_if (si queremos usar una palabra reservada como variable)
year_2021
year2021
current_year_2021
birth_year
num1
num2
"""
#Nombres de variables inválidos:

"""
first-name
first@name
first$name
num-1
1num
"""

# Variables en Python

first_name = 'Pablo'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 25
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
}

print('¡Hola, Mundo!') # El texto ¡Hola, Mundo! es un argumento
print('Hola', ',', 'Mundo', '!') # puede tomar múltiples argumentos, se han pasado cuatro argumentos
print(len('¡Hola, Mundo!')) # toma solo un argumento

# Imprimir los valores almacenados en las variables

print('Nombre:', first_name)
print('Longitud del nombre:', len(first_name))
print('Apellido: ', last_name)
print('Longitud del apellido: ', len(last_name))
print('País: ', country)
print('Ciudad: ', city)
print('Edad: ', age)
print('Casado: ', is_married)
print('Habilidades: ', skills)
print('Información de la persona: ', person_info)


#Declaración de múltiples variables en una línea

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsinki', 25, True

#Multiasignación de variables 

a = b = d = o = "Esteban Martinez"

print(first_name, last_name, country, age, is_married)
print('Nombre:', first_name)
print('Apellido: ', last_name)
print('País: ', country)
print('Edad: ', age)
print('Casado: ', is_married)

"""
Obtener la entrada del usuario usando la función integrada input(). Asignemos los datos que obtenemos de un usuario a las variables first_name y age. Ejemplo:
"""

'''
first_name = input('¿Cuál es tu nombre?: ')
age = input('¿Cuántos años tienes?: ')

print(first_name)
print(age)
'''

# Diferentes tipos de datos en Python
# Vamos a declarar variables con varios tipos de datos

first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 25                    # int

# Imprimir tipos
print(type('Asabeneh'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2, 3, 4]))   # list
print(type({'name':'Asabeneh','age':25, 'is_married':25}))  # dict
print(type((1,2)))          # tuple
print(type(zip([1,2],[3,4])))   # set

"""
Convertir un tipo de dato a otro tipo de dato. Usamos int(), float(), str()
"""

# int a float
num_int = 10
print('num_int', num_int)           # 10
num_float = float(num_int)
print('num_float:', num_float)      # 10.0

# float a int
gravity = 9.81
print(int(gravity))                 # 9

# int a str
num_int = 10
print(num_int)                      # 10
num_str = str(num_int)
print(num_str)                      # '10'

# str a int o float
num_str = '10.6'
print('num_int', int(float(num_str)))      # 10
print('num_float', float(num_str))  # 10.6

# str a list
first_name = 'Asabeneh'
print(first_name)                   # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)           # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']


###Numeros###

"""
Tipos de datos numéricos en Python:

Enteros: Números enteros (negativos, cero y positivos). Ejemplo: ... -3, -2, -1, 0, 1, 2, 3 ...
Números de punto flotante (decimales): Ejemplo: ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
Números complejos: Ejemplo: 1 + j, 2 + 4j, 1 - 1j
"""







