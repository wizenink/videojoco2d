import pygame
import sys
from pygame.locals import *
import random
sys.path.insert(0, "../")
from dialog import text
from character import *
from scene import serializer
from game import camera
# Inicializar la librería de pygame
pygame.init()

BLANCO = (255,255,255)

# Creamos la pantalla
pantalla = pygame.display.set_mode((800,600))

enemyGroup = pygame.sprite.Group()
playerGroup = pygame.sprite.Group()
solidGroup = pygame.sprite.Group()

enemigo = Enemy1()
player = Player(enemyGroup)
playerGroup.add(player.hitbox)
enemyGroup.add(enemigo.hitbox)
solidGroup.add(player.hitbox)
solidGroup.add(enemigo.hitbox)

clock = pygame.time.Clock()
font = pygame.font.Font(None,25)
message = text.DynamicText(font, "Xulián Basura...",0, autoreset=True)
#groupSprites = pygame.sprite.Group(player,enemigo)

groupSprites = pygame.sprite.Group(player)
hitboxGroup = pygame.sprite.Group(player.hitbox)
level = serializer.loadLevel("bigtest.png")

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
    camara.apply(player)
    level.draw(pantalla,camara)
    # Dibujamos un círculo de color blanco en esa posición en el buffer
    enemigo.move_cpu(player)
    enemigo.update(clock.get_time())
    player.move(pygame.key.get_pressed(), K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE)
    player.update(clock.get_time())
    player.draw(pantalla,camara)
    #player.attackHitbox.draw(pantalla,camara)
    #for hitbox in player.hitboxes:
    #    hitbox[0].draw(pantalla,camara)


    enemigo.draw(pantalla,camara)
    #message.drawText(pantalla)
    #tb.draw(pantalla)
    #tb.setText("Esto es una prueba del sistema de diálogo. sansadjnsdajknasdjnasdnajsndjasbjhsafbjasjbfjbasfbjnasbjfsjabf asdbabsjdhbjasbdhashdas")
    #groupSprites.draw(pantalla)
    # Actualizamos la pantalla
    pygame.display.update()
