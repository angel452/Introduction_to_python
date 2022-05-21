cantar1 = "Hola como estas"
cantar2 = " Yo estoy bien"

def imprimirDoble(paralbra):
    print(paralbra, paralbra)

def concatenar_doble (parte1, parte2):
    cat = parte1 + parte2
    imprimirDoble(cat)

concatenar_doble(cantar1, cantar2)