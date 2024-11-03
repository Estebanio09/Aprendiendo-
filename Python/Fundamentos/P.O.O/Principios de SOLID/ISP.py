"""
Interface segregation principle
"""

# no debemos depender de interfaces innecesarias o obligar al usuario a interfases o clases no necesarias
# si tenemos una clase trabajador podemos asumir que la persona trabaja duerme come ahora si queremos usar un robot trabajador estos métodos de dormir o comer no aplican o no tienen sentido.

# se puede hacer de la siguiente forma


class Trabajador:
    def trabajar(self):
        print("Trabajando...")


class Humano(Trabajador):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def dormir(self):
        print(f"{self.nombre} esta durmiendo")

    def comer(self):
        print(f"{self.nombre} esta comiendo")


class Robot(Trabajador):
    pass


esteban = Humano("Esteban", 25)
esteban.comer()
esteban.trabajar()
bender = Robot()
bender.trabajar()
