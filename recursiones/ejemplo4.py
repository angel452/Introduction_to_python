#imprimir numeros del 1 al 4
def imprimir (x):
    if x>0:
        imprimir(x-1)
        print(x)
        
def main():
    imprimir(4)

main()