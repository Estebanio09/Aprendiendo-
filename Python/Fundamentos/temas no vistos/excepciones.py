### Excepciones

# es como evitamos que la ejecución de nuestro programa no se interrumpa

# es como vamos a manejar los errores des nuestro código

#  creamos la función para sumar
def sumar():
    while True:
        a = input("Numero 1: ")
        b = input("Numero 2: ")

        # con try indicamos que inicia nuestro manejo a un posible error en este caso que el usuario no ingrese un número
        try:
            resultado = int(a) + int(b)
        # except es donde escribimos el código que se ejecutara en durante el error con Exception generalizamos pero podemos especificar el tipo de errores podemos usar varios except para otros tipos de errores 
        # con as podemos nombrar el error para hacer algo 
        except Exception as e:
            print("Ingresa números")
            print(type(e).__name__)
        # else se ejecuta la final si no se presento un error
        else:
            break
        # finally se ejecuta siempre que finalice el manejo de excepciones 
        finally:
            print("Me ejecuto siempre...")

    return resultado


print(sumar())




class MiExcepcion(Exception):
    def __init__(self,err ) -> None:
        print(f"Cometiste el siguiente error {err}")
        

try:
    a = input("Numero 1: ")
    b = input("Numero 2: ")
    resultado = int(a) + int(b)
    
    
except Exception as e:
    MiExcepcion(e)







