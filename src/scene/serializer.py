import numpy as np
from skimage import io as skio
import sys
from scene import scenec
sys.path.insert(0,"../")
from resourceManager import *
#Creacion de mapas
CROP = (40,60,0)
DESERT = (200,200,200)
GRASS = (0,255,0)
HOUSE = (0,0,0)
ROAD = (128,128,128)

default = { (0,0,0) : "grass.png", (255,255,255) : "desert.png"}
def loadLevel(levelName):
    levelImg = resourceManager.loadLevel(levelName)
    width = levelImg.get_width()
    height = levelImg.get_height()
    buffer =  pygame.surfarray.pixels3d(levelImg)
    map = []
    for y in range(height):
        row = [None] * width
        for x in range(width):
            row[x] = resourceManager.loadImage(default[tuple(buffer[x,y])])
        map.append(row)
    level = scenec.Scene(levelName,width,height,map,32,None)
    return level
