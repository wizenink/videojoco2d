import numpy as np
from skimage import io as skio

tilemap = {
    [0,0,0]       : CROP
    [255,255,255] : DESERT
    [0,255,0]     : GRASS
    [255,0,255]   : HOUSE
    [128,128,128] : ROAD
}
def loadLevel(levelName):
    levelPath = resourceManager.getLevel(levelName)
    level = skio.imread(levelPath)
    shape = level.shape
    for x in range(0,shape[0]):
        for y in range(0,shape[1]):
