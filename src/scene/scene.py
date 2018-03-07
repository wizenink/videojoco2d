import pygame
TILESIZE = 32
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Scene:
    map = [[]]
    name = ""
    width = 0
    height = 0
    def __init__(self,name,width,height,map):
        self.name = name
        self.height = height
        self.width = width
        self.map = map
    def map_to_screen(self, point):
        x = (SCREEN_WIDTH + (point[1] - point[0]) * TILESIZE) / 2
        y = (SCREEN_HEIGHT + (point[1] + point[0]) * TILESIZE) / 2
        return (x, y)
    def draw(self,displaysurf,width,height):
        for y in range(height):
            for x in range(width):
                cartx = x * TILESIZE
                carty = y * TILESIZE
                point = (cartx,carty)
                i = self.map_to_screen(point)
                displaysurf.blit(self.map[x][y],i)
