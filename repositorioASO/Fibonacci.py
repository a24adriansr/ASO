def fibonacci(n):
    secuencia = [0, 1]  # Inicializamos con los primeros dos números

    for i in range(2, n):
        seguinte_num = secuencia[-1] + secuencia[-2]  # Suma de los dos últimos
        if seguinte_num > n:
            break  # Terminamos si el siguiente número excede el límite
        secuencia.append(seguinte_num)

    return secuencia

# Pedir el número máximo hasta donde se generará la sucesión
numero = int(input("introduce o número máximo da sucesión: "))

# Generar y mostrar la sucesión de Fibonacci
resultado = fibonacci(numero)
print("Sucesión de Fibonacci hasta {}: {}".format(numero,resultado))


'''
nMax = int(input("Num mas alto:"))

lista = [0,1]
while True:
    sigNum = lista[-1] + lista[-2]
    if sigNum > nMax:
        break
    lista.append(sigNum)
print("Sucesión de fibonacci hasta {}: {}".format(nMax,))
'''

