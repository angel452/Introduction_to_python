def conteo (n):
    if n == 0:
        print("Despegue¡¡¡")
    else:
        print(n)
        conteo(n-1)

conteo(3)