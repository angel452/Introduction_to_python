import pygame, sys, random
pygame.init()

#crear ventana
ventana = [800,600]
screen = pygame.display.set_mode(ventana)

#reloj
clock = pygame.time.Clock()

#inicio del programa
salir = False

#insertar imagen
fondo = pygame.image.load("imagen_final.png").convert()

while not salir:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True

    #Dibujar pantalla
    screen.blit(fondo,[0, 0])

    #actualizar pandalla
    pygame.display.flip()
    clock.tick(50)

pygame.quit()