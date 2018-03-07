import pygame
import sys
from pygame.locals import *
sys.path.insert(0, "../")
from character import *

# Inicializar la librería de pygame
pygame.init()

BLANCO = (255,255,255)

# Creamos la pantalla
pantalla = pygame.display.set_mode((800,600))

player1 = Player()
enemigo = Enemy1()

clock = pygame.time.Clock()

groupSprites = pygame.sprite.Group(player1,enemigo)


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


    # Rellenamos la pantalla de color negro
    pantalla.fill((0,0,0))

    # Dibujamos un círculo de color blanco en esa posición en el buffer
    enemigo.move_cpu(player1)
    enemigo.update(clock.get_time())
    player1.move(pygame.key.get_pressed(), K_UP, K_DOWN, K_LEFT, K_RIGHT)
    player1.update(clock.get_time())
    groupSprites.draw(pantalla)

    # Actualizamos la pantalla
    pygame.display.update()
