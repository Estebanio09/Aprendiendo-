# crear un juego donde se pueda crear personajes fusionar personajes y mostrar personajes


class Personaje:
    def __init__(self, nombre, poder, velocidad, agilidad, rango) -> None:
        self.nombre = nombre
        self.poder = poder
        self.velocidad = velocidad
        self.agilidad = agilidad
        self.rango = rango

    def __repr__(self):
        return f"{self.nombre} (Poder: {self.poder}, Velocidad: {self.velocidad}, Agilidad: {self.agilidad}, Rango: {self.rango}"
    
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nuevo_poder = round(((self.poder + otro_pj.poder)/2)**1.34)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad)/2)**1.34)
        nueva_agilidad = round(((self.agilidad + otro_pj.agilidad)/2)**1.34)
        nuevo_rango = round(((self.rango + otro_pj.rango)/2)**1.34)
        return Personaje(nuevo_nombre,nuevo_poder,nueva_velocidad,nueva_agilidad,nuevo_rango)


def mostrar_menu():
    print(
        "\n1. Crear personaje\n2. Fusionar Personajes\n3. Mostrar personajes\n4. Salir\n"
    )


def crear_personaje(personajes_creados):
    nombre = input("\nIngresa el nombre del personaje: ").strip(" ").capitalize()
    poder = int(input("Ingresa el poder del personaje: ").strip(" "))
    velocidad = int(input("Ingresa la velocidad del personaje: ").strip(" "))
    agilidad = int(input("Ingresa la agilidad del personaje: ").strip(" "))
    rango = int(input("Ingresa el rango del personaje: ").strip(" "))
    personaje_creado = Personaje(nombre, poder, velocidad, agilidad, rango)
    personajes_creados.append(personaje_creado)
    print(f"\nPersonaje {nombre} fue creado exitosamente\n")
    
def fusionar_personajes(personajes_creados):
    if len(personajes_creados) < 2:
        print("Debes tener mínimo dos personajes para fusionar\n")
    else:
        mostrar_personajes(personajes_creados)
        num_pj1 = int(input("Selecciona el primer personaje a fusionar de la lista: "))
        num_pj2 = int(input("Selecciona el segundo personaje a fusionar de la lista: "))
        if 1 <= num_pj1 <= len(personajes_creados) and 1 <= num_pj2 <= len(personajes_creados) and num_pj1 != num_pj2:
            personaje1 = personajes_creados[num_pj1 - 1]
            personaje2 = personajes_creados[num_pj2 - 1]
            personaje_fusionado = personaje1 + personaje2
            personajes_creados.append(personaje_fusionado)
            print(f"Fusión exitosa el nuevo personaje es {personaje_fusionado}")
        else:
            print("Selección inválida.")


def mostrar_personajes(personajes_creados):
    print("\n")
    if len(personajes_creados) == 0:
        print("Aun no has creado un personaje\n")
    else:
        print("Personajes: ")
        for i, personaje in enumerate(personajes_creados):
            print(f"{i+1}. {personaje}")



def juego():
    personajes_creados = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_personaje(personajes_creados)
        elif opcion == "2":
            fusionar_personajes(personajes_creados)
        elif opcion == "3":
            mostrar_personajes(personajes_creados)
        elif opcion == "4":
            break
        else:
            print("Elije una opción valida\n")


juego()
