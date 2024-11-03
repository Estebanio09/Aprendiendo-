import openai


openai.api_key = ":'v"
system_rol = "Eres un analizador de sentimientos, yo te paso mensajes y tu analizas el sentimiento en la frase pueden ser negativas, neutrales o positivas ahora para la respuesta si es negativa es -1 si es neutral es 0 y si es positiva 1 las respuestas como ves son numeros dependiendo del grado de sentimiento puedes indicar la respuesta si es negativo puedes indicar su grado en escala de 0 a -1, neutral solo es 0 y positivo en escala de 0 a 1 las respuestas pueden tener máximo 4 caracteres "
mensajes = [{"role": "system", "content": system_rol}]


# creamos la clase sentimiento recibe el nombre y el color
class Sentimiento:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    # por medio del str definimos como se imprime en consola
    def __str__(self):
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color, self.nombre)


# creamos la clase analizadora que recibe una lista de rangos que puede mutar eso hace que no sea necesario modificar nuestra clase
class AnalizadorDeSentimientos:
    def __init__(self, rangos):
        self.rangos = rangos

    # analizar es un método que recibe un dato polaridad que es un numero float por medio de un bucle recorre los rangos
    def analizar_sentimientos(self, polaridad):
        # recorre rangos sacando el rango una tupla de dos floats
        for rango, sentimiento in self.rangos:
            # valida si el número en rango[0] es menor a polaridad y que rango[1] sea mayor o igual una vez encuentre en rango cual se ajusta
            if rango[0] < polaridad <= rango[1]:
                # retorna la instancia de sentimiento que en rango hace referencia a Sentimiento y por medio de su método especial __str__ se imprime con el formato pre establecido
                return sentimiento
        return Sentimiento("Muy Negativo", "31")


rangos = [
    ((-0.6, -0.3), Sentimiento("Negativo", "31")),
    ((-0.3, -0.1), Sentimiento("Algo Negativo", "31")),
    ((-0.1, 0.1), Sentimiento("Neutral", "33")),
    ((0.1, 0.4), Sentimiento("Algo Positivo", "32")),
    ((0.4, 0.9), Sentimiento("Positivo", "32")),
    ((0.9, 1), Sentimiento("Muy Positivo", "32")),
]
analizador = AnalizadorDeSentimientos()

while True:
    user_prompt = input("\x1b[1;33m" + "\nDime algo :" + "\x1b[0;37m")
    mensajes.append({"role": "user", "content": user_prompt})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=mensajes,
        max_tokens=8,
    )

    respuesta = completion.choices[0].message["content"]
    mensajes.append({"role": "assistant", "content": respuesta})

    sentimiento = analizador.analizar_sentimientos(float(respuesta))
    print(sentimiento)
