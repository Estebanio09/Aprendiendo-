# definimos nuestra clase con la palabra class y el nombre inicia en mayúscula
class Persona:
    # Utilizamos def y __init__ para iniciar nuestro constructor el cual recibe los para metros con los cuales construiremos nuestro objeto
    def __init__(self, name, surname, age, height, id="User 12345685"):
        # self hace referencia al constructor o asi mismo con el podemos crear las propiedades que va a tener nuestro objeto después del punto anexamos el nombre y le asignamos un valor.
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.fullname = f"{name} {surname}"
        self.__id = id  # propiedad privada

    # ahora vamos a definir las funciones
    def walk(self):
        print(f"{self.fullname} esta caminando")

    # función para verlos datos de nuestro objeto en un print utilizamos el __str__
    def __str__(self):
        return f"Nombre: {self.name} \nApellido: {self.surname}\nEdad: {self.age}\nAltura: {self.height}\nID: {self.__id}"


camilo = Persona("Camilo", "Martinez", 25, 1.78)
camilo.walk()
print(camilo)

# podemos cambiar los valores de nuestro objeto pero el constructor no se ve afectado
camilo.name = 666
print(camilo)

# no podemos alterar una propiedad que establecimos como privada
camilo.__id = 5244897
print(camilo)
