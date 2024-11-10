import constantes as co  # Constantes(co)
from personaje import Personaje  # Constructor Personaje
from weapon import Weapon

import pygame  # importar pygame

# Inicializar pygame
pygame.init()

# Inicializar ventana
ventana = pygame.display.set_mode((co.ANCHO, co.ALTO))

# Nombre de la ventana
pygame.display.set_caption("Star Cod")


# escalar la imagen
# cambiamos la escala de la imagen de nuestro personaje
def escalar_img(imagen, escala):
    w = imagen.get_width()
    h = imagen.get_height()

    nueva_imagen = pygame.transform.scale(imagen, (w * escala, h * escala))
    return nueva_imagen


# animaciones // importar imágenes del personaje 
animaciones = []
for i in range(7):
    
    # creamos una variable para almacenar la ruta de las imágenes que componen la animación
    img = pygame.image.load(
        f"Python//pygame//assets//images//characters//player//movimiento_{i}.png"
    )
    img = escalar_img(img, co.PERSONAJE_ESCALA)
    animaciones.append(img)

# animaciones // arma 
imagen_escopeta= pygame.image.load("Python//pygame//assets//images//weapons//arma.png")
imagen_escopeta = escalar_img(imagen_escopeta, co.ARMA_ESCALA)

# Hola jugador // crear jugador de clase personaje 
jugador = Personaje(250, 350, co.COLOR_PERSONAJE, animaciones)

# Crear un arma de la clase weapon 
escopeta = Weapon(imagen_escopeta, co.COLOR_ARMA)

# Definir variables de movimiento del jugador
mover_derecha = False
mover_izquierda = False
mover_arriba = False
mover_abajo = False

# Controlar el frame rate
reloj = pygame.time.Clock()

# Control de inicio/cierre
run = True

# Bucle que mantiene le programa en funcionamiento
while run:
    # Frame rate
    reloj.tick(co.FPS)

    # Indicamos el color de la ventana desde nuestras constantes(co) // ayuda a eliminar los cuadros dibujados antes
    ventana.fill(co.COLOR_FONDO)

    # Calcular el movimiento del jugador
    delta_x = 0
    delta_y = 0

    # si las variables son True toma el valor de las constantes y las usa la velocidad
    if mover_derecha:
        delta_x = co.VELOCIDAD_PERSONAJE

    if mover_izquierda:
        delta_x = -co.VELOCIDAD_PERSONAJE

    if mover_arriba:
        delta_y = -co.VELOCIDAD_PERSONAJE

    if mover_abajo:
        delta_y = co.VELOCIDAD_PERSONAJE

    # ejecutamos el método de movimiento en nuestra clase personaje
    jugador.movimiento(delta_x, delta_y)
    
    # llamamos el método que ejecuta la animación 
    jugador.update()
    
    # llamamos el método que ejecuta la animación del arma 
    escopeta.update(jugador)

    # Dibujando al (jugador) en la ventana
    jugador.dibujar(ventana)
    
    # Dibujando el arma
    escopeta.dibujar(ventana)

    # Recorres los eventos en el juego todo lo que pasa en nuestro juego
    for event in pygame.event.get():
        # Control de evento si es cerrar ventana finaliza el programa con nuestro control de inicio y cierre
        if event.type == pygame.QUIT:
            # Control de inicio y cierre
            run = False

        # Control de eventos en pulsaciones de teclas
        if event.type == pygame.KEYDOWN:
            # Si el evento es que se pulsa la tecla a la variable cambia a True mas abajo veras que hay un evento para cuando la tecla deja de ser pulsada
            if event.key == pygame.K_a:
                mover_izquierda = True

            if event.key == pygame.K_d:
                mover_derecha = True

            if event.key == pygame.K_w:
                mover_arriba = True

            if event.key == pygame.K_s:
                mover_abajo = True

        # Control de eventos cuando se deje de pulsar la tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False

            if event.key == pygame.K_d:
                mover_derecha = False

            if event.key == pygame.K_w:
                mover_arriba = False

            if event.key == pygame.K_s:
                mover_abajo = False

    # Actualiza nuestro programa constantemente
    pygame.display.update()

# Finaliza pygame
pygame.quit()
