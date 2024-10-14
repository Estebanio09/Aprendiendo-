# retornar todos los numero primos en un rango dado por el usuario

# creamos una función que nos indicara si es primo


def es_primo(num):
    # recibimos el numero
    for i in range(2, num):
        # generamos un bucle que genera los numero del 2 al numero indicado
        if num % i == 0:
            # dividimos el numero indicado por todos los numero generados por nuestro bucle y si su residuo es cero significa que es divisible por otros números por lo que retornamos false
            return False

    return True  # si no se cumple la condición no es divisible por ningún otro numero aparte del 1 y de si mismo


# creamos una función que recibe un numero 
def primos(num):
    #creamos una lista donde almacenar los números 
    primos = []
    #creamos un bucle que genera los numero del 2 al numero indicado mas 1
    for i in range(2, num + 1): 
        #con un condicional llamamos nuestra primera función la cual retorna flase si no es primo y true si es primo 
        if es_primo(i):
            #almacenamos el numero en una lista si es primo 
            primos.append(i)
    #retornamos la lista que contiene los números primos que están en el rango indicado 
    return primos


print(primos(17))
