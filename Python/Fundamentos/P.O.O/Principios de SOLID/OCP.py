"""
Open/Close principle
"""

# Abiertas para la extensión cerradas para la modificación

from uuid import uuid4


class Persona:
    def __init__(self, nombre: str, edad: int, email: str, numero_whatsapp: int = None):
        self.id = uuid4()
        self.__nombre = nombre
        self.__edad = edad
        self.__email = email
        self.__numero_whatsapp = numero_whatsapp

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def email(self):
        return self.__email

    @property
    def numero_whatsapp(self):
        return self.__numero_whatsapp

    # Definimos la representación del objeto lo que muestra la momento de imprimir
    def __repr__(self):
        return f"Persona ({self.nombre}, {self.edad}, {self.email})"


# creamos la plantilla para las clases notificadoras / esta esta abierta para que se creen mas clases para notificar pero no es necesario modificarla en este ejemplo esta cerrada a esto
class Notificador:
    def __init__(self, usuario: Persona, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    # establecemos un método obligatorio en las subclases que hereden
    def notificar(self):
        raise NotImplementedError


class NotificadorEmail(Notificador):
    def __init__(self, usuario, mensaje):
        super().__init__(usuario, mensaje)

    def notificar(self):
        print(
            f"Se envío el email correctamente\nMensaje: {self.mensaje}\nEnviado a: {self.usuario}"
        )


class NotificadorWhatsApp(Notificador):
    def __init__(self, usuario, mensaje):
        super().__init__(usuario, mensaje)

    def notificar(self):
        if self.usuario.numero_whatsapp is not None:
            print(
                f"Se envío el WhatsApp correctamente\nMensaje: {self.mensaje}\nEnviado a: {self.usuario.nombre}\nNumero: {self.usuario.numero_whatsapp}"
            )
        else:
            print(
                f"El usuario {self.usuario.nombre}, no tiene un número de WhatsApp registrado"
            )


user = Persona("Esteban", 25, "esteban@esteban.com")
print(user)  # (Esteban, 25, esteban@esteban.com)
user2 = Persona("Camilo", 27, "camilo@camilo.com", 3128858888)
print(user2) # Persona (Camilo, 27, camilo@camilo.com
notificar_user_email = NotificadorEmail(user, "Hola maní como estas")
notificar_user_email.notificar()
notificar_user_whatsapp = NotificadorWhatsApp(user, "hola mani")
notificar_user_whatsapp.notificar()  # El usuario Esteban, no tiene un número de WhatsApp registrado
NotificadorWhatsApp(user2,"mani como es").notificar()
"""
Se envío el WhatsApp correctamente
Mensaje: mani como es
Enviado a: Camilo
Numero: 3128858888
"""

# definimos clases especificas para métodos específicos como lo indica SRP, ahora como podemos ver la clase Notificador no sera modificada ya que si es necesario agregar o cambiar eso lo se realizara en la clases hijas que son las que definen el método para notificar el como mientras que nuestra clase padre Notificador da una platilla de las propiedades y especifica el método obligatorio 