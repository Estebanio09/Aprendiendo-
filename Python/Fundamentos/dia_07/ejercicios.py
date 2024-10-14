# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Ejercicios: Nivel 1

#Encuentra la longitud del conjunto it_companies.

print(len(it_companies)) #7

#Añade 'Twitter' a it_companies.

it_companies.add('Twitter')
print(it_companies) #{'IBM', 'Amazon', 'Oracle', 'Google', 'Microsoft', 'Facebook', 'Apple', 'Twitter'}

#Inserta varias empresas de TI a la vez en el conjunto it_companies.

it_companies.update(['Spotify', 'Meta', 'SpaceX', 'Dell', 'Activision'])
print(it_companies) #{'Dell', 'IBM', 'Microsoft', 'Twitter', 'Oracle', 'Google', 'SpaceX', 'Meta', 'Apple', 'Amazon', 'Activision', 'Facebook', 'Spotify'}

#Elimina una de las empresas del conjunto it_companies.
it_companies.discard('Dell')
print(it_companies) #{'Oracle', 'SpaceX', 'Microsoft', 'Apple', 'Google', 'IBM', 'Amazon', 'Facebook', 'Spotify', 'Activision', 'Meta', 'Twitter'}

#¿Cuál es la diferencia entre remove y discard?

#remove elimina el elemento pero si no se encuentra va a generar un error en el caso de discard elimina y si no esta no genera error 

#Ejercicios: Nivel 2

#Une los conjuntos A y B.

C = A.union(B)
print(C) # {19, 20, 22, 24, 25, 26, 27, 28}

#Encuentra la intersección entre A y B.

interseccion_sets = A.intersection(B)
print(interseccion_sets) # {19, 20, 22, 24, 25, 26}

#¿Es A un subconjunto de B?

print(A.issubset(B)) #True

#¿Son A y B conjuntos disjuntos?

print(A.isdisjoint(B)) #False

#Une A con B y luego B con A.

A.update(B)
B.update(A) 

print(A) #{19, 20, 22, 24, 25, 26, 27, 28}
print(B) #{19, 20, 22, 24, 25, 26, 27, 28}

#¿Cuál es la diferencia simétrica entre A y B?

diferencia = A.symmetric_difference(B)
print(diferencia) #set()

#Elimina los conjuntos por completo.

del A
del B 

#Ejercicios: Nivel 3

#Convierte las edades a un conjunto y compara la longitud de la lista con la del conjunto, ¿cuál es mayor?

ages_set = set(age)
print(ages_set) #{19, 22, 24, 25, 26}
print(len(age)) #8
print(len(ages_set)) #5

#Explica la diferencia entre los siguientes tipos de datos: cadena de texto (string), lista, tupla y conjunto.

#Son estructuras de datos, pero en el caso de las cadenas solo son texto plano, en el caso de las listas es un grupo de diferentes tipos de datos, la cual es ordenada, las túpalas es un grupo de datos ordenados, los cuales son inmutables después de que se define y un conjunto es una estructura que almacena datos la cual es desordenada y solo almacena una vez un mismo dato. 

prayer_set = set('Soy un profesor y me encanta inspirar y enseñar a las personas. ¿Cuántas palabras únicas se han usado en la oración? Utiliza el método split y un conjunto para obtener las palabras únicas'.split())

print(len(prayer_set)) #27


"""
Soy un profesor y me encanta inspirar y enseñar a las personas. ¿Cuántas palabras únicas se han usado en la oración? Utiliza el método split y un conjunto para obtener las palabras únicas.
"""