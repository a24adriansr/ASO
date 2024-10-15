#Añadimos en una variable la ruta absoluta del fichero
pathArchivo = '/etc/passwd'

#Abrimos el arvhico. Por defecto se abre de lectura ("r")
#Al hacerlo con el with, no es necesario cerrar el close.
with open(pathArchivo) as fr:
    #Leemos el archivo y lo guardamos en la variable sPasswd
    sPasswd = fr.read()


#Para convertirlo en una lista usamos lo siguiente:
with open(pathArchivo) as fr:
    lPasswd = fr.readlines()

#strip() se usa para sacar la 'basura' que queda al leer un fichero
for linea in lPasswd:
    print(linea.strip())






#Otra forma de hacer una lista
    #Con el split() hacemos que un fichero se convierta en una lista
    #separando los elementos a nuestro gusto. Por defecto usa los saltos de línea.
        #lPasswd = sPasswd.split('\n')
        #for linea in lPasswd:
        #   print(linea)