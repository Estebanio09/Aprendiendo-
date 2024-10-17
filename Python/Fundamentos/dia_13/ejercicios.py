#Filtrar solo números negativos y ceros en una lista usando comprensión de listas:
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print([i for i in numbers if i < 1]) #[-4, -3, -2, -1, 0]

#Aplanar la siguiente lista de listas de listas a una lista unidimensional:
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print([num for list1 in list_of_lists for list2 in list1 for num in list2]) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

#Usando comprensión de listas, crea la siguiente lista de tuplas:
"""
[(0, 1, 0, 0, 0, 0, 0),
 (1, 1, 1, 1, 1, 1, 1),
 (2, 1, 2, 4, 8, 16, 32),
 (3, 1, 3, 9, 27, 81, 243),
 (4, 1, 4, 16, 64, 256, 1024),
 (5, 1, 5, 25, 125, 625, 3125),
 (6, 1, 6, 36, 216, 1296, 7776),
 (7, 1, 7, 49, 343, 2401, 16807),
 (8, 1, 8, 64, 512, 4096, 32768),
 (9, 1, 9, 81, 729, 6561, 59049),
 (10, 1, 10, 100, 1000, 10000, 100000)]
"""
print ([(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)])

#Aplanar la siguiente lista a una nueva lista: [['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
countries_list = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print([[country.upper(),country[:3].upper(), city.upper()] for countires in countries_list for country, city in countires]) 
#[['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

#Cambiar la lista a una lista de diccionarios:
"""
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]
"""
print([{'country' : country.upper(), 'city' : city.upper() } for countires in countries_list for country, city in countires])
#[{'country': 'FINLAND', 'city': 'HELSINKI'}, {'country': 'SWEDEN', 'city': 'STOCKHOLM'}, {'country': 'NORWAY', 'city': 'OSLO'}]

#Cambiar la siguiente lista de listas a una lista de cadenas concatenadas:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
print([f"{name} {last_name}" for name_list in names for name, last_name in name_list])
#['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']