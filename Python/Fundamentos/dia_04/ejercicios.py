#1. Concatenar las cadenas 'Thirty', 'Days', 'Of', 'Python' en una sola cadena, 'Thirty Days Of Python'.

a = 'Thirty'
b = 'Days'
c = 'Of'
d = 'Python'

result = a + ' ' + b + ' ' + c + ' ' + d
print(result) #Thirty Days Of Python

#2. Concatenar las cadenas 'Coding', 'For', 'All' en una sola cadena 'Coding For All'.

result = 'Coding ' + 'For ' +  'All'
print(result) #Coding For All

#3. Declarar una variable llamada company y asignarle el valor "Coding For All".

company = "Coding For All"

#4. Imprimir la longitud de la cadena usando len().

print(len(company)) #14

#5. Cambiar todos los caracteres a mayúsculas usando upper().

print(company.upper())

#6. Cambiar todos los caracteres a minúsculas usando lower().

print(company.lower())

#7. Usar capitalize(), title(), y swapcase() para dar formato a la cadena.

print(company.capitalize()) #Coding for all
print(company.title())      #Coding for all
print(company.swapcase())   #cODING fOR aLL

#8. Cortar (slice) la primera palabra de la cadena.

print(company[7:]) # For All

#9. Comprobar si la cadena contiene la palabra "Coding" usando find() o index().

print(company)
print(company.find("Coding")) # 0
print(company.index("Coding"))# 0
print( "Coding" in company)   # True

#10. Reemplazar la palabra "Coding" por "Python".

print(company.replace("Coding", "Python")) #Python For All

#11. Cambiar "Python for Everyone" a "Python for All".

phrase = "Python for Everyone" 
print(phrase.replace("Everyone", "All")) #Python for All

#12. Dividir la cadena 'Coding For All' usando espacio como separador.

a, b, c = company.split()
print(a, b, c) #Coding For All

#14. Dividir la cadena "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" usando la coma como separador.

text = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

print(text.split(", ")) # ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#15 ¿Cuál es el carácter en el índice 0 de la cadena "Coding For All"

print(company[0]) #C

#16 ¿Cuál es el último índice de la cadena "Coding For All"?

print(company[-1]) #l

#17 ¿Qué carácter está en el índice 10 de la cadena "Coding For All"?

print(company[10]) #" "

#18 Crear un acrónimo o abreviatura para el nombre "Python For Everyone".
phrase = "Python for Everyone"
print((phrase[0] + phrase[7] + phrase[11]).upper()) # PFE

#19 Crear un acrónimo o abreviatura para el nombre "Coding For All".
company = "Coding For All"
print((company[0] + company[7] + company[11]).upper()) # CFA

#20 Usar index() para determinar la posición de la primera aparición de la letra 'C' en "Coding For All".

print(company.index('C')) #0

#21 Usar index() para determinar la posición de la primera aparición de la letra 'F' en "Coding For All".

print(company.index('F')) #7

#22 Usar rfind() para determinar la posición de la última aparición de la letra 'l' en "Coding For All People".

text = "Coding For All People"
print(text.rfind('l')) #19

#23 Usar index() o find() para encontrar la posición de la primera aparición de la palabra "because" en la siguiente oración: 'You cannot end a sentence with because because because is a conjunction'.

prayer = 'You cannot end a sentence with because because because is a conjunction'
print(prayer.index('because')) #31 

#24 Usar rindex() para encontrar la posición de la última aparición de la palabra "because" en la siguiente oración: 'You cannot end a sentence with because because because is a conjunction'.

print(prayer.rfind('because')) #47 

#25 Cortar (slice) la frase "because because because" en la oración: 'You cannot end a sentence with because because because is a conjunction'

print(prayer[ prayer.index('because') : prayer.rfind('because') + len('because') ]) #because because because

#26 Verificar si 'Coding For All' empieza con el subcadena "Coding".

print(company.startswith('Coding')) # True

#27 Verificar si 'Coding For All' termina con el subcadena "coding".

print(company.endswith('coding')) # False

#28 La cadena ' Coding For All ' tiene espacios en blanco al principio y al final, eliminarlos.

new_company = ' Coding For All '
print(new_company)
print(new_company.strip(" "))

#29 ¿Cuál de las siguientes variables devuelve True al usar el método isidentifier()?
'''
30DaysOfPython
thirty_days_of_python
'''

a = '30DaysOfPython'
b = 'thirty_days_of_python'

print(a.isidentifier()) # False
print(b.isidentifier()) # True

#30 La siguiente lista contiene los nombres de algunas bibliotecas de Python: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Unir la lista con el carácter # y un espacio.

new_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'] 
print("#" + " #".join(new_list)) #  #Django #Flask #Bottle #Pyramid #Falcon


