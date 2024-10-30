# crear un juego donde se pueda crear personajes fusionar personajes y mostrar personajes

# crear la clase el molde de nuestros personajes
class Personaje:
    # Definimos las propiedades de nuestros personajes
    def __init__(self, nombre, poder, velocidad, agilidad, rango) -> None:
        self.nombre = nombre
        self.poder = poder
        self.velocidad = velocidad
        self.agilidad = agilidad
        self.rango = rango

    # crear la representación de nuestros personajes para verlos en print
    def __repr__(self):
        return f"{self.nombre} (Poder: {self.poder}, Velocidad: {self.velocidad}, Agilidad: {self.agilidad}, Rango: {self.rango}"

    # creamos el método add para definir como se van a sumar
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nuevo_poder = round(((self.poder + otro_pj.poder) / 2) ** 1.34)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad) / 2) ** 1.34)
        nueva_agilidad = round(((self.agilidad + otro_pj.agilidad) / 2) ** 1.34)
        nuevo_rango = round(((self.rango + otro_pj.rango) / 2) ** 1.34)
        return Personaje(
            nuevo_nombre, nuevo_poder, nueva_velocidad, nueva_agilidad, nuevo_rango
        )


# creamos una función para mostrar el menu
def mostrar_menu():
    print(
        "\n1. Crear personaje\n2. Fusionar Personajes\n3. Mostrar personajes\n4. Salir\n"
    )


# creamos una función para crear personajes y recibimos la estructura donde almacenaremos la información
def crear_personaje(personajes_creados):
    # solicitamos al usurario ingresar los datos del personaje con strip(" ") eliminamos los espacios en blanco antes y al final del nombre
    nombre = input("\nIngresa el nombre del personaje: ").strip(" ").capitalize()
    # con int() pasamos de str a entero
    poder = int(input("Ingresa el poder del personaje: ").strip(" "))
    velocidad = int(input("Ingresa la velocidad del personaje: ").strip(" "))
    agilidad = int(input("Ingresa la agilidad del personaje: ").strip(" "))
    rango = int(input("Ingresa el rango del personaje: ").strip(" "))
    # creamos el personaje instanciando a Personaje y le pasamos las variables
    personaje_creado = Personaje(nombre, poder, velocidad, agilidad, rango)
    # almacenamos el personaje/objeto a una estructura de datos que llega por parámetro
    personajes_creados.append(personaje_creado)
    print(f"\nPersonaje {nombre} fue creado exitosamente\n")

# definimos una función para fusionar nuestros personajes // sumar, recibimos la estructura de datos donde se almacenan nuestros personajes 
def fusionar_personajes(personajes_creados):
    # validamos la longitud de la estructura si tiene menos de dos personaje imprimimos algo
    if len(personajes_creados) < 2:
        print("Debes tener mínimo dos personajes para fusionar\n")
    else:
        # llamamos al función mostrar personajes para indicar al usuario los personajes a fusionar 
        mostrar_personajes(personajes_creados)
        # solicitamos la posición del personaje a fusionar 
        num_pj1 = int(input("Selecciona el primer personaje a fusionar de la lista: "))
        num_pj2 = int(input("Selecciona el segundo personaje a fusionar de la lista: "))
        # validamos que el numero ingresado sea valido ya que no puede ser menor a uno y no puede ser mayor a la longitud de nuestros personajes 
        if (
            1 <= num_pj1 <= len(personajes_creados)
            and 1 <= num_pj2 <= len(personajes_creados)
            and num_pj1 != num_pj2 # validamos que no sean iguales 
        ):
            #obtenemos a los personajes mediante la posición 
            personaje1 = personajes_creados[num_pj1 - 1]
            personaje2 = personajes_creados[num_pj2 - 1]
            # sumamos o concatenamos a los personajes mediante el método __add__ que definimos en nuestra clase esto determino el comportamiento 
            personaje_fusionado = personaje1 + personaje2
            # agregamos nuestro nuevo personaje a nuestra lista 
            personajes_creados.append(personaje_fusionado)
            print(f"Fusión exitosa el nuevo personaje es {personaje_fusionado}")
        else:
            # si no se cumplen las condiciones imprimimos el mensaje 
            print("Selección inválida.")

# definimos la función que mostrara nuestros personajes recibe por parámetro la lista donde se almacenan
def mostrar_personajes(personajes_creados):
    print("\n")
    # validamos si la lista esta vacía de ser así mostramos mensaje en consola
    if len(personajes_creados) == 0:
        print("Aun no has creado un personaje\n")
    else:
        # si contiene personajes los imprimimos mediante un bucle numerate() devuelve el indice y el contenido el cual asignamos a las variables i y personaje 
        print("Personajes: ")
        for i, personaje in enumerate(personajes_creados):
            print(f"{i+1}. {personaje}")

#definimos una función que ejecuta nuestro juego 
def juego():
    # creamos nuestra lista donde almacenar los personajes 
    personajes_creados = []
    # creamos un bucle para mantener nuestro programa funcionando en True para que solo si pasamos un break se finalice 
    while True:
        # llamamos a la función mostrar menu el cual lo imprime 
        mostrar_menu()
        # pedimos que se ingrese una opción del menu 
        opcion = input("Seleccione una opción: ")
        # validamos que la opcion sea valida y compramos con if dependiendo de la selección llamamos las fusiones para realizar una acción 
        if opcion == "1":
            crear_personaje(personajes_creados)
        elif opcion == "2":
            fusionar_personajes(personajes_creados)
        elif opcion == "3":
            mostrar_personajes(personajes_creados)
        elif opcion == "4":
            break
        else:
            print("Elije una opción valida\n")

# iniciamos nuestro programa =)
juego()
