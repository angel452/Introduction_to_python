import pygame

#Colores
WHITE = (255,255,255)

#Inicializar pygame
pygame.init()

#Dimenciones de la ventana
ventana = (800,600)
screen = pygame.display.set_mode(ventana)

#---------------------- Jugador -----------------
player = pygame.image.load("player3.png")
player_pos_x = 0
player_pos_y = 300
player_mov_x = 0
player_mov_y = 0

#------------------------ Implementos ---------------
#Bomba
bomba = pygame.image.load("bomba.png")
bomba_pos_x = player_pos_x
bomba_pos_y = player_pos_y
la_variable = 0 
def poner_bomba(x,y):
    screen.blit(bomba,(x,y))

#Explocion 
bum = pygame.image.load("explosion.png")
bum_pos_x = 800
bum_pos_y = 600
sound = pygame.mixer.Sound("explosion.wav")

#Bucle principal
done = True
aux = 1
inicio_bomba = 10000
inicio_bum = 10000
while done:
    #Poner tiempo
    tiempo = pygame.time.get_ticks()//1000
    if aux == tiempo:
        aux += 1
        #print(tiempo)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    #Hacer que se mueva el jugador
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_mov_x = -0.3
            if event.key == pygame.K_RIGHT:
                player_mov_x = 0.3
            if event.key == pygame.K_UP:
                player_mov_y = -0.3
            if event.key == pygame.K_DOWN:
                player_mov_y = 0.3
            if event.key == pygame.K_SPACE:
                bomba_pos_x = player_pos_x
                bomba_pos_y = player_pos_y
                la_variable = 1
                inicio_bomba = tiempo
            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_mov_x = 0
            if event.key == pygame.K_RIGHT:
                player_mov_x = 0
            if event.key == pygame.K_UP:
                player_mov_y = 0
            if event.key == pygame.K_DOWN:
                player_mov_y = 0

    screen.fill(WHITE)
    #Colocar bomba
    if la_variable != 0:
        screen.blit(bomba,(bomba_pos_x,bomba_pos_y))
    
    #tiempo
    if tiempo == inicio_bomba + 2:
        #bomba.kill()
        print("Lo lograste")
        inicio_bomba = 1000
        #screen.blit(bomba,(500,500))
        bum_pos_x = bomba_pos_x - 55
        bum_pos_y = bomba_pos_y - 50
        bomba_pos_x = 800
        bomba_pos_y = 600

        inicio_bum = tiempo
        sound.play()
    if tiempo == inicio_bum + 2:
        inicio_bum = 10000
        bum_pos_x = 800
        bum_pos_y = 600
        
    #Poner jugador en pantalla
    screen.blit(player,(player_pos_x,player_pos_y))
    player_pos_x += player_mov_x
    player_pos_y += player_mov_y

    screen.blit(bum,(bum_pos_x,bum_pos_y))

    pygame.display.update()