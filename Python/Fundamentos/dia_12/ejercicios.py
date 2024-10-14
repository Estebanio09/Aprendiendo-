from random import randint , choice
import string


# Escribe una función que genere un random_user_id de seis dígitos o caracteres.

"""def random_user_id ():
    character_list = string.ascii_letters + string.digits
    num = len(character_list)
    password = ''
    for i in range(6):
        j = randint(0, num - 1)
        password = password + str(character_list[j])      
    return password"""

#print(random_user_id())


'''def random_user_id():
    # Crear una lista de caracteres (letras y dígitos)
    character_list = string.ascii_letters + string.digits
    # Generar la contraseña usando random.choice() para elegir aleatoriamente caracteres
    password = ''.join(choice(character_list) for i in range(6))
    return password

print(random_user_id())

#Modifica el ejercicio anterior. Declara una función llamada user_id_gen_by_user. No toma parámetros, pero toma dos entradas usando input(). Una de las entradas es el número de caracteres y la segunda entrada es el número de IDs que deben generarse.

def user_id_gen_by_user():
    character_list = string.ascii_letters + string.digits
    cantidad = int(input('Cuantos ID\'s necesitas: ' ))
    caracteres = int(input('Cuantos caracteres deben tener los ID\'s: '))
    for i in range(cantidad):
        print(''.join(choice(character_list) for i in range(caracteres)))'''
        
    
#user_id_gen_by_user()


# Función para generar un solo ID
def generate_user_id(length):
    character_list = string.ascii_letters + string.digits
    return ''.join(choice(character_list) for _ in range(length))

# Función principal que toma los datos de entrada y genera los IDs
def user_id_gen_by_user():
    try:
        num_ids = int(input("¿Cuántos ID's necesitas? "))
        num_characters = int(input("¿Cuántos caracteres deben tener los ID's? "))
        
        # Validación de que los valores sean positivos
        if num_ids <= 0 or num_characters <= 0:
            print("Por favor, introduce números positivos.")
            return
        
        # Generar y mostrar los ID's
        for _ in range(num_ids):
            print(generate_user_id(num_characters))
    except ValueError:
        print("Entrada no válida. Por favor, introduce números enteros.")
    
# Llamada a la función
#user_id_gen_by_user()

#Escribe una función llamada rgb_color_gen. Generará colores RGB (3 valores que varían entre 0 y 255 cada uno).

def rgb_color_gen():
     return f'rgb({randint(0,255)}, {randint(0,255)}, {randint(0,255)})'

def hexa_color_gen():
    characters_list = '0123456789abcdef'
    return '#'+''.join(choice(characters_list) for _ in range(6))

#print(rgb_color_gen())


#Escribe una función list_of_hexa_colors que devuelva cualquier cantidad de colores hexadecimales en un arreglo (seis números hexadecimales escritos después de #. El sistema numérico hexadecimal está compuesto por 16 símbolos: 0-9 y las primeras 6 letras del alfabeto, a-f).



def list_of_hexa_colors ( ):
    #es crea la lista con los valores existentes en los colores exa 
    characters_list = '0123456789abcdef'
    #creo la lista que retornare 
    new_list = []
    #creo un bucle que para generar una cantidad aleatoria de colores 
    for _ in range(randint(1, 10)):
        #genero colores tomando caracteres aleatorios de mi lista de caracteres con un bucle que se repite en 6 ocasiones y los junto con un join y los concateno con + # y los agrego a new_list con un append 
        new_list.append('#'+''.join(choice(characters_list) for _ in range(6)))
    #retorno mi lista con los colores 
    return new_list

#print(list_of_hexa_colors())

#Escribe una función list_of_rgb_colors que devuelva cualquier cantidad de colores RGB en un arreglo.

def list_of_rgb_colors ():
    new_list = []
    for _ in range(randint(1, 10)):
        new_list.append(rgb_color_gen())
    return new_list

#print(list_of_rgb_colors())

#Escribe una función generate_colors que pueda generar cualquier número de colores hexadecimales o RGB.

def generate_colors(tipo , n):
    new_list = []
    try:
        if tipo == 'hexa':
            for _ in range(n):
                new_list.append(hexa_color_gen())
            return new_list
        elif tipo == 'rgb':
            for _ in range(n):
                new_list.append(rgb_color_gen())
            return new_list
        else:
            return 'Selecciona un tipo válido: "hexa" o "rgb"'
    except Exception:
        return 'cantidad no valida'

def generar_colores1(tipo, n):
    # Validación de tipo
    if not isinstance(n, int) or n <= 0:
        return 'El número de colores debe ser un entero positivo'
    
    new_list = []
    
    # Selección del generador de color según el tipo
    if tipo == 'hexa':
        generador = hexa_color_gen
    elif tipo == 'rgb':
        generador = rgb_color_gen
    else:
        return 'Selecciona un tipo válido: "hexa" o "rgb"'
    
    # Bucle para generar los colores
    for _ in range(n):
        new_list.append(generador())
    
    return new_list

#print(generate_colors('hexa', 7))