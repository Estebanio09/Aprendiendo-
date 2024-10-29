class Animal:
    def comer(self):
        print("El animal esta comiendo")


class Mamifero(Animal):
    def amamantar(self):
        print("El mamífero está amamantando")


class Ave(Animal):
    def volar(self):
        print("El ave esta volando")


class Murcielago(Mamifero, Ave):
    pass


murcielago = Murcielago()
murcielago.comer()  # El animal esta comiendo
murcielago.amamantar()  # El mamífero está amamantando
murcielago.volar()  # El ave esta volando

piolin = Ave()
piolin.comer()  # El ave esta volando
piolin.volar()  # El ave esta volando

laika = Mamifero()
laika.amamantar() # El mamífero está amamantando
laika.comer() # El animal esta comiendo
