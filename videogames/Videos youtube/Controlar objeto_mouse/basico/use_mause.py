import pygame, sys
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

#bisivilidad del mouse
pygame.mouse.set_visible(0)

#inicio del programa
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #CONFIGURAR MAUNSE
    pos_mouse = pygame.mouse.get_pos()
    x = pos_mouse[0]
    y = pos_mouse[1]

    #Dibujar pantall
    screen.fill(BLACK)

    #--------------ZONA DE DIBUJO-----------------
    pygame.draw.rect(screen,RED,(x,y,100,100))
    #--------------- FIN ZONA DE DIBUJO---------- 

    #actualizar pandalla
    pygame.display.flip()
    clock.tick(50)
