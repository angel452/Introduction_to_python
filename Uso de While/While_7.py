#Escriba el logaritmo para los enteros impares del 1 al  10
import math
n = 1
while n <= 10:
    print ('Log de',n, '\t=\t', math.log(n))
    n = n + 2

#otra forma
import math
n = 1
while n <= 10:
    if n%2==1: # n es impar
        print('Log de',n, '\t=\t', math.log(n))
    n = n + 1

