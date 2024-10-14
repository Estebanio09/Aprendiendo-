                    ########    Diccionarios     ##########

#Un diccionario es una colección de datos emparejados (clave: valor) desordenada y modificable (mutable).

#### Creación de un diccionario
#Para crear un diccionario, utilizamos llaves {} o la función incorporada dict().

# Sintaxis
empty_dict = {}
# Diccionario con valores
dct = {'clave1':'valor1', 'clave2':'valor2', 'clave3':'valor3', 'clave4':'valor4'}

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finlandia',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Calle Espacial',
        'zipcode':'02210'
    }
}

#El diccionario anterior muestra que un valor puede ser de cualquier tipo de datos: cadena de texto, booleano, lista, tupla, conjunto o incluso otro diccionario.

#Las claves de los diccionarios pueden ser enteros o 

#####   Longitud del diccionario
#Verifica el número de pares 'clave: valor' en el diccionario.

# Sintaxis
dct = {'clave1':'valor1', 'clave2':'valor2', 'clave3':'valor3', 'clave4':'valor4'}
print(len(dct)) # 4

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finlandia',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Calle Espacial',
        'zipcode':'02210'
    }
}
print(len(person)) # 7

####    #####  Acceder a elementos del diccionario
#Podemos acceder a los elementos del diccionario haciendo referencia al nombre de la clave.

# Sintaxis
dct = {'clave1':'valor1', 'clave2':'valor2', 'clave3':'valor3', 'clave4':'valor4'}
print(dct['clave1']) # valor1
print(dct['clave4']) # valor4

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finlandia',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Calle Espacial',
        'zipcode':'02210'
    }
}
print(person['first_name'])  # Asabeneh
print(person['country'])     # Finlandia
print(person['skills'])      # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])   # JavaScript
print(person['address']['street']) # Calle Espacial
# print(person['city'])        # KeyError: 'city'

#Acceder a un elemento mediante el nombre de la clave genera un error si la clave no existe. Para evitar este error, primero debemos comprobar si una clave existe o podemos utilizar el método get()/conseguir. El método get devuelve None si la clave no existe.

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finlandia',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Calle Espacial',
        'zipcode':'02210'
    }
}

print(person.get('first_name'))  # Asabeneh
print(person.get('country'))     # Finlandia
print(person.get('skills'))      # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))        # None

######                  Añadir elementos a un diccionario

# Podemos añadir nuevos pares clave-valor a un diccionario.

# Sintaxis
dct = {'clave1':'valor1', 'clave2':'valor2', 'clave3':'valor3', 'clave4':'valor4'}
dct['clave5'] = 'valor5'

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finlandia',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Calle Espacial',
        'zipcode':'02210'
    }
}
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person) 
"""
{
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250, 
    'country': 'Finlandia', 
    'is_married': True, 
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python', 'HTML'], 
    'address': {
        'street': 'Calle Espacial', 
        'zipcode': '02210'
    }, 
    'job_title': 'Instructor'
}
"""

#                    ##     Modificación de elementos en un diccionario

#Podemos modificar elementos en un diccionario.

# Sintaxis
dct = {
    'clave1':'valor1', 
    'clave2':'valor2', 
    'clave3':'valor3', 
    'clave4':'valor4'
}

dct['clave1'] = 'valor-uno'

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finlandia',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Calle Espacial',
        'zipcode':'02210'
    }
}
person['first_name'] = 'Eyob'
person['age'] = 252
print(person) 
'''
{
'first_name': 'Eyob', 
'last_name': 'Yetayeh', 
'age': 252, 
'country': 'Finlandia', 
'is_married': True, 
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], 
'address': {
    'street': 'Calle Espacial', 
    'zipcode': '02210'
}
}
'''
#           #### Comprobación de claves en un diccionario

#Usamos el operador in para verificar si una clave existe en un diccionario.

# Sintaxis
dct = {'clave1':'valor1', 'clave2':'valor2', 'clave3':'valor3', 'clave4':'valor4'}
print('clave2' in dct)  # True
print('clave5' in dct)  # False

#               ##### Eliminar pares de clave y valor de un diccionario
'''
pop(key): Elimina el elemento con el nombre de clave especificado.
popitem(): Elimina el último elemento.
del: Elimina un elemento con el nombre de clave especificado.
'''

# Sintaxis
dct = {'clave1':'valor1', 'clave2':'valor2', 'clave3':'valor3', 'clave4':'valor4'}
dct.pop('clave1')  # Elimina el elemento 'clave1'
dct.popitem()      # Elimina el último elemento
del dct['clave2']  # Elimina el elemento 'clave2'
print(dct) # {'clave3': 'valor3'}

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finlandia',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Calle Espacial',
        'zipcode':'02210'
    }
}
person.pop('first_name')  # Elimina el elemento 'first_name'
person.popitem()          # Elimina el último elemento (address)
del person['is_married']  # Elimina el elemento 'is_married'

print(person) # {'last_name': 'Yetayeh', 'age': 250, 'country': 'Finlandia', 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']}

#               ## Cambiar un diccionario a una lista de elementos
#El método items() convierte el diccionario en una lista de tuplas.

# Sintaxis
dct = {'clave1':'valor1', 'clave2':'valor2', 'clave3':'valor3', 'clave4':'valor4'}
print(dct.items())  # dict_items([('clave1', 'valor1'), ('clave2', 'valor2'), ('clave3', 'valor3'), ('clave4', 'valor4')])

#               #####    Limpiar un diccionario
#Si no queremos los elementos en un diccionario, podemos limpiarlos usando el método clear().

# Sintaxis
dct = {'clave1':'valor1', 'clave2':'valor2', 'clave3':'valor3', 'clave4':'valor4'}
dct.clear()  # Vacía el diccionario
print(dct) # {}

#                   Eliminar un diccionario
#Si no vamos a usar el diccionario, podemos eliminarlo completamente con del.

# Sintaxis
dct = {'clave1':'valor1', 'clave2':'valor2', 'clave3':'valor3', 'clave4':'valor4'}
del dct

#                   Copiar un diccionario
#Podemos copiar un diccionario usando el método copy(). Esto nos ayuda a evitar la mutación del diccionario original.

# Sintaxis
dct = {'clave1':'valor1', 'clave2':'valor2', 'clave3':'valor3', 'clave4':'valor4'}
dct_copy = dct.copy()  # {'clave1':'valor1', 'clave2':'valor2', 'clave3':'valor3', 'clave4':'valor4'}

#                   Obtener las claves del diccionario como una lista
#El método keys() nos da todas las claves de un diccionario como una lista.

# Sintaxis
dct = {'clave1':'valor1', 'clave2':'valor2', 'clave3':'valor3', 'clave4':'valor4'}
claves = dct.keys()
print(claves)  # dict_keys(['clave1', 'clave2', 'clave3', 'clave4'])
print(type(claves))  #class 'dict_keys'

#                   Obtener los valores del diccionario como una lista

#El método values() nos da todos los valores de un diccionario como una lista.

# Sintaxis
dct = {'clave1':'valor1', 'clave2':'valor2', 'clave3':'valor3', 'clave4':'valor4'}
valores = dct.values()
print(valores)  # dict_values(['valor1', 'valor2', 'valor3', 'valor4'])
print(type(dct)) # class 'dict'

##### El método fromkeys() en Python se utiliza para crear un nuevo diccionario a partir de una secuencia de claves, asignando a todas ellas el mismo valor.

#   dict.fromkeys(keys, value)

#keys: es una secuencia que contiene las claves para el nuevo diccionario (puede ser una lista, tupla, etc.).
#value: es el valor que se asignará a todas las claves. Si no se especifica, el valor por defecto será None.

#Crear un diccionario con claves y un mismo valor:
keys = ['name', 'age', 'country']
value = 'unknown'
new_dict = dict.fromkeys(keys, value)
print(new_dict) # {'name': 'unknown', 'age': 'unknown', 'country': 'unknown'}

'''
¿Cuándo utilizar fromkeys()?
Es útil cuando necesitas crear un diccionario donde muchas claves tendrán el mismo valor inicial o valor por defecto.
'''
 