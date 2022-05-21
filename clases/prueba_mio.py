class Matriz():
    def __init__(self,columnas,filas,valor=0):
        self.columnas = columnas
        self.filas = filas

    def crear_matriz(aux,columnas,filas,valor):
        lista = []
        for i in range (columnas):
            lista.append([])
            for j in range(filas):
                lista[columnas].append(valor)
        self.matriz = lista

class Sobre_carga():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    #------------------  OPERADORES--------------
    #restar
    def __sub__(self, num):
        return sobrecarga(self.x - num.x, self.y - num.y)

    # Multiplicar 
    def __mul__(self, num):
        return sobrecarga(self.x * num, self.y * num)
    
    # Dividir     
    def __truediv__(self, nm):
        float_s = float(s)
        return sobrecarga(self.x / float_s, self.y / float_s)

    # Potenciar 
    def __pow__(self,num):
        return sobrecarga(self.x**num, self.y**num)
    
    #----------------------- COMPARADORES -----------------------
    def __lt__(self, ):
        return
    def __le__(self, ):
        return
    def __gt__(self, ):
        return
    def __ge__(self, ):
        return
    def __eq__(self, ):
        return
    def __ne__(self, ):
        return
    