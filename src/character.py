import pygame, sys, os
import time
import time as timeM
import _thread
import random
import ia
from pygame.locals import *
#from scene import *
from resourceManager import *
from director import *
from game.constants import *
import math

# for testing
# sys.path.insert(0, './test/')
# from groupTest import *

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

def inverseLooking(looking):
    if looking == UP:
        return DOWN
    elif looking == DOWN:
        return UP
    elif looking == LEFT:
        return RIGHT
    elif looking == RIGHT:
        return LEFT


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
    def __init__(self, width, hight, position, parentSprite, dmgGroup, solidGroup):
        super().__init__(width,hight,position)
        self.dmgGroup = dmgGroup
        self.parent = parentSprite
        self.solidGroup = solidGroup

    def collitionUpdate(self):

        collideList = pygame.sprite.spritecollide(self, self.solidGroup, False)

        for solidSprite in collideList:
            #DMG
            if self.dmgGroup != None:
                if solidSprite in self.dmgGroup:
                    self.parent.life -= solidSprite.parent.dmg
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
                enemy.parent.getDmg(self.parent.dmg ,self.parent.looking, timeToBlock = 30)



class  Character(MySprite):
    """docstring for Character."""
    def __init__(self, imageFile, coordFile, speed, animationDelay, director, dmgGroup, solidGroup):

        MySprite.__init__(self)

        self.sheet = resourceManager.loadImage(imageFile,colorkey=0)
        self.sheet = self.sheet.convert_alpha()

        # Load SpriteSheet Data
        # atackData
        walkData, atackData, self.deadData = resourceManager.loadData(coordFile)

        # Body Hitbox
        self.hitbox = BodyHitbox(25,47, self.position, self, dmgGroup, solidGroup)
        self.offsetHitbox = (83,62)

        # List of attack hitboxes
        self.hitboxes = []
        if atackData != None:
            # Order of hitboxes in the list matter [ UP, LEFT, DOWN, RIGHT]
            for i in range(3,7):
                self.attackHitbox = AttackHitbox(atackData[i][0],atackData[i][1], self.position,self, dmgGroup)
                self.attackOffsetHitbox = (atackData[i][2],atackData[i][3])
                self.hitboxes.append((self.attackHitbox,self.attackOffsetHitbox))

        #Variables ia
        #bloqueo por tiempo variables
        self.timeBlock = 0

        self.lastMove = STILL

        self.rightBlock = False
        self.leftBlock = False
        self.downBlock = False
        self.upBlock = False
        self.blockCount = 0
        self.dmgGroup = dmgGroup
        self.xInitialPosition = self.position[0]
        self.yInitialPosition = self.position[1]

        self.xLastPosition = self.position[0]
        self.yLastPosition = self.position[1]

        self.walkSprites, self.deadSprites = resourceManager.loadCharacterSprites(imageFile,coordFile)


        # Walk Sprites Load
        ###################
        self.sheetPositions = [0,0,0,0]
        sizexFrame = walkData[0][0]
        sizeyFrame = walkData[0][1]
        initPixel = walkData[1]
        numFrame = walkData[2]

        #self.image = self.sheet.subsurface(pygame.Rect(0,576,64,64))

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
        # Life
        self.maxlife = 100
        self.life = 100
        self.dead = False
        self.director = director

        #bloqueo por tiempo variables
        self.timeBlock = 0
        self.movement = STILL
        self.looking = UP
        self.atack = False
        self.numFrame = 0
        self.numDeadFrame = -1

        self.solidGroup = solidGroup
        self.dmg = 0

        self.speed = speed
        self.initialSpeed = self.speed
        # Retardo de la animación
        self.animationDelay = animationDelay
        # Contador del Retardo
        self.animationDelayCont = 0

    def getDmg(self, dmg, looking, timeToBlock = 10):
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

    def killAnimation(self):

        self.animationDelayCont -= 1
        if (self.animationDelayCont < 0):
            self.animationDelayCont = self.animationDelay
            self.numDeadFrame += 1

            if self.numDeadFrame < self.deadData[2]-1:
                self.image = self.deadSprites[self.numDeadFrame]
            else:
                self.image = self.deadSprites[self.deadData[2]-1]
                if self.numDeadFrame > self.deadData[2]-1+10:
                    self.dead = True


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
                    #print(self.hitboxes[self.looking][0])
                    self.hitboxes[self.looking][0].collitionUpdate()

            else:
                if self.numFrame >= len(self.sheetPositions[self.looking])-1:
                    self.numFrame = 1
                if self.numFrame < 0:
                    self.numFrame = len(self.sheetPositions[self.looking])-1

                if self.movement != STILL:
                    self.image = self.walkSprites[self.looking][self.numFrame]
                else:
                    self.image = self.walkSprites[self.looking][0]

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
        positionTmp = self.position #Save position for collision detection

        if self.life > 0:
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
                self.changeAnimation()
            else:
                self.timeBlock -= 1
        else:
            self.currentSpeed = (0,0)
            self.killAnimation()
            self.dmg = 0


        MySprite.update(self,time)
        self.updateHitboxPosition()

        # Collision Detection
        #####################


        self.solidGroup.remove(self.hitbox)
        collideList = pygame.sprite.spritecollide(self.hitbox, self.solidGroup, False)
        for solidSprite in collideList:
            if (not isinstance(solidSprite, InmobileSprite)) and ( solidSprite in self.dmgGroup.sprites()):
                if (isinstance(solidSprite, Fire)):
                    self.getDmg(solidSprite.parent.dmg, inverseLooking(self.looking), timeToBlock = 10)
                else:
                    self.getDmg(solidSprite.parent.dmg, solidSprite.parent.looking, timeToBlock = 30)
                    solidSprite.parent.getDmg(self.dmg, self.looking,timeToBlock = 10)

        if collideList:
            self.setPosition(positionTmp)
            self.updateHitboxPosition()



        self.solidGroup.add(self.hitbox)


        return

class Player(Character):
    "Personaje principal del juego"
    def __init__(self, director, dmgGroup = None, solidGroup = None):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        Character.__init__(self,'player.png','player.data', 0.2, 3, director, dmgGroup, solidGroup);
        self.dmg = 30
        self.lifeSprites = []
        self.addSprites()

    def addSprites(self):
        for i in range(1,11):
            image = resourceManager.loadImage("lifebar_"+str(i)+".png",folder = UI_FOLDER)
            image.set_colorkey((255,255,255))
            image.convert()
            self.lifeSprites.append(image)

    def move(self, keyPressed, up, down, left, right,atack):
        # Indicamos la acción a realizar segun la tecla pulsada para el jugador
        if not self.atack:
            if keyPressed[up]:
                Character.move(self,UP)
            elif keyPressed[left]:
                Character.move(self,LEFT)
            elif keyPressed[right]:
                Character.move(self,RIGHT)
            elif keyPressed[down]:
                Character.move(self,DOWN)
            elif keyPressed[atack]:
                Character.move(self,STILL)
                self.atack = True
                self.numFrame = -1
                self.director.sound.generalSoundManage(GAME_SOUND_EFFECT_EVENT_ARMAESPADAATAQUE1)

            else:
                Character.move(self,STILL)

    def drawUI(self,screen):
        if self.life <= 0:
            pass
        else:
            screen.blit(self.lifeSprites[int((self.life) / 10)-1],(DISPLAY_WIDTH*0.05,DISPLAY_HEIGHT*0.9))



class InmobileSprite(MySprite):

    def __init__(self, imageFile, position, folder = BUILD_FOLDER):

        MySprite.__init__(self)
        self.sheet = resourceManager.loadImage(imageFile, folder = folder)
        self.sheet = self.sheet.convert()
        #self.sheet = pygame.transform.scale(self.sheet,(120,140))
        self.image = self.sheet
        self.image.set_colorkey((255,0,255))
        self.rect = self.image.get_rect()
        self.setPosition(position)
        self.dmg = 0
        self.parent = self

    def getDmg(self, dmg, looking, timeToBlock = 10):
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

    def update(self, time):
        pass

class Building(InmobileSprite):
    def __init__(self,position,buildname = 'building.png'):
        InmobileSprite.__init__(self,buildname, position)


class Enemy(Character):
    "Enemigos del juego"
    def __init__(self, imageFile, coordFile, speed, animationDelay, director, dmgGroup, solidGroup):
        # Invocamos al constructor de la clase padre con la configuracion de este enemigo concreto
        Character.__init__(self, imageFile, coordFile, speed, animationDelay, director, dmgGroup, solidGroup)
        self.dmg = 15

    def move_cpu(self, player):
        # Indicamos las acciónes a realizar para el enemigo
        return


    def drawUI(self,screen,camera):
        health_color = (0,0,0)
        if self.life > 75:
            health_color = (0,255,0)
        elif self.life > 50:
            health_color = (255,125,0)
        elif self.life > 25:
            health_color = (255,0,0)
        else:
            health_color = (0,0,0)

        offset_x = 68
        offset_y = 64
        pygame.draw.rect(screen,health_color,( camera.apply(self)[0]+offset_x,camera.apply(self)[1]+offset_y,(self.life/self.maxlife) * 100 / 2,5))


class Enemy1(Enemy):
    "Enemigo 1"
    def __init__(self, director, dmgGroup, solidGroup):
        # Invocamos al constructor de la clase padre con la configuracion de este enemigo concreto
        Enemy.__init__(self,'eskeleton.png','eskeleton.data', 0.1, 3, director, dmgGroup, solidGroup)
        self.maxlife = 100

    def move_cpu(self, player):
        # Indicamos las acciónes a realizar para el enemigo
        #ia.iaVerticalGuardian(self, player)
        ia.iaFollow(self,player)

class InmobileSpriteDmg(MySprite):

    def __init__(self, imageFile, position, folder = BUILD_FOLDER):

        MySprite.__init__(self)
        self.sheet = resourceManager.loadImage(imageFile, folder = folder)
        self.sheet = self.sheet.convert()
        #self.sheet = pygame.transform.scale(self.sheet,(120,140))
        self.image = self.sheet
        self.image.set_colorkey((255,0,255))
        self.rect = self.image.get_rect()
        self.setPosition(position)
        self.dmg = 0
        self.parent = self

    def getDmg(self, dmg, looking, timeToBlock = 10):
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

    def update(self, time):
        pass

class Fire(InmobileSpriteDmg):
    "Just Fire"
    oldTime = 0
    lifespan = 10
    acc = 0
    looking = UP
    def __init__(self, imageFile, position, solidGroup,dmgGroup, folder = CHARACTER_SPRITE_FOLDER):

        InmobileSprite.__init__(self,imageFile,position,folder)
        self.dmgGroup = dmgGroup
        self.images = resourceManager.loadStaticAnimation(imageFile)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.setPosition(position)
        self.hitbox = self
        self.solidGroup = solidGroup
        self.dmg = 10
        self.parent = self
        self.animationDelay = 5
        self.animationDelayCont = self.animationDelay
        self.numFrame = 0
        self.dead = False

    def drawUI(self,screen,camera):
        pass
    def move_cpu(self,player):
        pass
    def getDmg(self, dmg, looking, timeToBlock = 10):
        pass

    def changeAnimation(self):
        self.animationDelayCont -= 1
        if (self.animationDelayCont < 0):
            self.animationDelayCont = self.animationDelay
            self.numFrame += 1

            if self.numFrame >= len(self.images)-1:
                self.numFrame = 0
            if self.numFrame < 0:
                self.numFrame = len(self.images)-1

            self.image = self.images[self.numFrame]

    def update(self, time):
        #No IA, Just Fire T.T
        now = timeM.time()
        if self.oldTime == 0:
            self.oldTime = now
            return
        delta = now - self.oldTime
        self.acc += delta
        if self.acc >= self.lifespan:
            self.acc = 0
            self.dead = True
        self.oldTime = now
        self.changeAnimation()

        self.solidGroup.remove(self)
        collideList = pygame.sprite.spritecollide(self.hitbox, self.solidGroup, False)
        for solidSprite in collideList:
            if (not isinstance(solidSprite, InmobileSprite)) and ( solidSprite in self.dmgGroup.sprites()):
                self.looking = inverseLooking(solidSprite.parent.looking)
                self.getDmg(solidSprite.parent.dmg, solidSprite.parent.looking, timeToBlock = 30)
                solidSprite.parent.getDmg(self.dmg, self.looking,timeToBlock = 10)


        #if collideList:
            #self.setPosition(positionTmp)
            #self.updateHitboxPosition()



        self.solidGroup.add(self)

class Warmond(Enemy):
    "Nigromante Warmond"
    lastTime = 0
    acctime = 12
    summonTimerCD = 3
    summonTimer = 0
    NENEMIES = 4
    spawnThread = None
    deathdone = False
    startDialogDone = False
    dialog = [["El emperador ha exigido la limpieza de cada aldea,","y no seré el que falle en su tarea."],["Te eliminaré junto al resto...","y pasaréis a formar parte de mi ejército"]]
    deathdialog = [["Con Warmond muerto, el camino del este está libre","y es tu mejor oportunidad de escapar","hacia las tierras del Este."]]
    def __init__(self,director,scene,dmgGroup,solidGroup):
        self.scene = scene
        self.director = director
        Enemy.__init__(self,"warmond.png","warmond.data",0.1,3,director,dmgGroup,solidGroup)
        self.maxlife = 500
        self.life = 500
        self.dmg = 15
        self.spawns = []
        for i in range(self.NENEMIES):
            e = Enemy1(self.director,dmgGroup = self.dmgGroup, solidGroup = self.solidGroup)
            e.dead = True
            self.spawns.append(e)
        #scene.addDialog(self.dialog)
        #director.dialog = True
    def doesCollide(self,rxt,ryt):
        for i in range(-1,2):
            for j in range(-1,2):
                if not self.scene. collisionMap[rxt+i][ryt+j]:
                    return True
        return False
    def spawner2(self):
        camera = self.scene.camera
        now = time.time()
        if self.lastTime == 0:
            self.lastTime = now
            return

        delta = now - self.lastTime
        self.acctime += delta
        if self.acctime >= 10:
            self.acctime = 0
            #rx = random.randint(int(camera.apply(self)[0]-10),int(camera.apply(self)[0]+10))
            #ry = random.randint(int(camera.apply(self)[1]-10),int(camera.apply(self)[1]+10))
            for enemy in self.spawns:
                if enemy.dead:
                    enemy.dead = False
                    enemy.life = enemy.maxlife
                    rx = 0
                    ry = 0
                    while True:
                        rx = random.randint(int(self.position[0]-512),int(self.position[0]+512))
                        ry = random.randint(int(self.position[1]-512),int(self.position[1]+512))
                        rxt = int(rx/32)
                        ryt = int(ry/32)
                        if self.doesCollide(rxt,ryt):
                            print("Avoided collision")
                            continue
                        else:
                            break
                    self.scene.addEnemy2(rx,ry,enemy)
        self.lastTime = now

    def move_cpu(self,player):
        if self.life <= 0 and not self.deathdone :
            self.scene.addDialog(self.deathdialog)
            self.director.dialog = True
            self.deathdone = True
            self.scene.bossDead = True
        if not self.startDialogDone and ia.getEuclideanDistance(self,player)<200:
            self.startDialogDone = True
            self.scene.addDialog(self.dialog)
            self.director.dialog = True
        if self.startDialogDone:
            ia.iaFollow(self,player)
            self.spawner2()


class TuxHand(Enemy):
    "Tux's Right Hand"
    lastTime = 0
    acctime = 12
    summonTimerCD = 3
    summonTimer = 0
    NENEMIES = 4
    spawnThread = None
    deathdone = False
    killPlayer = False
    dialog = [["Se acabó.","El emperador me ha pedido que acabe contigo,pero valdrás más como","gladiador en la Arena..."]]
    def __init__(self,director,scene,dmgGroup,solidGroup):
        self.scene = scene
        self.director = director
        Enemy.__init__(self,"tuxhand.png","tuxhand.data",0.1,3,director,dmgGroup,solidGroup)
        self.life = 100

    def spawner2(self):
        camera = self.scene.camera
        now = time.time()
        if self.lastTime == 0:
            self.lastTime = now
            return

        delta = now - self.lastTime
        self.acctime += delta
        if self.acctime >= 10:
            self.acctime = 0
            #rx = random.randint(int(camera.apply(self)[0]-10),int(camera.apply(self)[0]+10))
            #ry = random.randint(int(camera.apply(self)[1]-10),int(camera.apply(self)[1]+10))
            for i in range(self.NENEMIES):
                rx = random.randint(int(self.position[0]-512),int(self.position[0]+512))
                ry = random.randint(int(self.position[1]-512),int(self.position[1]+512))
                self.scene.addEnemy(rx,ry)
        self.lastTime = now
    def move_cpu(self,player):
        if (player.position[0] - 100 <= self.position[0] <= player.position[0] + 100) and (player.position[1] - 100 <= self.position[1] <= player.position[1] + 100) and not self.killPlayer:
            self.scene.addDialog(self.dialog)
            self.director.dialog = True
            self.killPlayer = True
        else:
            ia.iaFollow(self,player)
        if self.killPlayer:
            #START ATTACK ANIMATION
            #END THE GAME
            pass
        #self.spawner2()
        return

class Ludwig(Enemy):
    "Berzerk Ludwig"
    lastTime = 0
    acctime = 0
    summonTimerCD = 3
    summonTimer = 0
    NFIRES = 4
    spawnThread = None
    m = None
    movements = [(UP,(262.2000000000136,3175.4000000000283)), (STILL,(262.2000000000136,173.2000000000407))]

    def __init__(self,director,dmgGroup,solidGroup):
        Enemy.__init__(self,"ludwig.png","ludwig.data",0.05,3,director,dmgGroup,solidGroup)
        self.maxlife = 600
        self.life = 600
        self.m = None
        self.movements = [(UP,(262.2000000000136,3175.4000000000283)), (STILL,(262.2000000000136,173.2000000000407))]

    def move_cpu(self,player):
        if self.movements:
            if not self.m:
                self.m = self.movements.pop(0)

            if math.isclose(self.position[0],self.movements[0][1][0]-64,abs_tol=6) and math.isclose(self.position[1],self.movements[0][1][1]-64,abs_tol=6):
                self.m = self.movements.pop(0)
        self.move(self.m[0])

class Disas(Enemy):
    "Mago Disas"
    lastTime = 0
    acctime = 0
    summonTimerCD = 3
    summonTimer = 0
    NFIRES = 4
    spawnThread = None
    deathdone = False
    dialog = [["El camino está bloqueado,me he encargado de ello.","¡Calcinaré tus huesos antes de que intentes escapar!"]]
    deathdialog = [["El castillo ha sido asediado por el Ludwig","y ya no es un lugar seguro."],["Tu mejor opción es intentar escapar","por el camino del *oeste*"]]
    def __init__(self,director,scene,dmgGroup,solidGroup):
        self.scene = scene
        self.scene.addDialog(self.dialog)
        director.dialog = True
        Enemy.__init__(self,"disas.png","disas.data",0.1,3,director,dmgGroup,solidGroup)
        self.maxlife = 600
        self.life = 600


    def doesCollide(self,rxt,ryt):
        for i in range(-1,2):
            for j in range(-1,2):
                if not self.scene.collisionMap[rxt+i][ryt+j]:
                    return True
        return False
    def intersectsPlayer(self,rxt,ryt):
        px = int(self.scene.player.position[0]/32)
        py = int(self.scene.player.position[1]/32)
        if abs(rxt-px) <= 2 and abs(ryt-py) <= 2:
            return True
        else:
            return False

    def spawner2(self):
        camera = self.scene.camera
        now = time.time()
        if self.lastTime == 0:
            self.lastTime = now
            return

        delta = now - self.lastTime
        self.acctime += delta
        if self.acctime >= 10:
            self.acctime = 0
            #rx = random.randint(int(camera.apply(self)[0]-10),int(camera.apply(self)[0]+10))
            #ry = random.randint(int(camera.apply(self)[1]-10),int(camera.apply(self)[1]+10))
            i = 0
            while i < self.NFIRES:
                fire = Fire('fire.png',(315,1682),self.dmgGroup,self.solidGroup)
                while True:
                    rx = random.randint(int(self.scene.player.position[0]-256),int(self.scene.player.position[0]+256))
                    ry = random.randint(int(self.scene.player.position[1]-256),int(self.scene.player.position[1]+256))
                    rxt = int(rx/32)
                    ryt = int(ry/32)
                    if self.doesCollide(rxt,ryt) or self.intersectsPlayer(rxt,ryt):
                        continue
                    else:
                        break
                self.scene.addEnemyFire(rx,ry,fire)
                i += 1
        self.lastTime = now

    def move_cpu(self,player):
        if self.life <= 0 and not self.deathdone:
            self.scene.bossDead = True
            self.scene.addDialog(self.deathdialog)
            self.director.dialog = True
            self.deathdone = True
        #ia.iaFollow(self,player)
        self.spawner2()
        ia.iaFollow(self,player)
        #if self.spawnThread == None:
        #    self.spawnThread = _thread.start_new_thread(self.spawner,())
        return
