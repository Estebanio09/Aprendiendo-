import pandas as pd

# dataframe es la información básica con el nombre de las piezas y centímetros para armar el Excel

data = {
    "piezas": [
        "pata",
        "tablero",
        "puerta",
        "estante",
        "panel",
        "repisa",
        "cajón",
        "soporte",
        "manija",
        "bisagra",
    ],
    "centímetros": [40, 120, 60, 85, 90, 30, 50, 20, 5, 2],
    "material": [
        "madera",
        "madera",
        "madera",
        "madera",
        "madera",
        "madera",
        "metal",
        "metal",
        "metal",
        "metal",
    ],
    "peso_kg": [1.5, 8.0, 3.0, 2.0, 4.5, 1.0, 1.8, 0.5, 0.2, 0.1],
}

df = pd.DataFrame(data)

df.to_excel("Python/EjerciciosPracticos/SergieCode/muebles_medidas.xlsx", index=False)
