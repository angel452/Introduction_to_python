import pygame
import menu
from menu import Menu,Creditos,Settings #aqui importamos menu.py para tener la funcion menu y la funcion creditos
WIDTH, HEIGHT = 1013,525
icono = pygame.image.load('Imagenes/logo.png')
pygame.display.set_icon(icono)
pygame.display.set_caption("PACBOMBS")

pygame.mixer.init() #Para carcar sonido
sound = pygame.mixer.Sound("pacwalk0.ogg")
sound2 = pygame.mixer.Sound("ghostw.ogg")
sound3 = pygame.mixer.Sound("doom_map.ogg")
sound4 = pygame.mixer.Sound("explosion.wav")

#--------------COLORES------------------------------
BLACK       = (   0,   0,   0)
WHITE       = ( 255, 255, 255)
GREEN       = (   0, 255,   0)
RED         = ( 255,   0,   0)
BLUE        = (   0,   0, 255)
WHITEBLUE   = (   0, 170, 228)
PURPLE      = (  87,  35, 100)
WHITESOLID  = ( 277, 277, 277)
GRAY        = ( 184, 184, 192)
#---------------SPRITES RIGHT----------------------
pygame.display.set_mode() #habilite la primera pantalla

#-------------------  AREGLO DE IMAGENES ----------------------------
image_PR1= pygame.image.load("Imagenes/pacman0.png").convert()
image_PR2= pygame.image.load("Imagenes/pacman1.png").convert()
image_PR3= pygame.image.load("Imagenes/pacman2.png").convert()
imagePR = [image_PR1,image_PR2,image_PR3]

image_BR1= pygame.image.load("Imagenes/blinky1.png").convert()
image_BR2= pygame.image.load("Imagenes/blinky1.png").convert()
image_BR3= pygame.image.load("Imagenes/blinky1.png").convert()
imageBR = [image_BR1,image_BR2,image_BR3]

imageR = [imagePR,imageBR]

#---------------SPRITES LEFT----------------------

image_PL1= pygame.image.load("Imagenes/pacman0.png").convert()
image_PL2= pygame.image.load("Imagenes/pacman1_left.png").convert()
image_PL3= pygame.image.load("Imagenes/pacman2_left.png").convert()
imagePL = [image_PL1,image_PL2,image_PL3]

image_BL1= pygame.image.load("Imagenes/blinkyiz.png").convert()
image_BL2= pygame.image.load("Imagenes/blinky1iz.png").convert()
image_BL3= pygame.image.load("Imagenes/blinky1.png").convert()
imageBL = [image_BL1,image_BL2,image_BL3]

imageL = [imagePL,imageBL]

#---------------SPRITES UP----------------------

image_PU1= pygame.image.load("Imagenes/pacman0.png").convert()
image_PU2= pygame.image.load("Imagenes/pacman1_up.png").convert()
image_PU3= pygame.image.load("Imagenes/pacman2_up.png").convert()
imagePU = [image_PU1,image_PU2,image_PU3]

image_BU1= pygame.image.load("Imagenes/blinkyar.png").convert()
image_BU2= pygame.image.load("Imagenes/blinkyar.png").convert()
image_BU3= pygame.image.load("Imagenes/blinkyar.png").convert()
imageBU = [image_BU1,image_BU2,image_BU3]

imageU = [imagePU,imageBU]

#---------------SPRITES DOWN----------------------

image_PD1= pygame.image.load("Imagenes/pacman0.png").convert()
image_PD2= pygame.image.load("Imagenes/pacman1_down.png").convert()
image_PD3= pygame.image.load("Imagenes/pacman2_down.png").convert()
imagePD = [image_PD1,image_PD2,image_PD3]

image_BD1= pygame.image.load("Imagenes/blinkyab.png").convert()
image_BD2= pygame.image.load("Imagenes/blinkyab.png").convert()
image_BD3= pygame.image.load("Imagenes/blinkyab.png").convert()
imageBD = [image_BD1,image_BD2,image_BD3]

imageD = [imagePD,imageBD]

#-------------------------SKIN---------------------------------

images = [imageR,imageL,imageU,imageD] #Englobamos todas las imagenes de arriba 
image = [images[0][1][0],images[0][1][1],images[0][1][2]]
#image = images[direccion(rigtn,letft,up,dowun)][personaje][animación]

#Clase player
class Player(pygame.sprite.Sprite):
    def __init__(self): #Inicializador
        super(Player, self).__init__() #para formar un bucle
        self.images =  []
        self.ELE_P = 1 #nos permite escojer el personaje (=)
        self.image_0 = images[0][self.ELE_P][0]
        self.image_0.set_colorkey(WHITE)
        self.images.append(self.image_0)
        self.index=0        
        self.image = self.images[self.index] #    
        self.rect = pygame.Rect(75,45,39,42)
        self.rect.x=75  #posiciones
        self.rect.y=45  #posiciones
    
    #carga de sprites y movimiento    
    def update(self):
        self.tecla = pygame.key.get_pressed() #Reconose que tecla presione
        if self.tecla[pygame.K_RIGHT]:
            self.image = images[0][self.ELE_P] #[0] mirar a la derecha
            self.images = [self.image[0],self.image[1],self.image[2]]
            self.images[0].set_colorkey(WHITE)
            self.images[1].set_colorkey(WHITE)
            self.images[2].set_colorkey(WHITE)
            sound.play() #reproducir sonido
        
        if self.tecla[pygame.K_LEFT]:    
            self.image = images[1][self.ELE_P] #[1] mirar izquierda
            self.images = [self.image[0],self.image[1],self.image[2]]
            self.images[0].set_colorkey(WHITE)
            self.images[1].set_colorkey(WHITE)
            self.images[2].set_colorkey(WHITE)
            sound.play()
        if self.tecla[pygame.K_UP]:
            
            self.image = images[2][self.ELE_P] #[1] mirar arriba
            self.images = [self.image[0],self.image[1],self.image[2]]
            self.images[0].set_colorkey(WHITE)
            self.images[1].set_colorkey(WHITE)
            self.images[2].set_colorkey(WHITE)
            sound.play()
        if self.tecla[pygame.K_DOWN]:
            
            self.image = images[3][self.ELE_P] #[1] mirar abajo
            self.images = [self.image[0],self.image[1],self.image[2]]
            self.images[0].set_colorkey(WHITE)
            self.images[1].set_colorkey(WHITE)
            self.images[2].set_colorkey(WHITE)
            sound.play()
        #Para cargar animacion
        self.index += 1  #index == 0 anteriormente
        if self.index >= len(self.images): #self.images = 3 ya que son tres animaciones        
            self.index=0        
        self.image = self.images[self.index]
#-------PLAYER2-------------------------
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super(Player2, self).__init__()
        self.images =  []
        self.ELE_P = 0 #nos permite escojer el personaje (=)
        self.image_0 = images[0][self.ELE_P][0]
        self.image_0.set_colorkey(WHITE)
        self.images.append(self.image_0)
        self.index = 0        
        self.image = self.images[self.index]        
        self.rect = pygame.Rect(891,453,39,42)
        self.rect.x=891
        self.rect.y=453
    def update(self):
        self.tecla = pygame.key.get_pressed()
        if self.tecla[pygame.K_d]:
            self.image = images[0][self.ELE_P]
            self.images = [self.image[0],self.image[1],self.image[2]]
            self.images[0].set_colorkey(WHITE)
            self.images[1].set_colorkey(WHITE)
            self.images[2].set_colorkey(WHITE)
            sound2.play()
        if self.tecla[pygame.K_a]:
            self.image = images[1][self.ELE_P]
            self.images = [self.image[0],self.image[1],self.image[2]]
            self.images[0].set_colorkey(WHITE)
            self.images[1].set_colorkey(WHITE)
            self.images[2].set_colorkey(WHITE)
            sound2.play()
        if self.tecla[pygame.K_w]:
            self.image = images[2][self.ELE_P]
            self.images = [self.image[0],self.image[1],self.image[2]]
            self.images[0].set_colorkey(WHITE)
            self.images[1].set_colorkey(WHITE)
            self.images[2].set_colorkey(WHITE)
            sound2.play()
        if self.tecla[pygame.K_s]:
            self.image = images[3][self.ELE_P]
            self.images = [self.image[0],self.image[1],self.image[2]]
            self.images[0].set_colorkey(WHITE)
            self.images[1].set_colorkey(WHITE)
            self.images[2].set_colorkey(WHITE)
            sound2.play()
        self.index +=1        
        if self.index >= len(self.images):        
            self.index=0        
        self.image = self.images[self.index]

#----------------- CLASE BOMBA----------------------------
class Bombs(pygame.sprite.Sprite):
    def __init__(self):
        super(Bombs, self).__init__()
        self.bomba = pygame.image.load("Imagenes/bomba.png").convert() #subimos imagenes
        self.bomba.set_colorkey(BLACK)
        self.images = []
        self.images.append(self.bomba)
        self.image = self.images[0]
        self.la_variable = 0 #La variable 
        self.time=0
        self.explode = self.bomba #manejar las posiciones de la bomba 
        self.space = pygame.Rect(1013,525,35,33)
        self.bomba_estado = "listo"
        self.bomba_activa = "no_activa"
  #--------IMAGENES-----------------------
  # CRUZ
        self.bum_cruz_1 = pygame.image.load("Imagenes/explosion_cruz_1.png").convert() 
  #LINEA EN EL EJE X
        self.bum_lineax_1 = pygame.image.load("Imagenes/explosion_lineax_1.png").convert() 
  #LINEA EN EL EJE Y
        self.bum_lineay_1 = pygame.image.load("Imagenes/explosion_lineay_1.png").convert()
  #ESQUINAS
        self.bum_esquina_s_i = pygame.image.load("Imagenes/explosion_esq_s_i_1.png").convert()
        self.bum_esquina_s_d = pygame.image.load("Imagenes/explosion_esq_s_d_1.png").convert()    
        self.bum_esquina_i_i = pygame.image.load("Imagenes/explosion_esq_i_i_1.png").convert()
        self.bum_esquina_i_d = pygame.image.load("Imagenes/explosion_esq_i_d_1.png").convert()
    #BORDES
        self.bum_borde_arriba = pygame.image.load("Imagenes/explosion_borde_arriba.png").convert()
        self.bum_borde_abajo = pygame.image.load("Imagenes/explosion_borde_abajo.png").convert()
        self.bum_borde_derecha = pygame.image.load("Imagenes/explosion_borde_derecha.png").convert()
        self.bum_borde_izquierda = pygame.image.load("Imagenes/explosion_borde_izquierda.png").convert()
  #.-----------------------------------------------------------------------------------------------------
        self.bum_pos_x = 1013
        self.bum_pos_y = 525
        self.rect = pygame.Rect(self.bum_pos_x,self.bum_pos_y,35,33) #crea un rectangulo
        self.aux = 1 
        self.bum_exacto_x = 0
        self.bum_exacto_y = 0
        self.inicio_t_bomba = 10000
        self.inicio_t_bum = 10000
    
    def update(self):
    #---------------Colocar-bomba-------------
        if self.la_variable == 1:
            self.la_variable = 2 
        #----------------tiempo----------------
        if self.time == self.inicio_t_bomba + 2:
            print("bomba explotó")
            self.bomba_activa = "activa"
            sound4.play()
            self.rect = self.space #ponemos al rect en las posiciones del space
            self.inicio_t_bomba = 1000
            self.inicio_t_bum = self.time
            self.image = self.explode #vuelve a ser bomba en el sprite
            print(self.space)
            print(self.bum_exacto_x,self.bum_exacto_y )
            self.image.set_colorkey(BLACK)
        if self.time == self.inicio_t_bum + 1:
            self.image = self.bomba
            self.inicio_t_bum = 10000
            self.bum_pos_x = 1013
            self.bum_pos_y = 525
            self.rect = pygame.Rect(self.bum_pos_x,self.bum_pos_y,35,33)
            self.bomba_estado = "listo"
            self.bomba_activa = "no_activa"
        #-------------Condicionales para la explosion: ---------------------
        if self.bum_exacto_y % 102 != 96 and self.bum_exacto_x % 136 != 7:
            if self.bum_exacto_y == 45 and self.bum_exacto_x == 75:
                self.explode = self.bum_esquina_s_i
                self.bum_esquina_s_i.set_colorkey(BLACK)
            elif self.bum_exacto_y == 453 and self.bum_exacto_x == 75:
                self.explode = self.bum_esquina_i_i
                self.bum_esquina_i_i.set_colorkey(BLACK)
            elif self.bum_exacto_y == 45 and self.bum_exacto_x == 891:
                self.explode = self.bum_esquina_s_d
                self.bum_esquina_s_d.set_colorkey(BLACK)
            elif self.bum_exacto_y == 453 and self.bum_exacto_x == 891:
                self.explode = self.bum_esquina_i_d
                self.bum_esquina_i_d.set_colorkey(BLACK)
            elif self.bum_exacto_y % 102 != 96 and self.bum_exacto_x % 136 != 7 and self.bum_exacto_y == 453:
                self.explode = self.bum_borde_abajo
                self.bum_borde_abajo.set_colorkey(BLACK)
            elif self.bum_exacto_y % 102 != 96 and self.bum_exacto_x % 136 != 7 and self.bum_exacto_y == 45:
                self.explode = self.bum_borde_arriba
                self.bum_borde_arriba.set_colorkey(BLACK)
            elif self.bum_exacto_y % 102 != 96 and self.bum_exacto_x % 136 != 7 and self.bum_exacto_x == 891:
                self.explode = self.bum_borde_derecha
                self.bum_borde_derecha.set_colorkey(BLACK)
            elif self.bum_exacto_y % 102 != 96 and self.bum_exacto_x % 136 != 7 and self.bum_exacto_x == 75:
                self.explode = self.bum_borde_izquierda
                self.bum_borde_izquierda.set_colorkey(BLACK)
            else:
                self.explode = self.bum_cruz_1
                self.bum_cruz_1.set_colorkey(BLACK)
            self.space = pygame.Rect(self.bum_exacto_x-78,self.bum_exacto_y-60,68*3,51*3)
        if self.bum_exacto_y % 102 == 96 and self.bum_exacto_x % 136 != 7:
            self.explode = self.bum_lineay_1
            self.bum_lineay_1.set_colorkey(WHITE)
            self.space = pygame.Rect(self.bum_exacto_x,self.bum_exacto_y-60,68,51*3)  
        if self.bum_exacto_y % 102 != 96 and self.bum_exacto_x % 136 == 7:
            self.explode = self.bum_lineax_1
            self.bum_lineax_1.set_colorkey(WHITE)
            self.space = pygame.Rect(self.bum_exacto_x-78,self.bum_exacto_y,68*3,51)

class Game(object): #Importantisima
    def __init__(self):
        self.player = Player()
        self.player2 = Player2()
        self.acme = Bombs() #para el jugador 1
        self.acme2 = Bombs() #para el jugador 2
        self.game_over = False
        self.my_group = pygame.sprite.Group(self.player,self.player2)
        self.my_players = pygame.sprite.Group(self.player,self.player2) #
        self.my_bombs = pygame.sprite.Group()
    
    def process_events(self):
        pygame.init()
        self.acme.time = pygame.time.get_ticks()//1000 #para jugador 1
        if self.acme.aux == self.acme.time:
            self.acme.aux += 1
        self.acme2.time = pygame.time.get_ticks()//1000 #para jugador 2
        if self.acme2.aux == self.acme2.time:
            self.acme2.aux += 1
        if self.acme.bomba_activa == "activa" or self.acme2.bomba_activa == "activa": 
            self.my_bombs.add(self.acme)
            self.my_bombs.add(self.acme2)
            acerte = pygame.sprite.groupcollide(self.my_bombs,self.my_players, True, True) #reconoce las coliciones
            if acerte:
                self.game_over = True #aqui que returne ek game over y pida abrir de nuevo el juego
                #aqui volovemos la expresion verdadera para llevar el game over

        for event in pygame.event.get(): #obtiene cuando presionamos algo 
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN: #se reinicia todo 
                if self.game_over:
                    self.__init__() #renicia 
                    pygame.display.flip()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and self.player.rect.right < 875 and self.player.rect.y % 102 != 96 :
                    self.player.rect.x += 68
                if event.key == pygame.K_LEFT and self.player.rect.left > 110 and self.player.rect.y % 102 != 96 :
                    self.player.rect.x -= 68
                if event.key == pygame.K_UP and self.player.rect.top > 84 and self.player.rect.x % 136 != 7 :
                    self.player.rect.y -= 51
                if event.key == pygame.K_DOWN and self.player.rect.top < 417 and self.player.rect.x % 136 != 7 :
                    self.player.rect.y += 51
                if event.key == pygame.K_SPACE and self.acme.bomba_estado == "listo":
                    self.my_group.add(self.acme)
                    self.acme.rect = pygame.Rect(self.player.rect.x,self.player.rect.y,35,33)
                    self.acme.bum_pos_x = self.player.rect.x 
                    self.acme.bum_pos_y = self.player.rect.y 
                    self.acme.la_variable = 1 
                    self.acme.inicio_t_bomba = self.acme.time
                    self.acme.bum_exacto_x = self.player.rect.x
                    self.acme.bum_exacto_y = self.player.rect.y
                    self.acme.bomba_estado = "no_listo"
                if event.key == pygame.K_d and self.player2.rect.right < 875 and self.player2.rect.y % 102 != 96 :
                    self.player2.rect.x += 68
                if event.key == pygame.K_a and self.player2.rect.left > 110 and self.player2.rect.y % 102 != 96 :
                    self.player2.rect.x -= 68
                if event.key == pygame.K_w and self.player2.rect.top > 84 and self.player2.rect.x % 136 != 7 :
                    self.player2.rect.y -= 51
                if event.key == pygame.K_s and self.player2.rect.top < 417 and self.player2.rect.x % 136 != 7 :
                    self.player2.rect.y += 51
                if event.key == pygame.K_m and self.acme2.bomba_estado == "listo":
                    self.my_group.add(self.acme2)
                    self.acme2.rect = pygame.Rect(self.player2.rect.x,self.player2.rect.y,35,33)
                    self.acme2.bum_pos_x = self.player2.rect.x 
                    self.acme2.bum_pos_y = self.player2.rect.y 
                    self.acme2.la_variable = 1 
                    self.acme2.inicio_t_bomba = self.acme2.time
                    self.acme2.bum_exacto_x = self.player2.rect.x
                    self.acme2.bum_exacto_y = self.player2.rect.y
                    self.acme2.bomba_estado = "no_listo"
        return False #sigue corriendo el codigo ya que en el while running es falso 
    
    def run_logic(self):
        self.my_group.update() #para actualizar
    
    def display_frame(self,screen): #aqui dibujamos todas las imagenes
        screen.fill(WHITE)
        fondo = pygame.image.load("Imagenes/Fondo.png").convert()
        screen.blit(fondo,[0,0])
        pygame.display.update()
        if self.game_over:
            font=pygame.font.SysFont("serif",35)#fuente
            text = font.render("Game Over, click para continuar", False, BLACK)# texto
            center_x = (WIDTH//2)-(text.get_width()//2) #posiciones para que este en el centro 
            center_y = (HEIGHT//2)-(text.get_height()//2)  #posiciones para que este en el centro 
            screen.blit(text, [center_x,center_y])# ponerlo en pantalla
        if not self.game_over:
            self.my_group.draw(screen)
            pygame.display.flip()
        pygame.display.flip()

def main(): #aqui se llama a todo lo anterior 
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    FPS = 10 #Frames per second
    clock = pygame.time.Clock() #tiempo en el juego
    fase = 0
    menu = 0
    creditos = 1
    settings = 2
    PACBOMBS = 3
    running = False
    game = Game()
    pygame.mixer.music.load("menu_s.ogg")
    pygame.mixer.music.play(1) #insertamos musica una y otra vez
    while not running: #si mueres el running se vuelve verdadero y no corre nada de esto
        pygame.display.flip()
        if fase == menu: # 0 == 0
            f = Menu()
            if f == 0:
                fase = 3
                pygame.mixer.music.set_volume(0) #Bajamos volumen
                sound3.play()   
            elif f == 1:
                fase = 1
            elif f == 2:
                fase = 2
        elif fase == creditos:
            clock.tick(10)
            pygame.display.flip()
            f =  Creditos()#esta funcion imprime los nombres de los creadores
            if f == 0:
                fase = 0 #escape
        elif fase == settings:
            running = game.process_events()
            Settings()
            f = Settings()
            if f == 0:
                game.player.ELE_P = 0
                game.player2.ELE_P = 1
                print(game.player.ELE_P)
                fase = 0
            elif f == 1:
                game.player.ELE_P  = 1
                game.player2.ELE_P = 0
                print(game.player.ELE_P)
                fase = 0
            elif f == 2:
                fase = 0

        elif fase == PACBOMBS:
            running = game.process_events()
            game.run_logic()
            game.display_frame(screen)
            clock.tick(10) #cambio entre sprites posiblemente 
            if game.process_events() == 1: #
                fase = 0
    pygame.quit()

if __name__ == "__main__":
    main()