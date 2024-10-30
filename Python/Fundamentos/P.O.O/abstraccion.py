"""
                                                Abstracción 
"""

# Es ocultar la complejidad interna al momento de interactuar con el programa ejemplo 

class Auto:
    def __init__(self) -> None:
        self.estado = "Apagado"
        
    def encender_auto(self):
        self.estado == "Encendido"
        print("El auto se encendió Run Run")
        
    def conducir(self):
        if self.estado == "Apagado":
            self.encender_auto()
        print("El auto se esta condiciendo")
    
    
        
mi_auto = Auto()
# solo le pedimos conducir el usuario desconoce la lógica detrás 
mi_auto.conducir()