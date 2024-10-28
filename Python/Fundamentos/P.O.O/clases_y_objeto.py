# definimos una clase con la palabra reservada class
from uuid import uuid4


class NombreClase:
    # En esta podemos definir la propiedades que van a tener nuestros objeto
    porpiedad1 = "valor1"
    porpiedad2 = "valor2"
    porpiedad3 = "valor3"


class Celular:
    # Estas son propiedades estáticas
    marca = "Samsung"
    modelo = "S23"
    camara = "48MP"


# de esta forma creamos los objetos en base a nuestra clase ahora las propiedades serán siempre las mismas y que nuestra clase tiene propiedades fijas y celular1 un es una instancia de la clase celular
celular1 = Celular()
print(celular1)  # <__main__.Celular object at 0x00000165D1786F90>
print(celular1.marca)  # Samsung

# Y podemos crear los objetos que deseemos con nuestra clase reutilizando código
celular2 = Celular()
celular3 = Celular()

# Podemos reasignar los valores de las propiedades de un objeto ya creado
print(celular3.marca)  # Samsung
celular3.marca = "Apple"
print(celular3.marca)  # Apple

"""
                                          Atributos
"""
# son las variables que pertenecen a una clase

# atributos de instancia: se definen cuando instanciamos una clase // en resumen la especificamos el atributo cuando creamos el objeto


class FabricaCelulares:
    # Usamos el método __init__  este se ejecuta automáticamente cada vez que instanciamos nuestra clase // self: es una forma en la que hacemos referencia al mismo objeto o asi mismo // seguido podemos especificar las propiedades que vamos a recibir para crear nuestro objeto
    def __init__(self, marca, modelo, camara) -> None:
        # creamos nuestras propiedades de la siguiente forma self.propiedad = propiedad
        self.marca = marca
        self.modelo = modelo
        self.camara = camara


# para crear un nuevo objeto con propiedades definidas por nosotros lo hacemos generando una instancia a nuestra clase y pasando los detalles de las propiedades como argumentos

celular1 = FabricaCelulares("Xiaomi", "X57", "78MP")
print(celular1)  # <__main__.FabricaCelulares object at 0x00000240790170E0>
print(celular1.marca)  # Xiaomi
print(celular1.camara)  # 78MP

celular2 = FabricaCelulares("Apple", "Iphone 15 pro", "96MP")
print(celular2)  # <__main__.FabricaCelulares object at 0x0000021C46C1D090>
print(celular2.marca)  # Apple
print(celular2.camara)  # 96MP

"""
                                                Métodos
"""

# Un objeto puede tener propiedades/atributos y acciones o métodos un ejemplo una clase persona puede tener propiedades como peso, genero, altura ahora una persona puede realizar acciones como correr o saltar eso son los métodos

# un método es una función


class Celular_inteligente:
    def __init__(self, marca: str, color: str, camara: str):
        self.id = uuid4()
        self.marca = marca
        self.color = color
        self.camara = camara

    # para crear un método debemos pasar el parámetro self ya que con este hacemos referencia a nuestro objeto
    def llamar(self, numero="Numero privado"):
        print(f"Estas llamando a {numero}")

    # es importante siempre colocar el self ya que de lo contrario no hay una referencia que le indique a nuestro código que se esta auto referenciando
    def cortar(self):
        print("Cortaste la llamada")


celular3 = Celular_inteligente("Apple", "Rojo", "72MP")
print(celular3.color)  # Rojo
print(celular3.id)  # e064e0ce-2d97-4c89-8d0d-53782ec1a9a0
celular3.llamar()  # Estas llamando a Numero privado
celular3.llamar(310000000)  # Estas llamando a 310000000
celular3.cortar()  # Cortaste la llamada
