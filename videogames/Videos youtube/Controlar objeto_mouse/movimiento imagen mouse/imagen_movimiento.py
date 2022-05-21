import pygame, sys, random
pygame.init()



#crear ventana
ventana = [800,600]
screen = pygame.display.set_mode(ventana)

#reloj
clock = pygame.time.Clock()

#insertar imagen
fondo = pygame.image.load("espacio.png").convert()
player = pygame.image.load("player.png").convert()
player.set_colorkey([255,255,255]) #para quitar fondo

#visivilidad del mouse
pygame.mouse.set_visible(0)

salir = False
while not salir:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True
    
    #MOUSE
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]

    #Dibujar en la pantalla
    screen.blit(fondo,[0, 0])
    screen.blit(player,[x, y])

    #actualizar pandalla
    pygame.display.flip()
    clock.tick(50)

pygame.quit()