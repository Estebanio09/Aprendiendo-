###Cadenas de Texto (Strings)###


letter = "P"  # Una cadena puede ser un solo carácter o un conjunto de textos
print(letter)  # P
print(len(letter))  # 1
greeting = "Hola, Mundo!"  # Una cadena se puede crear usando comillas simples o dobles, "Hola, Mundo!"
print(greeting)  # Hola, Mundo!
print(len(greeting))  # 13
sentence = "Espero que estés disfrutando de los 30 días de Python"
print(sentence)

multiline_string = """Soy profesor y disfruto enseñar.
No encontré nada tan gratificante como empoderar a las personas.
Por eso creé los 30 días de Python."""
print(multiline_string)

# Otra forma de hacer lo mismo
multiline_string = """Soy profesor y disfruto enseñar.
No encontré nada tan gratificante como empoderar a las personas.
Por eso creé los 30 días de Python."""
print(multiline_string)

##Concatenación##

first_name = "Asabeneh"
last_name = "Yetayeh"
space = " "
full_name = first_name + space + last_name
print(full_name)  # Asabeneh Yetayeh

# si utilizamos las comas coloca automáticamente los espacios esto no es concatenación

txt = "Hola"
txt2 = "Mundo"
print(txt, txt2)  # Hola Mundo

new_txt = txt, txt2
print(new_txt)  # ('Hola', 'Mundo')
print(type(new_txt))  # class 'tuple'


# Verificando la longitud de una cadena usando la función integrada len()
print(len(first_name))  # 8
print(len(last_name))  # 7
print(len(first_name) > len(last_name))  # True
print(len(full_name))  # 16

##Secuencias de escape##

"""
En Python y otros lenguajes de programación, el símbolo \ seguido de un carácter es una secuencia de escape. Veamos los caracteres de escape más comunes:

\n: Nueva línea
\t: Tabulación (8 espacios)
\\: Barra invertida
\': Comilla simple (')
\": Comilla doble (")
"""

print(
    "Espero que todos estén disfrutando del desafío de Python.\n¿Estás?"
)  # Salto de línea
print("Días\tTemas\tEjercicios")  # Agregando un espacio de tabulación o 4 espacios
print("Día 1\t5\t5")
print("Día 2\t6\t20")
print("Día 3\t5\t23")
print("Día 4\t1\t35")
print("Este es un símbolo de barra invertida (\\)")  # Para escribir una barra invertida
print(
    'En cada lenguaje de programación comienza con "Hola, Mundo!"'
)  # Para escribir una comilla doble dentro de una comilla simple


###Formateo de cadenas###

# Solo cadenas:

first_name = "Asabeneh"
last_name = "Yetayeh"
language = "Python"
formated_string = "Soy %s %s. Enseño %s" % (first_name, last_name, language)
print(formated_string)

###Cadenas y números:

# Formateo de Cadenas al Estilo Antiguo (Operador %)

"""
%s: Cadena (o cualquier objeto con una representación de cadena, como números)
%d: Enteros
%f: Números de punto flotante
"%.número de dígitosf": Números de punto flotante con precisión fija
"""

radius = 10
pi = 3.14
area = pi * radius**2
formated_string = "El área de un círculo con un radio %d es %.2f." % (
    radius,
    area,
)  # 2 se refiere a los 2 dígitos significativos después del punto

python_libraries = ["Django", "Flask", "NumPy", "Matplotlib", "Pandas"]
formated_string = "Las siguientes son bibliotecas de Python: %s" % (python_libraries)
print(
    formated_string
)  # "Las siguientes son bibliotecas de Python:['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']"

# Formateo de Cadenas al Estilo Nuevo (str.format)

first_name = "Asabeneh"
last_name = "Yetayeh"
language = "Python"
formated_string = "Soy {} {}. Enseño {}".format(first_name, last_name, language)
print(formated_string)

a = 4
b = 3

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print(
    "{} / {} = {:.2f}".format(a, b, a / b)
)  # Limita a dos dígitos después del decimal
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a**b))

###Cadenas y números:

radius = 10
pi = 3.14
area = pi * radius**2
formated_string = "El área de un círculo con un radio {} es {:.3f}.".format(
    radius, area
)  # 3 dígitos después del decimal
print(formated_string)

###Interpolación de Cadenas / f-Strings (Python 3.6+)###

"""
Otro nuevo método de formateo de cadenas es la interpolación de cadenas, o f-strings. Las cadenas comienzan con f y podemos inyectar los datos en sus posiciones correspondientes.
"""

a = 4
b = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")  # limitamos los decimales a 2
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")


###Desempaquetado de Caracteres

language = "Python"
a, b, c, d, e, f = (
    language  # desempaquetando los caracteres de la secuencia en variables
)
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n


##Acceso a Caracteres en Cadenas por Índice

"""
En programación, la cuenta comienza desde cero. Por lo tanto, la primera letra de una cadena está en el índice cero y la última letra de una cadena está en la longitud de la cadena menos uno.
"""

# ['P', 'y', 't', 'h', 'o', 'n']
#   0    1    2    3    4    5    -->
#  -6   -5   -4   -3   -2   -1    <--

language = "Python"
first_letter = language[0]
print(first_letter)  # P
second_letter = language[1]
print(second_letter)  # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)  # n

# Si queremos comenzar desde el extremo derecho, podemos usar índices negativos. -1 es el último índice.

language = "Python"
last_letter = language[-1]
print(last_letter)  # n
second_last = language[-2]
print(second_last)  # o

###Cortando Cadenas en Python###

"""
En Python, podemos cortar cadenas en subcadenas.
"""

language = "Python"
first_three = language[
    0:3
]  # comienza en el índice cero y llega hasta 3, pero no incluye 3
print(first_three)  # Pyt
last_three = language[3:6]
print(last_three)  # hon
# Otra forma
last_three = language[-3:]
print(last_three)  # hon
last_three = language[3:]
print(last_three)  # hon

###Invirtiendo una Cadena

greeting = "¡Hola, Mundo!"
print(greeting[::-1])  # !odnuM ,aloH

# Omitiendo Caracteres Durante el Corte

language = "Python"
pto = language[0:6:2]  # salta de dos en dos   P  T  O
print(pto)  # Pto

######################### Métodos de Cadenas ###############################################

# capitalize(): Convierte el primer carácter de la cadena en mayúscula.
challenge = "treinta días de python"
print(challenge.capitalize())  # 'Treinta días de python'

# count(): Devuelve la cantidad de ocurrencias de una subcadena en la cadena.
# count(substring, start=.., end=..); start es un índice inicial para contar y end es el último índice a contar.

challenge = "treinta días de python"
print(challenge.count("y"))  # 1
print(challenge.count("í", 7, 14))  # 1
print(challenge.count("th"))  # 1

# endswith(): Comprueba si una cadena termina con un final especificado.

challenge = "treinta días de python"
print(challenge.endswith("on"))  # True
print(challenge.endswith("tion"))  # False

# expandtabs(): Reemplaza el carácter de tabulación por espacios; el tamaño de la tabulación predeterminado es 8. Toma como argumento el tamaño de la tabulación.

challenge = "treinta\tdías\tof\tpython"
print(challenge.expandtabs())  # 'treinta  días    de      python'
print(challenge.expandtabs(10))  # 'treinta    días      de        python'

# find(): Devuelve el índice de la primera ocurrencia de una subcadena; si no se encuentra, devuelve -1.

challenge = "treinta días de python"
print(challenge.find("y"))  # 17
print(challenge.find("th"))  # 18

# rfind(): Devuelve el índice de la última ocurrencia de una subcadena; si no se encuentra, devuelve -1.

challenge = "treinta días de python"
print(challenge.rfind("y"))  # 17
print(challenge.rfind("th"))  # 18

# format(): Formatea la cadena en una salida más agradable. Para más información sobre el formateo de cadenas, consulta este enlace.

first_name = "Asabeneh"
last_name = "Yetayeh"
age = 250
job = "profesor"
country = "Finlandia"
sentence = "Soy {} {}. Tengo {} años. Soy un {}. Vivo en {}.".format(
    first_name, last_name, age, job, country
)
print(
    sentence
)  # Soy Asabeneh Yetayeh. Tengo 250 años. Soy un profesor. Vivo en Finlandia.

radius = 10
pi = 3.14
area = pi * radius**2
result = "El área de un círculo con radio {} es {}".format(str(radius), str(area))
print(result)  # El área de un círculo con radio 10 es 314.0

# Metodos para cadenas

# index(): Devuelve el índice más bajo de una subcadena; los argumentos adicionales indican el índice inicial y final (por defecto, 0 y longitud de la cadena - 1). Si no se encuentra la subcadena, lanza un ValueError.

challenge = "treinta días de python"
sub_string = "dí"
print(challenge.index(sub_string))  # 8
# print(challenge.index(sub_string, 9))  # ValueError: substring not found

# rindex(): Devuelve el índice más alto de una subcadena; los argumentos adicionales indican el índice inicial y final (por defecto, 0 y longitud de la cadena - 1).

challenge = "treinta días de python, día para python"
sub_string = "dí"
print(challenge.rindex(sub_string))  # 24
# print(challenge.rindex(sub_string, 25))  #  ValueError: substring not found

# isalnum(): Verifica si todos los caracteres son alfanuméricos.

challenge = "TreintaDiasPython"
print(challenge.isalnum())  # True

challenge = "30DiasPython"
print(challenge.isalnum())  # True

challenge = "treinta días de python"
print(challenge.isalnum())  # False, el espacio no es un carácter alfanumérico

challenge = "treinta días de python 2019"
print(challenge.isalnum())  # False

# isalpha(): Comprueba si todos los elementos de la cadena son caracteres alfabéticos (a-z y A-Z).

challenge = "treinta días de python"
print(challenge.isalpha())  # False, el espacio es excluido nuevamente

challenge = "TreintaDiasPython"
print(challenge.isalpha())  # True

num = "123"
print(num.isalpha())  # False

# isdecimal(): Verifica si todos los caracteres en la cadena son decimales (0-9).

challenge = "treinta días de python"
print(challenge.isdecimal())  # False

challenge = "123"
print(challenge.isdecimal())  # True

challenge = "\u00bb2"
print(challenge.isdigit())  # False

challenge = "12 3"
print(challenge.isdecimal())  # False, el espacio no está permitido

# isdigit(): Verifica si todos los caracteres en la cadena son números (0-9 y algunos otros caracteres unicode para números).

challenge = "Treinta"
print(challenge.isdigit())  # False

challenge = "30"
print(challenge.isdigit())  # True

challenge = "\u00b2"
print(challenge.isdigit())  # True

# isnumeric(): Comprueba si todos los caracteres en una cadena son números o están relacionados con números (similar a isdigit(), pero acepta más símbolos, como ½).

num = "10"
print(num.isnumeric())  # True

num = "\u00bd"  # ½
print(num.isnumeric())  # True

num = "10.5"
print(num.isnumeric())  # False

# isidentifier(): Verifica si la cadena es un identificador válido, es decir, si es un nombre de variable válido.

challenge = "30DiasDePython"
print(challenge.isidentifier())  # False, porque comienza con un número

challenge = "treinta_dias_de_python"
print(challenge.isidentifier())  # True

# islower(): Comprueba si todos los caracteres alfabéticos en la cadena son minúsculas.

challenge = "treinta días de python"
print(challenge.islower())  # True

challenge = "Treinta días de python"
print(challenge.islower())  # False

# isupper(): Comprueba si todos los caracteres alfabéticos en la cadena son mayúsculas.

challenge = "treinta días de python"
print(challenge.isupper())  # False

challenge = "TREINTA DÍAS DE PYTHON"
print(challenge.isupper())  # True

# join(): Devuelve una cadena concatenada.

web_tech = ["HTML", "CSS", "JavaScript", "React"]
result = " ".join(web_tech)
print(result)  # 'HTML CSS JavaScript React'

web_tech = ["HTML", "CSS", "JavaScript", "React"]
result = "# ".join(web_tech)
print(result)  # 'HTML# CSS# JavaScript# React'

# strip(): Elimina los caracteres dados desde el principio y el final de la cadena.

challenge = "treinta días de pythonoonn"
print(challenge.strip("noth"))  # 'renta días de py'

# replace(): Reemplaza una subcadena con otra cadena dada.

challenge = "treinta días de python"
print(challenge.replace("python", "código"))  # 'treinta días de código'

# split(): Divide la cadena utilizando un separador dado o un espacio en blanco.

challenge = "treinta días de python"
print(challenge.split())  # ['treinta', 'días', 'de', 'python']

challenge = "treinta, días, de, python"
print(challenge.split(", "))  # ['treinta', 'días', 'de', 'python']

# title(): Devuelve una cadena en formato de título, con la primera letra de cada palabra en mayúscula.

challenge = "treinta días de python"
print(challenge.title())  # Treinta Días De Python

# swapcase(): Convierte todos los caracteres en mayúsculas a minúsculas y viceversa.

challenge = "treinta días de python"
print(challenge.swapcase())  # TREINTA DÍAS DE PYTHON

challenge = "Treinta Días De Python"
print(challenge.swapcase())  # tREINTA dÍAS dE pYTHON

# startswith(): Verifica si la cadena comienza con la subcadena especificada.
challenge = "treinta días de python"
print(challenge.startswith("treinta"))  # True

challenge = "30 días de python"
print(challenge.startswith("treinta"))  # False
