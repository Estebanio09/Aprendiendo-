# con property podemos definir getters y setters y deleter sin necesidad de llamarlos como métodos se llamarían como propiedades


class Persona:
    def __init__(self, nombre, edad) -> None:
        self.__nombre = nombre
        self.__edad = edad

    # usamos property para indicar que va actuar como un GET
    @property
    def nombre(self):
        return self.__nombre
    
    # usamos método.setter para indicar que va actuar como un SET
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # usamos método.deleter para que pueda eliminar propiedades privadas 
    @nombre.deleter
    def nombre(self):
        del self.__nombre



# Instanciamos nuestra clase para crear el objeto
esteban = Persona("Esteban", 25)
# Accedemos a nuestra propiedad privada como si solo fuese una propiedad gracias a el método get decorado por property
name = esteban.nombre
print(name)  # Esteban

#cambiamos el valor de la propiedad 
esteban.nombre = "Estebitan"
name = esteban.nombre
print(name) # Estebitan

del esteban.nombre

"""
name = esteban.nombre AttributeError: 'Persona' object has no attribute '_Persona__nombre'
"""