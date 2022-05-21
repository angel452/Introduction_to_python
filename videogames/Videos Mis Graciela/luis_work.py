mport pygame
#colores por si se necesitan
BLACK       = (   0,   0,   0)
WHITE       = ( 255, 255, 255)
GREEN       = (   0, 255,   0)
RED         = ( 255,   0,   0)
BLUE        = (   0,   0, 255)
WHITEBLUE   = (   0, 170, 228)
PURPLE      = (  87,  35, 100)
WHITESOLID  = ( 277, 277, 277)
#dimensiones del programa
WIDTH = 1013
HEIGHT = 525

pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("PACBOMBS")
fondo = pygame.image.load("Fondo.png").convert()#imagen de fondo
clock=pygame.time.Clock()
#clase para guadar el sprite de pacman
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pacman.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx=WIDTH//2
        self.rect.bottom= HEIGHT-10
        self.speed_x = 0
        self.speed_y = 0
    #funcion para cambiar movimiento
    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        keystate = pygame.key.get_pressed()
        # movimiento de derecha-izquierda con bordes
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        if self.rect.right > 940:#limite de derecha
            self.rect.right = 940
        if self.rect.left < 64:#limite de izquierda
            self.rect.left = 64
        #movimiento de arriba-abajo con bordes          
        if keystate[pygame.K_UP]:
            self.speed_y = -5
        if keystate[pygame.K_DOWN]:
            self.speed_y = 5
        self.rect.y += self.speed_y
        if self.rect.bottom > 505:#limite de abajo
            self.rect.bottom = 505
        if self.rect.top < 34:#limite de arriba
            self.rect.top = 34


#pygame.mouse.set_visible(0)
#agregar al grupo para ser usado
all_sprite_list = pygame.sprite.Group()
player = Player()
all_sprite_list.add(player)


running = True
#evento principal
while running:
    clock.tick(60)
    for event in pygame.event.get():
        print(event)#imprime lo que sucede
        mouse_pos = pygame.mouse.get_pos()
        print("m_p",mouse_pos)#imprime la posicion del mouse
        if event.type == pygame.QUIT:
            running = False
        print(player.rect.x,player.rect.y)#imprime la posicion del pacman
    all_sprite_list.update()#actualizacion de movimiento
    #zona de dibujo

    
    screen.blit(fondo,[0,0])#pone la imagen de fondo en el programa
    all_sprite_list.draw(screen)#dibuja el pacman
    #imprime los cuadrados negros(estos se pueden cambiar, el objetivo es que reconozca los conos para no chocarlos)
    pygame.draw.rect(screen, BLACK,(144,106,55,38))
    pygame.draw.rect(screen, BLACK,(277,106,55,38))
    pygame.draw.rect(screen, BLACK,(407,106,55,38))
    pygame.draw.rect(screen, BLACK,(540,106,55,38))
    pygame.draw.rect(screen, BLACK,(671,106,55,38))
    pygame.draw.rect(screen, BLACK,(804,106,55,38)) 
    pygame.draw.rect(screen, BLACK,(144,206,55,38))
    pygame.draw.rect(screen, BLACK,(277,206,55,38))
    pygame.draw.rect(screen, BLACK,(407,206,55,38))
    pygame.draw.rect(screen, BLACK,(540,206,55,38))
    pygame.draw.rect(screen, BLACK,(671,206,55,38))
    pygame.draw.rect(screen, BLACK,(804,206,55,38))   
    pygame.draw.rect(screen, BLACK,(144,306,55,38))
    pygame.draw.rect(screen, BLACK,(277,306,55,38))
    pygame.draw.rect(screen, BLACK,(407,306,55,38))
    pygame.draw.rect(screen, BLACK,(540,306,55,38))
    pygame.draw.rect(screen, BLACK,(671,306,55,38))
    pygame.draw.rect(screen, BLACK,(804,306,55,38)) 
    pygame.draw.rect(screen, BLACK,(144,406,55,38))
    pygame.draw.rect(screen, BLACK,(277,406,55,38))
    pygame.draw.rect(screen, BLACK,(407,406,55,38))
    pygame.draw.rect(screen, BLACK,(540,406,55,38))
    pygame.draw.rect(screen, BLACK,(671,406,55,38))
    pygame.draw.rect(screen, BLACK,(804,406,55,38))   
    pygame.display.flip()





pygame.quit()