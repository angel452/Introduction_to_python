import pygame, random
#COLORES
WHITE = (255,255,255)
BLACK = (0,0,0)

#CLASES
class Meteoro(pygame.sprite.Sprite):
    #constructor
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect() 
    #hacer que los meteoros se muevan
    def update(self):
        self.rect.y += 1
    
    #Para que meteoros regresen arriba
        if self.rect.y > 600:
            self.rect.y = -10
            self.rect.x = random.randrange(900)

class Player(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect() 
    #movimiento del jugador con mouse
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0]
        player.rect.y = mouse_pos[1]

pygame.init()

#crear ventana
ventana = [900,600]
screen = pygame.display.set_mode(ventana)

#reloj
clock = pygame.time.Clock()

salir = False
score = 0


meteor_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range (50):
    meteor = Meteoro()
    meteor.rect.x = random.randrange(900)
    meteor.rect.y = random.randrange(600)

    meteor_list.add(meteor)
    all_sprites_list.add(meteor)

player = Player()
all_sprites_list.add(player)

#visibilidad del mouse
pygame.mouse.set_visible(0)

while not salir:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True

    meteor_hit_list = pygame.sprite.spritecollide(player, meteor_list,True)

    all_sprites_list.update()

    for meteor in meteor_hit_list:
        score = score + 1
        print(score)

    #Dibujar en la pantalla
    screen.fill(WHITE)

    #DIBUJAR CREO
    all_sprites_list.draw(screen)

    #actualizar pandalla
    pygame.display.flip()
    clock.tick(50)

pygame.quit()