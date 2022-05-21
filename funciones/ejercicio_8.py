def valor_absoluto (x):
    if x < 0:
        return -x
    else:
        return x

a = int(input("Ingrese numero: "))
print("Su valor absoluto es: ", valor_absoluto(a))