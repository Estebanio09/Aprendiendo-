nombres = ["Camilo", "Francisco", "Tiago", "Lucas"]
apellidos = ["Martinez", "Rodirguez", "Astaiza", "Dalto"]

with open("Python/EjerciciosPracticos/Dalto/Nombre_y_Apellidos.txt", "w") as archivo:
    archivo.writelines("los datos son:\n\n")
    archivo.writelines(
        [
            f"Nombre: {a}\nApellido: {n}\n----------------\n"
            for a, n in zip(nombres, apellidos)
        ]
    )
