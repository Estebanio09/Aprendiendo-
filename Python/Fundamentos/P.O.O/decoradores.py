"""
Decoradores
"""


# Lo usamos para añadir funcionalidad a una función existente sin modificar el código ya creado // decora una función que le pasamos por parámetro


# creamos nuestra función decoradora la cual recibe como parámetro otra función
def decorador(funcion):
    # Definimos una función que ejecutara el digo extra para decorar la función que viene por parámetro
    def función_modificada():
        # Esto pueden ser validaciones que interactúen con la función que viene por parámetro
        print("Hola desde el decorador antes de ejecutar la función")
        # Ejecutamos la función que viene por parámetro
        funcion()
        print("Hola desde decorador después de ejecutar la función")

    # Retornamos la función que interactúo con la función que viene por parámetro
    return función_modificada


def saludar():
    print("Hola Esteban")


saludar()  # Hola Esteban
# Asi ejecutamos un decorador almacenándolo en una variable
saludo_decorado = decorador(saludar)
saludo_decorado()

"""
Hola desde el decorador antes de ejecutar la función
Hola Esteban
Hola desde decorador después de ejecutar la función
"""

# forma optima de ejecutar un decorador


@decorador
def saludo_2():
    print("hola soy saludo 2.0")
 

saludo_2()

"""
Hola desde el decorador antes de ejecutar la función
hola soy saludo 2.0
Hola desde decorador después de ejecutar la función
"""
