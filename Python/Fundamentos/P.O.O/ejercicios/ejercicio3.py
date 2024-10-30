from traceback import print_tb


class Personaje:
    def __init__(self, nombre, fuerza, velocidad) -> None:
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"

    def __add__(self, otro_pj):
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza) / 2) ** 2)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad) / 2) * 1.5)
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)


goku = Personaje("GOKU", 100, 100)
print(goku)  # GOKU (Fuerza: 100, Velocidad: 100)
vegeta = Personaje("Vegeta", 95, 95)
print(vegeta)  # Vegeta (Fuerza: 95, Velocidad: 95)
gogeta = goku + vegeta
print(gogeta)  # GOKU-Vegeta (Fuerza: 9506, Velocidad: 146))
jiren = Personaje("Jiren", 150, 160)
print(jiren) # Jiren (Fuerza: 150, Velocidad: 160)
jireta = jiren + gogeta
print(jireta) # Jiren-GOKU-Vegeta (Fuerza: 23309584, Velocidad: 230)