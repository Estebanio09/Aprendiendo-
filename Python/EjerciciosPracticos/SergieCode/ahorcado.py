import random


"""def obtener_palabra_secreta() -> str:
    palabras = [
        "java",
        "python",
        "javascript",
        "react",
        "angular",
        "tensorflow",
        "django",
        "typescript",
        "git",
    ]
    return random.choice(palabras)


def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"
    return adivinado


def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False

    print("Bienvenido al juego del ahorcado")
    print(f"tienes {intentos} para adivinar la palabra secreta")
    print(
        mostrar_progreso(palabra_secreta, letras_adivinadas),
        f"la cantidad de letras de la palabra es: {len(palabra_secreta)}",
    )

    while not juego_terminado and intentos > 0:
        adivinanza = input("introduce una letra: ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor introduce una letra válida (sólo escribir una letra)")
        elif adivinanza in letras_adivinadas:
            print("Ya has utilizado esa letra prueba con otra")
        else:
            letras_adivinadas.append(adivinanza)
            if adivinanza in palabra_secreta:
                print(
                    f"Bien has acertado, la letra '{adivinanza}' está en presente en la palabra"
                )
            else:
                intentos -= 1
                print(
                    f"¡Lo siento la letra! '{adivinanza}' no está presente en la palabra secreta"
                )
                print(f"Te quedan {intentos} intentos")
                
        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)
        if "_" not in progreso_actual:
            juego_terminado = True
            palabra_secreta = palabra_secreta.capitalize()
            print(f"Felicidades has ganado La palabra secreta es: {palabra_secreta}")
    if intentos == 0:
        palabra_secreta = palabra_secreta.capitalize()
        print(
            f"Lo sentimos mucho se te han acabado los intentos, la palabra secreta era {palabra_secreta}"
        )"""


def obtener_palabra_secreta():
    palabras_ahorcado = [
        "elefante",
        "computadora",
        "bicicleta",
        "astronauta",
        "mariposa",
        "biblioteca",
        "montana",
        "murcielago",
        "cocodrilo",
        "calendario",
        "xilofono",
        "automovil",
        "pinguino",
        "girasol",
        "aeropuerto",
        "camaleon",
        "hipopotamo",
        "delfin",
        "jirafa",
        "volcan",
    ]
    return random.choice(palabras_ahorcado)


def estado_actual(palabra_secreta, letras_adivinadas):
    estado_palabra_secreta = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            estado_palabra_secreta += letra
        else:
            estado_palabra_secreta += "_"
    return estado_palabra_secreta


def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    intentos = 10
    letras_adivinadas = []
    estado_juego = False

    print("Bienvenido al juego del ahorcado es hora de que adivines la palabra")
    print(f"Tienes {intentos} intentos para lograrlo")
    print(
        estado_actual(palabra_secreta, letras_adivinadas),
        f"la palabra secreta tiene {len(palabra_secreta)} letras",
    )

    while not estado_juego and intentos > 0:
        adivinando = input("Ingresa una letra: ").lower()

        if len(adivinando) != 1 or not adivinando.isalpha():
            print("Por favor introducir una letra válida (solo una letra)")
        elif adivinando in letras_adivinadas:
            print(f"La letra '{adivinando}' ya fue usada valida con otra")
        else:
            letras_adivinadas.append(adivinando)
            if adivinando in palabra_secreta:
                print(f"Bien '{adivinando}' esta en la palabra secreta")
            else:
                intentos -= 1
                print(f"La letra '{adivinando}' no esta en la palabra secreta")
                print(f"Te quedan {intentos} intentos")
        
        adivino = estado_actual(palabra_secreta, letras_adivinadas)
        print(adivino) 
        if '_' not in adivino:
            estado_juego = True
            palabra_secreta = palabra_secreta.capitalize()
            print(f"Felicidades la palabra secreta es {palabra_secreta}, te quedaban {intentos} intentos")
    
    if intentos == 0:
        palabra_secreta = palabra_secreta.capitalize()
        print(f"Agotaste tus intentos la palabra secreta es {palabra_secreta}")
            
juego_ahorcado()
