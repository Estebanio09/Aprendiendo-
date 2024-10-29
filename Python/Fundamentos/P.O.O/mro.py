"""
Method Resolution Order
"""

# Método de resolución de orden

# Si dos clases padres cuentan con métodos de nombres similares cual se ejecuta?
# Busca en orden en su padre según el orden

from pickle import OBJ


class A:
    def hablar(self):
        print("hablando desde A")

    def correr(self):
        print("Correr desde A")


class B(A):
    def hablar(self):
        print("hablando desde B")

    def correr(self):
        print("Correr desde B")


class C(A):
    def hablar(self):
        print("hablando desde C")

    def correr(self):
        print("Correr desde C")


class D(B, C):
    def hablar(self):
        print("hablando desde D ")


objeto = D()
# Prima su propia instancia
objeto.hablar()  # hablando desde D
# Prima la primera herencia en el caso de la clase D hereda primero de B
objeto.correr()  # Correr desde B

# ahora como podemos utilizar una en especifico 

#aclaramos la clase y le pasamos el objeto 

A.hablar(objeto) # hablando desde A