import pygame, sys, os
from pygame.locals import *
#from scene import *
from resourceManager import *
import numpy as np

# --------------------------
# --------------------------
# Constants
# --------------------------
# --------------------------

# Movement

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
STILL = 4


# Character Speed

PLAYER_SPEED = 0.2
PLAYER_ANIMATION_DELAY = 4

class MySprite(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.position = (100,100)
        self.currentSpeed = (0,0)
        self.speed = 0
        self.rect = pygame.Rect(64,64,64,64)

    def setPosition(self,position):
        self.position = position
        self.rect.left = self.position[0]
        self.rect.bottom = self.position[1]

    def increasePosition(self, increment):
        (posx, posy) = self.position
        (xIncrease, yIncrease) = increment
        self.setPosition((posx+xIncrease, posy+yIncrease))

    def update(self, time):
        xIncrease = self.currentSpeed[0]*time
        yIncrease = self.currentSpeed[1]*time
        self.increasePosition((xIncrease, yIncrease))

class  Character(MySprite):
    """docstring for Character."""
    def __init__(self, imageFile, coordFile, speed, animationDelay):

        MySprite.__init__(self)

        self.sheet = resourceManager.loadImage(imageFile)
        self.sheet = self.sheet.convert_alpha()

        walkData, atackData = resourceManager.loadData(coordFile)

        self.andar = resourceManager.loadCharacterSprites(imageFile,coordFile)

        # Generación de cordenadas
        # TODO Metelo no resourceManager que ten mais sentido

        # walk
        ######
        self.sheetPositions = [0,0,0,0]
        sizexFrame = walkData[0][0]
        sizeyFrame = walkData[0][1]
        initPixel = walkData[1]
        numFrame = walkData[2]

        self.image = self.sheet.subsurface(pygame.Rect(0,576,64,64))

        for j in range(4):
            tmp = []
            for i in range(0, numFrame):
                tmp.append(pygame.Rect(0+i*sizexFrame, initPixel+sizeyFrame*j, sizexFrame, sizeyFrame))
            self.sheetPositions[j] = tmp

        # atack
        #######
        self.sheetPositionsAtack = [0,0,0,0]
        sizexFrame = atackData[0][0]
        sizeyFrame = atackData[0][1]
        initPixel = atackData[1]
        numFrame = atackData[2]

        for j in range(4):
            tmp = []
            for i in range(0, numFrame):
                tmp.append(pygame.Rect(0+i*sizexFrame, initPixel+sizeyFrame*j, sizexFrame, sizeyFrame))
            self.sheetPositionsAtack[j] = tmp


        self.movement = STILL
        self.looking = UP
        self.atack = False
        self.numFrame = 0
        #self.rect = pygame.Rect(sizexFrame, sizeyFrame, 0, initPixel)

        self.speed = speed
        # Retardo de la animación
        self.animationDelay = animationDelay
        # Contador del Retardo
        self.animationDelayCont = 0

    def move(self, movement):
        self.movement = movement

    def changeAnimation(self):
        self.animationDelayCont -= 1

        if (self.animationDelayCont < 0):
            self.animationDelayCont = self.animationDelay
            self.numFrame += 1

            if self.atack:
                if self.numFrame >= len(self.sheetPositionsAtack[self.looking])-1:
                    self.atack = False

                self.image = self.sheet.subsurface(self.sheetPositionsAtack[self.looking][self.numFrame])


            else:
                if self.numFrame >= len(self.sheetPositions[self.looking])-1:
                    self.numFrame = 1
                if self.numFrame < 0:
                    self.numFrame = len(self.sheetPositions[self.looking])-1

                if self.movement != STILL:
                    self.image = self.andar[self.looking][self.numFrame]
                else:
                    self.image = self.andar[self.looking][0]

    def update(self, time):
        if not(self.atack):
            if (self.movement != STILL):
                self.looking = self.movement

                if self.movement == UP:
                    self.currentSpeed = (0,-self.speed)
                elif self.movement == LEFT:
                    self.currentSpeed = (-self.speed,0)
                elif self.movement == RIGHT:
                    self.currentSpeed = (self.speed,0)
                elif self.movement == DOWN:
                    self.currentSpeed = (0,self.speed)
            else:
                self.currentSpeed = (0,0)

        self.changeAnimation()

        MySprite.update(self,time)

        return

class Player(Character):
    "Cualquier personaje del juego"
    def __init__(self):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        Character.__init__(self,'demo.png','demo.data', 0.2, 4);


    def move(self, keyPressed, up, down, left, right,atack):
        # Indicamos la acción a realizar segun la tecla pulsada para el jugador
        if keyPressed[up]:
            Character.move(self,UP)
        elif keyPressed[left]:
            Character.move(self,LEFT)
        elif keyPressed[right]:
            Character.move(self,RIGHT)
        elif keyPressed[down]:
            Character.move(self,DOWN)
        elif keyPressed[atack]:
            self.atack = True
            self.numFrame = -1

        else:
            Character.move(self,STILL)












#
