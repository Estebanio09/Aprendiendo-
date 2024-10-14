###Booleanos###
"""
Un tipo de dato booleano representa uno de dos valores: True o False. El uso de estos tipos de datos se aclarará una vez que comencemos a usar el operador de comparación. La primera letra T de True y F de False debe estar en mayúscula, a diferencia de JavaScript.
"""
print(True)
print(False)

print(bool(1)) #True
print(bool(-1)) #True
print(bool('Hola')) #True
print(bool(['Hola', 52])) #True
print(bool({'Hola', 52})) #True

print(bool('')) #False
print(bool(0)) #False
print(bool([])) #False
print(bool({})) #False
print(bool(None)) #False


###Operadores de Asignación###

a = 8 
b = 5

b += a   # 5 + 8
print(b) # b = 13
b -= a   # 13 - 8
print(b) # b = 5
b *= a   # 5 * 8
print(b) # b = 40
b /= 2   # 40 / 2
print(b) # b = 20.0 
b %= 3   # 20.0 / 3 % = 2.0 guarda el resto de la división en la variable b 
print(b) # b = 2.0
b = 50   # b = 50 
b //= 3  # 50 // 3 división entera 
print(b) # b = 16
b **= 3  # 16 * 16 * 16
print(b) # b = 4096

"""
Operadores Aritméticos:

Suma (+): a + b
Resta (-): a - b
Multiplicación (*): a * b
División (/): a / b
Módulo (%): a % b
División entera (//): a // b
Exponenciación (**): a ** b
"""

# Operaciones Aritméticas en Python
# Enteros

print('Suma: ', 1 + 2)        # 3
print('Resta: ', 2 - 1)       # 1
print('Multiplicación: ', 2 * 3)  # 6
print('División: ', 4 / 2)    # 2.0  La división en Python da un número flotante
print('División: ', 6 / 2)     # 3.0         
print('División: ', 7 / 2)     # 3.5
print('División sin el residuo: ', 7 // 2)   # 3, da sin el número flotante
print('División sin el residuo: ', 7 // 3)   # 2
print('Módulo: ', 3 % 2)       # 1, da el residuo
print('Exponenciación: ', 2 ** 3) # 8, significa 2 * 2 * 2

###Números Flotantes###

print('Número de Punto Flotante, PI:', 3.14)
print('Número de Punto Flotante, gravedad:', 9.81)

##Números complejos
# Números complejos
print('Número complejo: ', 1 + 1j)
print('Multiplicando números complejos: ', (1 + 1j) * (1 - 1j))

# Declaración de la variable al principio

a = 3  # a es el nombre de la variable y 3 es un tipo de dato entero
b = 2  # b es el nombre de la variable y 2 es un tipo de dato entero

# Operaciones aritméticas y asignando el resultado a una variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# Debería haber usado 'suma' en lugar de 'total', pero 'sum' es una función incorporada; trata de evitar sobrescribir funciones incorporadas

print(total) # si no etiquetas tu impresión con alguna cadena, nunca sabrás de dónde proviene el resultado
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

#Ejemplo
print('== Suma, Resta, Multiplicación, División, Módulo ==')

# Declarando valores y organizándolos juntos
num_one = 3
num_two = 4

# Operaciones aritméticas
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Imprimiendo valores con etiqueta
print('total: ', total)
print('diferencia: ', diff)
print('producto: ', product)
print('división: ', div)
print('residuo: ', remainder)

# Calculando el área de un círculo
radius = 10                                # radio de un círculo
area_of_circle = 3.14 * radius ** 2       # dos signos * significan exponente o potencia
print('Área de un círculo:', area_of_circle)

# Calculando el área de un rectángulo
length = 10
width = 20
area_of_rectangle = length * width
print('Área de rectángulo:', area_of_rectangle)

# Calculando el peso de un objeto
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Agregando unidad al peso

# Calculando la densidad de un líquido
mass = 75  # en Kg
volume = 0.075  # en metros cúbicos
density = mass / volume  # 1000 Kg/m^3

###Operadores de comparación###

print(3 > 2)     # True, porque 3 es mayor que 2
print(3 >= 2)    # True, porque 3 es mayor que 2
print(3 < 2)     # False, porque 3 es mayor que 2
print(2 < 3)     # True, porque 2 es menor que 3
print(2 <= 3)    # True, porque 2 es menor que 3
print(3 == 2)    # False, porque 3 no es igual a 2
print(3 != 2)    # True, porque 3 no es igual a 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

#Comparar algo devuelve ya sea True o False:

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

"""
Además de los operadores de comparación mencionados, Python utiliza:

        is      : Devuelve True si ambas variables son el mismo objeto (x is y)

        is not  : Devuelve True si ambas variables no son el mismo objeto (x is not y)

        in:     : Devuelve True si la lista consultada contiene un determinado elemento (x in y)

        not in  : Devuelve True si la lista consultada no tiene un determinado elemento (x not in y)

"""

print('1 is 1', 1 is 1)                   # True - porque los valores de datos son iguales
print('1 is not 2', 1 is not 2)           # True - porque 1 no es 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A se encuentra en la cadena
print('B in Asabeneh', 'B' in 'Asabeneh') # False - no hay B mayúscula
print('coding' in 'coding for all') # True - porque 'coding for all' tiene la palabra 'coding'
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

        ###Operadores logicos###

#El operador lógico and en Python se utiliza para evaluar dos o más expresiones lógicas. Retorna True si todas las expresiones son verdaderas; de lo contrario, retorna False.
#condición1 and condición2

a = 5
b = 10

# Ambos deben ser verdaderos
resultado = (a > 0) and (b > 5)  # True, porque ambas condiciones son verdaderas
print(resultado)  # Imprime: True

resultado = (a > 0) and (b < 5)  # False, porque la segunda condición es falsa
print(resultado)  # Imprime: False

#El operador lógico or en Python se utiliza para evaluar dos o más expresiones lógicas. Retorna True si al menos una de las expresiones es verdadera; solo retorna False si todas las expresiones son falsas.
#condición1 or condición2

a = 5
b = 10

# Solo una de las condiciones necesita ser verdadera
resultado = (a > 0) or (b < 5)  # True, porque la primera condición es verdadera
print(resultado)  # Imprime: True

resultado = (a < 0) or (b < 5)  # False, porque ambas condiciones son falsas
print(resultado)  # Imprime: False

#El operador lógico not en Python se utiliza para invertir el valor de una expresión lógica. Si la expresión es True, not la convierte en False, y si es False, la convierte en True.
#not condición

a = True
b = False

# Invertir el valor de la condición
resultado = not a  # False, porque 'a' es True
print(resultado)  # Imprime: False

resultado = not b  # True, porque 'b' es False
print(resultado)  # Imprime: True

##más ejemplos 

print(3 > 2 and 4 > 3) # True - porque ambas declaraciones son verdaderas
print(3 > 2 and 4 < 3) # False - porque la segunda declaración es falsa
print(3 < 2 and 4 < 3) # False - porque ambas declaraciones son falsas
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - porque ambas declaraciones son verdaderas
print(3 > 2 or 4 < 3)  # True - porque una de las declaraciones es verdadera
print(3 < 2 or 4 < 3)  # False - porque ambas declaraciones son falsas
print('True or False:', True or False)
print(not 3 > 2)     # False - porque 3 > 2 es verdadero, luego not True da False
print(not True)      # False - Negación, el operador not convierte verdadero en falso
print(not False)     # True
print(not not True)  # True
print(not not False) # False


