numero = 17
for n in range(2,numero+1):
    resto = numero % n
    print("{} / {} ten resto {}".format(numero,n,resto))
    if resto != 0:
        print("F")