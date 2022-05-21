import pygame

#Inicializador
pygame.init()

#Dimenciones Ventanas - Screen
WIDTH, HEIGHT = 1013,525
screen = pygame.display.set_mode((WIDTH,HEIGHT))
fondo = pygame.image.load("Imagenes/Fondo.png").convert()

#-------------- COLORES ------------------
BLACK       = (   0,   0,   0)
WHITE       = ( 255, 255, 255)
GREEN       = (   0, 255,   0)
RED         = ( 255,   0,   0)
BLUE        = (   0,   0, 255)
WHITEBLUE   = (   0, 170, 228)
PURPLE      = (  87,  35, 100)
WHITESOLID  = ( 277, 277, 277)
GRAY        = ( 184, 184, 192)

FPS = 10#Frames per second

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.images =  []
        self.image_0 = pygame.image.load('Imagenes/pacman0.png').convert()
        self.image_0.set_colorkey(WHITE)
        self.images.append(self.image_0)
        self.index=0        
        self.image = self.images[self.index]        
        self.rect = pygame.Rect(75,45,39,42)
        self.rect.x=75
        self.rect.y=45

    #Obtener posiciones exactas
    def getx(self):
        return self.rect.x 

    def gety(self):
        return self.rect.y

    def update(self):
        self.tecla = pygame.key.get_pressed()
        if self.tecla[pygame.K_RIGHT]:
            self.images= []
            self.image_0= pygame.image.load("Imagenes/pacman0.png").convert()
            self.image_1= pygame.image.load("Imagenes/pacman1.png").convert()
            self.image_2= pygame.image.load("Imagenes/pacman2.png").convert()
            self.image_0.set_colorkey(WHITE)
            self.image_1.set_colorkey(WHITE)
            self.image_2.set_colorkey(WHITE)
            self.images.append(self.image_0)
            self.images.append(self.image_1)
            self.images.append(self.image_2)
        if self.tecla[pygame.K_LEFT]:
            self.images= []                    
            self.image_0= pygame.image.load("Imagenes/pacman0.png").convert()
            self.image_1= pygame.image.load("Imagenes/pacman1_left.png").convert()
            self.image_2= pygame.image.load("Imagenes/pacman2_left.png").convert()
            self.image_0.set_colorkey(WHITE)
            self.image_1.set_colorkey(WHITE)
            self.image_2.set_colorkey(WHITE)
            self.images.append(self.image_0)
            self.images.append(self.image_1)
            self.images.append(self.image_2)
        if self.tecla[pygame.K_UP]:
            self.images= []
            self.image_0= pygame.image.load("Imagenes/pacman0.png").convert()
            self.image_1= pygame.image.load("Imagenes/pacman1_up.png").convert()
            self.image_2= pygame.image.load("Imagenes/pacman2_up.png").convert()
            self.image_0.set_colorkey(WHITE)
            self.image_1.set_colorkey(WHITE)
            self.image_2.set_colorkey(WHITE)
            self.images.append(self.image_0)
            self.images.append(self.image_1)
            self.images.append(self.image_2)
        if self.tecla[pygame.K_DOWN]:
            self.images= []
            self.image_0= pygame.image.load("Imagenes/pacman0.png").convert()
            self.image_1= pygame.image.load("Imagenes/pacman1_down.png").convert()
            self.image_2= pygame.image.load("Imagenes/pacman2_down.png").convert()
            self.image_0.set_colorkey(WHITE)
            self.image_1.set_colorkey(WHITE)
            self.image_2.set_colorkey(WHITE)
            self.images.append(self.image_0)
            self.images.append(self.image_1)
            self.images.append(self.image_2)
        self.index +=1        
        if self.index >= len(self.images):        
            self.index=0        
        self.image = self.images[self.index]
player = Player()
#--------------------------------
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super(Player2, self).__init__()
        self.images =  []
        self.image_0 = pygame.image.load('Imagenes/blinky.png').convert()
        self.image_0.set_colorkey(WHITE)
        self.images.append(self.image_0)
        self.index=0        
        self.image = self.images[self.index]        
        self.rect = pygame.Rect(75,45,39,42)
        self.rect.x=75
        self.rect.y=45


    def update(self):
        self.tecla = pygame.key.get_pressed()
        if self.tecla[pygame.K_d]:
            self.images= []
            self.image_0= pygame.image.load("Imagenes/blinky.png").convert()
            self.image_0.set_colorkey(WHITE)
            self.images.append(self.image_0)
        if self.tecla[pygame.K_a]:
            self.images= []                    
            self.image_0= pygame.image.load("Imagenes/blinkyiz.png").convert()
            self.image_0.set_colorkey(WHITE)
            self.images.append(self.image_0)
        if self.tecla[pygame.K_w]:
            self.images= []
            self.image_0= pygame.image.load("Imagenes/blinkyar.png").convert()
            self.image_0.set_colorkey(WHITE)
            self.images.append(self.image_0)
        if self.tecla[pygame.K_s]:
            self.images= []
            self.image_0= pygame.image.load("Imagenes/blinkyab.png").convert()
            self.image_0.set_colorkey(WHITE)
            self.images.append(self.image_0)
        self.index +=1        
        if self.index >= len(self.images):        
            self.index=0        
        self.image = self.images[self.index]
player2 = Player2()

#----------------------- IMPLEMENTO:BOMBA---------------
bomba = pygame.image.load("Imagenes/bomba.png")
la_variable = 0 #La variable 
# -------------------------- IMPLEMENTO: EXPLOCION -----------
#IMAGENES
#CRUZ
bum_cruz_1 = pygame.image.load("Imagenes/explosion_cruz_1.png") 
#LINEA EN EL EJE X
bum_lineax_1 = pygame.image.load("Imagenes/explosion_lineax_1.png") 
#LINEA EN EL EJE Y
bum_lineay_1 = pygame.image.load("Imagenes/explosion_lineay_1.png")
#ESQUINAS
bum_esquina_s_i = pygame.image.load("Imagenes/explosion_esq_s_i_1.png")
bum_esquina_s_d = pygame.image.load("Imagenes/explosion_esq_s_d_1.png")
bum_esquina_i_i = pygame.image.load("Imagenes/explosion_esq_i_i_1.png")
bum_esquina_i_d = pygame.image.load("Imagenes/explosion_esq_i_d_1.png")

bum_borde_arriba = pygame.image.load("Imagenes/explosion_borde_arriba.png")
bum_borde_abajo = pygame.image.load("Imagenes/explosion_borde_abajo.png")
bum_borde_derecha = pygame.image.load("Imagenes/explosion_borde_derecha.png")
bum_borde_izquierda = pygame.image.load("Imagenes/explosion_borde_izquierda.png")
#.---------------------------------------------------------------
bum_pos_x = 1013
bum_pos_y = 525
sound = pygame.mixer.Sound("Sounds/explosion.wav")
aux = 1 
bum_exacto_x = 0
bum_exacto_y = 0
global bomba_estado
bomba_estado = "listo"
#----------------------------------------------------------
inicio_t_bomba = 10000
inicio_t_bum = 10000
#------------------------------------------------------------
my_group = pygame.sprite.Group(player,player2)
clock = pygame.time.Clock()
running = True
while running:
    # Inicializador de tiempo
    tiempo = pygame.time.get_ticks()//1000
    if aux == tiempo:
        aux += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print(player.rect.x,player.rect.y)
            if event.key == pygame.K_RIGHT and player.rect.right < 875 and player.rect.y % 102 != 96:
                player.rect.x += 68
            if event.key == pygame.K_LEFT and player.rect.left > 110 and player.rect.y % 102 != 96:
                player.rect.x -= 68
            if event.key == pygame.K_UP and player.rect.top > 84 and player.rect.x % 136 != 7:
                player.rect.y -= 51
            if event.key == pygame.K_DOWN and player.rect.top < 417 and player.rect.x % 136 != 7:
                player.rect.y += 51
            if event.key == pygame.K_SPACE:
                if bomba_estado == "listo":
                    bomba_pos_x = player.getx() 
                    bomba_pos_y = player.gety() 
                    la_variable = 1 
                    inicio_t_bomba = tiempo
                    bum_exacto_x = player.rect.x
                    bum_exacto_y = player.rect.y
                    bomba_estado = "disparado"
            if event.key == pygame.K_d and player2.rect.right < 875 and player2.rect.y % 102 != 96:
                player2.rect.x += 68
            if event.key == pygame.K_a and player2.rect.left > 110 and player2.rect.y % 102 != 96:
                player2.rect.x -= 68
            if event.key == pygame.K_w and player2.rect.top > 84 and player2.rect.x % 136 != 7:
                player2.rect.y -= 51
            if event.key == pygame.K_s and player2.rect.top < 417 and player2.rect.x % 136 != 7:
                player2.rect.y += 51
            
    my_group.update()
    screen.blit(fondo,[0,0])
    
    #---------------Colocar bomba-------------
    if la_variable != 0: 
        screen.blit(bomba,(bomba_pos_x,bomba_pos_y))
    
    #----------------tiempo----------------
    if tiempo == inicio_t_bomba + 2:
        print("bomba explotó")
        inicio_t_bomba = 10000
        bum_pos_x = bomba_pos_x - 83
        bum_pos_y = bomba_pos_y - 70
        bomba_pos_x = 1013
        bomba_pos_y = 525
        inicio_t_bum = tiempo
        sound.play()
    if tiempo == inicio_t_bum + 1:
        inicio_t_bum = 10000
        bum_pos_x = 1013
        bum_pos_y = 525
        bomba_estado = "listo"
    #-------------Condicionales para la explosion: ---------------------

    if bum_exacto_y % 102 != 96 and bum_exacto_x % 136 != 7:
        if bum_exacto_y == 45 and bum_exacto_x == 75:
            screen.blit(bum_esquina_s_i,(bum_pos_x,bum_pos_y))
        elif bum_exacto_y == 453 and bum_exacto_x == 75:
            screen.blit(bum_esquina_i_i,(bum_pos_x,bum_pos_y))
        elif bum_exacto_y == 45 and bum_exacto_x == 891:
            screen.blit(bum_esquina_s_d,(bum_pos_x,bum_pos_y))
        elif bum_exacto_y == 453 and bum_exacto_x == 891:
            screen.blit(bum_esquina_i_d,(bum_pos_x,bum_pos_y))
        elif bum_exacto_y % 102 != 96 and bum_exacto_x % 136 != 7 and bum_exacto_y == 453:
            screen.blit(bum_borde_abajo,(bum_pos_x,bum_pos_y))
        elif bum_exacto_y % 102 != 96 and bum_exacto_x % 136 != 7 and bum_exacto_y == 45:
            screen.blit(bum_borde_arriba,(bum_pos_x,bum_pos_y))
        elif bum_exacto_y % 102 != 96 and bum_exacto_x % 136 != 7 and bum_exacto_x == 891:
            screen.blit(bum_borde_derecha,(bum_pos_x,bum_pos_y))
        elif bum_exacto_y % 102 != 96 and bum_exacto_x % 136 != 7 and bum_exacto_x == 75:
            screen.blit(bum_borde_izquierda,(bum_pos_x,bum_pos_y))
        else:
            screen.blit(bum_cruz_1,(bum_pos_x,bum_pos_y))
    if bum_exacto_y % 102 == 96 and bum_exacto_x % 136 != 7:
        screen.blit(bum_lineay_1,(bum_pos_x,bum_pos_y))
    if bum_exacto_y % 102 != 96 and bum_exacto_x % 136 == 7:
        screen.blit(bum_lineax_1,(bum_pos_x,bum_pos_y))

    #---------------------- FIN ----------------------------- 
    my_group.draw(screen)
    pygame.display.update()
    pygame.display.flip()
    clock.tick(10)
pygame.quit()