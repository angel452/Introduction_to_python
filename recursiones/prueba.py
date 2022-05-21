def pascal(x):
    if x <= 0:
        return []
    elif x == 1:
        return [1]
    else:
        linea = [1]
        anterior_linea = pascal(x-1)
        print(anterior_linea)
    
pascal(5)