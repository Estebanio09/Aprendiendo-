import pygame


class Personaje:
    def __init__(self, x, y, color, animacion):
        # se almacena el tiempo en milisegundos desde que inicio pygame
        self.update_time = pygame.time.get_ticks()
        self.frame_index = 0
        self.imagen = animacion[self.frame_index]
        self.flip = False
        self.forma = self.imagen.get_rect()
        self.forma.center = (x, y)
        self.color = color
        self.animaciones = animacion
        # indice de la animación que se mostrara o la imagen que se mostrara
        
        
        
        
    def update(self):
        refresco_animación = 100
        self.imagen = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= refresco_animación:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0
            

    def movimiento(self, delta_x, delta_y):
        if delta_x < 0:
            self.flip = True
        elif delta_x > 0:
            self.flip = False
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y

    def dibujar(self, interfaz):
        imagen_flip = pygame.transform.flip(self.imagen, self.flip, False)
        interfaz.blit(imagen_flip, self.forma)
        #pygame.draw.rect(interfaz, self.color, self.forma, width=1)
