class Sentimiento:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def __str__(self):
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color, self.nombre)

rangos = [
    ((-0.6,-0.3), Sentimiento("Negativo", "31")),
    ((-0.3,-0.1), Sentimiento("Algo Negativo", "31")),
    ((-0.1,0.1), Sentimiento("Neutral", "33")),
    ((0.1,0.4), Sentimiento("Algo Positivo", "32")),
    ((0.4,0.9), Sentimiento("Positivo", "32")),
    ((0.9,1), Sentimiento("Muy Positivo", "32"))
]


print(rangos[2][1])