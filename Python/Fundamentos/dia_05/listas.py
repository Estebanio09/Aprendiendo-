### LISTAS ###

'''
En Python, existen cuatro tipos de colecciones de datos:

Lista: es una colección ordenada y modificable. Permite elementos duplicados.
Tupla: es una colección ordenada pero inmutable (no modificable). Permite elementos duplicados.
Conjunto (Set): es una colección no ordenada, no indexada e inmodificable, pero se pueden agregar nuevos elementos. No permite duplicados.
Diccionario: es una colección no ordenada, modificable e indexada. No permite duplicados.
'''

'''
Una lista es una colección de diferentes tipos de datos que es ordenada y modificable (mutable). Puede estar vacía o contener elementos de diferentes tipos de datos.
'''

#Cómo crear una lista

#Usando la función incorporada list()
# sintaxis
lst = list()
empty_list = list()  # esta es una lista vacía, no tiene elementos
print(len(empty_list))  # 0

#Usando corchetes []
# sintaxis
lst = []
empty_list = []  # esta es una lista vacía, no tiene elementos
print(len(empty_list))  # 0

#Usamos len() para encontrar la longitud de una lista.
fruits = ['banana', 'orange', 'mango', 'lemon']  # lista de frutas
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']  # lista de vegetales
animal_products = ['milk', 'meat', 'butter', 'yoghurt']  # lista de productos animales
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB']  # lista de tecnologías web
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']  # lista de países

# Imprimir las listas y su longitud
print('Frutas:', fruits)
print('Número de frutas:', len(fruits))
print('Vegetales:', vegetables)
print('Número de vegetales:', len(vegetables))
print('Productos animales:', animal_products)
print('Número de productos animales:', len(animal_products))
print('Tecnologías web:', web_techs)
print('Número de tecnologías web:', len(web_techs))
print('Países:', countries)
print('Número de países:', len(countries))

#Listas pueden tener elementos de diferentes tipos de datos

lst = ['Asabeneh', 250, True, {'country': 'Finland', 'city': 'Helsinki'}]  # lista con diferentes tipos de datos

        ######    Acceso a los elementos de una lista usando indexación positiva    ######

#Accedemos a cada elemento de una lista usando su índice. El índice de una lista comienza en 0

#   ['banana', 'mango', 'limon', 'naranja']
#        0        1        2          3        -->

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]  # estamos accediendo al primer elemento usando su índice
print(first_fruit)       # banana
second_fruit = fruits[1]
print(second_fruit)      # orange
last_fruit = fruits[3]
print(last_fruit)        # lemon

# Último índice
last_index = len(fruits) - 1
last_fruit = fruits[last_index]


#Accediendo a elementos de la lista usando indexación negativa
#La indexación negativa significa comenzar desde el final: -1 se refiere al último elemento, -2 se refiere al penúltimo elemento.

#   ['banana', 'mango', 'limon', 'naranja']
#       -4        -3      -2         -1        <--

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango

        #####  Desempaquetando elementos de una lista

# Primer ejemplo:

lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

# Segundo ejemplo:

fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits 
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']

# Tercer ejemplo:

first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10

# Cuarto ejemplo:

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)           # Germany
print(fr)           # France
print(bg)           # Belgium
print(sw)           # Sweden
print(scandic)      # ['Denmark', 'Finland', 'Norway', 'Iceland']
print(es)           # Estonia

            ###### Cortando (slicing) elementos de una lista ######

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]  # retorna todas las frutas
all_fruits = fruits[0:]   # si no establecemos dónde parar, toma todos los elementos restantes
orange_and_mango = fruits[1:3]  # no incluye el índice 3
orange_mango_lemon = fruits[1:] # desde índice 1 hasta el final
orange_and_lemon = fruits[::2]  # con un paso de 2, selecciona cada segundo elemento ['banana', 'mango']

            #### Cortando elementos de una lista ####

#Podemos especificar un rango de índices positivos definiendo el inicio, el final y el paso. El valor de retorno será una nueva lista. (Valores predeterminados: inicio = 0, final = len(lst) - 1 (último elemento), paso = 1).

### Indexación positiva:

fruits = ['banana', 'orange', 'mango', 'lemon']

all_fruits = fruits[0:4]  # retorna todas las frutas
# Esto también dará el mismo resultado que lo anterior
all_fruits = fruits[0:]   # si no establecemos el final, toma todos los elementos restantes
orange_and_mango = fruits[1:3]  # no incluye el índice 3
orange_mango_lemon = fruits[1:] # desde el índice 1 hasta el final
orange_and_lemon = fruits[::2]  # utilizando un tercer argumento (paso), tomará cada segundo elemento - ['banana', 'mango']

### Indexación negativa:

fruits = ['banana', 'orange', 'mango', 'lemon']

all_fruits = fruits[-4:]  # retorna todas las frutas
orange_and_mango = fruits[-3:-1]  # no incluye el último índice ['orange', 'mango']
orange_mango_lemon = fruits[-3:]  # esto tomará desde -3 hasta el final ['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1]  # un paso negativo tomará la lista en orden inverso ['lemon', 'mango', 'orange', 'banana']

### Modificando listas
# Una lista es una colección mutable o modificable de elementos ordenados. Vamos a modificar la lista de frutas.

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       # ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       # ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)       # ['avocado', 'apple', 'mango', 'lime']

###  Verificando elementos en una lista
# Podemos verificar si un elemento es miembro de una lista usando el operador in. Veamos el siguiente ejemplo:

fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

### Añadiendo elementos a una lista
# Para añadir un elemento al final de una lista existente, usamos el método append().

# Sintaxis
"""
lst = list()
lst.append(item)
"""

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)         # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime') 
print(fruits)         # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']

### Insertando elementos en una lista
# Podemos usar el método insert() para insertar un solo elemento en un índice especificado dentro de una lista. Ten en cuenta que los otros elementos serán desplazados a la derecha. El método insert() toma dos argumentos: el índice y el elemento a insertar.

# Sintaxis
'''
lst = ['item1', 'item2']
lst.insert(index, item)
'''

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple')  # Inserta 'apple' entre 'orange' y 'mango'
print(fruits)              # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')    # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)

            ######  Eliminando elementos de una lista

# El método remove elimina un elemento específico de una lista.

# Sintaxis
"""
lst = ['item1', 'item2']
lst.remove(item)
"""

fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - este método elimina la primera ocurrencia del elemento en la lista
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']

#### Eliminando elementos usando pop
# El método pop() elimina el índice especificado (o el último elemento si no se especifica un índice).

# Sintaxis
'''
lst = ['item1', 'item2']
lst.pop()       # último elemento
lst.pop(index)
'''

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']

#### Eliminando elementos usando del
# La palabra clave del elimina el índice especificado y también puede usarse para eliminar elementos dentro de un rango de índices. También puede eliminar completamente la lista.

'''
# Sintaxis
lst = ['item1', 'item2']
del lst[index]  # solo un elemento
del lst         # para eliminar la lista completamente
'''

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # esto elimina elementos entre los índices dados, ¡así que no elimina el elemento con índice 3!
print(fruits)       # ['orange', 'lime']
del fruits
# print(fruits)       # Esto debería dar: NameError: name 'fruits' is not defined

#### Limpiando elementos de una lista
# El método clear() vacía la lista:

'''
# Sintaxis
lst = ['item1', 'item2']
lst.clear()
'''

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []

#### Copiando una lista
#Es posible copiar una lista reasignándola a una nueva variable de la siguiente manera: list2 = list1. Ahora, list2 es una referencia de list1, cualquier cambio que hagamos en list2 también modificará el original, list1. Pero hay muchos casos en los que no queremos modificar el original, sino tener una copia diferente. Una forma de evitar el problema anterior es usando copy().

'''
# Sintaxis
lst = ['item1', 'item2']
lst_copy = lst.copy()
'''

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

                    #### Uniendo listas

# Hay varias maneras de unir o concatenar dos o más listas en Python.

# Operador más (+)

# Sintaxis
'''list3 = list1 + list2'''

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)  # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']


#### Uniendo usando el método extend()
# El método extend() permite agregar elementos de una lista a otra lista.

# Sintaxis
'''
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)
'''

num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1)  # Numbers: [0, 1, 2, 3, 4, 5, 6]

negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)  # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits)  # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

#### Contando elementos en una lista
# El método count() devuelve el número de veces que un elemento aparece en una lista.

# Sintaxis
'''
lst = ['item1', 'item2']
lst.count(item)
'''

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))  # 1

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))  # 3

#### Encontrando el índice de un elemento
# El método index() devuelve el índice de un elemento en la lista.

# Sintaxis

'''
lst = ['item1', 'item2']
lst.index(item)
'''

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))  # 1

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))  # 2, la primera ocurrencia

#### Invirtiendo una lista
# El método reverse() invierte el orden de una lista.

# Sintaxis
'''
lst = ['item1', 'item2']
lst.reverse()
'''

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)  # ['lemon', 'mango', 'orange', 'banana']

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)  # [24, 25, 24, 26, 25, 24, 19, 22]

#### Ordenando elementos de una lista
# Para ordenar listas, podemos usar el método sort() o la función incorporada sorted(). El método sort() reordena los elementos de la lista en orden ascendente y modifica la lista original. Si se pasa reverse=True, la lista se ordenará en orden descendente.

# sort(): este método modifica la lista original

# Sintaxis
'''
lst = ['item1', 'item2']
lst.sort()                # ascendente
lst.sort(reverse=True)    # descendente
'''

# Ejemplo:
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)  # ordenado en orden alfabético, ['banana', 'lemon', 'mango', 'orange']

fruits.sort(reverse=True)
print(fruits)  # ['orange', 'mango', 'lemon', 'banana']

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)  # [19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True)
print(ages)  # [26, 25, 25, 24, 24, 24, 22, 19]

# sorted(): devuelve la lista ordenada sin modificar la lista original

# Ejemplo:
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))  # ['banana', 'lemon', 'mango', 'orange']
print(fruits) # ['banana', 'orange', 'mango', 'lemon']

# Orden inverso
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits, reverse=True)
print(fruits)  # ['orange', 'mango', 'lemon', 'banana']

