"""
                Python

- Comentario de varias lineas
"""

"""
- Comentario de varias lineas 
- Nueva linea 
"""

# comentario


# variables
nombre = "Esteban"
edad = 25
altura = 1.70
casado = False


# funciones del sistema
# print()  = imprime en pantalla
print(nombre)  # Esteban
print(edad)  # 25
# type()  imprime el tipo de dato
print(type(nombre))  # <class 'str'>
print(type(edad))  # <class 'int'>


# operadores aritméticos

dinero = 10000
chetos = 3500
merienda = 5000

# tienda

# resta
vueltos = dinero - chetos
print(vueltos)  # 6500

# suma
dinero = vueltos + merienda
print(dinero)  # 11500

# producto
ahorro = merienda * 7
print(ahorro)  # 35000

# sumar y reasignar valor
dinero += ahorro
print(dinero)  # 46500

# division
banco = dinero / 2
print(banco)  # 23250.0

# strings // cadenas de texto
apellido = "Velez"

# concatenar
nombre_completo = nombre + apellido
print(nombre_completo)  # EstebanVelez
nombre_completo = nombre + " " + apellido
print(nombre_completo)  # Esteban Velez

print("Hola, mundo")  # Hola, mundo
# formatear
print(f"Hola, {nombre} ¿cómo estás?")  # Hola, Esteban ¿cómo estás?

# Operador de comparación

print(dinero)  # 46500
print(chetos)  # 3500

print(dinero > chetos)  # True

print(banco)  # 23250.0

print(banco < dinero)  # True
print(dinero < banco)  # False

dinero = 5000
banco = 5000

print(dinero == banco)  # True
print(dinero == chetos)  # False
print(chetos)  # 3500

print(chetos <= dinero)  # True
print(dinero >= banco)  # True

# Operadores lógicos
# or // o 
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

condicion_1 = True
condicion_2 = False


