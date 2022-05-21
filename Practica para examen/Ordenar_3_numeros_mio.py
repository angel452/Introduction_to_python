numero_1=int(input("ingrese numero 1: "))
numero_2=int(input("ingrese numero 2: "))
numero_3=int(input("ingrese numero 3: "))
print("el orden de mayor a menor es: ")

if numero_1>numero_2 and numero_1>numero_3:
    primero = numero_1
    if numero_2>numero_3:
        segundo=numero_2
        tercero=numero_3
    else:
        segundo=numero_3
        tercero=numero_2
    print (primero,segundo,tercero)

if numero_2>numero_1 and numero_2>numero_3:
    primero = numero_2
    if numero_1>numero_3:
        segundo=numero_1
        tercero=numero_3
    else:
        segundo=numero_3
        tercero=numero_1
    print (primero,segundo,tercero)

if numero_3>numero_1 and numero_3>numero_2:
    primero = numero_3
    if numero_1>numero_2:
        segundo=numero_1
        tercero=numero_2
    else:
        segundo=numero_2
        tercero=numero_1
    print (primero,segundo,tercero)

    