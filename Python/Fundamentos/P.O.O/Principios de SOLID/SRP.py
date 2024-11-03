"""
Principio de Responsabilidad Única
"""

# Una clase solo puede tener un motivo/razón por el cual cambiar una sola responsabilidad o tarea.


# creamos una clase
class Auto:
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
        # self.combustible = 100

    # una funcion para moverse esto es mucho mas complicado y se puede alagar mucho por lo que la clase ya es compleja ahora hay funciones para agregar y descontar combustible abajo esto no debería ser así estamos sobre cargando la función.
    def mover(self, distancia: int):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print("El auto se ha movido con éxito")
        else:
            print("No hay suficiente combustible")

    def obtener_posicion(self):
        return self.posicion

    """
    Estas funciones están sobre cargando la clase  esto no es optimo asi que crearemos una nueva clase 
    
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
    
    def obtener_combustible(self):
        return self.combustible
    """


# creamos una clase para dar manejo a las funciones necesarias para interactuar con el tanque de combustible
class Tanque_de_combustible:
    def __init__(self):
        self.combustible = 100
    # Funciones aunque relacionadas con el auto no suman la lógica que encierra auto asi aplicamos SRP
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible

    def usar_combustible(self, cantidad: int):
        self.combustible -= cantidad


tanque = Tanque_de_combustible()
mi_auto = Auto(tanque)

mi_auto.mover(50)
print(mi_auto.obtener_posicion())  # 50
mi_auto.mover(50)
print(mi_auto.obtener_posicion())  # 100
mi_auto.mover(5)
print(mi_auto.obtener_posicion()) # 105
mi_auto.mover(100) # No hay suficiente combustible