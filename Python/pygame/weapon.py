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
        self.forma.x += jugador.forma.width / 2
        self.forma.y += 10
        

    def dibujar(self, interfaz):
        interfaz.blit(self.imagen, self.forma)
        #pygame.draw.rect(interfaz, self.color, self.forma, width=1)
