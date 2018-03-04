import pygame
import math

class Renderable():
    position_x = 0.0
    position_y = 0.0
    def __init__(self,sprite):
        self.sprite = sprite
