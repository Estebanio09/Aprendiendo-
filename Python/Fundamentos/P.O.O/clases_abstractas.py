"""
Clases abstractas
"""

# Son clases que usamos para crear otras clases, pero esta no puede ser instanciada para crear un objeto
# La usamos como plantilla para crear otras clases
# Al definir un método abstracto se obliga a todas las clases que hereden a implementar este método

# importamos abc para usar una clase abstracta // abstractclassmethod es un decorador
from abc import ABC, abstractclassmethod


# al crear la clase debemos pasar la importación como parámetro así no se podrá instancia
class Persona(ABC):
    # con este decorador indicamos un método que debe ser implementado en todas la clases que hereden
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad) -> None:
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    # definimos un método que debe ser implementado siempre
    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")

# creamos la clase con la herencia 
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    # creamos el método obligatorio de nuestra plantilla
    def hacer_actividad(self):
        print(f"Estoy estudiando {self.actividad}")


class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Estoy trabajando en {self.actividad}")


estebandido = Trabajador("Estebandido", 25, "Masculino", "Robar")
esteban = Estudiante("Esteban", 27, "Masculino", "Programación")

estebandido.presentarse()  # Hola, mi nombre es Estebandido y tengo 25 años7
esteban.presentarse()  # Hola, mi nombre es Estebandido y tengo 25 años
estebandido.hacer_actividad()  # Estoy trabajando en Robar
esteban.hacer_actividad()  # Estoy estudiando Programación
