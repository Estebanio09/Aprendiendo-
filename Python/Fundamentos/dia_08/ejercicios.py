# Ejercicios: Día 8

#Crea un diccionario vacío llamado dog.

dog = dict()
print(type(dog)) # class 'dict'

#Añade name, color, breed, legs, age al diccionario dog.

dog['name'] = 'Nube'
dog['color'] = 'White'
dog['breed'] = 'False'
dog['legs'] = 4
dog['age'] = 1
print(dog) # {'name': 'Nube', 'color': 'White', 'breed': 'False', 'legs': 4, 'age': 1}

#Crea un diccionario de estudiante y añade first_name, last_name, gender, age, marital_status, skills, country, city, y address como claves del diccionario.

estudiante = {
    'first_name' : 'Esteban',
    'last_name' : 'Martinez',
    'gender' : 'Masculino',
    'age' : 25,
    'material_status' : 'soltero',
    'skills' : ['Python', 'Javascript', 'HTML', 'CSS', 'React'],
    'country' : 'Colombia',
    'city' : 'Bogotá',
    'address' : {
        'calle' : '57c',
        'numero' : '77k - 20'
    }
}

#Obtén la longitud del diccionario de estudiant

print(estudiante)

#Obtén el valor de skills y verifica el tipo de dato, debe ser una lista.

print(estudiante['skills']) # ['Python', 'Javascript', 'HTML', 'CSS', 'React']
print(type(estudiante['skills'])) # class 'list'

#Modifica los valores de skills añadiendo una o dos habilidades

estudiante['skills'] = estudiante['skills'] + ['SQL', 'Node js']
estudiante['skills'].append('GIT')
print(estudiante) #{'first_name': 'Esteban', 'last_name': 'Martinez', 'gender': 'Masculino', 'age': 25, 'material_status': 'soltero', 'skills': ['Python', 'Javascript', 'HTML', 'CSS', 'React', 'SQL', 'Node js', 'GIT'], 'country': 'Colombia', 'city': 'Bogotá', 'address': {'calle': '57c', 'numero': '77k - 20'}}

#Obtén las claves del diccionario como una lista.

list_keys = list(estudiante.keys())
print(list_keys) #['first_name', 'last_name', 'gender', 'age', 'material_status', 'skills', 'country', 'city', 'address']

#Obtén los valores del diccionario como una lista.

list_values = list(estudiante.values())
print(list_values) #['Esteban', 'Martinez', 'Masculino', 25, 'soltero', ['Python', 'Javascript', 'HTML', 'CSS', 'React', 'SQL', 'Node js', 'GIT'], 'Colombia', 'Bogotá', {'calle': '57c', 'numero': '77k - 20'}

#Convierte el diccionario a una lista de tuplas usando el método items().

list_tuples = list(estudiante.items())
print(list_tuples) #[('first_name', 'Esteban'), ('last_name', 'Martinez'), ('gender', 'Masculino'), ('age', 25), ('material_status', 'soltero'), ('skills', ['Python', 'Javascript', 'HTML', 'CSS', 'React', 'SQL', 'Node js', 'GIT']), ('country', 'Colombia'), ('city', 'Bogotá'), ('address', {'calle': '57c', 'numero': '77k - 20'})]

#Elimina uno de los elementos del diccionario.

del estudiante['material_status']
print(estudiante) #{'first_name': 'Esteban', 'last_name': 'Martinez', 'gender': 'Masculino', 'age': 25, 'skills': ['Python', 'Javascript', 'HTML', 'CSS', 'React', 'SQL', 'Node js', 'GIT'], 'country': 'Colombia', 'city': 'Bogotá', 'address': {'calle': '57c', 'numero': '77k - 20'}}

#Elimina uno de los diccionarios.

del estudiante