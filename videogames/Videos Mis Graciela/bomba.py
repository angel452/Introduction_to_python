import pygame, random
#COLORES
WHITE = (255,255,255)
BLACK = (0,0,0)

#INICIALIZAR PYGAME
pygame.init()

#DIMENCIONES DE LA VENTANA
ventana = (800,600)
screen = pygame.display.set_mode(ventana)

#Colocar un icono al juego
icon_juego = pygame.image.load("ic_juego.jpg") 
pygame.display.set_icon(icon_juego)

#Colocar un fondo de pantalla (imagen)
fondo_juego  = pygame.image.load("fondo2.jpg")

#----------------------------- JUGADORES ----------------------------------
#Colocar el jugador
player = pygame.image.load("nave.png")
player_pos_L = 400 - (player.get_size()[0]//2)
player_pos_A = 600 - (player.get_size()[1])
player_mov_L = 0 
player_mov_A = 0 

#------------------------------ IMPLEMENTOS -----------------------------
#Colocar una bala
bala = pygame.image.load("bala.png")
bala_pos_L = player_pos_L
bala_pos_A = player_pos_A
bala_mov_A = 5
bala_estado = "listo" #"ya disparó"
def disparar_bala(x,y):
    global bala_estado
    bala_estado = "disparado"
    screen.blit(bala,(x,y))

#Colocar un titulo a la panalla
pygame.display.set_caption("Primer Juego")

#BUCLE PINCIPAL
done = True
while done:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            done = False
        #Para que se mueva el objeto
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                player_mov_L = -3
            if evento.key == pygame.K_RIGHT:
                player_mov_L = 3
            if evento.key == pygame.K_UP:
                player_mov_A = -3
            if evento.key == pygame.K_DOWN:
                player_mov_A = 3
            if evento.key == pygame.K_SPACE:
                if bala_estado == "listo":
                    bala_pos_L = player_pos_L + (15)
                    disparar_bala(bala_pos_L, bala_pos_A)
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                player_mov_L = 0
            if evento.key == pygame.K_RIGHT:
                player_mov_L = 0
            if evento.key == pygame.K_UP:
                player_mov_A = 0
            if evento.key == pygame.K_DOWN:
                player_mov_A = 0
    
    #Poner color u imagen a la ventana (background)
    #screen.fill(WHITE) # para un fondo solido
    screen.blit(fondo_juego,(0,0)) #uso de blit para una imagen como fondo 

    #Poner jugador en pantalla 
    screen.blit(player,(player_pos_L,player_pos_A))
    player_pos_L += player_mov_L
    player_pos_A += player_mov_A
    if player_pos_L <= 0:
        player_pos_L = 0
    elif player_pos_L >= 735:
        player_pos_L = 735

    #Colocar una bala en pantalla
    if bala_pos_A < 0:
        bala_pos_A = player_pos_A
        bala_estado = "listo"
    if bala_estado == "disparado":
        disparar_bala(bala_pos_L, bala_pos_A)
        bala_pos_A -= bala_mov_A

    #actualizar pantalla 
    pygame.display.update()