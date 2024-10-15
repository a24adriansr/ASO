#!/usr/bin/python

#Programa que lea un carácter por teclado y compruebe si es una letra mayúscula.

'''
letra = input("Introduce unha letra:")
if letra.isupper():
    print("É maiúscula")
else:
    print("Is not")
'''
'''
letrinha = input("Dame unha letra: ")
#Pasa UN SOLO CARÁCTER a ASCII
asciiLetra = ord(letrinha)
print(asciiLetra)
if asciiLetra >= 65 and asciiLetra <= 90:
    print("A letra introducida é unha maiúscula")
else:
    print("Non é maiúscula")
'''

try:
    texto = input("Dame unha letra ")
    letrinha = texto [0]
#O texto en python é unha lista de carácteres
##O elemento [0] é o primeiro carácter
#ord()Pasa UN SOLO CARÁCTER a ASCII
    asciiLetra = ord(letrinha)
#print(asciiLetra)
    if asciiLetra >= 65 and asciiLetra <= 90:
        print("A letra introducida {} é unha maiúscula".format(letrinha))
    else:
        print("A letra {} non é maiúscula").format(letrinha)
except:
    print("Introduce carácter válido")