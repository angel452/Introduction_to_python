def hanoi (disco, ini, medio, fin):
    if disco > 0:
        hanoi(disco -1, ini, fin, medio)
        print("Mueva el disco ", disco, "desde el poste", ini, "hasta el poste", fin)
        hanoi(disco -1, medio, ini, fin)

def main():
    num_Discos = 3
    hanoi(num_Discos,1,2,3)

main()
