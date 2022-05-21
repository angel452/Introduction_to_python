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

#coordenadas del cuadrado
coord_x = 10
coord_y = 10

#definir velocidad
x_speed = 0
y_speed = 0

#inicio del programa
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #eventos del teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3
            if event.key == pygame.K_UP:
                y_speed = -3
            if event.key == pygame.K_DOWN:
                y_speed = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            if event.key == pygame.K_RIGHT:
                x_speed = 0
            if event.key == pygame.K_UP:
                y_speed = 0
            if event.key == pygame.K_DOWN:
                y_speed = 0

    #Dibujar pantalla
    screen.fill(BLACK)

    coord_x = coord_x + x_speed
    coord_y = coord_y + y_speed

    #--------------ZONA DE DIBUJO-----------------
    pygame.draw.rect(screen,RED,(coord_x,coord_y, 100, 100))
    #--------------- FIN ZONA DE DIBUJO---------- 

    #actualizar pandalla
    pygame.display.flip()
    clock.tick(50)
