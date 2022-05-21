# Busqueda lineal
def busc_lineal (lista,num):
    for i in range(len(lista)):
        if lista[i] == num:
            print("El numero", num, "Se encuentra en la posicion ", i)
    print("no se encuentra")

def main():
    lista = [2,21,4,4,2,54,21,53,35,53,2,21,213,1,21,211,2,3,23,12,31,31,4,5,5,6,6,77,1,1,23,1,2,31]
    num = int(input("Ingrese numero a buscar: "))
    busc_lineal(lista,num)

main()