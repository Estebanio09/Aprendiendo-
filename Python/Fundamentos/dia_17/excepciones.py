"""
Manejo de Excepciones
"""

"""
Python usa try y except para manejar errores de forma elegante. Una salida elegante (o manejo elegante) de errores es una técnica simple de programación: un programa detecta una condición de error grave y "sale de manera controlada". A menudo, el programa imprime un mensaje de error descriptivo en un terminal o registro como parte de esta salida, lo que hace que nuestra aplicación sea más robusta. Las excepciones suelen deberse a causas externas al programa, como una entrada incorrecta, un nombre de archivo erróneo, la imposibilidad de encontrar un archivo o un dispositivo de entrada/salida defectuoso. El manejo elegante de errores evita que nuestras aplicaciones se bloqueen.
"""

# Hemos cubierto los diferentes tipos de errores de Python en la sección anterior. Si usamos try y except en nuestro programa, no se generarán errores en esos bloques.

# try y except

try:
    pass
    # código en este bloque si todo va bien
except:
    pass
    # código en este bloque se ejecuta si algo va mal

try:
    print(10 + "5")
except:
    print("Algo salió mal")

"""
En el ejemplo anterior, el segundo operando es una cadena. Podríamos cambiarlo a float o int para sumarlo con el 
número y hacer que funcione. Sin ningún cambio, el segundo bloque (except) se ejecutará.
"""

try:
    name = input("Ingresa tu nombre:")
    year_born = input("Año en que naciste:")
    age = 2019 - year_born
    print(f"Eres {name}. Y tu edad es {age}.")
except:
    print("Algo salió mal")

# En el ejemplo anterior, el bloque de excepción se ejecutará y no sabemos exactamente cuál es el problema. Para analizar el problema, podemos usar diferentes tipos de errores con except.

# En el siguiente ejemplo, manejará el error y también nos indicará el tipo de error generado:

try:
    name = input("Ingresa tu nombre:")
    year_born = input("Año en que naciste:")
    age = 2019 - year_born
    print(f"Eres {name}. Y tu edad es {age}.")
except TypeError:
    print("Ocurrió un error de tipo")
except ValueError:
    print("Ocurrió un error de valor")
except ZeroDivisionError:
    print("Ocurrió un error de división por cero")

# En el código anterior, el resultado será TypeError. Ahora, agreguemos un bloque adicional:

try:
    name = input("Ingresa tu nombre:")
    year_born = input("Año en que naciste:")
    age = 2019 - int(year_born)
    print(f"Eres {name}. Y tu edad es {age}.")
except TypeError:
    print("Ocurrió un error de tipo")
except ValueError:
    print("Ocurrió un error de valor")
except ZeroDivisionError:
    print("Ocurrió un error de división por cero")
else:
    print("Normalmente me ejecuto con el bloque try")
finally:
    print("Siempre me ejecuto.")


# También se puede abreviar el código anterior de la siguiente manera:

try:
    name = input("Ingresa tu nombre:")
    year_born = input("Año en que naciste:")
    age = 2019 - int(year_born)
    print(f"Eres {name}. Y tu edad es {age}.")
except Exception as e:
    print(e)


"""
Empaquetado y Desempaquetado de Argumentos en Python
Python utiliza dos operadores para empaquetar y desempaquetar:

* para listas o tuplas
** para diccionarios
Veamos el siguiente ejemplo. La función toma solo argumentos, pero tenemos una lista. Podemos desempaquetar la lista para que funcione como argumentos.

Desempaquetado
Desempaquetado de Listas
"""


def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e


lst = [1, 2, 3, 4, 5]
# print(sum_of_five_nums(lst)) # TypeError: faltan 4 argumentos posicionales

# Este código produce un error porque la función espera cinco argumentos, no una lista. Para solucionar esto, podemos desempaquetar la lista:


def sum_of_five_nums1(a, b, c, d, e):
    return a + b + c + d + e


lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums1(*lst))  # 15

# También podemos usar el desempaquetado en funciones como range, que espera un inicio y un fin:

args = [2, 7]
numbers = range(*args)
print(list(numbers))  # [2, 3, 4, 5, 6]

# Otro ejemplo de desempaquetado en listas o tuplas:

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)   

#Desempaquetado de Diccionarios

def unpacking_person_info(name, country, city, age):
    return f'{name} vive en {country}, {city}. Tiene {age} años.'

dct = {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
print(unpacking_person_info(**dct))  # Asabeneh vive en Finland, Helsinki. Tiene 250 años.

"""
                                                Empaquetado
                                                
A veces, no sabemos cuántos argumentos se pasarán a una función. Podemos usar el empaquetado para permitir una cantidad arbitraria de argumentos.
"""
# Empaquetado de Listas

def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s

print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28

#Empaquetado de Diccionarios

def packing_person_info(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh", country="Finland", city="Helsinki", age=250)) # {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}

"""
Expansión en Python
Como en JavaScript, la expansión también es posible en Python:
"""

lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7]

"""
Enumerate
Si necesitamos un índice de una lista, usamos enumerate:
"""

for index, item in enumerate([20, 30, 40]):
    print(index, item)

"""
SALIDA
0 20
1 30
2 40
"""

"""
Zip
Para combinar listas mientras iteramos sobre ellas:
"""

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []

for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit': f, 'veg': v})

print(fruits_and_veges)
# [{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, ...]


names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']
*nordic_countries, es, ru = names

print("Nordic countries:", nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
print("Estonia:", es)  # 'Estonia'
print("Russia:", ru)   # 'Russia'
