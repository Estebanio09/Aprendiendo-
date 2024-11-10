"""
¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
- Recuerda que todas las instrucciones de participación están en el
  repositorio de GitHub.

   Lo primero... ¿Ya has elegido un lenguaje?
 - No todos son iguales, pero sus fundamentos suelen ser comunes.
 - Este primer reto te servirá para familiarizarte con la forma de participar
   enviando tus propias soluciones.

  EJERCICIO:
 - Crea un comentario en el código y coloca la URL del sitio web oficial del
   lenguaje de programación que has seleccionado.
 - Representa las diferentes sintaxis que existen de crear comentarios
   en el lenguaje (en una línea, varias...).
 - Crea una variable (y una constante si el lenguaje lo soporta).
 - Crea variables representando todos los tipos de datos primitivos
   del lenguaje (cadenas de texto, enteros, booleanos...).
 - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
debemos comenzar por el principio.
"""

# https://www.python.org/

# Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).

# soy un comentario en una línea

"""
    Soy un comentario de varias línea 
    soy otra línea del mismo comentario
    y yo otra
"""

"""
    También soy un comentario en varias líneas
    y yo soy una línea mas 
"""

soy_una_variable = "mi variable"

SOY_UNA_CONSTANTE = (
    "Soy una constante, pero puedo cambiar ya que python no tiene constantes"
)

my_string = "cadena o string"
my_int = 15
my_float = 15.2
my_complex = 14j
my_bool = False
my_list = [1, 2, 3]
my_tuple = (1, 2, 3, my_list)
my_set = {1, 2, 3, 4, my_tuple, my_list}
my_dit = {"key": "value", "key2": "value2"}
my_none = None

print("Hola, python")