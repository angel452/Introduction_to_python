#quick short
#paso 1: pivote va a ser el primer numero
#econcontrat un numeor mayor al pivote de izquierda a derecha
#encontrar un numero menor o igual al pivote de derecha a izquierda
#esas dos posiciones se comparar, enumera desde el 0 al len(lista-1) y INI DEBE SER MENOR QUE FIN
#si no se cumple lo de arriba, cambia pivote con fin
lista = [7,6,7,5,1,2,9,15,10]
def partir(lista,i,d):
    pivote=lista[i]
    ini=i
    fin=d
    while ini<fin:
        while lista[ini]<=pivote and ini<len(lista)-1 :
            ini=ini+1
        while lista[fin]>pivote and fin>0:
            fin=fin-1
        if ini<fin:
            aux=lista[ini]
            lista[ini]=lista[fin]
            lista[fin]=aux
    variable=pivote
    lista[i]=lista[fin]
    lista[fin]=variable
    return fin

def ord_rapido(lista,izq,der):
    pivote = lisa[0]
    ini = lista [0]
    fin = lista[len(lista-1)]
    while pivote < lista[1]
    if izq < der:
        pp = partir(lista,izq,der)
        ord_rapido(lista,i,pp-1)
        ord_rapido(lista,pp+1,d)