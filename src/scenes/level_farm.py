import pygame
import pyganim #maybe not needed
import sys
sys.path.insert(0,"../")
from scene.scenec import *
from scene import serializer
from resourceManager import *
from character import *

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
		self.lvlname = "level_farm.png"
		width,height,map = serializer.loadLevel(self.lvlname)
		Scene.__init__(self,self.lvlname,width,height,map,32,director)
		self.initLevel()

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
				# Si el event es la pulsación de la tecla Escape
				if event.type == KEYDOWN and event.key == K_ESCAPE:
						# Se sale del programa
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
					collidable = InmobileSprite("empty.png",(y*32.5,x*32.5),folder = TILE_FOLDER)
					self.solidGroup.add(collidable)
					#self.solids.append(collidable)


	def initLevel(self):
		
		self.searchCollidables()

		self.playerGroup.add(self.player.hitbox)
		self.solidGroup.add(self.player.hitbox)
		self.player.setPosition((315,1382))
		self.player.updateHitboxPosition()

		casa = Building((600,400))
		self.solidGroup.add(casa)
		self.solids.append(casa)
		self.addEnemy(300,300)
