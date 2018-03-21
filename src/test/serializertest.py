import pygame
import sys
from pygame.locals import *
sys.path.insert(0, "../")
from scene import serializer
pygame.init()
pantalla = pygame.display.set_mode((800,600))
level = loadLevel("bigtest.png")
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for evento in pygame.event.get():
        if evento.type == KEYDOWN and evento.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        level.draw(pantalla)
        pygame.display.update()
