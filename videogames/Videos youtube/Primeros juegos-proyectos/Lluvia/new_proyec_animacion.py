import pygame, sys, random
pygame.init()

#COLORES
WHITE = (250,250,250)
RED = (250,0,0)
BLACK = (0,0,0)

#crear ventana
ventana = (800, 500)
screen = pygame.display.set_mode(ventana)

#reloj
clock = pygame.time.Clock()

#aqui se guardan los puntos que el random da abajo
coor_list = []
for i  in range (100):
    x = random.randint(0,800)
    y = random.randint(0,500)
    coor_list.append([x,y])

#inicio del programa
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #Dibujar pantall
    screen.fill(BLACK)

    for i  in coor_list:
        x = i[0]
        y = i[1]
        pygame.draw.circle (screen,WHITE,(x,y),1)
        #hacer la caida de los puntos aumentando valores a las y = i[1]
        i[1] = i[1] + 1
        if i[1] > 500:
            i[1] = 0
    
    #actualizar pandalla
    pygame.display.flip()
    clock.tick(50)
