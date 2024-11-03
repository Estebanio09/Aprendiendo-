"""
Dependency Inversion Principle
"""

# clases grandes o clases importantes no deben tener dependencias como un corrector ortográfico no debe depender de un diccionario

# creamos la clase que define como serán los verificadores

from abc import ABC, abstractmethod


class VerificadorOrtografico(ABC):
    # definimos un método abstracto que debe ser definido en todas las clases que hereden
    @abstractmethod
    def verificar_palabra(self):
        pass


# clase que hereda del verificadorOrtografico
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # lógica para verificar la palabra
        pass


# clase que hereda del verificadorOrtografico
class ServicioWeb(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # lógica para verificar la palabra por un servicio web
        pass


class CorrectorOrtografico:
    def __init__(self, verificador=VerificadorOrtografico):
        self.verificador = verificador

    def corregir_texto(self, texto):
        self.verificador  # usamos el verificador para verificar la palabra esto tiene mucha mas lógica pero nuestra clase no depende de un solo verificador ahora puede usar cualquiera de los dos si uno falla
