import pygame


class Personaje:
    def __init__(self, x, y, color, animacion):
        # se almacena el tiempo actual en el momento que se creo la instancia de Personaje en milisegundos desde que inicio pygame
        self.update_time = pygame.time.get_ticks()
        # variable que indica que imagen en la lista se muestra para la animacion 
        self.frame_index = 0
        # Imagen actual 
        self.imagen = animacion[self.frame_index]
        # variable para rotar al personaje
        self.flip = False
        # forma del personaje la cual es un cubo
        self.forma = self.imagen.get_rect()
        # Posicion del personaje 
        self.forma.center = (x, y)
        # color de area de colisiones 
        self.color = color
        # recibe la lista de las imágenes que componen la animación 
        self.animaciones = animacion   
        
    # Método para actualizar el estado constante del personaje 
    def update(self):
        # tiempo en milisegundos 
        refresco_animación = 100
        # cambiamos la imagen según cambie el index en de la lista
        self.imagen = self.animaciones[self.frame_index]
        # se mide el tiempo actual y el tiempo desde el ultimo cambio en (self.update_time // ultima vez que se actualizo) si es mayor a la tasa de refresco 
        if pygame.time.get_ticks() - self.update_time >= refresco_animación:
            # se suma 1 al index que indica la imagen de la animación
            self.frame_index += 1
            # se actualiza el tiempo en mi jugador o  (self.update_time // ultima vez que se actualizo)
            self.update_time = pygame.time.get_ticks()
        # si el index llega a la ultima imagen de las animaciones retorna a 0 y empieza de nuevo 
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0
            
    # método para realizar el movimiento de mi personaje
    def movimiento(self, delta_x, delta_y):
        # si el delta x es mayor a 0 flip pasa a true esta variable indica que nuestro personaje giro 
        if delta_x < 0:
            self.flip = True
        elif delta_x > 0:
            self.flip = False
        self.forma.x += delta_x
        self.forma.y += delta_y
        #print(f"{self.forma.x}, {self.forma.y}")

    def dibujar(self, interfaz):
        imagen_flip = pygame.transform.flip(self.imagen, self.flip, False)
        interfaz.blit(imagen_flip, self.forma)
        #pygame.draw.rect(interfaz, self.color, self.forma, width=1)
