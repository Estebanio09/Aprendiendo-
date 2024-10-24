# cambiar el tipo de dato de edad
import pandas as pd

df = pd.read_csv("Python/EjerciciosPracticos/Dalto/data_frame.txt")
print(type(df["edad"][0]))  # <class 'numpy.int64'>
df["edad"] = df["edad"].astype(str)
print(type(df["edad"][0]))  # <class 'str'>
