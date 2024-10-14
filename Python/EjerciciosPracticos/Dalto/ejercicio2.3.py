# crear la serie fibonacci entre 0 y el numero dado

# creamos una función que recibe un número
def fibonacci(num):
    # creamos dos variables que almacenan los numero iniciales de la serie fibonacci
    a, b = 0, 1
    # creamos una lista para almacenar los valores empezando por un 0
    fibonacci_list = [0]
    # creamos un bucle para generar repeticiones
    for i in range(num):
        # validamos si b es mayor que el numero que recibimos por parámetro
        if b > num:
            # si b es mayor retornamos la lista donde almacenamos la secuencia
            return fibonacci_list
        # si b aun no es mayor
        else:
            # agregamos el valor actual de b a nuestra lista
            fibonacci_list.append(b)
            # reasignamos los valores de nuestras variables al tiempo ahora a pasa a tener el valor de b y b pasa a tener el valor de a + b
            a, b = b, a + b


print(fibonacci(21))
