####             Tuplas               ####
"""
Una tupla es una colección de diferentes tipos de datos que es ordenada e inmutable. Las tuplas se escriben con paréntesis, (). Una vez que una tupla es creada, no se pueden cambiar sus valores. No se pueden utilizar los métodos add, insert o remove en una tupla porque no es modificable (mutable). A diferencia de las listas, las tuplas tienen pocos métodos. Métodos relacionados con las tuplas:
"""

'''
tuple(): para crear una tupla vacía.
count(): para contar el número de veces que un elemento especificado aparece en una tupla.
index(): para encontrar el índice de un elemento especificado en una tupla.
Operador: para unir dos o más tuplas y crear una nueva tupla.
'''

####  Creación de una tupla
# Tupla vacía: Creando una tupla vacía

# Sintaxis
empty_tuple = ()
# o usando el constructor de tuple
empty_tuple = tuple()

# Tupla con valores iniciales:

# Sintaxis

tpl = ('elemento1', 'elemento2', 'elemento3')
fruits = ('banana', 'naranja', 'mango', 'limón')

#### Longitud de una tupla
#Usamos el método len() para obtener la longitud de una tupla.

# Sintaxis
'''
tpl = ('elemento1', 'elemento2', 'elemento3')
print(len(tpl)) #3
'''

#### Accediendo a elementos de una tupla

#Indexación positiva
#Similar al tipo de dato lista, usamos indexación positiva o negativa para acceder a los elementos de una tupla.

# Sintaxis
'''
tpl = ('elemento1', 'elemento2', 'elemento3')
primer_elemento = tpl[0]
segundo_elemento = tpl[1]
'''
frutas = ('banana', 'naranja', 'mango', 'limón')
primera_fruta = frutas[0]
segunda_fruta = frutas[1]
ultimo_indice = len(frutas) - 1
ultima_fruta = frutas[ultimo_indice]

#Indexación negativa
#La indexación negativa significa comenzar desde el final. -1 se refiere al último elemento, -2 al penúltimo y el negativo de la longitud de la lista/tupla se refiere al primer elemento.

# Sintaxis
'''
tpl_2 = ('elemento1', 'elemento2', 'elemento3', 'elemento4')
primer_elemento = tpl_2[-4]
segundo_elemento = tpl_2[-3]
'''
frutas = ('banana', 'naranja', 'mango', 'limón')
primera_fruta = frutas[-4]
segunda_fruta = frutas[-3]
ultima_fruta = frutas[-1]

####  Cortar (slicing) tuplas
#Podemos cortar una sub-tupla especificando un rango de índices donde empezar y dónde terminar en la tupla. El valor de retorno será una nueva tupla con los elementos especificados.

# Sintaxis
'''
tpl = ('elemento1', 'elemento2', 'elemento3', 'elemento4')
todos_los_elementos = tpl[0:4]    # todos los elementos
todos_los_elementos = tpl[0:]     # todos los elementos
elementos_medios = tpl[1:3]       # no incluye el elemento en el índice 3
'''
frutas = ('banana', 'naranja', 'mango', 'limón')
todas_las_frutas = frutas[0:4]    # todos los elementos
todas_las_frutas = frutas[0:]     # todos los elementos
naranja_mango = frutas[1:3]       # no incluye el elemento en el índice 3
naranja_hasta_el_resto = frutas[1:]

# Sintaxis
tpl = ('elemento1', 'elemento2', 'elemento3', 'elemento4')
todos_los_elementos = tpl[-4:]         # todos los elementos
elementos_medios = tpl[-3:-1]          # no incluye el elemento en el índice -1
frutas = ('banana', 'naranja', 'mango', 'limón')
todas_las_frutas = frutas[-4:]         # todos los elementos
naranja_mango = frutas[-3:-1]          # no incluye el elemento en el índice -1
naranja_hasta_el_resto = frutas[-3:]

#### Cambiando tuplas a listas
# Podemos convertir tuplas en listas y viceversa. Las tuplas son inmutables, así que si queremos modificarlas, primero debemos convertirlas en una lista.

# Sintaxis
'''
tpl = ('elemento1', 'elemento2', 'elemento3', 'elemento4')
lst = list(tpl)
'''

frutas = ('banana', 'naranja', 'mango', 'limón')
frutas = list(frutas)
frutas[0] = 'manzana'
print(frutas)     # ['manzana', 'naranja', 'mango', 'limón']
frutas = tuple(frutas)
print(frutas)     # ('manzana', 'naranja', 'mango', 'limón')

#### Verificar un elemento en una tupla
# Podemos verificar si un elemento existe en una tupla utilizando in. Retorna un valor booleano.

# Sintaxis
'''
tpl = ('elemento1', 'elemento2', 'elemento3', 'elemento4')
print('elemento2' in tpl) # True
'''

frutas = ('banana', 'naranja', 'mango', 'limón')
print('naranja' in frutas) # True
print('manzana' in frutas) # False
#frutas[0] = 'manzana'  # TypeError: el objeto 'tuple' no soporta la asignación de elementos

#### Uniendo tuplas
# Podemos unir dos o más tuplas utilizando el operador +.

# Sintaxis
tpl1 = ('elemento1', 'elemento2', 'elemento3')
tpl2 = ('elemento4', 'elemento5', 'elemento6')
tpl3 = tpl1 + tpl2
frutas = ('banana', 'naranja', 'mango', 'limón')
vegetales = ('Tomate', 'Papa', 'Repollo', 'Cebolla', 'Zanahoria')
frutas_y_vegetales = frutas + vegetales
print(frutas_y_vegetales) #  ('banana', 'naranja', 'mango', 'limón', 'Tomate', 'Papa', 'Repollo', 'Cebolla', 'Zanahoria')

#### Eliminando tuplas
#No es posible eliminar un solo elemento de una tupla, pero sí es posible eliminar toda la tupla utilizando del.

# Sintaxis
tpl1 = ('elemento1', 'elemento2', 'elemento3')
del tpl1
frutas = ('banana', 'naranja', 'mango', 'limón')
del frutas
