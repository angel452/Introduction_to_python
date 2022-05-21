class Vehiculo():
    def __init__(self,color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "Color: " + self.color + ", Ruedas: " + str(self.ruedas))

class Cche (Vehiculo):
    def __init__(self,color,ruedas,velocidad,cilindrada):
        super().__init__(color,ruedas) #Herecia de la anterior
        #Vehiculo.__init__(color,ruedas) otra forma
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return super().__str__() + ", Velocidad: " + str(self.velocidad) + ", Cilindrada: " + str(self.cilindrada)
        # Arriba se llama el str de la anterior funcion    

class Camioneta(Vehiculo):
    def __init__(self, color, ruedas,velocidad,cilindrada,carga):
        super().__init__(color,ruedas,velocidad,cilindrada)
        self.carga = carga
    def __str__(self):
        return super().__str__()+ ", Kilos de carga: " + str(self.carga)

class Bicicleta(Vehiculo):
    def __init__(self,)

class Motocicleta(Bicicleta):
    def __init__(self,color,ruedas,tipo,velocidad,cilindrada):
        super().__init__ (color,ruedas,tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return super().__str__()


def main():
    