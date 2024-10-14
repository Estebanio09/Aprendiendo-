            ### Conjuntos (Sets)  ####

# Un conjunto es una colección de elementos. Permíteme llevarte de vuelta a tus lecciones de Matemáticas en la escuela primaria o secundaria. La definición matemática de un conjunto también se puede aplicar en Python. Un conjunto es una colección de elementos no ordenados y sin índice que son distintos entre sí. En Python, el conjunto se utiliza para almacenar elementos únicos, y es posible encontrar la unión, intersección, diferencia, diferencia simétrica, subconjunto, superconjunto y conjuntos disjuntos entre conjuntos.

#### Creación de un Conjunto
# Usamos la función incorporada set().

# Sintaxis
st = set()

#Crear un conjunto con elementos iniciales
# Sintaxis
st = {'item1', 'item2', 'item3', 'item4'}

fruits = {'banana', 'orange', 'mango', 'lemon'}

#### Obtener la longitud de un Conjunto
#Usamos el método len() para encontrar la longitud de un conjunto.

# Sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
print(len(st)) #4

fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits)) #4

'''
Acceder a elementos en un Conjunto
Usamos bucles para acceder a los elementos. Veremos esto en la sección de bucles.

Comprobar un elemento
Para verificar si un elemento existe en un conjunto, utilizamos el operador de pertenencia in.
'''
# Sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
print("¿El conjunto st contiene item3?", 'item3' in st)  # ¿El conjunto st contiene item3? True

fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits)  # True

#### Añadiendo Elementos a un Conjunto
#Una vez que un conjunto ha sido creado, no podemos cambiar sus elementos, pero podemos añadir elementos adicionales.

#Añadir un elemento utilizando add()

# Sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
print(st) # {'item5', 'item3', 'item1', 'item2', 'item4'} el orden es aleatorio porque los conjuntos no tienen un orden específico 

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits) # {'mango', 'orange', 'lime', 'lemon', 'banana'}  el orden es aleatorio porque los conjuntos no tienen un orden específico

#### Añadir varios elementos utilizando update()
# El método update() permite añadir varios elementos a un conjunto. update() toma una lista como argumento.

# Sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5', 'item6', 'item7'])
print(st) #{'item4', 'item6', 'item2', 'item5', 'item7', 'item1', 'item3'}

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
fruits.update(vegetables)
print(fruits) #{'cabbage', 'banana', 'mango', 'tomato', 'carrot', 'potato', 'onion', 'lemon', 'orange'} el orden es aleatorio porque los conjuntos no tienen un orden específico

#### Eliminando Elementos de un Conjunto
#Podemos eliminar un elemento de un conjunto utilizando el método remove(). Si el elemento no se encuentra, el método remove() lanzará un error, por lo que es recomendable verificar si el elemento existe en el conjunto dado. Sin embargo, el método discard() no genera errores si el elemento no se encuentra.

# Sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')

#El método pop() elimina un elemento aleatorio de la lista y devuelve el elemento eliminado.

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # elimina un elemento aleatorio del conjunto

#Si estamos interesados en el elemento eliminado:

fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()

#### Limpiar Elementos en un Conjunto
#Si queremos limpiar o vaciar el conjunto, utilizamos el método clear().

# Sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits)  # set()

#### Eliminar un Conjunto
#Si queremos eliminar el conjunto por completo, utilizamos el operador del. 

# Sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
del st

fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

#### Convertir Lista a Conjunto
#Podemos convertir una lista a un conjunto y un conjunto a una lista. Convertir una lista a conjunto elimina duplicados, reservando solo los elementos únicos.

# Sintaxis
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - el orden es aleatorio porque los conjuntos no tienen un orden específico

fruits = ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']
fruits = set(fruits)  # {'mango', 'lemon', 'banana', 'orange'} - el orden es aleatorio porque los conjuntos no tienen un orden específico

####  Unir Conjuntos
# Podemos unir dos conjuntos utilizando el método union() o update().

'''
Unión
Este método devuelve un nuevo conjunto.
'''

# Sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
st4 = st1 | st2

print(st4) #{'item1', 'item5', 'item2', 'item4', 'item6', 'item7', 'item3', 'item8'} - el orden es aleatorio porque los conjuntos no tienen un orden específico
print(st3) # {'item2', 'item5', 'item4', 'item3', 'item7', 'item8', 'item6', 'item1'} - el orden es aleatorio porque los conjuntos no tienen un orden específico

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
print(fruits.union(vegetables))  # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'} - el orden es aleatorio porque los conjuntos no tienen un orden específico

'''
Update
Este método inserta los elementos de un conjunto en otro conjunto dado
'''

# Sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2)  # el contenido de st2 se añade a st1

print(st1) # {'item1', 'item6', 'item8', 'item2', 'item3', 'item5', 'item4', 'item7'} - el orden es aleatorio porque los conjuntos no tienen un orden específico

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
fruits.update(vegetables)
print(fruits)  # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'} - el orden es aleatorio porque los conjuntos no tienen un orden específico

#### Encontrar Elementos de Intersección
#El método intersection() devuelve un conjunto de elementos que están en ambos conjuntos.

# Sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st3 = st1 & st2
print(st3) #{'item3', 'item2'}
st1.intersection(st2)  # {'item3', 'item2'}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers)  # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.intersection(dragon)  # {'o', 'n'}

####   Comprobando Subconjuntos y Superconjuntos
#Un conjunto puede ser un subconjunto o un superconjunto de otros conjuntos:

# Subconjunto: issubset()
# Superconjunto: issuperset()

### Subconjunto (Subset)
#Un conjunto A es un subconjunto de otro conjunto B si todos los elementos de A están contenidos en B. En otras palabras, A está "dentro" de B.
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
# Verificar si A es un subconjunto de B
print(A.issubset(B))  # True, porque todos los elementos de A están en B
print(A <= B) # True, porque todos los elementos de A están en B


### Superconjunto (Superset)
#Un conjunto B es un superconjunto de otro conjunto A si contiene todos los elementos de A. En otras palabras, B incluye a A.
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
# Verificar si B es un superconjunto de A
print(B.issuperset(A))  # True, porque todos los elementos de A están en B
print( B > A) # True, porque todos los elementos de A están en B

# Sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1)  # True
st1.issuperset(st2)  # True

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers)  # False, porque es un superconjunto
whole_numbers.issuperset(even_numbers)  # True

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.issubset(dragon)  # False

####  Comprobando la Diferencia entre Dos Conjuntos
#Devuelve la diferencia entre dos conjuntos difference() // Devuelve los elementos que no están en el otro conjunto 

# Sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1)  # set()
st1.difference(st2)  # {'item1', 'item4'} => st1\st2
print(st1 ^ st2) # {'item1', 'item4'}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers)  # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.difference(dragon)  # {'p', 'y', 't'}
dragon.difference(python)  # {'d', 'r', 'a', 'g'}

####   Encontrando la Diferencia Simétrica entre Dos Conjuntos
#Devuelve la diferencia simétrica entre dos conjuntos. Devuelve un conjunto que contiene todos los elementos de ambos conjuntos, excepto los que están en ambos. Matemáticamente: (A\B) ∪ (B\A)

# Sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# Significa (A\B) ∪ (B\A)
st2.symmetric_difference(st1)  # {'item1', 'item4'}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers)  # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}


#### Uniéndose a Conjuntos
#Si dos conjuntos no tienen ningún elemento en común, se llaman conjuntos disjuntos. Podemos verificar si dos conjuntos son disjuntos usando el método isdisjoint().

# Sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1)  # False

even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers)  # True, porque no hay elementos en común

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.isdisjoint(dragon)  # False, hay elementos comunes {'o', 'n'}


