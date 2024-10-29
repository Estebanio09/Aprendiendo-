class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad 
    
    def presentarse(self):
        print(f"Mi nombre es {self.nombre} y mi edad es {self.edad}")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado) -> None:
        super().__init__(nombre, edad)
        self.grado = grado 
        
    def mostrar_grado(self):
        print(f"Grado: {self.grado}")
        
estudiante = Estudiante("Esteban", 25, 9)
estudiante.presentarse() # Mi nombre es Esteban y mi edad es 25
estudiante.mostrar_grado() # Grado: 9