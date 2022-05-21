import pygame,random
pygame.init()

#CREACION DE CLASES
class Laser(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("laser.png").convert()
        self.image.set_colorkey(WHITE) 
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 5

class Meteor(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert()
        self.image.set_colorkey(WHITE) 
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert()
        self.image.set_colorkey(WHITE) 
        self.rect = self.image.get_rect()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0]
        player.rect.y = 510


#COLORES
BLACK = (0,0,0)
WHITE = (255,255,255)

#bisivilidad del mouse
pygame.mouse.set_visible(0)

#Crear ventana
tam_vantana = (900,600)
screen = pygame.display.set_mode(tam_vantana)

#Temoporizador 
clock = pygame.time.Clock()

#ADICIONAL
score = 0 #marcador

# AGRAGAR TODOS A SPRITE
all_sprite_list = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()

#------------------PARA EL METEOR -------------------
for i in range (40):
    meteor = Meteor()
    meteor.rect.x = random.randrange(800)
    meteor.rect.y = random.randrange(350)
    meteor_list.add(meteor)
    all_sprite_list.add(meteor)


# CREAMOS INSTANCIAS
player = Player()
all_sprite_list.add(player)

done = 0 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        #HACER QUE APARESCA UN LASER
        if event.type ==  pygame.MOUSEBUTTONDOWN:
            laser = Laser()
            laser.rect.x = player.rect.x + 74
            laser.rect.y = player.rect.y - 25
            
            all_sprite_list.add(laser)
            laser_list.add(laser)
        


    #Mostrar pantalla
    all_sprite_list.update()

    #HACER LAS COLISIONES
    for laser in laser_list:
        meteor_hit_list = pygame.sprite.spritecollide(laser,meteor_list, True)
        for meteor in meteor_hit_list:
            all_sprite_list.remove(laser)
            laser_list.remove(laser)
            score += 1
            print(score)
        if laser.rect.y < -10:
            all_sprite_list.remove(laser)
            laser_list.remove(laser)

    screen.fill(WHITE)
    all_sprite_list.draw(screen)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()

