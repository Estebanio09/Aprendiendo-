#Calcular los tiempos en los que puede tardar una persona en decir una frase

#una persona promedio puede decir dos palabras por segundo

#pedir al usuario que diga una frase y calcular el tiempo que le tardaría en decir la misma 

frase = input('Dime una frase: ') # pedimo al usuario ingresar una frase y la almacenamos en una variable
list_frase = frase.split(' ') # tomamos la cadena y la dividimos en una lista usando los especios como referencia 
print(f'Puedes tardar un promedio de {len(list_frase) // 2} segundos en decir esta frase')# imprimimos una frase y en le formarto calculamos el promedio de 2 palabras por segundo con la longitud de la lista la cual nos indica la cantidad de palabras



