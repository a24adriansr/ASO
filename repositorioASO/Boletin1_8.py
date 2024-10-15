
'''
inicio = 2
fin = 10
for n in range(inicio, fin+1):
    if n == 10:
        break
    else:
        print(n)
'''


#Queremos que non mostre os números do 5 ao 10 
inicio = 1
fin = 15
for n in range(inicio,fin+1):
    if n >= 5 and n <= 10:
        continue
    else:
        print(n)



#Programa que pinte en pantalla las tablas de multiplicar del 1 al 10

'''
##Este foi o meu intento (SPOILER: FALLIDO)
primeiroNum = 1
ultimoNum = 10
multiplicacao = primeiroNum * ultimoNum
for n in range(primeiroNum,ultimoNum):
    print('{} x {} = {}'.format(primeiroNum,ultimoNum,multiplicacao))
'''


#Tabla do 1
'''
numA = 1
for numB in range(1,11):
    print("{} x {} = {}".format(numA,numB,numA*numB))
'''

for numA in range(1,11):
    print("A tabla do {}".format(numA))
    print("-"*20)
    for numB in range(1,11):
        print("{} x {} = {}".format(numA,numB,numA*numB))
    print("-"*20)