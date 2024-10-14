#Crea una tupla vacía.

new_tuple = ()

#Crea una tupla que contenga los nombres de tus hermanas y hermanos (hermanos imaginarios están bien).

primos = ('Juan', 'Andres', 'Arturo', 'Ivan')
primas = ('Sara', 'Evelyn', 'Gabriela', 'Zabdy')

#Une las tuplas de hermanos y hermanas y asígnala a la variable siblings.

primates_jsjsjs = primas + primos 
print(primates_jsjsjs) # ('Sara', 'Evelyn', 'Gabriela', 'Zabdy', 'Juan', 'Andres', 'Arturo', 'Ivan')

#¿Cuántos hermanos tienes?

print(len(primates_jsjsjs))

# Modifica la tupla siblings y añade el nombre de tu padre y madre, y asígnala a la variable family_members.

family_members = list(primates_jsjsjs)
family_members.append('Astrid')
family_members.append('Camilo')
print(family_members) #['Sara', 'Evelyn', 'Gabriela', 'Zabdy', 'Juan', 'Andres', 'Arturo', 'Ivan', 'Astrid', 'Camilo']
family_members = tuple(family_members)
print(family_members) #('Sara', 'Evelyn', 'Gabriela', 'Zabdy', 'Juan', 'Andres', 'Arturo', 'Ivan', 'Astrid', 'Camilo')

#Desempaqueta los hermanos y padres de la tupla family_members.

a, b, c, d, e, f, g, *restantes = family_members
print(a, b, c, d, e, f, g )# Sara Evelyn Gabriela Zabdy Juan Andres Arturo0
print(restantes) # ['Ivan', 'Astrid', 'Camilo']

#Crea tuplas de frutas, verduras y productos de origen animal. Une las tres tuplas y asígnalas a una variable llamada food_stuff_tp.

frutas = ('manzana', 'banano', 'pera', 'kiwi')
verduras = ('tomate', 'cebolla', 'apio', 'zanahoria')
food_stuff_tp = frutas + verduras
print(food_stuff_tp) #('manzana', 'banano', 'pera', 'kiwi', 'tomate', 'cebolla', 'apio', 'zanahoria')

#Cambia la tupla food_stuff_tp a una lista food_stuff_lt.

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt) #['manzana', 'banano', 'pera', 'kiwi', 'tomate', 'cebolla', 'apio', 'zanahoria']

#Extrae los elementos del medio de la tupla food_stuff_tp o de la lista food_stuff_lt.

food_stuff_lt.pop(len(food_stuff_lt) // 2,)
print(food_stuff_lt) #['manzana', 'banano', 'pera', 'kiwi', 'cebolla', 'apio', 'zanahoria']

#Extrae los primeros tres y los últimos tres elementos de la lista food_stuff_lt.

primera_rebanada = food_stuff_lt[0:3]
print(primera_rebanada) #['manzana', 'banano', 'pera']
ultima_rebanada = food_stuff_lt[-3:]
print(ultima_rebanada) #['cebolla', 'apio', 'zanahoria']
print(food_stuff_lt)

#Elimina completamente la tupla food_stuff_tp.

del food_stuff_tp

'''
Verifica si un elemento existe en una tupla:
Verifica si 'Estonia' es un país nórdico.
Verifica si 'Islandia' es un país nórdico.
'''

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries) #False
print('Iceland' in nordic_countries) #True


