class fraccion(): #principio
    #constructor
    def __init__(self,arriba,abajo):
        #self = de uno mismo
        self.num = arriba #de esa misma fraccion el elemento num
        self.dem = abajo #de esa misma fraccion el elemento Dem

    def mostrar(self):
        print(self.num, "/", self.dem)

#crearndo o declarando la instancia (objeto especifico) = en este caso fraccion en F
f = fraccion(7,3)
#crearndo o declarando la instancia (objeto especifico) = en este caso fraccion en G
g = fraccion(9,5)

f.mostrar()
g.mostrar()

#acceder al atributo especifico (numeradores)
print("Este es el numerador: ", f.num)
print("Este es el numerador: ", g.num)