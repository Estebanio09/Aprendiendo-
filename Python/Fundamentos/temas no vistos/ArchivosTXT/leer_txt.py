# Debemos especificarla ruta del archivo para poder ingresar junto con el la función open() esto lo almacenamos a una variable ahora para la codificación internacional es con encoding="UTF-8"
"""
archivo_sin_leer = open(
    "c:/Users/camil/OneDrive/Escritorio/Desde 0/Python/Fundamentos/temas no vistos/ArchivosTXT/archivo.txt",
    encoding="UTF-8"
)
"""

# con el método read() podemos leer el archivo
"""archivo = archivo_sin_leer.read()"""
# con la método readlines() leemos el archivo y nos retorna un arreglo con todas las línea del archivo (esto consume ram si el archivo es muy largo se consumirá toda la ram de nuestro PC) ahora importante un archivo solo se puede ler una vez
"""lineas = archivo_sin_leer.readlines()"""
# Recordemos que \n es un salto de línea

# Con el método readline() leemos una sola linea del archivo
"""linea = archivo_sin_leer.readline()"""
# Con el método close() cerramos el archivo
"""archivo_sin_leer.close()"""

# leer de forma optima con with open 
# para modificar en el archivo podemos agregar "w" esto nos dará el permiso sobre escribir el archivo para agregar usamos el permiso "a"
with open(
    "c:/Users/camil/OneDrive/Escritorio/Desde 0/Python/Fundamentos/temas no vistos/ArchivosTXT/archivo.txt","w", encoding="UTF-8",
) as archivo:
    # Leer el archivo 
    """contenido = archivo.read()"""
    # no es necesario cerrar el archivo 
    
    #con el método writelines sobre escribimos el texto del archivo a este le podemos pasar un iterable como lo es un solo string o una lista 
    """archivo.writelines("hola maestro como andas esto es desde writelines")"""
    
    
    
    
    
