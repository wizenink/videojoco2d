import numpy as np
from skimage import io as skio
from scene import Scene

CROP = (40,60,0)
DESERT = (200,200,200)
GRASS = (0,255,0)
HOUSE = (0,0,0)
ROAD = (128,128,128)

TILESIZE = 40

tilemap = {
    [0,0,0]       : CROP
    [255,255,255] : DESERT
    [0,255,0]     : GRASS
    [255,0,255]   : HOUSE
    [128,128,128] : ROAD
}

def loadLevel(levelName):
    levelImg = resourceManager.getLevel(levelName)
    tilemapDict = resourceManager.getTilemap(levelMap)
    shape = levelImg.shape
    width = shape[0]
    height = shape[1]
    map = [[]]
    for y in range(0,height):
        row = [None] * width
        for x in range(0,width):
            row[x] = tilemapDict[levelImg[x,y]]
        map.append(row)
    level = Scene(levelName,width,height,map)
