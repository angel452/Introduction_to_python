class rectangulo():
    def __init__(self,x,y,alto,ancho):
        self.ejex = x
        self.ejey = y
        self.alto1 = alto
        self.ancho1 = ancho

    def mostrar(self):
        print("Punto inicial: ", self.ejex, ",", self.ejey)
        print("Ancho: ", self.ancho1)
        print("Largo: ", self.alto1)
'''
class centroide():
    def __init__(self,ancho,largo):
        self.ancho1 = 


    def centroide (ancho, largo):
        centroide_ancho = self.ancho/2
        centroide_largo = self.largo/2
        return "Centroide en punto: ", centroide_ancho,centroide_largo
    
'''
def main():
    
datos = rectangulo(5,3,7,5)
datos.mostrar()
    