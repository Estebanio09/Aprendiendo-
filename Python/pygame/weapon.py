import math
import pygame


class Weapon:
    def __init__(self, imagen, color):
        self.imagen_original = imagen
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.forma = self.imagen.get_rect()
        self.color = color

    def update(self, jugador):
        self.forma.center = jugador.forma.center
        if not jugador.flip:
            
            
            self.forma.x += jugador.forma.width / 2
            self.rotar_arma(False)
        if jugador.flip:
            self.forma.x -= jugador.forma.width / 2
            self.rotar_arma(True)
        self.forma.y += 10

        # mover la escopeta con el mouse
        # mouse.ger_pos() trae la posicion del mouse en todas las actualizaciones
        posicion_mouse = pygame.mouse.get_pos()
        diferencia_x = posicion_mouse[0] - self.forma.centerx
        diferencia_y = -(posicion_mouse[1] - self.forma.centery)
        self.angulo = math.degrees(math.atan2(diferencia_y, diferencia_x))

    def rotar_arma(self, rotar: bool):
        if rotar:
            imagen_flip = pygame.transform.flip(self.imagen_original, True, False)
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)
        else:
            imagen_flip = pygame.transform.flip(self.imagen_original, False, False)
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)

    def dibujar(self, interfaz):
        self.imagen= pygame.transform.rotate(self.imagen, self.angulo)
        interfaz.blit(self.imagen, self.forma)
        # pygame.draw.rect(interfaz, self.color, self.forma, width=1)
