#Una función que indique quién es el profesor y el asistente, solicita los nombres y la edad de cada participante ahora el mayor será el profe y el menor será el asistente al llamar la función debes especificar la cantidad de estudiantes 

def profe_asistente ( numero_estudiantes ):
    # declaramos la funcion y estabelcemos el parametro de la cantidad de estudiantes
    
    
    participantes = [] 
    # creamos una lista donde almacenar los participantes
    
    
    for estudiante in range(numero_estudiantes): 
        # creamos un bucle para solicitar los datos se repetira tantas veces como estudiantes participen 
        
        
        nombre = input('Nombre del estudiante: ') 
        #almacenamos el nombre 
        
        
        edad = int(input('Ingresa la edad del estudiante: ')) 
        # Almacenamos la edad 
        
        
        participantes.append(( nombre, edad ))  
        # igresamos un tupla a la lista con los datos del estudiante 
        
        
    participantes.sort(key=lambda x: x[1]) 
    # organizamos la lista de menor a mayor utilizando una lambada la cual toma como parametro el segundo item de la tupla que es donde esta la edad que es un dato entero el cual podemos organizar de mayor a menor 
    
    
    profe = participantes[-1][0] 
    # ya con la lista organizada ingresamos al último el cual sera el mayor y tomamos su nombre para guardarlo en la variable 
    
    
    asistente = participantes[0][0] 
    # igual, ya que la lista esta organizada tomamos el primero el cual sera el menor y lo almacenamos en la variable 
    
    
    return f'El profesor es {profe} y el esistente es {asistente}' 
# retornamos una frase con los nombres de quienes son el profe y el asistente 
    
# print(profe_asistente(3))        