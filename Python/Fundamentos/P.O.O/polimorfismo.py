"""
Polimorfismo
"""

# El resultado de un método puede variar dependiendo el objeto


class Perro:
    def sonido(self):
        print("Guau")


class Gato:
    def sonido(self):
        print("Miau")


def hacer_sonido(animal):
    animal.sonido()


gato = Gato()
perro = Perro()

perro.sonido()  # Guau
gato.sonido()  # Miau

hacer_sonido(gato)  # Miau

# apuntes es un tema poco complejo 
