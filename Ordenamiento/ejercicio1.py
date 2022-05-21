# Metodo de Burbuja
# Comparar dos elementos, si el siguiente es menor que el actual...se realiza un intercambio
def ord_burbuja(lista):
    for j in range(len(lista)-1):
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                temporal = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temporal

def main():
    lista = [6,4,2,5,3,1]
    lista_b = [3,6,1,7,3,2,8,9,10]
    ord_burbuja(lista)
    ord_burbuja(lista_b)
    print(lista)
    print(lista_b)

main()

        