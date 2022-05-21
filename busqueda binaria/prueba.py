#busqueda binaria
def ordenar(lista):
    for j in range(len(lista)-1):
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                temporal = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temporal

def bus_binaria(lista,num,ini,fin):
    central = (ini+fin)//2
    if num == lista[central]:
        return central
    elif num > lista[central]:
        ini = central + 1
        return bus_binaria(lista,num,ini,fin)
    elif num < lista[central]:
        fin = central - 1
        return bus_binaria(lista,num,ini,fin)

lista = [6,4,5,7,2,3,8,9,1,14,25,67,34,23,75,100,234,1111,24,2321]
ordenar(lista)
ini = 0
fin = len(lista)-1
num = int(input("Ingrese numero que desea buscar: "))
print("Esta es la lista ordenada: ")
print(lista)
print("El numero", num, "se encuentra en la posicion :",bus_binaria(lista,num,ini,fin))
    