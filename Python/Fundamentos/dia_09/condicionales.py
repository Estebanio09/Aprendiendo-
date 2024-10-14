#####Condicionales#####

"""
Por defecto, las sentencias en un script de Python se ejecutan secuencialmente de arriba hacia abajo. Si la lógica del procesamiento lo requiere, el flujo secuencial de ejecución puede alterarse de dos maneras:

#Ejecución condicional: un bloque de una o más sentencias se ejecutará si cierta expresión es verdadera.
#Ejecución repetitiva: un bloque de una o más sentencias se ejecutará repetitivamente mientras cierta expresión sea verdadera.
"""

#           #####   Condición If

#En Python y otros lenguajes de programación, la palabra clave if se usa para verificar si una condición es verdadera y ejecutar el bloque de código. Recuerda la indentación después de los dos puntos.

# Sintaxis
'''
if condición:
    este bloque de código se ejecuta si la condición es verdadera
'''

a = 3
if a > 0:
    print('A es un número positivo') # A es un número positivo

#Como puedes ver en el ejemplo anterior, 3 es mayor que 0. La condición fue verdadera y el bloque de código se ejecutó. Sin embargo, si la condición es falsa, no veremos ningún resultado. Para ver el resultado de la condición falsa, debemos tener otro bloque, que será else.

#           #####   If Else

#Si la condición es verdadera, se ejecutará el primer bloque, si no, se ejecutará el bloque else.

'''
# Sintaxis
if condición:
    este bloque de código se ejecuta si la condición es verdadera
else:
     este bloque de código se ejecuta si la condición es falsa

'''

a = 3
if a < 0:
    print('A es un número negativo')
else:
    print('A es un número positivo') #A es un número positivo

#La condición anterior resulta ser falsa, por lo tanto, se ejecutó el bloque else. ¿Y qué pasa si nuestra condición tiene más de dos casos? Podemos usar elif.

#               ####  If Elif Else

#En nuestra vida diaria, tomamos decisiones constantemente. No solo verificamos una o dos condiciones, sino múltiples condiciones. De manera similar, en la programación también existen múltiples condiciones. Usamos elif cuando tenemos varias condiciones.

'''
# Sintaxis
if condición:
    código
elif condición:
    código
else:
    código
'''

a = 0
if a > 0:
    print('A es un número positivo')
elif a < 0:
    print('A es un número negativo')
else:
    print('A es cero') #A es cero

#               ###### Sintaxis abreviada (Short Hand)
'''
código si condición else código
'''
a = 3
print('A es positivo') if a > 0 else print('A es negativo') # A es positivo

#                  #####    Condiciones anidadas
#Las condiciones pueden anidarse.

'''
if condición:
    código
    if condición:
        código
'''

a = 0
if a > 0: # a no es mayor 0
    if a % 2 == 0:
        print('A es un número entero positivo y par')
    else:
        print('A es un número positivo')
elif a == 0: # a es igual a 0 
    print('A es cero') #A es cero
else:
    print('A es un número negativo')

#Podemos evitar escribir condiciones anidadas usando operadores lógicos como and.

#           #####   Condiciones con Operadores Lógicos

##### Condiciones con Operadores and

'''
if condición and(y) condición:
    código
'''

a = 0
if a > 0 and a % 2 == 0: # a no es mayor a cero y el resto de a ÷ 2 es cero 
    print('A es un número entero positivo y par')
elif a > 0 and a % 2 !=  0: # a no es mayor a cero y el resto de a ÷ 2 no es cero 
    print('A es un número positivo')
elif a == 0: # a es igual a 0 
    print('A es cero') #  es cero
else:
    print('A es negativo')

#### Condiciones con Operadores or

'''
if condición or(o) condición:
    código
'''

usuario = 'James'
nivel_acceso = 3
if usuario == 'admin' or nivel_acceso >= 4:
    print('Acceso concedido')
else:
    print('Acceso denegado') # Acceso denegado

