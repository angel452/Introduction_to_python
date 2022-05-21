class punto():
    def __init__(self,x,y):
        self.ejex = x
        self.ejey = y
    
    def sumar (self,punto2):
        ''' #otra forma
        punto_resultante = punto
        punto_resultante.x = self.x + punto2.x
        punto_resultante.y = self.y + punto2.y
        return punto_resultante
        '''
        return punto(self.x + punto2.x,self.y + punto2.y)
    def mostrar(self):
        print("Punto: ", self.ejex, ",", self.ejey)

def main ():
    p1 = punto(3,4)
    p2 = punto(7,9)
    p3 = p1.sumar(p2)
    p3.mostrar

main()
