import pygame
class Scene:
    map = [[]]
    name = ""
    width = 0
    height = 0
    def __init__(self,name,width,height,map,tilemap):
        self.name = name
        self.height = height
        self.width = width
        self.map = map
    def draw(self,displaysurf,width,height):
        for y in range(height):
            for x in range(width):
                pygame.draw.blit(displaysurf,this.map[x,y],(y*TILESIZE,x*TILESIZE))
