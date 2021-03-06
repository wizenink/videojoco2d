import pygame
import sys
from pygame.locals import *
import random
sys.path.insert(0, "../")
from dialog import text
from character import *
from scene import serializer,scenec
from game import camera
# from groupTest import *

# Inicializar la librería de pygame
pygame.init()

BLANCO = (255,255,255)

# Creamos la pantalla
pantalla = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

enemyGroup = pygame.sprite.Group()
playerGroup = pygame.sprite.Group()
solidGroup = pygame.sprite.Group()

player = Player(dmgGroup = enemyGroup, solidGroup = solidGroup)
enemigo = Enemy1(dmgGroup = playerGroup, solidGroup = solidGroup)
casa = Building((600,400))

playerGroup.add(player.hitbox)
enemyGroup.add(enemigo.hitbox)
solidGroup.add(player.hitbox)
solidGroup.add(enemigo.hitbox)
solidGroup.add(casa)

player.setPosition((300,300))
player.updateHitboxPosition()

clock = pygame.time.Clock()
font = pygame.font.Font(None,25)
message = text.DynamicText(font, "Xulián Basura...",0, autoreset=True)
#groupSprites = pygame.sprite.Group(player,enemigo)

hitboxGroup = pygame.sprite.Group(player.hitbox)
levelName,width,height,map = serializer.loadLevel("bigtest.png")
level = scenec.Scene(levelName,width,height,map,32,solidGroup,None)


#collidables = [MySprite()] * 100
#for c in collidables:
#    c.image = resourceManager.loadImage("enemy1.png")
#    c.rect = pygame.Rect(random.randrange(0,10)*32,random.randrange(0,10)*32,32,32)
#    print(c.rect)
#level.add_collidables(collidables)

camara = camera.Camera(camera.complex_camera,100*32,100*32)
pygame.key.set_repeat(100)

# Bucle infinito
while True:
    clock.tick(60)
    # Para cada evento posible
    for evento in pygame.event.get():

            # Si el evento es la pulsación de la tecla Escape
            if evento.type == KEYDOWN and evento.key == K_ESCAPE:
                    # Se sale del programa
                    pygame.quit()
                    sys.exit()
            if evento.type == pygame.USEREVENT: message.update()
            if (evento.type == KEYDOWN and evento.key == K_SPACE): message.update()


    # Rellenamos la pantalla de color negro
    pantalla.fill((0,0,0))
    camara.update(player)
    #camara.apply(enemigo)
    level.draw(pantalla)
    # Dibujamos un círculo de color blanco en esa posición en el buffer
    player.move(pygame.key.get_pressed(), K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE)
    player.update(clock.get_time())
    enemigo.move_cpu(player)
    enemigo.update(clock.get_time())
    player.draw(pantalla,camara)
    player.hitbox.draw(pantalla,camara)
    enemigo.hitbox.draw(pantalla,camara)
    casa.draw(pantalla,camara)

    for hitbox in player.hitboxes:
        hitbox[0].draw(pantalla,camara)


    enemigo.draw(pantalla,camara)
    #message.drawText(pantalla)
    #tb.draw(pantalla)
    #tb.setText("Esto es una prueba del sistema de diálogo. sansadjnsdajknasdjnasdnajsndjasbjhsafbjasjbfjbasfbjnasbjfsjabf asdbabsjdhbjasbdhashdas")
    #groupSprites.draw(pantalla)
    # Actualizamos la pantalla
    pygame.display.update()
