"""
principio de sustitución de Liskov
"""

# si una clase B hereda de una clase A la clase A debe poder usarse en todos los lugares que en los que se usaría B

"""
podemos definir una clase ave la cual tiene un método volar ahora hay aves que no vuelan por lo que la clase ave no puede utilizar su método volar si se instancia un pinguino
se realizaría de la siguiente forma 
"""

# plantilla 
class Ave:
    def __init__(self, nombre, peso, color):
        self.nombre = nombre
        self.peso = peso
        self.color = color

# para objetos que heredan pero no pueden realizar métodos específicos 
class AveNoVoladora(Ave):
    def __init__(self, nombre, peso, color):
        super().__init__(nombre, peso, color)

    def volar(self):
        print("no puedo volar")


class AveVoladora(Ave):
    def __init__(self, nombre, peso, color):
        super().__init__(nombre, peso, color)

    def volar(self):
        print(f"{self.nombre} esta volando...")
