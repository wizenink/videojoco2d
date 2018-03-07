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
		Button.__init__(self,screen,"nombre_do_puto_boton.jpg",(580,530))
	def action(self):
		self.screen.menu.runGame()

class ExitButton(Button):
	def __init__(self,screen):
		Button.__init__(self,screen,"nombre_doutro_puto_boton.jpg",(580,560))
	def action(self):
		self.screen.menu.exitProgram()


class TextGUI(ElementGUI):
	def __init__(self,screen,font,color,text,pos):
		self.image = font.render(text,True,color)
		ElementGUI.__init(self,screen,self.image.get_rect())
		self.definePosition(pos)

	def draw(self,screen):
		screen.blit(self.image,self.rect)

class TextPlay(TextGUI):
	def __init__(self,screen):
		font = pygame.font.SysFont('arial',26)
		TextGUI.__init__(screen,font,(0,0,0),"Play",(610,530,))
	def action(self):
		self.screen.menu.runGame()

class TextExit(TextGUI):
	def __init__(self,screen):
		font = pygame.font.SysFont('arial',26)
		TextGUI.__init__(screen,font,(0,0,0),"Exit",(610,565))
	def action(self):
		self.screen.menu.exitProgram()

class ScreenGUI:
	def __init__(self,menu,nameImage):
		self.menu = menu
		#Load background images
		self.image = resourceManager.loadImage(nameImage)
		self.image = pygame.transform.scale(self.image, (DISPLAY_WIDTH,DISPLAY_HEIGHT))
		#Element GUI List
		self.elementsGUI = []

	def events(self,event_list):
		for event in event_list:
			if event.type == MOUSEBUTTONDOWN:
				self.elementClick = None
				for element in self.elementsGUI:
					if element.elementPosition(event.pos)
						self.elementClick = element
			if event.type == MOUSEBUTTONUP:
				for element in self.elementsGUI:
					if element.elementPosition(event.pos)
						if (element == self.elementClick):
							element.action()

	def draw(self,screen):
		#Drawing background image
		screen.blit(self.image,self.image.get_rect())
		#Buttons now
		for element in self.elementsGUI:
			element.draw(pantalla)
					
class MainScreenGUI(ScreenGUI):
	def __init__(self,menu):
		ScreenGUI.__init__(self,menu,'main_screen.jpg')
		
		playButton = PlayButton(self)
		exitButton = ExitButton(self)
		self.elementsGUI.append(playButton)
		self.elementsGUI.append(exitButton)

		textPlay = TextPlay(self)
		textExit = TextExit(self)
		self.elementsGUI.append(textPlay)
		self.elementsGUI.append(textExit)
	
class Menu(Scene):
	def __init__(self,director):
		Scene.__init__(self,director)
		self.screenList = []
		self.listScreens.append(MainScreenGUI(self))
		self.showMainScreen()

	def update(self, *args):
		return
	
	def events(self,events_list):
		for event in events_list:
			if event.type = KEYDOWN:
				if event.key == K_ESCAPE:
					self.exitProgram()
			elif event.type == pygame.QUIT:
				self.director.exitProgram()
		
		self.screenList[self.actualScreen].events(events_list)
	
	def draw(self,screen):
		self.screenList[self.actualScreen].draw(screen)

	def exitProgram(self):
		self.director.exitProgram()
	
	def runGame(self):
		scene = Scene(self.director)
		self.director.pushScene(scene)

	def showMainScreen(self):
		self.actualScreen = 0
		




#TO-DO REST OF MENU