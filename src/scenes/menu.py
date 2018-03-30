import pygame
import pyganim
from pygame.locals import *
from scene.scenem import *
from scene import serializer
from resourceManager import *
from scenes import level_farm, level_trisquel_forest, level_castle_lindisfarne
import sys
sys.path.insert(0,"../")
from sound.soundManager import *
from game.constants import *

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

	def draw(self): 
		print("Should be overrided")

	def action(self):
		print("Should be overrided")

class Button(ElementGUI):
	def __init__(self,screen,imageName,pos):
		self.image = resourceManager.loadImage(imageName,-1,folder = MENU_FOLDER)
		self.image = pygame.transform.scale(self.image,(100,100))

		ElementGUI.__init__(self,screen,self.image.get_rect())
		self.definePosition(pos)
	def draw(self,screen):
		screen.blit(self.image,self.rect)

class PlayButton(Button):
	def __init__(self,screen):
		Button.__init__(self,screen,"play_button.png",(300,300))
	def action(self):
		self.screen.menu.runGame()

class ExitButton(Button):
	def __init__(self,screen):
		Button.__init__(self,screen,"exit_button.png",(400,300))
	def action(self):
		self.screen.menu.exitProgram()


class TextGUI(ElementGUI):
	def __init__(self,screen,font,color,text,pos):
		self.image = font.render(text,True,color)
		ElementGUI.__init__(self,screen,self.image.get_rect())
		self.definePosition(pos)

	def draw(self,screen):
		screen.blit(self.image,self.rect)

class TextPlay(TextGUI):
	def __init__(self,screen,pos):
		font = resourceManager.loadFont("BLKCHCRY.TTF",26)
		TextGUI.__init__(self,screen,font,(55,47,45),"Play",(95,250 + (pos * 40)))
	def action(self):
		self.screen.menu.runGame()

class TextResume(TextGUI):
	def __init__(self,screen,pos):
		font = resourceManager.loadFont("BLKCHCRY.TTF",26)
		TextGUI.__init__(self,screen,font,(55,47,45),"Resume",(95,250 + (pos * 40)))
	def action(self):
		self.screen.menu.resumeGame()

class TextExit(TextGUI):
	def __init__(self,screen,pos):
		font = resourceManager.loadFont("BLKCHCRY.TTF",26)
		TextGUI.__init__(self,screen,font,(55,47,45),"Exit",(95,250 + (pos * 40)))
	def action(self):
		self.screen.menu.exitProgram()

class TextOptions(TextGUI):
	def __init__(self,screen,pos):
		font = resourceManager.loadFont("BLKCHCRY.TTF",26)
		TextGUI.__init__(self,screen,font,(55,47,45),"Options",(95,250 + (pos * 40)))
	def action(self):
		self.screen.menu.options()

class TextReturn(TextGUI):
	def __init__(self,screen,pos):
		font = resourceManager.loadFont("BLKCHCRY.TTF",26)
		TextGUI.__init__(self,screen,font,(55,47,45),"Return",(95,250 + (pos * 40)))
	def action(self):
		self.screen.menu.menureturn()

class TextResolution(TextGUI):
	def __init__(self,screen,pos):
		font = resourceManager.loadFont("BLKCHCRY.TTF",26)
		TextGUI.__init__(self,screen,font,(55,47,45),"Resolution",(95,250 + (pos * 40)))
	def action(self):
		self.screen.menu.menuResolution()

class TextResolution1(TextGUI):
	def __init__(self,screen,pos):
		font = resourceManager.loadFont("BLKCHCRY.TTF",26)
		TextGUI.__init__(self,screen,font,(55,47,45),"640x480",(95,250 + (pos * 40)))
	def action(self):
		self.screen.menu.changeResolution(640,480)

class TextResolution2(TextGUI):
	def __init__(self,screen,pos):
		font = resourceManager.loadFont("BLKCHCRY.TTF",26)
		TextGUI.__init__(self,screen,font,(55,47,45),"1280x960",(95,250 + (pos * 40)))
	def action(self):
		self.screen.menu.changeResolution(1280,960)

class TextResolution3(TextGUI):
	def __init__(self,screen,pos):
		font = resourceManager.loadFont("BLKCHCRY.TTF",26)
		TextGUI.__init__(self,screen,font,(55,47,45),"1920x1080",(95,250 + (pos * 40)))
	def action(self):
		self.screen.menu.changeResolution(1920,1080)

class ScreenGUI:
	def __init__(self,menu,nameImage):
		self.menu = menu
		#Load background images
		self.image = resourceManager.loadImage(nameImage,folder = MENU_FOLDER)
		self.image = pygame.transform.scale(self.image, (DISPLAY_WIDTH ,DISPLAY_HEIGHT))
		#Element GUI List
		self.elementsGUI = []
		self.elementSelected = 0
		self.selection = pygame.transform.scale(resourceManager.loadImage("selection.png",-1,folder = MENU_FOLDER),(32,16))
	def events(self,event_list):
		for event in event_list:
			if event.type == MOUSEBUTTONDOWN:
				self.elementClick = None
				for element in self.elementsGUI:
					if element.elementPosition(event.pos):
						self.elementClick = element
			if event.type == MOUSEBUTTONUP:
				for element in self.elementsGUI:
					if element.elementPosition(event.pos):
						if (element == self.elementClick):
							element.action()
							
			if event.type == KEYDOWN and event.key == K_UP:
				self.elementSelected = (self.elementSelected - 1) % len(self.elementsGUI)
				self.clickSound()
			if event.type == KEYDOWN and event.key == K_DOWN:
				self.elementSelected = (self.elementSelected + 1) % len(self.elementsGUI)
				self.clickSound()
			if event.type == KEYDOWN and event.key == K_RETURN:
				self.elementsGUI[self.elementSelected].action()
				self.startSound()

	def clickSound(self):
		self.menu.director.sound.generalSoundManage(GAME_SOUND_MENU_EVENT_MOVE_UP)

	def startSound(self):
		self.menu.director.sound.generalSoundManage(GAME_SOUND_MENU_EVENT_OK)

	def draw(self,screen):
		#Drawing background image
		screen.blit(self.image,self.image.get_rect())
		#Buttons now
		#Este screen blit sirve para dibujar el cursor de seleccionado
		screen.blit(self.selection,(45,225 +(self.elementSelected * 40)))
		for element in self.elementsGUI:
			element.draw(screen)


class MainScreenGUI(ScreenGUI):
	def __init__(self,menu):
		ScreenGUI.__init__(self,menu,'main_screen.jpg')
		
		#playButton = PlayButton(self)
		#exitButton = ExitButton(self)
		#self.elementsGUI.append(playButton)
		#self.elementsGUI.append(exitButton)
		textPlay = TextPlay(self,0)
		textExit = TextExit(self,1)
		self.elementsGUI.append(textPlay)
		self.elementsGUI.append(textExit)
		

class MenuPauseGUI(ScreenGUI):
	def __init__(self,menu):
		ScreenGUI.__init__(self,menu,'main_screen.jpg')
		
		#playButton = PlayButton(self)
		#exitButton = ExitButton(self)
		#self.elementsGUI.append(playButton)
		#self.elementsGUI.append(exitButton)
		textResume = TextResume(self,0)
		textExit = TextExit(self,1)
		self.elementsGUI.append(textResume)
		self.elementsGUI.append(textExit)
	
class MenuOptionsGUI(ScreenGUI):
	def __init__(self,menu):
		ScreenGUI.__init__(self,menu,'main_screen.jpg')
		
		#playButton = PlayButton(self)
		#exitButton = ExitButton(self)
		#self.elementsGUI.append(playButton)
		#self.elementsGUI.append(exitButton)
		textReturn = TextReturn(self,0)
		self.elementsGUI.append(textReturn)

class MenuResolutionGUI(ScreenGUI):
	def __init__(self,menu):
		ScreenGUI.__init__(self,menu,'main_screen.jpg')
		
		#playButton = PlayButton(self)
		#exitButton = ExitButton(self)
		#self.elementsGUI.append(playButton)
		#self.elementsGUI.append(exitButton)
		textReturn = TextReturn(self,3)
		textResolution1 = TextResolution1(self,0)
		textResolution2 = TextResolution2(self,1)
		textResolution3 = TextResolution3(self,2)
		self.elementsGUI.append(textResolution1)
		self.elementsGUI.append(textResolution2)
		self.elementsGUI.append(textResolution3)
		self.elementsGUI.append(textReturn)


	
class Menu(Scene):
	def __init__(self,director):
		Scene.__init__(self,"main_menu",director)
		self.screenList = []
		self.screenList.append(MainScreenGUI(self))
		self.screenList.append(MenuOptionsGUI(self))
		self.screenList.append(MenuResolutionGUI(self))
		self.showMainScreen()
		self.mouse_down = False 
		self.cursor = pygame.transform.scale(resourceManager.loadImage("cursor.png",-1,folder = MENU_FOLDER),(32,32))
		self.cursor_clicked = pygame.transform.scale(resourceManager.loadImage("cursor_clicked.png",-1,folder = MENU_FOLDER),(32,32))

	#dibuja el cursor custom
	def drawCursor(self,screen,x,y):
		if self.mouse_down:
			screen.blit(self.cursor_clicked,(x,y))
		else:
			screen.blit(self.cursor,(x,y))

	def music(self):
		self.director.sound.generalSoundManage(GAME_SOUND_MUSIC_EVENT_MUSIC_6, repeat = -1)
	def update(self, *args):
		return

	def groupDraws(self, *args):
		pass
	
	def events(self,events_list):
		for event in events_list:
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					self.exitProgram()
			elif event.type == pygame.QUIT:
				self.director.exitProgram()
		#self.mouse_down = pygame.mouse.get_pressed()[0]
		
		self.screenList[self.actualScreen].events(events_list)

	def menuResolution(self):
		self.actualScreen = 2

	def options(self):
		self.actualScreen = 1

	def draw(self,screen):
		self.screenList[self.actualScreen].draw(screen)
		pos = pygame.mouse.get_pos()
		x = pos[0]
		y = pos[1]
		self.drawCursor(screen,x,y)

	def exitProgram(self):
		self.director.exitProgram()
	
	def changeResolution(self,x,y):
		self.director.screen = pygame.display.set_mode((x,y))

	def menureturn(self):
		self.showMainScreen()


	def runGame(self):
		first = level_farm.Level(self.director)
		self.director.swapScene(first)

	def showMainScreen(self):
		self.actualScreen = 0

	def drawUI(self, screen):
		pass

class MenuPause(Scene):
	def __init__(self,director):
		Scene.__init__(self,"main_menu",director)
		self.screenList = []
		self.screenList.append(MenuPauseGUI(self))
		self.screenList.append(MenuOptionsGUI(self))
		self.showMainScreen()
		self.mouse_down = False 
		self.cursor = pygame.transform.scale(resourceManager.loadImage("cursor.png",-1,folder = MENU_FOLDER),(32,32))
		self.cursor_clicked = pygame.transform.scale(resourceManager.loadImage("cursor_clicked.png",-1,folder = MENU_FOLDER),(32,32))

	#dibuja el cursor custom
	def drawCursor(self,screen,x,y):
		if self.mouse_down:
			screen.blit(self.cursor_clicked,(x,y))
		else:
			screen.blit(self.cursor,(x,y))

	def music(self):
		self.director.sound.generalSoundManage(GAME_SOUND_MUSIC_EVENT_MUSIC_6, repeat = -1)

	def update(self, *args):
		return

	def groupDraws(self, *args):
		pass
	
	def events(self,events_list):
		for event in events_list:
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					self.resumeGame()
			elif event.type == pygame.QUIT:
				self.director.exitProgram()
		#self.mouse_down = pygame.mouse.get_pressed()[0]
		
		self.screenList[self.actualScreen].events(events_list)
	
	def draw(self,screen):
		self.screenList[self.actualScreen].draw(screen)
		pos = pygame.mouse.get_pos()
		x = pos[0]
		y = pos[1]
		self.drawCursor(screen,x,y)


	def menureturn(self):
		self.showMainScreen()

	def options(self):
		self.actualScreen = 1

	def exitProgram(self):
		self.director.exitProgram()
	
	def resumeGame(self):
		self.director.exitScene()

	def showMainScreen(self):
		self.actualScreen = 0

	def drawUI(self, screen):
		pass


