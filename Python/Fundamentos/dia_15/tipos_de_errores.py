"""
Tipos de Errores en Python
"""

"""
Cuando escribimos código, es común que cometamos un error tipográfico u otros errores comunes. Si nuestro código no se ejecuta, el
intérprete de Python mostrará un mensaje con información sobre dónde ocurre el problema y el tipo de error. A veces, también nos sugiere una
posible solución. Entender los diferentes tipos de errores en los lenguajes de programación nos ayudará a depurar nuestro código rápidamente
y nos hará mejores en lo que hacemos.
"""

"""
Veamos los tipos de errores más comunes uno por uno. Primero, abramos nuestro shell interactivo de Python. Ve a la terminal de tu
computadora y escribe 'python'. El shell interactivo de Python se abrirá.
"""

# SyntaxError

# Ejemplo 1: SyntaxError
"""
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
"""

# Como puedes ver, cometimos un error de sintaxis porque olvidamos encerrar la cadena con paréntesis, y Python ya sugiere la solución. Vamos a corregirlo.

print("hello world")  # hello world

# El error fue un SyntaxError. Después de la corrección, nuestro código se ejecutó sin problemas. Veamos más tipos de errores.

# NameError

# Ejemplo 1: NameError

"""
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
"""

# Como puedes ver en el mensaje anterior, el nombre age no está definido. Es cierto que no definimos una variable age, pero intentamos imprimirla como si lo hubiéramos hecho. Ahora, vamos a corregir esto declarando la variable y asignándole un valor.

age = 25
print(age)  # 25

# El tipo de error fue un NameError. Depuramos el error definiendo el nombre de la va

# IndexError

# Ejemplo 1: IndexError

"""
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
"""

# En el ejemplo anterior, Python levantó un IndexError porque la lista solo tiene índices del 0 al 4, por lo tanto, el índice estaba fuera de rango.

# ModuleNotFoundError

# Ejemplo 1: ModuleNotFoundError

"""
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
"""

# En el ejemplo anterior, agregué una 's' extra a math intencionadamente, y se levantó un ModuleNotFoundError. Vamos a corregirlo eliminando la 's' extra de math.

import math

# Corregimos el error, así que ahora podemos usar algunas funciones del módulo math.

# AttributeError

# Ejemplo 1: AttributeError

"""
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'
"""

# Como puedes ver, cometí otro error. En lugar de pi, intenté llamar a la función PI del módulo math. Esto levantó un AttributeError, lo que significa que la función no existe en el módulo. Vamos a corregirlo cambiando de PI a pi.

print(math.pi)  # 3.141592653589793

# Ahora, al llamar a pi desde el módulo math, obtuvimos el resultado correcto.

# KeyError

# Ejemplo 1: KeyError

"""
>>> users = {'name': 'Asab', 'age': 250, 'country': 'Finland'}
>>> users['name']
'Asab'
>>> users['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
"""

# Como puedes ver, hubo un error tipográfico en la clave utilizada para obtener el valor del diccionario, lo que resultó en un KeyError. La corrección es bastante sencilla. ¡Vamos a hacerlo!
"""
>>> users['country']
'Finland'
"""

# Depuramos el error, nuestro código se ejecutó y obtuvimos el valor esperado.

# TypeError

# Ejemplo 1: TypeError

"""
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

# En el ejemplo anterior, se levantó un TypeError porque no podemos sumar un número a una cadena. La primera solución sería convertir la cadena a int o float. Otra solución sería convertir el número a cadena (el resultado entonces sería '43'). Sigamos la primera corrección.

"""
>>> 4 + int('3')
7
>>> 4 + float('3')
7.0
"""

# El error fue eliminado y obtuvimos el resultado esperado.

# ImportError

# Ejemplo 1: ImportError

"""
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math'
"""

# No hay una función llamada power en el módulo math, se llama con un nombre diferente: pow. Corregimos el error.

from math import pow

print(pow(2, 3))  # 8.0

# ValueError

"""
>>> int('12a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '12a'
"""

# En este caso, no podemos convertir la cadena dada a un número, debido a la letra 'a' en ella.

#ZeroDivisionError

"""
>>> 1 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
"""

#No podemos dividir un número por cero.

"""
Hemos cubierto algunos de los tipos de errores en Python. Si deseas saber más, consulta la documentación oficial de Python sobre los tipos
de errores. Si aprendes a leer y entender estos errores, podrás depurar tus errores más rápido y convertirte en un mejor programador.
"""