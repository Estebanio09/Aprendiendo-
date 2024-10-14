#Declarar una lista vacía:

new_list = []

#Declarar una lista con más de 5 elementos:

new_list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']

#Encontrar la longitud de tu lista:

print(len(new_list)) #6

#Obtener el primer elemento, el elemento del medio y el último elemento de la lista:

print(new_list[0]) #apple
print(new_list[len(new_list)//2]) #date
print(new_list[-1]) #fig

#Declarar una lista llamada mixed_data_types (nombre, edad, altura, estado civil, dirección):

mixed_data_types = ['Esteban', 25, 1.76, False, 'calle 57 c # 284']

#Declarar una variable de lista llamada it_companies y asignar valores iniciales:

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#Imprimir el número de empresas en la lista:

print(len(it_companies)) #7 

#Imprimir la primera, la media y la última empresa:

print(it_companies[0]) #Facebook
print(it_companies[len(it_companies)  // 2]) #Apple
print(it_companies[-1]) #Amazon

#Imprimir la lista después de modificar una de las empresas:

it_companies[3] = 'BYD' 
print(it_companies) #['Facebook', 'Google', 'Microsoft', 'BYD', 'IBM', 'Oracle', 'Amazon']

#Agregar una empresa de TI a it_companies:

it_companies.append('HBO')
print(it_companies) #['Facebook', 'Google', 'Microsoft', 'BYD', 'IBM', 'Oracle', 'Amazon', 'HBO']

#Insertar una empresa de TI en el medio de la lista de empresas:

it_companies.insert(len(it_companies) // 2, 'Netflix')
print(it_companies) #['Facebook', 'Google', 'Microsoft', 'BYD', 'Netflix', 'IBM', 'Oracle', 'Amazon', 'HBO']

#Cambiar uno de los nombres de las empresas de TI a mayúsculas (¡excluyendo IBM!):

change_company = it_companies.index('Google')
print(change_company)
it_companies[change_company] = it_companies[change_company].upper() 
print(it_companies) #['Facebook', 'GOOGLE', 'Microsoft', 'BYD', 'Netflix', 'IBM', 'Oracle', 'Amazon', 'HBO']

#Unir las it_companies con una cadena '#; ':

joined_companies = '#; '.join(it_companies)
print(joined_companies) #      Facebook#; GOOGLE#; Microsoft#; BYD#; Netflix#; IBM#; Oracle#; Amazon#; HBO

#Comprobar si existe cierta empresa en la lista it_companies:

print('IBM' in it_companies) # True

#Ordenar la lista usando el método sort():

print(it_companies) #  ['Facebook', 'GOOGLE', 'Microsoft', 'BYD', 'Netflix', 'IBM', 'Oracle', 'Amazon', 'HBO']
it_companies.sort()
print(it_companies) #  ['Amazon', 'BYD', 'Facebook', 'GOOGLE', 'HBO', 'IBM', 'Microsoft', 'Netflix', 'Oracle']

#Invertir la lista en orden descendente usando el método reverse():

it_companies.reverse()
print(it_companies)  #  ['Oracle', 'Netflix', 'Microsoft', 'IBM', 'HBO', 'GOOGLE', 'Facebook', 'BYD', 'Amazon']

#Eliminar las primeras 3 empresas de la lista:

del it_companies[0:3]
print(it_companies)  #  ['IBM', 'HBO', 'GOOGLE', 'Facebook', 'BYD', 'Amazon']

#Eliminar las últimas 3 empresas de la lista:

del it_companies[-3:]
print(it_companies)  #  ['IBM', 'HBO', 'GOOGLE'

#Eliminar la empresa o empresas de TI del medio:
del it_companies[len(it_companies) // 2]
print(it_companies) # ['IBM', 'GOOGLE']

#Eliminar la última empresa de TI de la lista:
it_companies.pop()
print(it_companies) # ['IBM']

#Eliminar todas las empresas de TI de la lista:
it_companies.clear()
print(it_companies) #[]

# Destruir la lista de empresas de TI:
del it_companies

#Unir las siguientes listas:  
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

full_stack_list = front_end + back_end

#Después de unir las listas, copia la lista unida y asígnala a una variable full_stack. Luego inserta Python y SQL después de Redux.

full_stack = full_stack_list.copy()
full_stack.insert(full_stack.index('Redux') + 1 , 'Python')
full_stack.insert(full_stack.index('Redux') + 1 , 'SQL')

print(full_stack) # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'SQL', 'Python', 'Node', 'Express', 'MongoDB']

'''Ejercicios: Nivel 2'''

#Lista de edades de 10 estudiantes:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Ordenar la lista y encontrar la edad mínima y máxima: 

ages.sort()
print(ages) # [19, 19, 20, 22, 24, 24, 24, 25, 25, 26]
print(ages[0], ages[-1] )

# Agregar la edad mínima y máxima nuevamente a la lista:

ages.sort()
max_age =  ages[-1]
min_age = ages[0]

ages.append(max_age)
ages.append(min_age)
print(ages) # [19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 26, 19]

#Encontrar la edad mediana:

ages.sort()
print(ages[len(ages) // 2]) #24

#Encontrar la edad promedio:

average = sum(ages) // len(ages) 
print(average) #22

#Encontrar el rango de las edades:

ages.sort()
range = ages[0] + ages[-1]
print(range) #45

#Comparar el valor de (min - average) y (max - average), usar el método abs():

comparison = abs(min_age - average) - abs(max_age - average)
print(comparison) # -1

#Encontrar el o los países del medio en la lista de países:

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(countries[len(countries) // 2])

#Dividir la lista de países en dos listas iguales, si es par, si no, un país más para la primera mitad:

a, b, c, *scandic_countries = countries
print(a) #China
print(b) #Russia
print(c) #Russia
print(scandic_countries) #['Finland', 'Sweden', 'Norway', 'Denmark']