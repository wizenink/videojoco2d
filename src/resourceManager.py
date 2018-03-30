import pygame, sys, os
from pygame.locals import *
import configparser
import numpy as np

dirname = os.path.dirname(__file__)

# Constants
MAIN_FOLDER = os.path.join(dirname,"../res")
MENU_FOLDER = os.path.join(MAIN_FOLDER,"menu")
FONT_FOLDER = os.path.join(MAIN_FOLDER,'fonts')
UI_FOLDER = os.path.join(MAIN_FOLDER,"ui")
BUILD_FOLDER = os.path.join(MAIN_FOLDER,'buildings')
TILE_FOLDER = os.path.join(MAIN_FOLDER,'tiles')
CHARACTER_SPRITE_FOLDER = os.path.join(MAIN_FOLDER,"characters")
BLUEPRINT_LEVEL_FOLDER = os.path.join(MAIN_FOLDER,"level")
TERRAIN_TEXTURE_FOLDER = os.path.join(MAIN_FOLDER,"texture")

# Data Sprite Constants

WALK_DATA = "walk"
ATTACK_DATA = "attack"


class resourceManager(object):
    resources = {}

    @classmethod
    def loadImage(cls, name, colorkey = None, folder = CHARACTER_SPRITE_FOLDER):
        if name in cls.resources:
            return cls.resources[name]
        else:
            fullname = os.path.join(folder,name)
            try:
                image = pygame.image.load(fullname)
            except pygame.error:
                print('Cannot load image:')
                print(pygame.get_error())
                raise SystemExit
            image = image.convert()

            if colorkey is not None:
                if colorkey is -1:
                    colorkey = image.get_at((0,0))
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
            walk.append((int(config[WALK_DATA]['rectx']),int(config['walk']['recty'])))
            walk.append(int(config[WALK_DATA]['starty']))
            walk.append(int(config[WALK_DATA]['frames']))

            deadAnimation = []
            deadAnimation.append((int(config['deadAnimation']['rectx']),int(config['deadAnimation']['recty'])))
            deadAnimation.append(int(config['deadAnimation']['starty']))
            deadAnimation.append(int(config['deadAnimation']['frames']))

            if 'attack' in config:
                if not ('attackHitbox' in config):
                    print("Spritesheet data file is malformed, 'attack' section found but no 'attackHitbox' section")
                    raise SystemExit

                attack = []
                attack.append((int(config['attack']['rectx']),int(config['attack']['recty'])))
                attack.append(int(config['attack']['starty']))
                attack.append(int(config['attack']['frames']))
                attack.append(  [   int(config['attackHitbox']['uphight']),
                                    int(config['attackHitbox']['upwidth']),
                                    int(config['attackHitbox']['uphightoffset']),
                                    int(config['attackHitbox']['upwidthoffset'])
                                ])
                attack.append(  [   int(config['attackHitbox']['lefthight']),
                                    int(config['attackHitbox']['leftwidth']),
                                    int(config['attackHitbox']['lefthightoffset']),
                                    int(config['attackHitbox']['leftwidthoffset'])
                                ])
                attack.append(  [   int(config['attackHitbox']['righthight']),
                                    int(config['attackHitbox']['rightwidth']),
                                    int(config['attackHitbox']['righthightoffset']),
                                    int(config['attackHitbox']['rightwidthoffset'])
                                ])
                attack.append(  [   int(config['attackHitbox']['downhight']),
                                    int(config['attackHitbox']['downwidth']),
                                    int(config['attackHitbox']['downhightoffset']),
                                    int(config['attackHitbox']['downwidthoffset'])
                                ])

            else:
                attack = None

            cls.resources[name] = (walk, attack, deadAnimation)
            return (walk, attack, deadAnimation)


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
    def loadFont(cls, name,size):
        if name in cls.resources:
            return cls.resources[name]
        else:
            fullname = os.path.join(FONT_FOLDER,name)
            try:
                font = pygame.font.Font(fullname,size)
            except pygame.error:
                print ('Cannot load font:',fullname)
                raise SystemExit
            # Se almacena
            cls.resources[name] = font
            # Se devuelve
            return font


    @classmethod
    def loadCharacterSprites(cls, name, coordFile, colorkey = None):

        image = cls.loadImage(name)
        walkData, atackData, deadData = resourceManager.loadData(coordFile)

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

        # dead
        ######
        sheetPositions = []
        print(sheetPositions)
        sizexFrame = deadData[0][0]
        sizeyFrame = deadData[0][1]
        initPixel = deadData[1]
        numFrame = deadData[2]
        print(sizexFrame)
        print(sizeyFrame)
        print(initPixel)
        print(numFrame)

        for i in range(0, numFrame):
            sheetPositions.append(pygame.Rect(0+i*sizexFrame, initPixel+sizeyFrame-sizeyFrame, sizexFrame, sizeyFrame))
            print(sheetPositions)
        deadSprites = []
        print(sheetPositions)
        for j in range(0,numFrame):
            deadTmp = image.subsurface(sheetPositions[j])
            deadSprites.append(cls.imageMod(deadTmp))


        return walkSprites, deadSprites

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
