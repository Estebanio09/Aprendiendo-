# proteger los elementos de una clase formas de restringir el acceso a información confidencial de cualquier tipo


class MiClase:
    def __init__(self) -> None:
        # podemos especificar el grado de privacidad esto en python es débil pero indica que es privado se especifica con _ aun podemos acceder a la información pero se entiende que no deberíamos
        self._atributo_casi_privado = "valor"
        # se especifica ques es privado y python no nos permitirá acceder acceder de forma directa.
        self.__atributo_privado = "valor"

    # asi como existen las propiedades privadas también existen los métodos privados
    def __hablar(self):
        print("Hola master esto es privado")


objeto = MiClase()

"""
print(object.__atributo_privado)

Traceback (most recent call last):
  File "c:\Python\Fundamentos\P.O.O\encapsulamiento.py", line 15, in <module>
    print(object.__atributo_privado)
          ^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: type object 'object' has no attribute '__atributo_privado'
"""

# esto pasa por que estoy intentando acceder a una propiedad //método privada
"""
objeto.__hablar()
Traceback (most recent call last):
  File "c:Python\Fundamentos\P.O.O\encapsulamiento.py", line 30, in <module>
    objeto.__hablar()
    ^^^^^^^^^^^^^^^
AttributeError: 'MiClase' object has no attribute '__hablar'
"""

