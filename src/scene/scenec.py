import pygame
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Scene:
    map = [[]]
    name = ""
    width = 0
    height = 0
    collidables = []
    def __init__(self,name,width,height,map,tilesize):
        self.name = name
        self.height = height
        self.width = width
        self.map = map
        self.TILESIZE = tilesize

    def add_collidables(self,collidables):
        self.collidables = collidables

    def draw(self,displaysurf,camera):
        for y in range(self.height):
            for x in range(self.width):
                i = (x * self.TILESIZE + camera.getX(), y * self.TILESIZE + camera.getY())
                displaysurf.blit(self.map[x][y],i)
        for c in self.collidables:
            x,y = c.rect.topleft
            displaysurf.blit(c.image,(x+camera.getX(),y+camera.getY()))
