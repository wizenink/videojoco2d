import pygame
import pyganim
from pygame.locals import *
from scene import *
from resourceManager import *

class ElementGUI:
	def __init__(self,screen,rect):
		self.screen = screen
		self.rect = rect
	def definePosition(self,pos):
		(posx,posy) = pos
		self.rect.left = posx
		self.rect.bottom = posy
	def elementPosition(self,pos):
		(posx,posy) = pos
		if (posx>=self.rect.left) and (posx<=self.rect.right) and (posy>=self.rect.top) and (posy <= self.rect.bottom):
			return True
		else: 
			return False
	#TO-DO		
	def draw(self): 
	#TO-DO
	def action(self):

	class Button(ElementGUI):
		def __init__(self,screen,imageName,pos):
			self.image = resourceManager.loadImage(imageName,-1)
			self.image = pygame.transform.scale(self.image,(20,20))

			ElementGUI.__init__(self,pantalla,self.image.get_rect())
			self.definePosition(pos)
		def draw(self,screen):
			screen.blit(self.image,self.rect)
	
	class PlayButton(Button):
		def __init__(self,screen):
			Button.__init__(self,screen,"nombre_do_puto_boton",(580,530))
		def action(self):
			self.screen.menu.runGame()

	class ExitButton(Button):
		def __init__(self,screen):
			Button.__init__(self,screen,"nombre_doutro_puto_boton",(580,560))
		def action(self):
			self.screen.menu.exitProgram()


class TextGUI(ElementGUI):
	def __init__(self,screen,font,color,text,pos):
		self.image = font.render(text,True,color)
		ElementGUI.__init(self,screen,self.image.get_rect())
		self.definePosition(pos)

	def draw(self,screen):
		screen.blit(self.image,self.rect)

#TO-DO REST OF MENU