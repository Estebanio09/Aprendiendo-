first_name = "Esteban"               # Variable de primer nombre
last_name = "Martinez"               # Variable de apellido   
full_name = first_name + last_name   # Nombre completo (concatenación de first_name y last_name)
country = "Colombia"                 # Variable de país
city = "Bogotá"                      # Variable de ciudad
age = 25                             # Variable de edad
year = 2024                          # Variable de año   
is_married = False                   # Variable de estado civil (booleano)   
is_true = True                       # Variable booleana
is_light_on = False                  # Otra variable booleana

first_name, last_name, country, age, is_married = "Juan", "Pérez", "Mexico", 25, True

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print("La longitud de tu nombre es ", len(first_name))
print(len(first_name) == len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

pi = 3.1416 
circle_radio = 30

area_of_circle = (circle_radio ** 2) * pi 
print(area_of_circle)  

circum_of_circle = (pi * 2) * circle_radio 
print(circum_of_circle)

user_radio = input("Ingresa el radio del círculo ")
user_area = (int(user_radio) ** 2) * pi
print("El area del círculo es " , int(user_area))

first_name = input("¿Cual es tu nombre? ")
last_name = input("¿Cual es tu apellido? ")
last_country = input("¿Cual es tu país? ")
age = input("¿Cual es tu edad? ")



