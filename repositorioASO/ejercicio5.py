#Escribir un programa que vaya solicitando al usuario que ingrese nombres,
    # a) Si el nombre se encuentra en la agenda (implementada con un dicionario)
    # debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es
    # correcto y eliminar el contacto
    # b) Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente
    # El usuario puede usar la cadena "*", para salir del programa.
    # c) Guarda la agenda en un archivo de texto: miAgenda.txt


############################################################################3

#Definimos el diccionario agenda
dAgenda = {}

while True:
    #Pedimos nombre de contacto
    nombre = input("Dame un nombre de contacto: ")
    #Buscamos si está en la agenda, si no está pedirá el teléfono y los guarda en la agenda
    if nombre in dAgenda:
        pass
    elif nombre == '*':
        break
    else:
        telefono = input("Introduce el teléfono: ")
        dAgenda.setdefault(nombre,telefono)

    print(dAgenda)