"""
Métodos especiales
"""


# son métodos que inician con dos guiones bajos y terminan con dos guiones bajos
# se usan para el uso de métodos especiales que con métodos normales no podríamos usar
class Persona:
    # __init__  Método constructor
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    # __str__ nos devuelve una representación del objeto en formato texto
    def __str__(self):  # al momento de usar print en el objeto esto es lo que se imprime
        return f"Persona(nombre={self.nombre}, edad={self.edad})"
    
    # __repr__ Nos muestra una representación del objeto el cual podemos reconstruir 
    def __repr__(self):
        return f"Persona('{self.nombre}', {self.edad})"

    # __add__ podemos definir el comportamiento al momento de sumar o concatenar dos objetos esto es sobre carga de operadores
    def __add__(self, otro):
        # definimos como se sumarían o concatenarían las edades
        nuevo_valor_edad = self.edad + otro.edad

        return Persona(self.nombre + otro.nombre, nuevo_valor_edad)


dalto = Persona("Lucas", 21)
esteban = Persona("Camilo", 25)
aleja = Persona("Alejandra", 24)

# Se imprime asi por el método str
print(esteban) # Persona(nombre=Camilo, edad=25)

repre = repr(esteban)
print(repre) #Persona('Camilo', 25) 
print( eval(repre)) # Persona(nombre=Camilo, edad=25)

# vemos como se comporta el sumar dos objetos ya que lo definimos en nuestra clase con __add__
nueva_persona = dalto + esteban
print(nueva_persona.edad)  # 46
print(nueva_persona.nombre)  # LucasCamilo



