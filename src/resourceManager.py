import pygame, sys, os
from pygame.locals import *
import configparser


# Constants
MAIN_FOLDER = "/Users/Bruno/Desktop/CIIE/videojoco2d/res/"
CHARACTER_SPRITE_FOLDER = MAIN_FOLDER + "characters/"
BLUEPRINT_LEVEL_FOLDER = MAIN_FOLDER + "level/"
TERRAIN_TEXTURE_FOLDER = MAIN_FOLDER + "texture/"


class resourceManager(object):
    resources = {}

    @classmethod
    def loadImage(cls, name, colorkey = None):
        if name in cls.resources:
            return cls.resources[name]
        else:
            fullname = os.path.join(CHARACTER_SPRITE_FOLDER,name)
            try:
                image = pygame.image.load(fullname)
            except pygame.error:
                print('Cannot load image:'), fullname
                print(pygame.get_error())
                raise SystemExit
            image = image.convert()
            if colorkey is not None:
                if colorkey is -1:
                    colorkey = imagen.get_at((0,0))
                imagen.set_colorkey(colorkey, RLEACCEL)
            # Se almacena
            cls.resources[name] = image
            # Se devuelve
            return image

    @classmethod
    def loadData(cls, name):
        if name in cls.resources:
            return cls.resources[name]
        else:
            fullname = os.path.join(CHARACTER_SPRITE_FOLDER,name)
            config = configparser.ConfigParser()
            config.sections()
            config.read(fullname)
            result = []
            result.append((int(config['walk']['rectx']),int(config['walk']['recty'])))
            result.append(int(config['walk']['starty']))
            result.append(int(config['walk']['frames']))

            cls.resources[name] = result
            return result


    @classmethod
    def loadLevel(cls, name, colorkey = None):
        if name in cls.resources:
            return cls.resources[name]
        else:
            fullname = os.path.join(BLUEPRINT_LEVEL_FOLDER,name)
            try:
                image = pygame.image.load(fullname)
            except pygame.error:
                print ('Cannot load image:'), fullname
                raise SystemExit
            image = image.convert()
            if colorkey is not None:
                if colorkey is -1:
                    colorkey = imagen.get_at((0,0))
                imagen.set_colorkey(colorkey, RLEACCEL)
            # Se almacena
            cls.resources[name] = image
            # Se devuelve
            return imagen
