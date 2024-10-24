import pandas as pd

df = pd.read_excel("Python/EjerciciosPracticos/SergieCode/muebles_medidas.xlsx")


def cm_a_pulgadas(cm):
    return cm / 2.54


df["pulgadas"] = df["centímetros"].apply(cm_a_pulgadas)

print(df["pulgadas"])

df.to_excel("Python/EjerciciosPracticos/SergieCode/muebles_medidas_convertidas.xlsx", index=False)

print(
    "Conversión completada y guardada en un nuevo archivo llamado 'muebles_medidas_convertidas.xlsx'"
)
