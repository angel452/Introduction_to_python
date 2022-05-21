class matriz:
    def __init__(self,row,col,valor=0):
        self.row=row
        self.col=col
        self.lista=[]
        for i in range(self.row):
            a =[]
            for j in range(self.col):
                a.append(valor)
            self.lista.append(a)
        

    def __str__(self):
        cad=""
        for i in range(self.row):
            for j in range(self.col):
                cad = cad + str(self.lista[i][j]) + "\t"
            cad +="\n"
        return cad
    
    def set_valores(self, m):
        if (self.col*self.row ==len(m)):
            a=0
            for i in range(self.row):
                for j in range(self.col):
                    self.lista[i][j]=m[a]
                    a+=1

    def __lt__(self,mat2):
        if mat2.row == self.row and mat2.col == self.col:
            comparacion = matriz(self.row,self.col,False)
            for i in range(self.row):
                for j in range(self.col):
                    if self.lista[i][j] < mat2.lista[i][j]:
                        comparacion.lista[i][j]=True  
            return comparacion
        print ("No se puede comparar")

    def __le__(self,mat2):
        if mat2.row == self.row and mat2.col == self.col:
            comparacion = matriz(self.row,self.col,False)
            for i in range(self.row):
                for j in range(self.col):
                    if self.lista[i][j] <= mat2.lista[i][j]:
                        comparacion.lista[i][j]=True  
            return comparacion
        print ("No se puede comparar")

    def __eq__(self,mat2):
        if mat2.row == self.row and mat2.col == self.col:
            comparacion = matriz(self.row,self.col,False)
            for i in range(self.row):
                for j in range(self.col):
                    if self.lista[i][j] == mat2.lista[i][j]:
                        comparacion.lista[i][j]=True  
            return comparacion
        print ("No se puede comparar")

    def __ne__(self,mat2):
        if mat2.row == self.row and mat2.col == self.col:
            comparacion = matriz(self.row,self.col,False)
            for i in range(self.row):
                for j in range(self.col):
                    if self.lista[i][j] != mat2.lista[i][j]:
                        comparacion.lista[i][j]=True  
            return comparacion
        print ("No se puede comparar")

    def __gt__(self,mat2):
        if mat2.row == self.row and mat2.col == self.col:
            comparacion = matriz(self.row,self.col,False)
            for i in range(self.row):
                for j in range(self.col):
                    if self.lista[i][j] > mat2.lista[i][j]:
                        comparacion.lista[i][j]=True  
            return comparacion
        print ("No se puede comparar")

    def __ge__(self,mat2):
        if mat2.row == self.row and mat2.col == self.col:
            comparacion = matriz(self.row,self.col,False)
            for i in range(self.row):
                for j in range(self.col):
                    if self.lista[i][j] >= mat2.lista[i][j]:
                        comparacion.lista[i][j]=True  
            return comparacion
        print ("No se puede comparar")

    def __add__(self, m):
        if (self.row==m.row) and(self.col==m.col):
            res = matriz(self.row, self.col)
            for i in range(self.row):
                for j in range(self.col):
                    res.lista[i][j]=self.lista[i][j]+m.lista[i][j]
            return res
        print("No se puede sumar")
    
    def __sub__(self, m):
        if (self.row==m.row) and(self.col==m.col):
            res = matriz(self.row, self.col)
            for i in range(self.row):
                for j in range(self.col):
                    res.lista[i][j]=self.lista[i][j]-m.lista[i][j]
            return res
        print("No se puede sumar")

    def __mul__(self, m):
        if (self.row==m.row) and(self.col==m.col):
            res = matriz(self.row, self.col)
            for i in range(self.row):
                for j in range(self.col):
                    res.lista[i][j]=self.lista[i][j]*m.lista[i][j]
            return res
        print("No se puede sumar")

    def __truediv__(self, m):
        if (self.row==m.row) and(self.col==m.col):
            res = matriz(self.row, self.col)
            for i in range(self.row):
                for j in range(self.col):
                    res.lista[i][j]=self.lista[i][j]/m.lista[i][j]
            return res
        print("No se puede sumar")

    def __pow__(self, m):
        if (self.row==m.row) and(self.col==m.col):
            res = matriz(self.row, self.col)
            for i in range(self.row):
                for j in range(self.col):
                    res.lista[i][j]=self.lista[i][j]**m.lista[i][j]
            return res
        print("No se puede sumar")
    
    def transpuesta (self):
        t = matriz(self.col,self.row)
        for f in range (self.col):
            for c in range(self.row):
                t.lista[f][c] = self.lista[c][f]
        return t

class matriz_cuadrada(matriz):
    def __init__(self,n,matrix):
       super().__init__(n,n,matrix)

matri1=matriz(2,5,9)
matri2=matriz(2,5,5)

matri1.set_valores([1, 2, 3, 1, 6, 10, 4, 3, -1, -2])
matri2.set_valores([0, 2, 1, 1, 5, -4, 4, 2, -1, -3])
print(matri1)
print(matri2)
print("Suma")
print(matri1+matri2)
print("Resta")
print(matri1-matri2)
print("Mult")
print(matri1*matri2)
print("potencia")
print(matri1**matri2)

print("menor")
print(matri1<matri2)
print("menor igual")
print(matri1<=matri2)
print("igual")
print(matri1==matri2)
print("diferente")
print(matri1!=matri2)
print("mayor")
print(matri1>matri2)
print("mayor igual")
print(matri1>=matri2)