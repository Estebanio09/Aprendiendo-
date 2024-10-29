# Con la herencia podemos reutilizar el código o propiedades de una clase anterior o padre como lo es la clase persona es el padre y la clase estudiante es la clase hija un estudiante es una persona y podemos reutilizar mucho código con esto

# definimos nuestra clase padre en esta caso persona


class Persona:
    def __init__(self, nombre, edad, nacionalidad) -> None:
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f"{self.nombre} esta hablando...")


# definimos nuestra clase hija en este caso empleado un empleado es una persona por lo que podemos reutilizar las propiedades ya definidas en persona y usarlas en empleado
class Empleado(Persona):
    # a nuestra nueva clase le podemos asignar nuevas propiedades debemos especificar las que vamos a heredar y las nuevas
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario) -> None:
        # con super().__init__() especificamos las propiedades que se heredan
        super().__init__(nombre, edad, nacionalidad)
        # definimos nuevas propiedades para nuestra clase Empleado
        self.trabajo = trabajo
        self.salario = salario


# creamos nuestro objeto con la clase empleado pero nos solicita las propiedades de nuestra clase padre
empleado1 = Empleado("Camilo", "edad", "Colombia", "Programador", 15000000)
# desde nuestro objeto podemos acceder a los métodos de nuestra clase padre
empleado1.hablar()

"""
                                                            Herencia jerárquica 
"""

# ahora están las super clases y subclases. Super clases: son clases primarias de las que derivan varias clases, un ejemplo de es Persona ya que pueden derivar clases como empleado o estudiante dependen de Persona esto es herencia jerárquica


# Estudiante depende de persona tiene las propiedades de persona y agregamos las propiedades de un estudiante
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, universidad, notas) -> None:
        # en super no pasamos self
        super().__init__(nombre, edad, nacionalidad)
        self.universidad = universidad
        self.notas = notas


"""
                                                            Herencia múltiple 
"""
# en este caso podemos heredar propiedades de mas de una clase y lo hacemos de la siguiente forma


class Artista:
    def __init__(self, habilidad) -> None:
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"


# Creamos la clase que va a heredar dos clases Persona y Artista
# ignoramos que creamos una clase Empleado
class EmpleadoArtista(Persona, Artista):
    # Especificamos las propiedades de las dos herencias y las nuevas que va a tener nuestra nueva clase
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa) -> None:
        # Cambiamos la función super() por la clase y las propiedades que heredamos de esta
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        # Creamos nuestras nuevas propiedades
        self.salario = salario
        self.empresa = empresa

        # podemos usar métodos de nuestras clases padres para nuevos métodos

    def hablar_y_habilidad(self):
        # importante usar super() ya que esto le indica que debe buscar en las clases padres si usamos self buscara en si misma no en los padres
        super().hablar()
        super().mostrar_habilidad()

    def presentarse(self):
        return f"Hola soy {self.nombre}, {super().mostrar_habilidad()} y trabajo en {self.empresa}"


user1 = EmpleadoArtista("Esteban", 25, "Colombia", "Pro", 1500000, "Condor")
print(user1.nombre)  # Esteban
user1.hablar()  # Esteban esta hablando...

user1.hablar_y_habilidad()  # Esteban esta hablando... Mi habilidad es: Pro
print(user1.presentarse())  # Hola soy Esteban, Mi habilidad es: Pro y trabajo en Condor

# issubclass() podemos validar si una clase es subclase de otra clase
print(issubclass(EmpleadoArtista, Persona))  # True
# isinstance() podemos ver si un objeto es una instancia de una clase, cuenta también si la clase es una subclase o tiene herencia de otra clase como en este ejemplo Persona es una super clase 
print(isinstance(user1, EmpleadoArtista))  # True
print(isinstance(user1, Persona)) # True
