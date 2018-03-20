import pygame, sys, os
from pygame.locals import *
#from scene import *
from resourceManager import *
from director import *

# for testing
sys.path.insert(0, './test/')
from groupTest import enemyGroup, playerGroup, solidGroup

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
    old = (0,0)
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.position = (100,100)
        self.old = self.position
        self.currentSpeed = (0,0)
        self.speed = 0
        self.rect = pygame.Rect(64,64,64,64)

    def setPosition(self,position):
        self.old = self.position
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

    def draw(self,surface,camera):
        surface.blit(self.image,camera.apply(self))

class Hitbox(MySprite):

    def __init__(self, width, hight, position):
        super(Hitbox, self).__init__()
        self.image = pygame.Surface((width,hight))
        self.image.fill((255,255,255))
        self.image.set_alpha(125)
        self.rect = self.image.get_rect()
        self.position = position

    def setPosition(self,position, offset):
        positionTmp = (position[0] + offset[0], position[1] + offset[1])
        MySprite.setPosition(self,positionTmp)

class BodyHitbox(Hitbox):
    def __init__(self, width, hight, position, parentSprite, dmgGroup):
        super().__init__(width,hight,position)
        self.dmgGroup = dmgGroup
        self.parent = parentSprite

    def collitionUpdate(self):

        if self.collideGroup != None:
            collideList = pygame.sprite.spritecollide(self,self.dmgGroup, False)

            for solidSprite in collideList:
                #DMG
                if solidSprite in dmgGroup:
                    self.parent.life -= solidSprite.parent.characterDmg
                #Move back
                self.parent.currentSpeed = (-self.parent.currentSpeed[0], -self.parent.currentSpeed[1])



class AttackHitbox(Hitbox):
    def __init__(self, width, hight, position, parentSprite, dmgGroup):
        super().__init__(width,hight,position)
        self.dmgGroup = dmgGroup
        self.parent = parentSprite

    def collitionUpdate(self):
        if self.dmgGroup != None:
            collideList = pygame.sprite.spritecollide(self,self.dmgGroup, False)

            for enemy in collideList:
                enemy.parent.getDmg(self.characterDmg ,self.parent.looking)
                print(-30)



class  Character(MySprite):
    """docstring for Character."""
    def __init__(self, imageFile, coordFile, speed, animationDelay, dmgGroup):

        MySprite.__init__(self)

        self.sheet = resourceManager.loadImage(imageFile,colorkey=0)
        self.sheet = self.sheet.convert_alpha()

        # Load SpriteSheet Data
        # atackData
        walkData, atackData = resourceManager.loadData(coordFile)

        # Body Hitbox
        self.hitbox = BodyHitbox(25,47, self.position, self, dmgGroup)
        self.offsetHitbox = (83,62)

        # List of attack hitboxes
        self.hitboxes = []
        if atackData != None:
            # Order of hitboxes in the list matter [ UP, LEFT, RIGHT, DOWN ]
            for i in range(3,7):
                self.attackHitbox = AttackHitbox(atackData[i][0],atackData[i][1], self.position,self, dmgGroup)
                self.attackOffsetHitbox = (atackData[i][2],atackData[i][3])
                self.hitboxes.append((self.attackHitbox,self.attackOffsetHitbox))

        # Life
        self.life = 100

        #bloqueo por tiempo variables
        self.timeBlock = 0

        self.andar = resourceManager.loadCharacterSprites(imageFile,coordFile)

        # Walk Sprites Load
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

        # Attack
        #######
        if atackData != None:
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

        # Init variables
        self.movement = STILL
        self.looking = UP
        self.atack = False
        self.numFrame = 0
        #self.rect = pygame.Rect(sizexFrame, sizeyFrame, 0, initPixel)

        self.characterDmg = 0

        self.speed = speed
        # Retardo de la animación
        self.animationDelay = animationDelay
        # Contador del Retardo
        self.animationDelayCont = 0

    def getDmg(self, dmg, looking, timeToBlock = 30):
        #quitamos daño
        self.life -= dmg
        self.timeBlock = timeToBlock
        #desplazamos al afectado hacia el sentido contrario del golpe
        if looking == UP:
            self.currentSpeed = (0,-self.speed)
        elif looking == LEFT:
            self.currentSpeed = (-self.speed,0)
        elif looking == RIGHT:
            self.currentSpeed = (self.speed,0)
        elif looking == DOWN:
            self.currentSpeed = (0,self.speed)


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
                if self.numFrame == 3:
                    self.hitboxes[self.looking][0].collitionUpdate()
                    print(":)")
                    print(self.looking)

            else:
                if self.numFrame >= len(self.sheetPositions[self.looking])-1:
                    self.numFrame = 1
                if self.numFrame < 0:
                    self.numFrame = len(self.sheetPositions[self.looking])-1

                if self.movement != STILL:
                    self.image = self.andar[self.looking][self.numFrame]
                else:
                    self.image = self.andar[self.looking][0]

    def updateHitboxPosition(self):

        # Update Body Hitbox Position
        self.hitbox.setPosition(self.position, self.offsetHitbox)

        # Update Attack hitboxes Position
        for hitboxinfo in self.hitboxes:
            hitbox = hitboxinfo[0]
            offsetHitbox = hitboxinfo[1]
            hitbox.setPosition(self.position, offsetHitbox)


    def update(self, time):

        # Movement Zone
        ################
        if self.timeBlock == 0:
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
        else:
            self.timeBlock -= 1

        self.changeAnimation()

        MySprite.update(self,time)

        if self.life <= 0:
            print("moriche")

        self.updateHitboxPosition()

        #Dmg Zone
        #########


        # Collition Zone
        ################

        self.hitbox.collitionUpdate()

        return

class Player(Character):
    "Personaje principal del juego"
    def __init__(self, dmgGroup = None):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        Character.__init__(self,'demo.png','demo.data', 0.2, 3, dmgGroup);
        self.characterDmg = 30

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

class Enemy(Character):
    "Enemigos del juego"
    def __init__(self, imageFile, coordFile, speed, animationDelay, dmgGroup = None):
        # Invocamos al constructor de la clase padre con la configuracion de este enemigo concreto
        Character.__init__(self, imageFile, coordFile, speed, animationDelay, dmgGroup);
        self.characterDmg = 20

    def move_cpu(self, player):
        # Indicamos las acciónes a realizar para el enemigo
        return

class Enemy1(Enemy):
    "Enemigo 1"
    def __init__(self,dmgGroup = None):
        # Invocamos al constructor de la clase padre con la configuracion de este enemigo concreto
        Enemy.__init__(self,'enemy1.png','enemy1.data', 0.1, 3);

    def move_cpu(self, player):
        # Indicamos las acciónes a realizar para el enemigo
        # Movemos solo a los enemigos que esten en la pantalla
        if self.rect.left>0 and self.rect.right< DISPLAY_WIDTH and self.rect.bottom>0 and self.rect.top< DISPLAY_HEIGHT:

            # Por ejemplo, intentara acercarse al jugador mas cercano en el eje x

            xdiference = player.position[0] - self.position[0]
            ydiference = player.position[1] - self.position[1]
            #print(xdiference)
            #print(ydiference)

            mayor = abs(xdiference) >= abs(ydiference)

            #Diferencia de dos para contemplar que el exprite no eté en el mismo sitio por distancia de menos de dos pixeles y se mueva igual
            if mayor and (xdiference > 2):
                  Character.move(self,RIGHT)
            elif mayor and (xdiference < -2):
                Character.move(self,LEFT)
            elif not mayor and (ydiference > 2):
                Character.move(self,DOWN)
            elif not mayor and (ydiference < -2):
                Character.move(self,UP)
            else: Character.move(self,STILL)



        # Si este personaje no esta en pantalla, no hara nada
        else:
            Character.move(self,STILL)










#
