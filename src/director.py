import pygame,pyglet
import sys
from game.constants import *
from scene import * 
from pygame.locals import * 

class Director():
	def __init__(self):
		#pila
		self.stack = []
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
		pygame.display.set_caption("Reign of Shendralar")
		#salir del juego
		self.exit_scene = False

	def pygameLoop(self,scene):
		clock = pygame.time.Clock()
		self.exit_scene = False
		pygame.event.clear()
		while not self.exit_scene:
			#Sincronizamos a 144 fps
			time_spent = clock.tick(FPS)

			scene.events(pygame.event.get())
			scene.update(clock.get_time())
			scene.draw(self.screen)
			scene.groupDraws(self.screen)

			pygame.display.update()

	def run(self):
		#pygame.init()
		self.screen = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))

		while(len(self.stack)>0):
			scene = self.stack[len(self.stack)-1]
			self.pygameLoop(scene)
		
		pygame.quit()


	def stopScene(self):
		if (len(self.stack)>0):
			self.exit_scene = True 

	def exitScene(self):
		self.stopScene()
		if (len(self.stack)>0):
			self.stack.pop()

	def exitProgram(self):
		self.stopScene()
		self.stack = []

	def swapScene(self,scene):
		self.stopScene()
		if (len(self.stack)>0):
			self.stack.pop()
		self.stack.append(scene)

	def pushScene(self,scene):
		self.stopScene()
		self.stack.append(scene)
	

	