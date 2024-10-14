#Obtén la edad del usuario usando input("Ingresa tu edad: "). Si el usuario tiene 18 años o más, dale la retroalimentación: "Tienes la edad suficiente para conducir". Si es menor de 18, dile cuántos años le faltan para poder conducir.

#Ejemplo de salida:
'''
Ingresa tu edad: 30
Tienes la edad suficiente para aprender a conducir.
Ingresa tu edad: 15
Te faltan 3 años para poder aprender a conducir.
'''

#edad = int(input('Ingresa tu edad ')) 

'''
if edad >= 18: 
    print('Tienes la edad suficiente para aprender a conducir.')
else:
    print(f'Te faltan {18 - edad} años para aprender a conducir')
'''

#Compara los valores de mi_edad y tu_edad usando if ... else. ¿Quién es mayor (yo o tú)? Usa input("Ingresa tu edad: ") para obtener la edad como entrada. Puedes usar una condición anidada para imprimir 'año' si la diferencia es de un año, 'años' si es mayor y un texto personalizado si mi_edad = tu_edad.

#Ejemplo de salida:

'''
Ingresa tu edad: 30
Tienes 5 años más que yo.
'''

'''
mi_edad = 25

if mi_edad > edad:
    if mi_edad - edad == 1:
        print('Tienes un año menos que yo')
    else:
        print(f'Tienes {mi_edad - edad} años menos que yo')
elif mi_edad < edad:
    if edad - mi_edad == 1:
        print('Tienes un año mas que yo')
    else:
        print(f'Tienes {edad - mi_edad} años más que yo')
else:
    print('Tenemos la misma edad')

'''

#Obtén dos números del usuario usando input(). Si a es mayor que b, imprime "a es mayor que b". Si a es menor que b, imprime "a es menor que b". De lo contrario, imprime "a es igual a b".

'''
a = int(input('Ingresa el numero a '))
b = int(input('Ingresa el numero b '))

if a > b:
    print('a es mayor que b')
elif b > a:
    print('b es mayor que a')
else:
    print('a es igual a b')
'''

'''
Escribe un código que asigne calificaciones a los estudiantes según sus puntuaciones:

90-100, A
70-89, B
60-69, C
50-59, D
0-49, F
'''

'''
calificacion = int(input('Ingresa la calificación '))

if calificacion < 50:
    print('Tu nota es F')
elif calificacion < 60:
    print('Tu nota es D')
elif calificacion < 70:
    print('Tu nota es C')
elif calificacion < 90:
    print('Tu nota es B')
else:
    print('Tu nota es A')
'''

"""
Verifica si la estación es otoño, invierno, primavera o verano. Si el usuario introduce:

Septiembre, octubre o noviembre, la estación es otoño.
Diciembre, enero o febrero, la estación es invierno.
Marzo, abril o mayo, la estación es primavera.
Junio, julio o agosto, la estación es verano.
"""

"""
estacion = input('Ingresa el mes a validar ').capitalize()

if estacion in ['Septiembre', 'Octubre', 'Noviembre']:
    print('Es Otoño')
elif estacion in ['Diciembre', 'Enero', 'Febrero']:
    print('Es Invierno')
elif estacion in ['Marzo', 'Abril', 'Mayo']:
    print('Es Primavera')
elif estacion in ['Junio', 'Julio', 'Agosto']:
    print('Es Verano')
else:
    print(f'{estacion} no es un mes valido o esta mal escrito')
"""

# La siguiente lista contiene algunas frutas:

frutas = ['banana', 'naranja', 'mango', 'limón']
"""
Si una fruta no está en la lista, añádela a la lista e imprime la lista modificada. Si la fruta ya existe, imprime: 'Esa fruta ya existe en la lista'.
"""

"""
select_user_fruta = input('Ingrese una fruta ').lower()

if select_user_fruta in frutas:
    print('Esa fruta ya existe en la lista')
else:
    frutas.append(select_user_fruta)
    print(frutas)
"""

persona = {
    'primer_nombre': 'Esteban',
    'apellido': 'Martinez',
    'edad': 25,
    'país': 'Colombia',
    'casado': False,
    'habilidades': ['JavaScript', 'React',  'MongoDB', 'Node',  'SQL', 'Veiu', 'Java', 'HTML'],
    'dirección': {
        'calle': 'Calle del Espacio',
        'código_postal': '02210'
    }
}

#Verifica si el diccionario de la persona tiene la clave habilidades. Si es así, imprime la habilidad del medio en la lista de habilidades.

if 'habilidades' in persona:
    if len(persona['habilidades']) % 2 == 0:
        print(persona['habilidades'][len(persona['habilidades']) // 2 - 1 ], persona['habilidades'][len(persona['habilidades']) // 2])
    else:
        print(persona['habilidades'][len(persona['habilidades']) // 2])

#Verifica si el diccionario de la persona tiene la clave habilidades. Si es así, verifica si la persona tiene la habilidad 'Python' e imprime el resultado.

if 'habilidades' in persona:
    if 'Python' in persona['habilidades']:
        print(f'Python esta en el indice {persona['habilidades'].index('Python')}')

#Si la persona tiene solo JavaScript y React en sus habilidades, imprime 'Es un desarrollador frontend'. Si la persona tiene Node, Python y MongoDB, imprime 'Es un desarrollador backend'. Si tiene React, Node y MongoDB, imprime 'Es un desarrollador fullstack'. Si no, imprime 'Título desconocido'. (Para resultados más precisos, se pueden anidar más condiciones).

if 'habilidades' in persona:
    if 'JavaScript' in persona['habilidades'] and 'React' in persona['habilidades'] and not ('Python' in persona['habilidades'] or 'Node' in persona['habilidades'] or 'MongoDB' in persona['habilidades']):
        print('Es un desarrollador frontend')
    elif 'Python' in persona['habilidades'] and 'Node' in persona['habilidades'] and 'MongoDB' in persona['habilidades']:
        print('Es un desarrollador backend')
    elif 'React' in persona['habilidades'] and 'Node' in persona['habilidades'] and 'MongoDB' in persona['habilidades']:
        print('Es un desarrollador fullstack')
    else:
        print('Título desconocido')