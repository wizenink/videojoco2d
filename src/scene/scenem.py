import pygame
#Esta clase es la usada para escenas de MENU
class Scene:
    def __init__(self,name,director):
        self.name = name
        self.director = director
        
    def events(self,events):
        print("Should override this method")

    def update(self):
        print("Should override this method")

    def draw(self,*args):
        print("Should override this method")
    
    def groupDraws(self,*args):
        print("Should override this method")
