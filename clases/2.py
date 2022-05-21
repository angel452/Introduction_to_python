def set_valor(self,i,j,val):
        self.elem[i][j]=val
def __lt__(self,mat2):
        comparacion = matriz(self.col,self.row,0)
        if len(mat2.elem) == len(self.elem) and len(mat2.elem[0]) == len(self.elem[0]):
            for i in range(len(self.elem)):
                for j in range(len(self.elem[i])):
                    if self.elem[i][j] < mat2.elem[i][j]:
                        comparacion.set_valor(i,j,True)  
                    else:
                        comparacion.set_valor(i,j,False)
            return comparacion
        return
