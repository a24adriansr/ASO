#Escribir un programa que vaya solicitando al usuario que ingrese nombres,
    # a) Si el nombre se encuentra en la agenda (implementada con un dicionario)
    # debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es
    # correcto y eliminar el contacto
    # b) Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente
    # El usuario puede usar la cadena "*", para salir del programa.
    # c) Guarda la agenda en un archivo de texto: miAgenda.txt


############################################################################3


#Importamos path de la librería os
from os import path



#Definimos el diccionario agenda
dAgenda = {}
#Definimos la variable que guardará el archivo .txt
archAgenda = './Agenda.txt'

#Vamos a rellenar el diccionario dAgenda con los contactos 
#que ya existen en el archiv agenda.txt

#Hacemos un if para que compruebe si la variable archAgenda es un archivo,
#si lo es, ejecuta el código, sino continua
if path.isfile(archAgenda):
    #Abre el archivo para lectura
    with open(archAgenda, 'r') as fr:
        #Establece una variable lineas que lea las lineas del archivo que abrimos
        lineas = fr.readlines()
    #buscamos cada una de las lineas
    for l in lineas:
        #Hacemos listas de cada una de las lineas separadas por ':'
        ll = l.split(':')
        #Metemos en el diccionario las listas, usando como el valor 0 de clave y el 1 de valor
        dAgenda.setdefault(ll[0].strip(),ll[1].strip())
else:
    pass



while True:
    #Pedimos nombre de contacto
    nombre = input("Introduce el nombre (Escribe '*' para salir): ")
    #Buscamos si está en la agenda, con el in buscamos en las claves del diccinario
    if nombre in dAgenda:
        #Si está imprime el nombre y el número asociado
        print("El teléfono de {} es {}".format(nombre,dAgenda[nombre]))
        #Y pregunta que quieres hacer con ese dato
        print("¿Que te interesa hacer?\n1: Modificar teléfono\n2: Modificar nombre contacto\n3: Eliminar el contacto\nOtra: No hacer nada)")
        
        op = input("Opción: ")
        if op == "1":
            #Con un input pedimos el número de teléfono y lo guardamos en una variable
            tlf = input("Nuevo teléfono de {}: ".format(nombre))
            #Añadimos la variable antes creada
            dAgenda[nombre] = tlf
        if op == "2":
            #Pedimos el nuevo nombre y lo guardamos en la variable
            nNombre = input("Nuevo nombre de contacto {}: ".format(nombre))
            #Añadimos el nNombre teniendo en cuente el teléfono del anterior nombre
            dAgenda.setdefault(nNombre,dAgenda[nombre])
            #Eliminamos el anterior nombre
            dAgenda.pop(nombre)
        if op == "3":
            #Texto de aviso y con el .pop se elimina el contacto
            print("Eliminamos el contacto")
            dAgenda.pop(nombre)
        else:
            pass
    #En caso de que se escriba un '*' terminará el bucle y sale del programa
    elif nombre == '*':
        break
    #En caso de que no esté en la agenda, pedirá el número de teléfono y lo agrega
    #con el nombre como clave y el teléfono como atributo
    else:
        telefono = input("Introduce el teléfono: ")
        dAgenda.setdefault(nombre,telefono)

    print(dAgenda)

#Terminamos de trabajar con el diccionario Agenda en RAM 
#y queremos guardar todo en un archivo archAgenda
#Creamos una variable para el texto que esté vacía
textoAgenda = ""
#buscamos la clave y el valor de todo el diccionario
for k,v in dAgenda.items():
    #Añadimos a la variable de texto vacía la clave y valor que acabamos de buscar
    textoAgenda += "{} : {}\n".format(k,v)
print(textoAgenda)

#Guardamos ese texto en el archivo agenda que creamos al principio del script
#Primero lo abrimos para escritura con un alias fw
with open(archAgenda,'w') as fw:
    #Usando .write() y el alias le añadimos la variable de texto que creamos anteriormente
    fw.write(textoAgenda)