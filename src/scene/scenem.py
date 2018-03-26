import pygame
import sys
#Esta clase es la usada para escenas de MENU
class Scene:
    def __init__(self,name,director):
        self.name = name
        self.director = director

    def music(self):
        print("Should override this method") 
        
    def events(self,events):
        print("Should override this method")

    def update(self):
        print("Should override this method")

    def draw(self,*args):
        print("Should override this method")
    
    def groupDraws(self,*args):
        print("Should override this method")
