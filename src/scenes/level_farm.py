import pygame
import pyganim #maybe not needed
import sys
sys.path.insert(0,"../")
from scene.scenec import *
from scene import serializer
from resourceManager import *
from character import *
from scenes import menu
from scenes import level_castle_lindisfarne
from util.levelDesigner import *
sys.path.insert(0,"./dialog")
from diag import *

#RGB 100,100,100 ROCA
#RGB 255,255,255 GRASS
#RGB 94,113,255 WATER
#RGB 94,255,98 TREE

offset_x = 65
offset_y = 70

class Level(Scene):
	bossSpawned = False
	bossDead = False
	def __init__(self,director):
		pygame.time.set_timer(WARMOND_SUMMONTIMER,200)
		#Test variables
		self.debug = 1
		self.firstTime = False
		##############
		self.enemyGroup = pygame.sprite.Group()
		self.playerGroup = pygame.sprite.Group()
		self.solidGroup = pygame.sprite.Group()
		#Si estamos en modo debug no colisionaremos con nada
		if (self.debug):
			self.player = Player(director, dmgGroup = self.enemyGroup, solidGroup = pygame.sprite.Group())
		else:
			self.player = Player(director, dmgGroup = self.enemyGroup, solidGroup = self.solidGroup)
		self.solids = []
		self.enemys = []
		self.dialogs = []
		self.lvlname = "level_farm.png"
		self.lvlfile = "level_farm.txt"
		self.designer = Designer(self.lvlfile)
		width,height,map = serializer.loadLevel(self.lvlname)
		Scene.__init__(self,self.lvlname,width,height,map,32,director)
		self.fenceRemoved = False
		self.initLevel()

	def music(self):
		self.director.sound.generalSoundManage(GAME_SOUND_MUSIC_EVENT_MUSIC_1,repeat = -1)

	def addEnemy(self,x,y):
		enemy = Enemy1(self.director,dmgGroup = self.playerGroup, solidGroup = self.solidGroup)
		enemy.setPosition((x,y))
		enemy.updateHitboxPosition()
		self.enemys.append(enemy)
		self.enemyGroup.add(enemy.hitbox)


	def addEnemy2(self,x,y,enemy):
		enemy.setPosition((x,y))
		enemy.updateHitboxPosition()
		self.enemys.append(enemy)
		self.enemyGroup.add(enemy.hitbox)


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

	def addItem(self,event):
		#GreenTree
		if event.type == KEYDOWN and event.key == K_1:
			self.addGreenTree((self.player.position[0]+offset_x,self.player.position[1]+offset_y))
			self.designer.writeFile("greentree",(self.player.position[0]+offset_x,self.player.position[1]+70))
		#RedTree
		elif event.type == KEYDOWN and event.key == K_2:
			self.addRedTree((self.player.position[0]+offset_x,self.player.position[1]+offset_y))
			self.designer.writeFile("redtree",(self.player.position[0]+offset_x,self.player.position[1]+70))
		#Tent
		elif event.type == KEYDOWN and event.key == K_3:
			self.addTent((self.player.position[0]+offset_x,self.player.position[1]+offset_y))
			self.designer.writeFile("tent",(self.player.position[0]+offset_x,self.player.position[1]+70))
		#Misc2
		elif event.type == KEYDOWN and event.key == K_4:
			self.addMisc((self.player.position[0]+offset_x,self.player.position[1]+offset_y),2)
			self.designer.writeFile("misc2",(self.player.position[0]+offset_x,self.player.position[1]+70))
		#Plants
		elif event.type == KEYDOWN and event.key == K_5:
			self.addMisc((self.player.position[0]+offset_x,self.player.position[1]+offset_y),4)
			self.designer.writeFile("plants",(self.player.position[0]+offset_x,self.player.position[1]+70))
		#House
		elif event.type == KEYDOWN and event.key == K_6:
			self.addHouse((self.player.position[0]+offset_x,self.player.position[1]+offset_y))
			self.designer.writeFile("house",(self.player.position[0]+offset_x,self.player.position[1]+70))
		#Fiddlesticks
		elif event.type == KEYDOWN and event.key == K_7:
			self.addMisc((self.player.position[0]+offset_x,self.player.position[1]+offset_y),5)
			self.designer.writeFile("fiddlesticks",(self.player.position[0]+offset_x,self.player.position[1]+70))
		#Misc1
		elif event.type == KEYDOWN and event.key == K_8:
			self.addMisc((self.player.position[0]+offset_x,self.player.position[1]+offset_y),1)
			self.designer.writeFile("misc1",(self.player.position[0]+offset_x,self.player.position[1]+70))
		#Misc3
		elif event.type == KEYDOWN and event.key == K_9:
			self.addMisc((self.player.position[0]+offset_x,self.player.position[1]+offset_y),3)
			self.designer.writeFile("misc3",(self.player.position[0]+offset_x,self.player.position[1]+70))
		elif event.type == KEYDOWN and event.key == K_0:
			self.addCastle((self.player.position[0]+offset_x,self.player.position[1]+offset_y))
			self.designer.writeFile("castle",(self.player.position[0]+offset_x,self.player.position[1]+70))
		elif event.type == KEYDOWN and event.key == K_l:
			self.addFence((self.player.position[0]+offset_x,self.player.position[1]+offset_y))
			self.designer.writeFile("fence",(self.player.position[0]+offset_x,self.player.position[1]+70))

	def loadItemsFromFile(self):
		items = self.designer.readFile()
		for item in items:
			if item[0] == "greentree":
				self.addGreenTree(item[1])
			elif item[0] == "redtree":
				self.addRedTree(item[1])
			elif item[0] == "tent":
				self.addTent(item[1])
			elif item[0] == "misc2":
				self.addMisc(item[1],2)
			elif item[0] == "plants":
				self.addMisc(item[1],4)
			elif item[0] == "house":
				self.addHouse(item[1])
			elif item[0] == "fiddlesticks":
				self.addMisc(item[1],5)
			elif item[0] == "misc1":
				self.addMisc(item[1],1)
			elif item[0] == "misc3":
				self.addMisc(item[1],3)
			elif item[0] == "castle":
				self.addCastle(item[1])
			elif item[0] == "fence":
				self.addFence(item[1])

	def events(self,events):
		for event in events:
			# Pausa
			if self.debug:
				pygame.mouse.set_visible(1)
				self.addItem(event)
				if event.type == KEYDOWN and event.key == K_c:
					self.solids = []
			if event.type == KEYDOWN and event.key == K_p:
				self.director.dialog = not self.director.dialog
			# Si el event es la pulsación de la tecla Escape
			if event.type == KEYDOWN and event.key == K_ESCAPE:
					# Se sale del programa
				menuscene = menu.MenuPause(self.director)
				self.director.pushScene(menuscene)



			#if event.type == pygame.USEREVENT: message.update()s
			#if (event.type == KEYDOWN and event.key == K_SPACE): message.update()

			if not self.director.dialog:
				self.player.move(pygame.key.get_pressed(), K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE)
				for enemy in self.enemys:
					enemy.move_cpu(self.player)
			else:
				if event.type == KEYDOWN and event.key == K_SPACE:
					if self.dialogs:
						if not self.dialogs[0].allDialogDone():
							self.dialogs[0].qUpdate()
						else:
							print("No more dialogs")
							self.dialogs.pop(0)
							self.director.dialog = False


	def update(self,time):
		self.camera.update(self.player)
		self.camera.apply(self.player)
		self.player.update(time)
		if not self.firstTime:
			self.director.dialog = not self.director.dialog
			self.firstTime = True
		if self.bossDead:
			if not self.fenceRemoved:
				self.solidGroup.remove(self.fencePassLevel)
				self.solids.remove(self.fencePassLevel)
				self.fenceRemoved = True
		if ( 3100 <= self.player.position[0] <= 3120) and (2200 <= self.player.position[1] <= 1240) and self.bossDead:
			newscene = level_castle_lindisfarne.Level(self.director)
			self.director.swapScene(newscene)
		#if ( 1000 <= self.player.position[0] <= 1300) and (2400 <= self.player.position[1] <= 2800) and not self.bossSpawned:
		#	boss = Warmond(self.director,self,self.playerGroup,self.solidGroup)
		#	self.addEnemy2(1183,2612,boss)
		#	self.bossSpawned = True
		for enemy in self.enemys:
			if enemy.dead:
				self.solidGroup.remove(enemy.hitbox)
				self.enemyGroup.remove(enemy.hitbox)
				self.enemys.remove(enemy)
				#self.solids.remove(enemy)
			else:
				enemy.update(time)

	def groupDraws(self,screen):
		self.player.draw(screen,self.camera)
		#self.player.hitbox.draw(screen,self.camera)
		self.player.hitboxes[1][0].draw(screen,self.camera)
		self.player.hitboxes[3][0].draw(screen,self.camera)

		for solid in self.solids:
			solid.draw(screen,self.camera)

		for enemy in self.enemys:
			enemy.draw(screen,self.camera)
			enemy.drawUI(screen,self.camera)
		self.player.drawUI(screen)

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
		dialog = Dialog("test",textDialog)
		self.dialogs.append(dialog)

	def addCastle(self,pos):
		castle = Building(pos,buildname = 'castle.png')

		self.solidGroup.add(castle)
		self.solids.append(castle)

	def addFence(self,pos):
		fence = Building(pos,buildname = 'fence.png')

		self.solidGroup.add(fence)
		self.solids.append(fence)

		return fence


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
		self.fencePassLevel = self.addFence((3175.4000000000124,2304.6000000000117))
		self.playerGroup.add(self.player.hitbox)
		self.solidGroup.add(self.player.hitbox)
		self.player.setPosition((315,1382))
		self.player.updateHitboxPosition()
		firstDialog = [["En el reino de Shendralar, cada diez años, su rey Tux",
		"convoca una purga para diezmar y amedrentar a su pueblo",
		"Sus sicarios se disponen a atacar el pueblo."],
		["Se rumorea que el necromántico Warmond ha venido","personalmente a cumplir los designios del emperador"],["Corre el rumor de que se le ha visto en","*la playa al sur del pueblo*"]]
		self.addDialog(firstDialog)

		#boss = Warmond(self.director,self,self.playerGroup,self.solidGroup)
		#self.addEnemy2(350,1750,boss)
		self.loadItemsFromFile()
		#self.addEnemy(315,1682)
		boss = Warmond(self.director,self,self.playerGroup,self.solidGroup)
		self.addEnemy2(1183,2612,boss)
		self.bossSpawned = True

		fire = Fire('fire.png',(315,1682),self.solidGroup)
		fire.setPosition((315,1682))
		#fire.updateHitboxPosition()
		self.enemys.append(fire)
		#self.solids.append(fire)
		self.enemyGroup.add(fire)
		#self.fencePassLevel = self.addFence((3175.4000000000124,2304.6000000000117))



