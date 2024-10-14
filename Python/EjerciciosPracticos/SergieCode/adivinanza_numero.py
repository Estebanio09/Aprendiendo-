"""
Crea una función para crear un juego en el que el usuario tenga que adivinar un número del uno al cien, define las variables necesarias,
un contador de intentos, un número aleatorio del uno al cien y una para la condición con un bucle que valide la condición y solicita el número
del usuario verifica que lo que ingreso el usuario es un número pásalo a entero guárdalo y ahora verifica si es menor, si es mayor o si acertó
o si no ingreso un número4
"""

from random import randint


# creamos la función
def juego_adivinanza():
    print("¡Bienvenido al juego de adivinanza de número!")
    print("Debes adivinar un número entre el 1 al 100")
    print("¡intenta adivinarlo!")
    # creamos una variable para almacenar los intentos
    intentos = 0
    # creamos una variable donde almacenamos el número secreto
    numero_secreto = randint(1, 100)
    # creamos una variable con la que validaremos si el bucle se repite o no
    adivinando = False

    # creamos el bucle que al negar adivinando si es False pasara a True y en el momento que la variable pase a True sera False por lo que el bucle terminara
    while not adivinando:
        # solicitamos el número al usuario
        adivinanza = input("Introduzca un número del 1 al 100: ")
        # sumamos un intento
        intentos += 1
        # validamos si el dato que ingreso el usuario es un numero
        if adivinanza.isdigit():
            # lo pasamos a un entero
            adivinanza = int(adivinanza)
            # validamos si el numero que ingreso el usuario es menor al secreto y le indicamos al usuario que el numero secreto es mayor
            if adivinanza < numero_secreto:
                print(f"El número secreto es mayor a {adivinanza}")
            # validamos si el numero que ingreso el usuario es mayor al secreto y le indicamos al usuario que el numero secreto es menor
            elif adivinanza > numero_secreto:
                print(f"El número secreto es menor a {adivinanza}")
            # si las anteriores no se cumplieron es por que es igual el usuario acertó y le indicamos el numero secreto y los intentos
            else:
                print(
                    f"¡Felicidades has ganado! El número {numero_secreto} es el secreto y lo has logrado en {intentos} intentos."
                )
                # cambiamos la variable para que el bucle se rompa
                adivinando = True
        # si no es un numero lo que ingreso el cliente le recordamos que debe ser un número
        else:
            print("Por favor introduzca un número válido entre el 1 y el 100")


juego_adivinanza()
