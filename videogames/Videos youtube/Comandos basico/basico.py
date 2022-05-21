import pygame, sys
pygame.init()

#definir colores
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

#crear ventana
tam_ventana = (800,500)
screen = pygame.display.set_mode(tam_ventana)
pygame.display.set_caption("hola mundo")
#crear timepo 
clock = pygame.time.Clock()

#cordanadas del objeto
cord_x = 400
cord_y = 200

#velocidada del objeto
speed_x = 3
speed_y = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # Hacer que no salga del margen 
    if (cord_x > 720 or cord_x < 0):
        speed_x = speed_x * -1 
    if (cord_y > 320 or cord_y < 0):
        speed_y = speed_y * -1 
    
    cord_x = cord_x + speed_x
    cord_y = cord_y + speed_y

    #poner color al fondo
    screen.fill(WHITE)
    #------------ ZONA DE DIBUJO -------------
    '''
    pygame.draw.line(screen, GREEN, [0,100], [100,300], 5) #[pnt de partida],[pnto de llegada], grosor
    pygame.draw.rect(screen, BLACK, (150,10,80,80)) #(punto x, punto y, largo, ancho)
    pygame.draw.circle(screen, BLACK, (200,200),30)
    
    #dibujar varios cuadrados a la vez
    
    for i in range (100,700,100):
        pygame.draw.rect(screen, BLACK,(i,230,50,50)) #(variable, posicion, tamaño, tamaño)
        pygame.draw.line(screen, GREEN,(i,0),(i,100),5)
    ''' 

    pygame.draw.rect(screen, RED, (cord_x,cord_y,80,80))
    #------------- FIN DE ZONA DE DIBUJIO ---------------------------------------
    #actualizar pandalla
    pygame.display.flip()
    clock.tick(60)
