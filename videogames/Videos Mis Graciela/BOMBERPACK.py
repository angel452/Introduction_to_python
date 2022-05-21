import pygame, random

#COLORES
WHITE = (255,255,255)
BLACK = (0,0,0)

#INICIAR PYGAME
pygame.init()

#DIMENCIONES DE LA VENTANA
ventana = 800,529
screen = pygame.display.set_mode(ventana)

#Colorar iconos al juego
icon_juego = pygame.image.load("icono_juego.png")
pygame.display.set_icon(icon_juego)

#COLOCAR UN FONDO DE PANTALLA
fondo_juego = pygame.image.load("background1.png")

#-------------------------- JUGADORES ---------
#COLOCAR JUGARDOR
player = pygame.image.load("player3.png")
player_pos_x = 65
player_pos_y = 30
player_mov_x = 0
player_mov_y = 0

#ENEMIGOS

#------------------------- IMPLEMETOS -----------
#Colocar bomba
bomba = pygame.image.load("bala.png")
bomba_pos_x = player_pos_x
bomba_pos_y = player_pos_y
bomba_mov_y = 5
bomba_estado = "listo"
def poner_bomba(x,y):
    global bomba_estado
    bomba_estado = "disparado"
    screen.blit(bomba,(x,y))

#COLOCAR UN TITULO A LA PANTALLA
pygame.display.set_caption("BOMBERPACK")

#BUCLE PRINCIPAL
done = True
while done:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            done = False
        #PARA QUE SE MUEVA EL JUGADOR
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                player_mov_x = -5
            if evento.key == pygame.K_RIGHT:
                player_mov_x = +5
            if evento.key == pygame.K_UP:
                player_mov_y = -5
            if evento.key == pygame.K_DOWN:
                player_mov_y = +5
            if evento.key == pygame.K_SPACE:
                if bomba_estado == "listo":
                    bomba_pos_x = player_pos_x + (15)
                    poner_bomba(bomba_pos_x, bomba_pos_y)
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                player_mov_x = 0
            if evento.key == pygame.K_RIGHT:
                player_mov_x = 0
            if evento.key == pygame.K_UP:
                player_mov_y = 0
            if evento.key == pygame.K_DOWN:
                player_mov_y = 0

    #Colocar las imagenes cargadas en panalla
    screen.blit(fondo_juego,(0,0))

    #Colocar player en pantala
    screen.blit(player,(player_pos_x,player_pos_y))
    player_pos_x += player_mov_x
    player_pos_y += player_mov_y
    if player_pos_x <= 65:
        player_pos_x = 65
    elif player_pos_x >= 735:
        player_pos_x = 735
    elif player_pos_y <= 30:
        player_pos_y = 30
    elif player_pos_y >= 475:
        player_pos_y = 475
    
    #Colocar bomba en pantalla
    if bomba_pos_y < 0:
        bomba_pos_y = player_pos_y
        bomba_estado = "listo"
    if bomba_estado == "dispadaro":
        poner_bomba(bomba_pos_x, bomba_pos_y)
        bomba_pos_y -= bomba_mov_y

    #actualizar pantalla
    pygame.display.update()