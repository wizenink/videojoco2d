import pygame
import pyganim #maybe not needed
import sys
sys.path.insert(0,"../")
from scene.scenec import *
from scene import serializer
from resourceManager import *
from character import *
sys.path.insert(0,"./dialog")
from diag import *

#RGB 100,100,100 ROCA
#RGB 255,255,255 GRASS
#RGB 94,113,255 WATER
#RGB 94,255,98 TREE

class Level(Scene):
	def __init__(self,director):
		self.enemyGroup = pygame.sprite.Group()
		self.playerGroup = pygame.sprite.Group()
		self.solidGroup = pygame.sprite.Group()
		self.player = Player(director, dmgGroup = self.enemyGroup, solidGroup = self.solidGroup)
		self.solids = []
		self.enemys = []
		self.dialogs = []
		self.lvlname = "level_farm.png"
		width,height,map = serializer.loadLevel(self.lvlname)
		Scene.__init__(self,self.lvlname,width,height,map,32,director)
		self.initLevel()

		#Test variables
		self.debug = 0
	def music(self):
		self.director.sound.generalSoundManage(GAME_SOUND_MUSIC_EVENT_MUSIC_1,repeat = -1)

	def addEnemy(self,x,y):
		enemy = Enemy1(self.director,dmgGroup = self.playerGroup, solidGroup = self.solidGroup)
		enemy.setPosition((x,y))
		enemy.updateHitboxPosition()
		self.enemys.append(enemy)
		self.enemyGroup.add(enemy.hitbox)
		self.addSolid(enemy)

	def addSolid(self,solid):
		#Si es un building
		try:
			self.solidGroup.add(solid.hitbox)
		except:
			self.solidGroup.add(solid)

		self.solids.append(solid)

	def removeEnemy(self,enemy):
		self.enemys.remove(enemy)

	def removeSolid(self,solid):
		self.solids.remove(solid)

	def events(self,events):
		for event in events:
				# Pausa
				if event.type == KEYDOWN and event.key == K_p:
					self.director.pause = not self.director.pause
				if event.type == KEYDOWN and event.key == K_o:
					if self.dialogs:
						self.dialogs[0].queueScreen()
				# Si el event es la pulsación de la tecla Escape
				if event.type == KEYDOWN and event.key == K_ESCAPE:
						# Se sale del programa
						if self.debug:
							self.addGreenTree(self.player.position)
							print(self.player.position)
						else:
							pygame.quit()
							sys.exit()

				#if event.type == pygame.USEREVENT: message.update()s
				#if (event.type == KEYDOWN and event.key == K_SPACE): message.update()

		self.player.move(pygame.key.get_pressed(), K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE)
		for enemy in self.enemys:
			enemy.move_cpu(self.player)

	def update(self,time):
		self.camera.update(self.player)
		self.camera.apply(self.player)
		self.player.update(time)
		for enemy in self.enemys:
			enemy.update(time)

	def groupDraws(self,screen):
		self.player.draw(screen,self.camera)
		for enemy in self.enemys:
			enemy.draw(screen,self.camera)
		for solid in self.solids:
			solid.draw(screen,self.camera)

	def searchCollidables(self):
		for x in range(self.width):
			for y in range(self.height):
				if (self.map[x][y])[1] == True:
					collidable = InmobileSprite("empty.png",((y)*32+self.camera.getX(),(x+1)*32+self.camera.getY()),folder = TILE_FOLDER)
					self.solidGroup.add(collidable)
					#self.solids.append(collidable)

	def updateDialog(self,screen):
		if self.dialogs:
			self.dialogs[0].update()
			self.dialogs[0].draw(screen)


	def addDialog(self, textDialog):
		testDialog = [["Quiero drama velazque plx dame drma que me ahburo","velazke ablaaaaameeeee equis favoh plz y dimelo","","velazke io zoy wapa? vlazque plz io zoy wapa plx dimeloh ne"],["This is","the second page","cool,right?"]]
		dialog = Dialog("test",testDialog)
		self.dialogs.append(dialog)


	def addTent(self,pos):
		tent = Building(pos,buildname = 'cab.png')

		self.solidGroup.add(tent)
		self.solids.append(tent)

	def addFarm(self,pos):
		farm = Building(pos,buildname = 'farm.png')

		self.solidGroup.add(farm)
		self.solids.append(farm)

	def addHouse(self,pos):
		house = Building(pos,buildname = 'building.png')

		self.solidGroup.add(house)
		self.solids.append(house)

	def addMisc(self,pos,x):
		if x == 1:
			misc = Building(pos,buildname = 'farm_misc1.png')
		elif x == 2:
			misc = Building(pos,buildname = 'farm_misc2.png')
		elif x == 3:
			misc = Building(pos,buildname = 'farm_misc3.png')
		elif x == 4:
			misc = Building(pos,buildname = 'plants.png')
		elif x == 5:
			misc = Building(pos,buildname = 'fiddlesticks.png')

		self.solidGroup.add(misc)
		self.solids.append(misc)

	def addRedTree(self,pos):
		tree = Building(pos,buildname = 'redtree.png')

		self.solidGroup.add(tree)
		self.solids.append(tree)

	def addGreenTree(self,pos):
		greenTree = Building(pos,buildname = 'greentree.png')

		self.solidGroup.add(greenTree)
		self.solids.append(greenTree)

	def initLevel(self):

		self.searchCollidables()

		self.playerGroup.add(self.player.hitbox)
		self.solidGroup.add(self.player.hitbox)
		self.player.setPosition((315,1382))
		self.player.updateHitboxPosition()
		self.addDialog(None)

		self.addGreenTree((1337.60,2385.00))
		self.addGreenTree((1357.60,2520.00))
		self.addGreenTree((1204.60,2520.00))
		self.addGreenTree((1090.60,2458.00))
		self.addGreenTree((1173.60,2371.00))
		self.addMisc((477.99,1603.80),5)
		self.addMisc((515.39,1616.40),4)
		self.addMisc((508.59,1349.19),3)
		self.addRedTree((1199.80,1920.80))
		self.addRedTree((2937.80,1765.80))
		self.addHouse((340.39,1341.79))
		self.addTent((370,2243))
		self.addTent((442,2277))
		self.addTent((260,2267))
		self.addMisc((370,2290),2)


		self.addEnemy(315,1682)
