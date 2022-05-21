#ordenamiento por seleccion
# La cosa es buscar el elemento menor y ponerlo en la primera posicion
def ord_seleccion (lista):
    for j in range(len(lista)):
        pos_min = j
        for i in range(j+1,len(lista)):
            if lista[i] < lista[pos_min]:
                pos_min = i  
        if pos_min != j:
            temp = lista[j]
            lista[j] = lista[pos_min]
            lista[pos_min] = temp

def main ():
    lista = [6,4,2,5,3,1]
    ord_seleccion(lista)
    print(lista)

main ()