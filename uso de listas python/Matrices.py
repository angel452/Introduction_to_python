#matriz de 2 x 3
matriz_2x3 = [[1,2,3],[4,5,6]]
print(matriz_2x3)

#matriz de 3 x 3 (operaciones)
matriz = [[1,2,3],[4,5,6],[7,8,9]]

print(matriz)
print(len(matriz))
print(len(matriz[0]))
print(matriz[1][2])

#Recorrer listas 

for i in range (0,len(matriz)):
    for j in range (0, len(matriz[0])):
        print(matriz[i][j], end=" ")
    print()
    
