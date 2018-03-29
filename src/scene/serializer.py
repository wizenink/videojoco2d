import numpy as np
from skimage import io as skio
import sys
from scene import scenec
sys.path.insert(0,"../")
from resourceManager import *
import random
#Creacion de mapas
DESERT = (255,142,50)
WATER = (94,113,255)
ROCK = (100,100,100)
GRASS = (255,255,255)
TREE = (94,255,98)
TREE2 = (95,255,99)
FLOWERS = (255,0,120)
TEST = (0,0,0)
UPPER_GRASS = (255,255,20)
UPPER_LEFT_GRASS = (100,20,255)
UPPER_RIGHT_GRASS = (30,30,255)
LEFT_GRASS = (100,200,255)
RIGHT_GRASS = (255,200,100)
BOTTOM_GRASS = (20,255,255)
BOTTOM_LEFT_GRASS = (93,46,162)
BOTTOM_RIGHT_GRASS = (162,46,93)




#RGB 100,100,100 ROCA
#RGB 255,255,255 GRASS
#RGB 94,113,255 WATER
#RGB 94,255,98 TREE

def collidable(tupla):
    if tupla == "water.png" or tupla == "tree.png":
        return True
    return False
def randomnum():
    return str(random.randint(1,4))


def loadLevel(levelName):
    levelImg = resourceManager.loadLevel(levelName)
    width = levelImg.get_width()
    height = levelImg.get_height()
    buffer =  pygame.surfarray.pixels3d(levelImg)
    map = []
    for y in range(height):
        row = [None] * width
        for x in range(width):
            default = { BOTTOM_RIGHT_GRASS : "grass_right_bottom.png",
            DESERT : "desert.png", 
            BOTTOM_LEFT_GRASS : "grass_left_bottom.png", 
            BOTTOM_GRASS : "grass_mid_bottom.png", 
            RIGHT_GRASS : "grass_right.png", 
            LEFT_GRASS : "grass_left.png", 
            UPPER_RIGHT_GRASS : "grass_right_upper.png", 
            UPPER_GRASS : "grass_mid_upper.png",  
            UPPER_LEFT_GRASS : "grass_left_upper.png", 
            FLOWERS : "flowers_"+randomnum()+".png", 
            GRASS : "grass_mid.png", 
            WATER : "water.png", 
            ROCK : "rock.png", 
            TREE : "tree.png", 
            TREE2 : "tree.png",
            TEST : 'grass.png'}
            tupla = default[tuple(buffer[x,y])]
            if collidable(tupla):
                row[x] = (resourceManager.loadImage((tupla),folder = TILE_FOLDER), True)
            else:
                row[x] = (resourceManager.loadImage((tupla),folder = TILE_FOLDER) , False)
        map.append(row)
    return width,height,map
