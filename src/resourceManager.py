import pygame, sys, os
from pygame.locals import *
import configparser
import numpy as np

dirname = os.path.dirname(__file__)

# Constants
MAIN_FOLDER = os.path.join(dirname,"../res")
CHARACTER_SPRITE_FOLDER = os.path.join(MAIN_FOLDER,"characters")
BLUEPRINT_LEVEL_FOLDER = os.path.join(MAIN_FOLDER,"level")
TERRAIN_TEXTURE_FOLDER = os.path.join(MAIN_FOLDER,"texture")


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
                print('Cannot load image:')
                print(pygame.get_error())
                raise SystemExit
            image = image.convert()

            if colorkey is not None:
                if colorkey is -1:
                    colorkey = imagen.get_at((0,0))
                image.set_colorkey(colorkey, RLEACCEL)
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
            walk = []
            walk.append((int(config['walk']['rectx']),int(config['walk']['recty'])))
            walk.append(int(config['walk']['starty']))
            walk.append(int(config['walk']['frames']))


            atack = []
            atack.append((int(config['atack']['rectx']),int(config['atack']['recty'])))
            atack.append(int(config['atack']['starty']))
            atack.append(int(config['atack']['frames']))

            cls.resources[name] = (walk, atack)
            return (walk, atack)


    @classmethod
    def loadLevel(cls, name, colorkey = None):
        if name in cls.resources:
            return cls.resources[name]
        else:
            fullname = os.path.join(BLUEPRINT_LEVEL_FOLDER,name)
            try:
                image = pygame.image.load(fullname)
            except pygame.error:
                print ('Cannot load image:',fullname)
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
    def loadCharacterSprites(cls, name, coordFile, colorkey = None):

        image = cls.loadImage(name)
        walkData, atackData = resourceManager.loadData(coordFile)

        # Generación de cordenadas
        # TODO Metelo no resourceManager que ten mais sentido

        # walk
        ######
        sheetPositions = [0,0,0,0]
        sizexFrame = walkData[0][0]
        sizeyFrame = walkData[0][1]
        initPixel = walkData[1]
        numFrame = walkData[2]

        for j in range(4):
            tmp = []
            for i in range(0, numFrame):
                tmp.append(pygame.Rect(0+i*sizexFrame, initPixel+sizeyFrame*j, sizexFrame, sizeyFrame))
            sheetPositions[j] = tmp

        walkSprites = [[],[],[],[]]

        for i in range(4):
            for j in range(numFrame):
                walkTmp = image.subsurface(sheetPositions[i][j])
                walkSprites[i].append(cls.imageMod(walkTmp))

        return walkSprites

    @classmethod
    def imageMod(cls,image):
        array = np.empty((64, 64, 3), dtype=np.uint8)
        pygame.pixelcopy.surface_to_array(array,image)

        newImage = np.empty((128, 128, 3), dtype=np.uint8)

        for i in range(128):
            for j in range(128):
                if i > 64 and j > 64:
                    newImage[i,j] = array[i-64][j-64]
                else:
                    newImage[i,j] = array[0][0]

        image = pygame.surfarray.make_surface(newImage)
        image.set_colorkey((0,0,0))
        return image
