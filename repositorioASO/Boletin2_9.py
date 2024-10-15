#!/usr/bin/python3

'''
Crear una función para validación de contraseñas. Dicho módulo, deberá cumplir con los siguientes criterios de aceptación:
    • La contraseña debe contener un mínimo de 8 caracteres .
    • Una contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico (de estas cuatro condiciones debe cumplir tres) .
    • La contraseña no puede contener espacios en blanco .
    • Contraseña válida, retorna True .
    • Contraseña no válida, retorna False 
'''

#########Definimos a función###############

def passValida(contrasinal):
    from re import compile,search

    contrasinal= str(input("Introduce un contrasinal: "))

    patronEspacios = compile('\s')

    valida = False

    if len(contrasinal) >= 8 and not compile('\s').search(contrasinal):
        print("Seguinte")
        contador = 0 #Contador de condicións
        if compile('[a-z]').search(contrasinal):contador+=1 #Se o contrasinal ten algunha minúscula
        if compile('[A-Z]').search(contrasinal):contador+=1 #Se o contrasinal ten algunha maiúscula
        if compile('[0-9]').search(contrasinal):contador+=1 #Se o contrasinal ten números
        if compile('\W').search(contrasinal):contador+=1 # Se hai simbolos
        if contador >= 3:valida=True

    else:
        print("Contrasinal non válido")
    return valida
######################################

#######Proba de chamar á función######
'''
p1 = input("Introduce contrasinal : ")

if passValida(p1):
    print("É valida")
else:
    print("Non válida")
'''