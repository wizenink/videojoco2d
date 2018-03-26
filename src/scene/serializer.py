import numpy as np
from skimage import io as skio
import sys
from scene import scenec
sys.path.insert(0,"../")
from resourceManager import *
#Creacion de mapas
WATER = (94,113,255)
ROCK = (100,100,100)
GRASS = (255,255,255)
TREE = (94,255,98)
TEST = (0,0,0)



#RGB 100,100,100 ROCA
#RGB 255,255,255 GRASS
#RGB 94,113,255 WATER
#RGB 94,255,98 TREE

default = { GRASS : "grass.png", WATER : "water.png", ROCK : "rock.png", TREE : "tree.png", TEST : 'grass.png'}
def loadLevel(levelName):
    levelImg = resourceManager.loadLevel(levelName)
    width = levelImg.get_width()
    height = levelImg.get_height()
    buffer =  pygame.surfarray.pixels3d(levelImg)
    map = []
    for y in range(height):
        row = [None] * width
        for x in range(width):
            row[x] = resourceManager.loadImage(default[tuple(buffer[x,y])],folder = TILE_FOLDER)
        map.append(row)
    level = scenec.Scene(levelName,width,height,map,32,None)
    return level
