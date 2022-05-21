# Ordenamiento por insercion
# seleccionar y defrente ponerlo en su lugar
# ejemplo de las cartas
def ord_insercion (lista):
    for i in range (1,len(lista)):
        principal = lista[i]
        j = i-1
        while j >= 0 and principal < lista[j]:
            lista[j+1] = lista[j]
            j = j -1
            lista[j+1] = principal
        

def main ():
    lista = [6,4,2,1,3,5]
    ord_insercion(lista)
    print(lista)

main ()