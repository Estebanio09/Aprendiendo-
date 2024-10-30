# con ellas podemos acceder y modificar las propiedades privadas

from traceback import print_tb


class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self._nombre = nombre
        self._edad = edad
        self.__cuenta_bancaria = 12584416384

    # Para acceder a propiedades semi privadas usamos métodos con la palabra get(leer) o set(modificar)
    def get_nombre(self):
        return self._nombre

    # Para acceder a propiedades privadas usamos un método similar al anterior GET
    def get__cuenta_bancaria(self):
        return self.__cuenta_bancaria

    # Para cambiar propiedades privadas usamos el SET
    def set_cuenta_bancaria(self, new_cuenta):
        self.__cuenta_bancaria = new_cuenta


# creamos nuestro objeto
esteban = Persona("Esteban", 25)
# acedemos a uan propiedad semi privada
print(esteban.get_nombre())  # Esteban
# accedemos y almacenamos una propiedad privada
cuenta = esteban.get__cuenta_bancaria()
# imprimimos la propiedad privada
print(cuenta)  # 12584416384

# Cambiamos el valor de una propiedad privada 
esteban.set_cuenta_bancaria(5566441122)
new_cuenta = esteban.get__cuenta_bancaria()
print(new_cuenta) # 5566441122
