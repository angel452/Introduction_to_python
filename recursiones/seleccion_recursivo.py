def seleccion_recur (a,i=0,j=0,flag=1):
    sice = len(lista)
    if (i < sice-1):
        if (flag):
            j = i + 1
        if (j < sice):
            if (lista[i] > a[j]):
                a[i], a[j] = a[j], a[i]
                seleccion_recur(a,i,j+1,0)
            seleccion_recur(a,i+1,0,1)

def seleccion(lista):
    for i in range(len(lista)):
        pos_min = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[pos_min]:
                pos_min = j
        if pos_min != i:
            temporal = lista[i]
            lista[i] = lista[pos_min]
            lista[pos_min] = temporal

lista = [5,7,9,10,3,5]
seleccion_recur(lista)
print(lista)
seleccion(lista)
print(lista)


