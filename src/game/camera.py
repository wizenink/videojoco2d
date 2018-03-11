import sys
import pygame
from game.constants import *
class Camera(object):
    def __init__(self,camera_func,max_x,max_y):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, max_x, max_y)
    def apply(self,target):
        return target.rect.move(self.state.topleft)
    def update(self,target):
        self.state = self.camera_func(self.state,target.rect)
    def getX(self):
        return self.state[0]
    def getY(self):
        return self.state[1]

def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect # l = left,  t = top
    _, _, w, h = camera      # w = width, h = height
    return pygame.Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)

def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+HALF_WIDTH, -t+HALF_HEIGHT, w, h # center player

    l = min(0, l)                           # stop scrolling at the left edge
    l = max(-(camera.width-WIN_WIDTH), l)   # stop scrolling at the right edge
    t = max(-(camera.height-WIN_HEIGHT), t) # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top

    return pygame.Rect(l, t, w, h)
