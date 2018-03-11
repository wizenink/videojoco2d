import sys
import pygame
from pygame.locals import *
sys.path.insert(0,"../scene")
from scene import Scene

pygame.init()
pantalla = pygame.display.set_mode((800,600))
tile = pygame.image.load("/home/david/Documentos/cuarto/CIIE/videojoco2d/res/tiles/grass.png")
tile2 = pygame.image.load("/home/david/Documentos/cuarto/CIIE/videojoco2d/res/tiles/desert.png")
map = [[tile,tile2],[tile2,tile]]
level = Scene("test",2,2,map,16)
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for evento in pygame.event.get():
        if evento.type == KEYDOWN and evento.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        level.draw(pantalla)
        pygame.display.update()
