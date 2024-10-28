class Estudiante:
    def __init__(self, nombre: str, edad: int, grado: int):
        self.nombre = nombre
        self.edad = edad 
        self.grado = grado
    
    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando...")
        

nombre = input("Cual es tu nombre: ")
edad = input("Cual es tu edad: ")
grado = input("Cual es tu grado: ")

estudiante1 = Estudiante(nombre, edad, grado)

while True:
    accion = input()
    if accion.lower() == "estudiar":
        estudiante1.estudiar()
        break
    