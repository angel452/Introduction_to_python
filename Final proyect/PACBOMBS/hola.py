import pygame
import menu
from menu import Menu,Creditos #aqui importamos menu.py para tener la funcion menu y la funcion creditos
pygame.init()
WIDTH, HEIGHT = 1013,525
screen = pygame.display.set_mode((WIDTH,HEIGHT))
fondo = pygame.image.load("Imagenes\Fondo.png").convert()
icono = pygame.image.load('Imagenes\logo.png')
pygame.display.set_icon(icono)
pygame.display.set_caption("PACBOMBS")
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
#Clase player
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

    #carga de sprites y movimiento    
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
#-------PLAYER2-------------------------
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super(Player2, self).__init__()
        self.images =  []
        self.image_0 = pygame.image.load('Imagenes/blinky.jpeg').convert()
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
            self.image_0= pygame.image.load("Imagenes/blinky.jpeg").convert()
            self.image_0.set_colorkey(WHITE)
            self.images.append(self.image_0)
        if self.tecla[pygame.K_a]:
            self.images= []                    
            self.image_0= pygame.image.load("Imagenes/blinyiz.jpeg").convert()
            self.image_0.set_colorkey(WHITE)
            self.images.append(self.image_0)
        if self.tecla[pygame.K_w]:
            self.images= []
            self.image_0= pygame.image.load("Imagenes/blinkyar.jpeg").convert()
            self.image_0.set_colorkey(WHITE)
            self.images.append(self.image_0)
        if self.tecla[pygame.K_s]:
            self.images= []
            self.image_0= pygame.image.load("Imagenes/blinkyab.jpeg").convert()
            self.image_0.set_colorkey(WHITE)
            self.images.append(self.image_0)
        self.index +=1        
        if self.index >= len(self.images):        
            self.index=0        
        self.image = self.images[self.index]
#esta comentado para que menu funcione, aqui falta crear una funcion jugar para que ejecute solo el juegp
'''
player2 = Player2()
my_group = pygame.sprite.Group(player,player2)
'''
#aqui definimos las fases, las que son las pantallas en el menu
clock = pygame.time.Clock()
fase = 0
menu = 0
creditos = 1
settings = 2
PACBOMBS = 3

running = True
while running:
    if fase == menu:
        f = Menu()
        if f == 0:
            fase = 3
        elif f == 1:
            fase = 1
        elif f == 2:
            fase = 2
    elif fase == creditos:
        Creditos()#esta funcion imprime los nombres de los creadores
    elif fase == settings:
        print("aca ponemos los settings")
    elif fase == PACBOMBS:
        print("Pacbombs")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and player.rect.right < 875 and player.rect.y % 102 != 96:
                player.rect.x += 68
            if event.key == pygame.K_LEFT and player.rect.left > 110 and player.rect.y % 102 != 96:
                player.rect.x -= 68
            if event.key == pygame.K_UP and player.rect.top > 84 and player.rect.x % 136 != 7:
                player.rect.y -= 51
            if event.key == pygame.K_DOWN and player.rect.top < 417 and player.rect.x % 136 != 7:
                player.rect.y += 51
            if event.key == pygame.K_d and player2.rect.right < 875 and player2.rect.y % 102 != 96:
                player2.rect.x += 68
            if event.key == pygame.K_a and player2.rect.left > 110 and player2.rect.y % 102 != 96:
                player2.rect.x -= 68
            if event.key == pygame.K_w and player2.rect.top > 84 and player2.rect.x % 136 != 7:
                player2.rect.y -= 51
            if event.key == pygame.K_s and player2.rect.top < 417 and player2.rect.x % 136 != 7:
                player2.rect.y += 51
    #comentamos esto para que el menu funcione
    '''
    screen.blit(fondo,[0,0])
    
    my_group.update()
    my_group.draw(screen)
    pygame.display.update()
            
    '''
    clock.tick(10)
    pygame.display.flip()
pygame.quit()
