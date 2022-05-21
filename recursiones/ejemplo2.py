#funcion factorial
def factorial_no_recursivo(n):
    multiplicacion = 1
    while n > 0:
        multiplicacion = n*multiplicacion
        n = n-1
    print(multiplicacion)

def main_no_recursivo():
    factorial_no_recursivo(3)

def factorial(n):
  if n == 1:
    return 1
  else:
    return n * factorial(n-1)

def main ():
    x = int(input("Hallar factorial: "))
    print(factorial(x))

main()