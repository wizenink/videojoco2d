import pygame 
import pyganim #maybe not needed
import sys
sys.path.insert(0,"../")
from scene.scenec import *
from scene import serializer
from resourceManager import *

class Level(Scene):
	def __init__(self,director):
		self.solids = []
		self.enemys = []
		self.lvlname = "level_farm.png"
		self.level = serializer.loadLevel(self.lvlname)
		Scene.__init__(self,self.lvlname,self.level.width,self.level.height,self.level.map,32,director)


	def addEnemy(self,enemy):
		self.enemys.append(enemy)

	def addSolid(self,solid):
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



