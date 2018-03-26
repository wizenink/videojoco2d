import pygame
import sys
sys.path.insert(0,"../")
from game import camera
from character import *
#Esta clase es SOLO para escenas de niveles, ya que aqui usamos la camara

class Scene:
    def __init__(self,name,width,height,map,tilesize,solids,director):
        self.name = name
        self.height = height
        self.width = width
        self.map = map
        self.TILESIZE = tilesize
        self.director = director
        self.camera = camera.Camera(camera.complex_camera,100*32,100*32)
        self.collidables = []

    def music(self):
        print("Should override this method")

    def add_collidables(self,collidables):
        self.collidables = collidables

    def events(self,events):
        print("Should override this method")

    def update(self):
        print("Should override this method")

    def draw(self,displaysurf):
        for x in range(self.width):
            for y in range(self.height):
                this = (self.map[x][y])
                if this[1] == True:
                    collidable = Hitbox(32,32,(x,y))
                    solids.add(collidable)
                i = (y * self.TILESIZE + self.camera.getX(), x * self.TILESIZE + self.camera.getY())
                displaysurf.blit(this[0],i)

