# Módulo datetime en Python

# Python cuenta con el módulo datetime para manejar fechas y horas.

from datetime import datetime, date, time, timedelta
# print(dir(datetime))

"""
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
"""

# Con los comandos dir o help, puedes ver las funciones disponibles en un módulo. En datetime, nos enfocaremos en date, datetime, time y timedelta.

# Obtener Información de Fecha y Hora


now = datetime.now()
print(now)  # Ejemplo: 2021-07-08 07:34:46.549883

# Obtener componentes individuales
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp() # representación única de un tiempo formato estándar 

print(day, month, year, hour, minute)  # 29 10 2024 3 55
print("timestamp", timestamp)  # timestamp 1730192126.388094
print(f"{day}/{month}/{year}, {hour}:{minute}")  # 8/7/2021, 7:38

# El timestamp es el número de segundos desde el 1 de enero de 1970 en UTC.

# Formateo de Fechas con strftime

new_year = datetime(2020, 1, 1) # establecemos una fecha y en base a esto podemos comenzar con una fecha especifica 
print(new_year)  # 2020-01-01 00:00:00

# Formato personalizado
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute

print(f"{day}/{month}/{year}, {hour}:{minute}")  # 1/1/2020, 0:0

# Para formatear la fecha y la hora, se utiliza el método strftime.

# Fecha y hora actual
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)

# Formato mm/dd/YY H:M:S
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print("time one:", time_one)

# Formato dd/mm/YY H:M:S
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
print("time two:", time_two)

# Convertir una Cadena en Fecha y Hora con strptime

# strptime convierte una cadena de texto a un objeto datetime según el formato especificado.


date_string = "5 December, 2019"
print("date_string =", date_string)  # date_string = 5 December, 2019

# Convertir a objeto de fecha
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)  # date_object = 2019-12-05 00:00:00

# Uso de date desde el módulo datetime

# El módulo datetime también permite trabajar solo con fechas usando date.

# Crear una fecha específica
d = date(2020, 1, 1)
print(d)

# Fecha actual
print("Current date:", d.today())  # Ejemplo: 2019-12-05

# Componentes de la fecha actual
today = date.today()
print("Current year:", today.year)  # Ejemplo: 2019
print("Current month:", today.month)  # Ejemplo: 12
print("Current day:", today.day)  # Ejemplo: 5

# Objetos de Tiempo para Representar Horas

# El módulo datetime permite crear objetos de time para representar horas.


# Hora por defecto (00:00:00)
a = time()
print("a =", a)  # a = 00:00:00

# Especificar hora, minutos y segundos
b = time(10, 30, 50)
print("b =", b)  # b = 10:30:50

# Especificar con argumentos de palabras clave
c = time(hour=10, minute=30, second=50)
print("c =", c)  # c = 10:30:50

# Incluyendo microsegundos
d = time(10, 30, 50, 200555)
print("d =", d)  # d = 10:30:50.200555

# Diferencia entre Dos Fechas

# Es posible calcular la diferencia entre dos fechas usando operadores de resta.

today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today

print("Time left for new year: ", time_left_for_newyear)  # 27 días, 0:00:00

# También funciona con objetos datetime para incluir horas y minutos.

t1 = datetime(year=2019, month=12, day=5, hour=0, minute=59, second=0)
t2 = datetime(year=2020, month=1, day=1, hour=0, minute=0, second=0)
diff = t2 - t1

print("Time left for new year:", diff)  # 26 días, 23:01:00

# Diferencia entre Dos Momentos con timedelta

# El objeto timedelta permite definir intervalos de tiempo y calcular diferencias.


t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2

print("t3 =", t3)  # t3 = 86 días, 22:56:50
