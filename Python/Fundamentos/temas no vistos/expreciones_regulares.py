import re

# las expresiones regulares son para encontrar patrones o coincidencia y darle un manejo

texto = """Hola capo como vas 3 
esta es la segunda línea 2?
este Es el final de la línea 1
14862. 
879 61886 652 3168 8741 684 66 81816 7677 61 68778 64664 55
capo hola 
el final
abababa ab ab ab abab ab 
"""

# Esto me indica cuando se encuentra una coincidencia ahora al imprimir en pantalla me arroja un objeto
texto1 = re.search("es", texto)
print(texto1)  # <re.Match object; span=(20, 22), match='es'>

# Esto lo usamos para que nos retorne todas las coincidencias que se encuentren en la cadena que le pasemos
resultado = re.findall("esta", texto)
print(resultado)  # 'esta']

# con flags= re.IGNORECASE podemos indicarle que omita si son mayúsculas o minúsculas
resultado1 = re.findall("es", texto, flags=re.IGNORECASE)
print(resultado1)  # ['es', 'es', 'es', 'Es']

"""
                                    Expresiones 
"""

# usamos la r antes de la cadena para indicar que vamos a usar expresiones

# \d -> busca dígitos numéricos del 0 al 9
resultado = re.findall(r"\d", texto)
print(resultado)  # ['3', '2', '1']

# \D -> busca todo menos dígitos numéricos 0-9
resultado = re.findall(r"\D", texto)

# \w -> busca caracteres alfa numéricos [a-z A-Z 0-9]
resultado = re.findall(r"\D", texto)

# \W -> busca todo menos caracteres
resultado = re.findall(r"\W", texto)

# \s -> busca espacios en blanco tabs saltos de linea
resultado = re.findall(r"\s", texto)

# . -> busca todo menos saltos de línea
resultado = re.findall(r".", texto)

# \n -> buscamos todos los saltos de línea
resultado = re.findall(r"\n", texto)

# \ -> cancelar caracteres especiales todos los que no son alfa numéricos
resultado = re.findall(r"\.", texto)

# \ -> cancelar caracteres especiales todos los que no son alfa numéricos
resultado = re.findall(r"\.", texto)

# uno que busca un número, seguido de un punto y un espacio
resultado = re.findall(r"\d\.\s", texto)
print(resultado)  # ['2. ']

# buscar el comienzo y final de la línea

# ^ -> busca el comienzo de la línea
resultado = re.findall(r"^", texto)
# podemos usarla para validar si una cadena empieza por una serie definida de caracteres
resultado = re.findall(r"^hola", texto, flags=re.IGNORECASE)
print(resultado)
resultado = re.findall(r"^capo", texto, flags=re.IGNORECASE)
print(resultado)  # []

# con flags= re.M   le indicamos que cuente cada salto de línea como una línea nueva // Multiline
resultado = re.findall(r"^capo", texto, flags=re.M)
print(resultado)  # ['capo']

# $ -> busca el final de la línea // el dolar se deja en el final para que se interprete correctamente
resultado = re.findall(r"final$", texto)
print(resultado)

# {n} -> busca n cantidad de veces el valor de la izquierda // \d{3} busca tres números
resultado = re.findall(r"\d{3}", texto)
print(resultado)  #  ['148']

# y así podemos ir sumando la forma en la que buscamos
resultado = re.findall(r"\d{3}\s", texto)
print(
    resultado
)  # ['879 ', '886 ', '652 ', '168 ', '741 ', '684 ', '816 ', '677 ', '778 ', '664 ']

# {n,m} -> numero mínimo de veces n // máximo número de veces m
resultado = re.findall(r"\d{1,4}\s", texto)
print(
    resultado
)  # ['3 ', '1\n', '879 ', '1886 ', '652 ', '3168 ', '8741 ', '684 ', '66 ', '1816 ', '7677 ', '61 ', '8778 ', '4664 ', '55\n']

# con mínimo y máximo solo cuenta el primer carácter a la derecha ahora si queremos agrupar debemos encerrar en () por cada n números de veces solo devolverá solo un resultado
resultado = re.findall(r"(ab){2,6}", texto)
print(resultado)  # ['ab', 'ab']

# | -> como operador or es uno o el otro retorna una a una
resultado = re.findall(r"\d{2,8}|hola", texto, flags=re.IGNORECASE)
print(
    resultado
)  # ['Hola', '14862', '879', '61886', '652', '3168', '8741', '684', '66', '81816', '7677', '61', '68778', '64664', '55', 'hola']

# [] -> indicamos que los elementos dentro los debe devolver no importa el orden
resultado = re.findall(r"[aeiou]", texto)
print(resultado)  # una lista con todas la vocales

# busquemos una fecha en un texto

text = "Hola mi nombre es esteban y tengo 25 años y nací el 09/01/1999"

x = re.findall(r"\d{2}/\d{2}/\d{4}", text)

print(x)  # ['09/01/1999']
