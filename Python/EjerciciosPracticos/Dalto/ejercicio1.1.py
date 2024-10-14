# Calcular los promeidos de otrso cursos a comparación de los de dalto

# datos de duración en horas de otros cursos
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4

# datos de duración en horas de el curso de dalto
dalto_curso = 1.5

# duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

# diferencias de duración

# promedio de duración con otros cursos

diferencia_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_max = 100 - dalto_curso / otros_cursos_max * 100
diferencia_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

print('--------------------------')
print(f"el curso de dalto dura un {diferencia_min}% menos que el mas rapido")
print(f"el curso de dalto dura un {diferencia_max:.2f}% menos que el mas lento")
print(
    f"el curso de dalto dura un {diferencia_promedio:.2f}% menos que le promedio de los cursos"
)

# Calculando el tiempo innecesario eliminado en edición

tiempo_promedio_eliminado_otros = 100 - otros_cursos_promedio / crudo_promedio * 100
tiempo_promedio_eliminado_dalto = 100 - dalto_curso / crudo_dalto * 100

print('--------------------------')
print(f'el promedio de tiempo innecesario borrado en otros cursos es de {tiempo_promedio_eliminado_otros}% ')
print(f'el promeido de tiempo innecesario borrado por dalto es de un {tiempo_promedio_eliminado_dalto:.2f}%')

#Mostrando difenecias si el curso durara unas 10 horas 

print('--------------------------')
print(f'Ver 10 horas del curso de dalto equivale a ver {otros_cursos_promedio / dalto_curso * 10:.1f} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {dalto_curso / otros_cursos_promedio * 10:.1f} horas del curso de dalto')