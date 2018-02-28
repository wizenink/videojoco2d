import pygame,pyglet
import sys
from scene import * 
from pygame.locals import * 

FPS = 144
DISPLAY_WIDTH = 640
DISPLAY_HEIGHT = 480

class Director():
	def __init__(self):
		#pila
		self.stack
		#salir del juego
		self.exit_game = False
	
	def pygameLoop(self,scene):
		clock = pygame.time.Clock()
		self.exit_game = False
		pygame.event.clear()
		while not self.exit_game:
			#Sincronizamos a 144 fps
			time_spent = reloj.tick(FPS)

			scene.eventos(pygame.event.get())
			scene.update(time_spent)
			scene.dibujar(scene.screen)

			pygame.display.flip()

	def run(self):
		pygame.init()
		self.screen = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))

		while(len(self.pila)>0):
			scene = self.stack[len(self.stack)-1]
			self.pygameLoop(scene)
		
		pygame.quit()


	def stopScene(self):
		if (len(self.stack)>0):
			scene = self.stack[len(self.stack)-1]
			self.exit_game = True 

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
	

	