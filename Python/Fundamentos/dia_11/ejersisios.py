# Declara una función llamada add_two_numbers. Toma dos parámetros y devuelve la suma.


def add_two_numbers(num1, num2):
    return num1 + num2


# print(add_two_numbers(5,8)) #13

# El área de un círculo se calcula de la siguiente manera: área = π x r x r. Escribe una función que calcule el área de un círculo, area_of_circle.


def area_of_circle(radio):
    return 3.14 * radio**2


# print(area_of_circle(30)) #2826.0

# Escribe una función llamada add_all_nums que tome un número arbitrario de argumentos y sume todos los argumentos. Verifica si todos los elementos de la lista son de tipo numérico. Si no, da una retroalimentación adecuada.


def add_all_nums(*nums):
    for num in nums:
        if type(num) not in (int, float):
            return "todos deben ser numeros"
    return sum(nums)


# print(add_all_nums(2,5,2)) # 9

# La temperatura en °C se puede convertir a °F usando esta fórmula: °F = (°C x 9/5) + 32. Escribe una función que convierta de °C a °F, convert_celsius_to_fahrenheit.


def convert_celsius_to_fahrenheit(celsius):
    return f"{celsius}° celsius es {(celsius * 9/5) + 32 }° Fahrenheit"


# print(convert_celsius_to_fahrenheit(25)) #25° celsius es 77.0° fahrenheit

# Escribe una función llamada check_season, toma un parámetro de mes y devuelve la estación: Otoño, Invierno, Primavera o Verano.


def check_season(mes):
    if type(mes) is str:
        mes = mes.capitalize()
        if mes in ["Septiembre", "Octubre", "Noviembre"]:
            return "Es Otoño"
        elif mes in ["Diciembre", "Enero", "Febrero"]:
            return "Es Invierno"
        elif mes in ["Marzo", "Abril", "Mayo"]:
            return "Es Primavera"
        elif mes in ["Junio", "Julio", "Agosto"]:
            return "Es Verano"

    return f"{mes} no es un mes valido"


# print(check_season(input('Ingresa un mes ')))

# Declara una función llamada print_list. Toma una lista como parámetro e imprime cada elemento de la lista.

datos = [
    {"nombre": "Ana", "edad": 25, "ocupación": "Ingeniera", "ciudad": "Madrid"},
    {"nombre": "Luis", "edad": 30, "ocupación": "Doctor", "ciudad": "Barcelona"},
    {"nombre": "María", "edad": 22, "ocupación": "Estudiante", "ciudad": "Valencia"},
    {"nombre": "Pedro", "edad": 28, "ocupación": "Programador", "ciudad": "Sevilla"},
    {"nombre": "Carla", "edad": 35, "ocupación": "Abogada", "ciudad": "Bilbao"},
    {"nombre": "Jorge", "edad": 40, "ocupación": "Arquitecto", "ciudad": "Zaragoza"},
    {"nombre": "Lucía", "edad": 27, "ocupación": "Diseñadora", "ciudad": "Granada"},
    {"nombre": "Alberto", "edad": 32, "ocupación": "Profesor", "ciudad": "Alicante"},
    {"nombre": "Marta", "edad": 29, "ocupación": "Consultora", "ciudad": "Santander"},
]


def print_list(lista):
    for item in lista:
        print(item)


# print_list(datos)

# Declara una función llamada reverse_list. Toma un array como parámetro y devuelve el array invertido (usa bucles).


def reverse_list(lista):
    new_list = []
    for i in range(len(lista) - 1, -1, -1):
        new_list.append(lista[i])
    return new_list


print(reverse_list([1, 2, 3, 4, 5]))

print(reverse_list(["A", "B", "C"]))

# Declara una función llamada capitalize_list_items. Toma una lista como parámetro y devuelve la lista con los elementos en mayúscula.


def capitaliza_list_items(lista):
    new_list = []
    for i in lista:
        new_list.append(i.upper())
    return new_list


print(capitaliza_list_items(list("abcdefghijklmnopqrstuvwxyz2")))

# Declara una función llamada add_item. Toma una lista y un parámetro item. Devuelve la lista con el item agregado al final.


def add_item(lista, item):
    lista.append(item)
    return lista


numbers = [2, 3, 7, 9]

print(add_item(numbers, 5))
print(add_item(["C", "B", "A"], "G"))


# Declara una función llamada remove_item. Toma una lista y un item como parámetros. Devuelve la lista con el item eliminado.
def remove_item(lista, item):
    new_list = lista.copy()
    new_list.remove(item)
    return new_list


print(remove_item(numbers, 3))
print(remove_item(["C", "B", "A", "G"], "B"))

food_staff = ["Potato", "Tomato", "Mango", "Milk"]

print(remove_item(food_staff, "Mango"))

# Declara una función llamada sum_of_numbers. Toma un número como parámetro y suma todos los números en ese rango.


def sum_of_numbers(num):
    sum_numbers = 0
    for i in range(num + 1):
        sum_numbers += i
    return sum_numbers


print(sum_of_numbers(100))

# Declara una función llamada sum_of_odds. Toma un número como parámetro y suma todos los números impares en ese rango.


def sum_of_odds(num):
    sum_number = 0
    for i in range(num + 1):
        if i % 2 != 0:
            sum_number += i
    return sum_number


print(sum_of_odds(30))


# Declara una función llamada sum_of_even. Toma un número como parámetro y suma todos los números pares en ese rango.


def sum_of_even(num):
    sum_numbers = 0
    for i in range(num + 1):
        if i % 2 == 0:
            sum_numbers += i
    return sum_numbers


print(sum_of_even(10))

# Declara una función llamada evens_and_odds. Toma un número entero positivo como parámetro y cuenta la cantidad de números pares e impares en ese rango.


def evens_and_odds(num):
    even_numbers = 0
    odd_numbers = 0
    for i in range(num + 1):
        if i % 2 != 0:
            odd_numbers += 1
        else:
            even_numbers += 1
    return (
        f"El número de pares es {even_numbers} y el numero de impares es {odd_numbers}"
    )


print(evens_and_odds(100))


# Llama a tu función is_empty, toma un parámetro y verifica si está vacío o no.


def is_empty(item=False):
    if bool(item):
        return "El elemento no esta vacío"
    else:
        return "El elemento esta vacío"


print(is_empty(""))
