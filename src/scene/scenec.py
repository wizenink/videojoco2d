import pygame
import sys
sys.path.insert(0,"../")
from game import camera
from character import *
#Esta clase es SOLO para escenas de niveles, ya que aqui usamos la camara

class Scene:
    def __init__(self,name,width,height,map,tilesize,director):
        self.name = name
        self.height = height
        self.width = width
        self.map = map
        self.TILESIZE = tilesize
        self.director = director
        self.camera = camera.Camera(camera.complex_camera,100*32,100*32)
        self.player = Player()
        self.collidables = []
    def add_collidables(self,collidables):
        self.collidables = collidables

    def events(self,events):
        print("Should override this method")

    def update(self):
        print("Should override this method")

    def draw(self,displaysurf):
        for y in range(self.height):
            for x in range(self.width):
                i = (x * self.TILESIZE + self.camera.getX(), y * self.TILESIZE + self.camera.getY())
                displaysurf.blit(self.map[x][y],i)
        for c in self.collidables:
            x,y = c.rect.topleft
            displaysurf.blit(c.image,(x+self.camera.getX(),y+self.camera.getY()))

    