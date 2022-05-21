import math
def distancia (x1,x2,y1,y2):
    dx = x2 - x1
    dy = y2 - y1
    suma_de_cuadrados = dx**2 + dy ** 2
    resultado = math.sqrt(suma_de_cuadrados)
    return resultado

print(distancia(3,4,6,7))