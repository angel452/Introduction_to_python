import pygame, sys, random
pygame.init()

#COLORES
WHITE = (250,250,250)
BLACK = (0,0,0)

#---------------CONFIGURACION DE LOS JUGADORES--------
player_ancho = 15
player_largo = 100
#PLAYER 1
player1_coor_x = 50
player1_coor_y = 200
player1_speed_y = 0
#PLAYER 2
player2_coor_x = 750
player2_coor_y = 200
player2_speed_y = 0
#PELOTA
pelota_coor_x = 400
pelota_coor_y = 300
pelota_speed_x = 5
pelota_speed_y = 5


#crear ventana
ventana = (800, 600)
screen = pygame.display.set_mode(ventana)

#reloj
clock = pygame.time.Clock()

#game over
game_over = False

#inicio del programa
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
        if event.type == pygame.KEYDOWN:
            #jugaroor1
            if event.key == pygame.K_w:
                player1_speed_y = -5
            if event.key == pygame.K_s:
                player1_speed_y = 5
            #jugador2
            if event.key == pygame.K_UP:
                player2_speed_y = -5
            if event.key == pygame.K_DOWN:
                player2_speed_y = 5
        
        if event.type == pygame.KEYUP:
            #jugaroor1
            if event.key == pygame.K_w:
                player1_speed_y = 0
            if event.key == pygame.K_s:
                player1_speed_y = 0
            #jugaroor2
            if event.key == pygame.K_UP:
                player2_speed_y = 0
            if event.key == pygame.K_DOWN:
                player2_speed_y = 0
    
    #condicionales para manejo de pelota
    if pelota_coor_y > 590 or pelota_coor_y < 10:
        pelota_speed_y = pelota_speed_y *-1
    if pelota_coor_x > 800 or pelota_coor_x < 0:
        pelota_coor_x = 400
        pelota_coor_y = 300
        pelota_speed_x = pelota_speed_x * -1
        pelota_speed_y = pelota_speed_y * -1
    

    #MODIFICAR LAS COORDENADAS DE LOS JUGADORES Y PELOTA
    player1_coor_y = player1_coor_y + player1_speed_y
    player2_coor_y = player2_coor_y + player2_speed_y
    pelota_coor_x = pelota_coor_x + pelota_speed_x
    pelota_coor_y = pelota_coor_y + pelota_speed_y
    #Dibujar pantall
    screen.fill(BLACK)

    #crear personajes:
    #-----------------------ZONA DE DIBUJO--------------------
    jugador_1 = pygame.draw.rect(screen,WHITE,(player1_coor_x,player1_coor_y,player_ancho,player_largo))
    jugador_2 = pygame.draw.rect(screen,WHITE,(player2_coor_x,player2_coor_y,player_ancho,player_largo))
    pelota = pygame.draw.circle(screen,WHITE,(pelota_coor_x,pelota_coor_y),10)
    #adornos
    pygame.draw.line(screen, WHITE, [400,800], [400,0], 5)
    #-----------------------fIN DE ZONA DE DIBUJO-----------

    #COLISIONES Y CONTACTO CON JUGADORES:
    if pelota.colliderect(jugador_1) or pelota.colliderect(jugador_2):
        pelota_speed_x = pelota_speed_x * -1

    #actualizar pandalla
    pygame.display.flip()
    clock.tick(50)

pygame.quit()
