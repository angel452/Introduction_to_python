def __add__(self,other):
        if self.filas==other.filas and self.columnas==other.columnas:
            #a=self.lista
            mat= matriz(self.filas,self.columnas,0)
            for i in range(0,self.filas):
                for j in range(0,self.columnas):
                    mat.lista[i][j]=self.lista[i][j]+other.lista[i][j]
            #matriz.imprimir(a)
            return mat
        else:
            print("No se puede efectuar")