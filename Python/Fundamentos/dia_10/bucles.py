##### Bucles

'''
La vida está llena de rutinas. En programación también realizamos muchas tareas repetitivas. Para manejar estas tareas repetitivas, los
lenguajes de programación utilizan bucles. El lenguaje de programación Python proporciona dos tipos de bucles:

Bucle while
Bucle for
'''

#           ####    Bucle while
'''
Usamos la palabra reservada while para crear un bucle while. Se utiliza para ejecutar repetidamente un bloque de instrucciones hasta que se
cumpla una condición dada. Cuando la condición se vuelve falsa, las líneas de código después del bucle continuarán ejecutándose.
'''
"""
while condición:
    el código va aquí
"""
count = 0
while count < 5:
    print(count)
    count = count + 1

#Este código imprime de 0 a 4.

'''
En el bucle while anterior, la condición se vuelve falsa cuando count es 5. Es entonces cuando el bucle se detiene. Si estamos interesados en ejecutar un bloque de código una vez que la condición ya no sea verdadera, podemos usar else.
'''
#   Sintaxis con else

'''
while condición:
    el código va aquí
else:
    el código va aquí
'''

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
#En este ejemplo, el bucle while se detiene cuando count es 5, y la ejecución continúa con la declaración else. Como resultado, se imprimirá 5.

#           ####    Break y Continue - Parte 1

#Break: Usamos break cuando queremos salir o detener el bucle.

#Sintaxis de break

'''
while condición:
    el código va aquí
    if otra_condición:
        break

'''

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
#Este bucle while solo imprime 0, 1 y 2, pero cuando llega a 3, se detiene.

#Continue: Con la instrucción continue podemos saltar la iteración actual y continuar con la siguiente.

#Sintaxis de continue
'''
while condición:
    el código va aquí
    if otra_condición:
        continue

'''

count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1
#Este bucle while imprime solo 0, 1, 2 y 4 (se salta el 3).


#           ####    Bucle for
'''
La palabra clave for se utiliza para hacer un bucle for, similar a otros lenguajes de programación, pero con algunas diferencias en la 
sintaxis. El bucle se usa para iterar sobre una secuencia (que puede ser una lista, una tupla, un diccionario, un conjunto o una cadena).
'''

#Bucle for con listas

'''
for iterador en lista:
    el código va aquí
'''

números = [0, 1, 2, 3, 4, 5]
for número in números:  # número es un nombre temporal que se refiere a los elementos de la lista, válido solo dentro de este bucle
    print(número)       # los números se imprimirán línea por línea, de 0 a 5

#Bucle for con cadenas(Strings)
'''
for iterador en cadena:
    el código va aquí
'''

lenguaje = 'Python'
for letra in lenguaje:
    print(letra)

#También puedes usar el índice de la cadena:

for i in range(len(lenguaje)):
    print(lenguaje[i])

#range() en Python es una función que genera una secuencia de números enteros, comenzando desde un valor inicial hasta (pero sin incluir) un valor final. Se utiliza a menudo en bucles para iterar un número específico de veces.

'''
range(start, stop, step)
'''

'''
start (opcional): El número desde el que comienza la secuencia. Si no se especifica, por defecto es 0.
stop: El número en el que se detiene la secuencia (no se incluye en el rango).
step (opcional): La diferencia entre los números sucesivos de la secuencia. El valor predeterminado es 1.
'''
for i in range(5):
    print(i)
    
'''También se puede recorrer de la siguiente forma con la funcion enumerate que devuelve una tupla con el índice y el valor'''

numeros = [5,1,6,2,95,61,6,846,51,5,8,2,47,4,7,1,2,3,9,5,4,78,44,58,9,85]

for num in enumerate(numeros):
    indice, valor = num
    print(f'el indice {indice} es {valor}')

# Desempaquetado en el bucle 
for indice, valor in enumerate(numeros):
    print(f'el indice {indice} es {valor}')
    
    
    
#Bucle for con tuplas

'''
for iterador en tupla:
    el código va aquí
'''

números = (0, 1, 2, 3, 4, 5)
for número in números:
    print(número)

#Bucle for con diccionarios

#Al hacer un bucle sobre un diccionario, obtienes la clave del diccionario.

'''
for iterador en diccionario:
    el código va aquí
'''

persona = {
    'nombre': 'Asabeneh',
    'apellido': 'Yetayeh',
    'edad': 250,
    'país': 'Finlandia',
    'casado': True,
    'habilidades': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'dirección': {
        'calle': 'Calle Espacial',
        'código_postal': '02210'
    }
}
for clave in persona:
    print(clave)

#Si deseas imprimir tanto las claves como los valores, puedes hacer lo siguiente:

for clave, valor in persona.items():
    print(clave, valor)


#Bucles con conjuntos(Sets)

'''
for iterador en conjunto:
    el código va aquí
'''

empresas_tecnológicas = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for empresa in empresas_tecnológicas:
    print(empresa)

#           ####    Break y Continue - Parte 2

#Break: Usamos break cuando queremos detener el bucle antes de que se complete.

'''
for iterador en secuencia:
    el código va aquí
    if condición:
        break
'''

números = (0, 1, 2, 3, 4, 5)
print(type(números)) #class 'tuple'
for número in números:
    print(número)
    if número == 3:
        break

#En el ejemplo anterior, el bucle se detiene cuando llega al número 3.

#Continue: Usamos continue cuando queremos saltar algunos de los pasos en la iteración del bucle.

'''
for iterador en secuencia:
    el código va aquí
    if condición:
        continue
'''

números = (0, 1, 2, 3, 4, 5)
for número in números:
    print(número)
    if número == 3:
        continue
    print('El siguiente número debería ser', número + 1) if número != 5 else print('Fin del bucle')
print('fuera del bucle')

#En el ejemplo anterior, si el número es igual a 3, el paso después de la condición (pero dentro del bucle) se omite y la ejecución del bucle continúa si quedan más iteraciones.

#           #####   La Función range()

'''
La función range() se usa para generar una lista de números. El range(start, end, step) toma tres parámetros: inicio, fin e incremento. 
Por defecto, comienza en 0 y el incremento es 1. La secuencia generada con range necesita al menos 1 argumento (el fin).
'''

#Ejemplos de creación de secuencias usando range:

lst = list(range(11)) 
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

st = set(range(1, 11))  # Se indican el inicio y el fin de la secuencia, el paso es 1 por defecto
print(st)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0, 11, 2)) 
print(lst)  # [0, 2, 4, 6, 8, 10]

st = set(range(0, 11, 2)) 
print(st)  # {0, 2, 4, 6, 8, 10}

#Sintaxis del for con range:

'''
for iterador in range(inicio, fin, paso):
    # código aquí
'''

for número in range(11):
    print(número)  # imprime de 0 a 10, sin incluir el 11

#               ####    Bucle for anidado

#Podemos escribir bucles dentro de otro bucle.

'''
for x en y:
    for t en x:
        print(t)
'''

persona = {
    'nombre': 'Asabeneh',
    'apellido': 'Yetayeh',
    'edad': 250,
    'país': 'Finlandia',
    'casado': True,
    'habilidades': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'dirección': {
        'calle': 'Calle Espacial',
        'código_postal': '02210'
    }
}

for clave in persona:
    if clave == 'habilidades':
        for habilidad in persona['habilidades']:
            if habilidad == 'Node': # si habilidad es igual a 'Node'
                continue # omite el resto de codigo y continua con el bucle // no imprime 'Node' 
            print(habilidad)


#               ####       For con else

#Si queremos ejecutar algún mensaje cuando el bucle termine, usamos else.

'''
for iterador en range(inicio, fin, paso):
    hacer algo
else:
    print('El bucle terminó')
'''

for número in range(11):
    print(número)  # imprime de 0 a 10, sin incluir el 11
else:
    print('El bucle se detiene en', número)

#               ####    La declaración pass

#En Python, cuando se requiere una declaración (después de dos puntos :), pero no queremos ejecutar ningún código allí, podemos usar la palabra pass para evitar errores. También se puede usar como un marcador de posición para futuras declaraciones.

'''
for número en range(6):
    pass
'''