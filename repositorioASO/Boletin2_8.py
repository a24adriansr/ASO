#!/usr/bin/python3

from re import compile,search

alfanumerico = compile(r'[^a-zA-Z0-9]')

valida = False

u = input("Introduce un usuario: ")

if len(u) >= 6 and len(u) <= 12 and not compile('\W').search(u):
    print("Seguimos") 

contador = 0

if len(u) <= 6: print(" El nombre de usuario debe contener al menos 6 caracteres")
contador+=1
print(contador)
if len(u) >= 12: print("El nombre de usuario no puede contener más de 12 caracteres")
contador+=1
print(contador)
if search(alfanumerico,u): print("El nombre de usuario puede contener solo letras y números")
contador+=1
print(contador)
if contador == 3:valida=True

if contador < 3:valida=False

print(valida)