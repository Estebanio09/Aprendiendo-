
from functools import reduce



countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Explica la diferencia entre map, filter, y reduce.

"""
map: Aplica una función a cada elemento de un iterable (como una lista) y devuelve un nuevo iterable con los resultados.

filter: Filtra los elementos de un iterable que cumplen con un criterio específico, devolviendo solo los elementos que cumplen con la condición.

reduce: Toma una función que combina dos elementos y la aplica de manera acumulativa a los elementos de un iterable, reduciendo el iterable a un solo valor."""

# Explica la diferencia entre función de orden superior, closure, y decorador.

"""
Función de orden superior: Es una función que toma otra función como argumento o devuelve una función como resultado.

Closure: Es una función que "recuerda" el entorno en el que fue creada, permitiendo que una función interna acceda a las variables locales de la función externa incluso después de que la función externa haya terminado de ejecutarse.

Decorador: Es un patrón de diseño que permite modificar o extender el comportamiento de una función o método sin modificar su estructura original, envolviéndola en otra función.
"""

# Define una función antes de usar map, filter, o reduce, y muestra ejemplos.

# filter


def par(x):
    return x % 2 == 0


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numeros_pares = list(filter(par, numeros))
print(numeros_pares)  # [2, 4, 6, 8]

# map

numeros_cuadrados = list(map(lambda x: x**2, numeros))
print(numeros_cuadrados)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# reduce

restandose = reduce(lambda x, y: x - y, numeros)
print(restandose)  # -43

# Usa un bucle for para imprimir cada país en la lista countries.

for country in countries:
    print(country)

# Usa un bucle for para imprimir cada nombre en la lista names.
for name in names:
    print(name)

# Usa un bucle for para imprimir cada número en la lista numbers.
for num in numbers:
    print(num)

# Usa map para crear una nueva lista cambiando cada país a mayúsculas en la lista countries.

countries_upp = list(map(lambda x: x.upper(), countries))
print(countries_upp)  # ['ESTONIA', 'FINLAND', 'SWEDEN', 'DENMARK', 'NORWAY', 'ICELAND']

# Usa map para crear una nueva lista cambiando cada número a su cuadrado en la lista

squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Usa map para cambiar cada nombre a mayúsculas en la lista names.
capitalized_names = list(map(lambda x: x.upper(), names))
print(capitalized_names)  # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Usa filter para filtrar los países que contienen "land".
filter_country = list(filter(lambda x: "land" in x, countries))
print(filter_country)  # ['Finland', 'Iceland']

# Usa filter para filtrar los países que tienen exactamente seis caracteres.
filter_country = list(filter(lambda x: len(x) == 6, countries))
print(filter_country)  # ['Sweden', 'Norway']

# Usa filter para filtrar los países que contienen seis letras o más.

filter_country = list(filter(lambda x: len(x) >= 6, countries))
print(
    filter_country
)  # ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

# Usa filter para filtrar los países que empiezan con la letra 'E'.

filter_country = list(filter(lambda x: x.startswith("E"), countries))
print(filter_country)  # ['Estonia']

# Encadena dos o más iteradores de listas (por ejemplo, arr.map(callback).filter(callback).reduce(callback)).
## Suma de cuadrados de números pares

Sum_of_squares_of_even_numbers = reduce(
    lambda x, y: x + y, map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))
)

print(Sum_of_squares_of_even_numbers)

# Declara una función llamada get_string_lists que toma una lista como parámetro y devuelve una lista que contiene solo elementos de tipo cadena.
variety_of_data = [
    42,
    3.14,
    "Hola, mundo!",
    True,
    None,
    [1, 2, 3, 4],
    (5, 6, 7),
    {"nombre": "Camila", "edad": 23},
    {9, 10, 11},
    bytes(5),
    bytearray(5),
    frozenset([1, 2, 3]),
    complex(2, 3),
    range(10),
    b"hello",
]


def get_string_lists(_list):
    return list(filter(lambda x : type(x) is str, _list))

print(get_string_lists(variety_of_data)) #['Hola, mundo!']

#Usa reduce para sumar todos los números en la lista numbers.

add_all_the_numbers = reduce(lambda x, y : x + y, numbers)
print(add_all_the_numbers) #55

#Usa reduce para concatenar todos los países y producir la siguiente oración: "Estonia, Finlandia, Suecia, Dinamarca, Noruega, e Islandia son países del norte de Europa."

print(reduce(lambda x, y : x +", "+ y, countries) + " son países del norte de Europa") #Estonia, Finland, Sweden, Denmark, Norway, Iceland son países del norte de Europa

#Declara una función llamada categorize_countries que devuelva una lista de países con algún patrón común (por ejemplo, 'land', 'ia', 'island', 'stan').

european_countries = [
    'Albania', 'Germany', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 
    'Belgium', 'Belarus', 'Bosnia and Herzegovina', 'Bulgaria', 
    'Cyprus', 'Croatia', 'Denmark', 'Slovakia', 'Slovenia', 
    'Spain', 'Estonia', 'Finland', 'France', 'Georgia', 
    'Greece', 'Hungary', 'Iceland', 'Italy', 'Kazakhstan', 
    'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'North Macedonia', 
    'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Norway', 
    'Netherlands', 'Poland', 'Portugal', 'United Kingdom', 'Czech Republic', 
    'Romania', 'Russia', 'San Marino', 'Serbia', 'Sweden', 'Switzerland', 
    'Turkey', 'Ukraine', 'Vatican City'
]

def categorize_countries (coincidence) -> str:
    new_list = list(filter(lambda x : coincidence in x , european_countries))
    return new_list

print(categorize_countries("land"))

#Crea una función que devuelva un diccionario donde las claves sean las letras iniciales de los países y los valores sean el número de nombres de países que comienzan con esa letra.

def initials (_list) -> list:
    _dict = {}
    for country in _list:
        if country[:1] in _dict:
            _dict[country[:1]] += 1
        else:
            _dict[country[:1]] = 1
    return dict(sorted(_dict.items(), key= lambda i : i[1], reverse=True))
    
print(initials(european_countries))

#Declara una función llamada get_first_ten_countries que devuelva una lista con los primeros diez países.

def get_first_ten_countries (_list):
    return _list[:10]

print(get_first_ten_countries(european_countries))

#Declara una función llamada get_last_ten_countries que devuelva los últimos diez países.
def get_last_ten_countries (_list):
    return _list[-10:]

print(get_last_ten_countries(european_countries))

