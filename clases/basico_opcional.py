class fraccion:
    def __init__(self, arriba = 10, abajo = 13):
        self.num = arriba
        self.dem = abajo

    def mostrar (self):
        print(self.num, "/", self.dem)
    
    def set_num(self, num):
        self.num = num

    def set_dem(self, dem):
        self.dem = dem

#Declaraicon de la  instantcia
f = fraccion(4,3)
g = fraccion()
x = 12
y = 45
g.set_dem(x)
g.set_num(y)