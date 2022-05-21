def pascal(x):
    if x <= 0:
        return []
    elif x == 1:
        return [1]
    else:
        anterior_linea = pascal(x-1)
        linea = [1]
        for i in range (len(anterior_linea)-1):
            linea.append(anterior_linea[i] + anterior_linea[i+1])
        linea = linea + [1]
    return linea

def main():
    print(pascal(3))

main()