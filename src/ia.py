import character
import math
from game import graph as graphc

def getEuclideanDistance(object1,object2):
	return math.ceil(math.sqrt((math.pow((object2.position[0] - object1.position[0]),2) + math.pow((object2.position[1] - object1.position[1]),2))))

def calcMovement(act,sig):
	ax,ay = act
	sx,sy = sig
	if ax == sx:
		return character.DOWN if (sy-ay) > 0 else character.UP
	if ay == sy:
		return character.RIGHT if (sx-ax) > 0 else character.LEFT
	return character.STILL
def iaFollow3(self, player, graph):
	listaPos,_ = iaFollow2(self,player,graph)
	if listaPos == [] or len(listaPos) == 1:
		return
	actualPos = listaPos[0]
	sigPos = listaPos[1]
	(xSigPos,ySigPos) = sigPos
	(xActualPos,yActualPos) = actualPos
	#graph to window meter
	#xSigPos = xSigPos * 32
	#ySigPos = ySigPos * 32

	xdiference = xSigPos - xActualPos
	ydiference = ySigPos - yActualPos

	mayor = abs(xdiference) >= abs(ydiference)

	#Diferencia de dos para contemplar que el exprite no eté en el mismo sitio por distancia de menos de dos pixeles y se mueva igual
	self.move(calcMovement(actualPos,sigPos))



def iaFollow2(self,player,graph):
	playerpos = (int(player.position[0]/32),int(player.position[1]/32))
	selfpos = (int(self.position[0]/32),int(self.position[1]/32))
	#path =  graphc.find_path(graph,int(self.position/32),int(player.position/32))
	path = graphc.find_path(graph,selfpos,playerpos)
	#print(self.position,player.position)
	#print(graph.dict[(47,18)])
	#print(path)
	return path
def iaFollow(self, player):
	# Movemos solo a los enemigos que esten en la pantalla
	#if self.rect.left>0 and self.rect.right< DISPLAY_WIDTH and self.rect.bottom>0 and self.rect.top< DISPLAY_HEIGHT:

		# Por ejemplo, intentara acercarse al jugador mas cercano en el eje x o y
		xdiference = player.position[0] - self.position[0]
		ydiference = player.position[1] - self.position[1]

		mayor = abs(xdiference) >= abs(ydiference)

		#Diferencia de dos para contemplar que el exprite no eté en el mismo sitio por distancia de menos de dos pixeles y se mueva igual
		if mayor and (xdiference > 2):
			self.move(character.RIGHT)
		elif mayor and (xdiference < -2):
			self.move(character.LEFT)
		elif not mayor and (ydiference > 2):
			self.move(character.DOWN)
		elif not mayor and (ydiference < -2):
			self.move(character.UP)
		else:
			self.move(character.STILL)
    #Si este personaje no esta en pantalla, no hara nada
	#else:
		#Character.move(self,STILL)

def iaFollowsContinuos(self, player):
	# Movemos solo a los enemigos que esten en la pantalla
	#if self.rect.left>0 and self.rect.right< DISPLAY_WIDTH and self.rect.bottom>0 and self.rect.top< DISPLAY_HEIGHT:

		sameX = False
		sameY = False

		# Por ejemplo, intentara acercarse al jugador mas cercano en el eje x o y
		xdiference = player.position[0] - self.position[0]
		ydiference = player.position[1] - self.position[1]

		xMoreDistance = abs(xdiference) >= abs(ydiference)

		if self.xLastPosition == self.position[0]:
			sameX = True

		if self.yLastPosition == self.position[1]:
			sameY = True

		self.xLastPosition = self.position[0]
		self.yLastPosition = self.position[1]

		#Diferencia de dos para contemplar que el exprite no esté en el mismo sitio por distancia de menos de dos pixeles y se mueva igual
		if xMoreDistance and (xdiference > 2) and not sameX:
			self.move(character.RIGHT)
		elif xMoreDistance and (xdiference < -2) and not sameX:
			self.move(character.LEFT)
		elif not xMoreDistance and (ydiference > 2) and not sameY:
			self.move(character.DOWN)
		elif not xMoreDistance and (ydiference < -2) and not sameY:
			self.move(character.UP)
		else:
			self.move(character.STILL)

    #Si este personaje no esta en pantalla, no hara nada
	#else:
		#Character.move(self,STILL)

def iaFollowsContinuos2(self, player):

	# Variables sobre la posicion anterior
	sameX = False
	sameY = False

	#intento de movimiento anterior
	lastMove = self.lastMove

	# Por ejemplo, intentara acercarse al jugador mas cercano en el eje x o y
	#Calcular distancias en eje x e y
	xdiference = player.position[0] - self.position[0]
	ydiference = player.position[1] - self.position[1]

	#misma x o y que jugador
	sameXPlayer = (player.position[0] == self.position[0])
	sameYPlayer = (player.position[1] == self.position[1])

	#Variable para conocer mayor distancia
	xMoreDistance = abs(xdiference) >= abs(ydiference)

	#Actualizamos variables sobre posición anterior
	if self.xLastPosition == self.position[0]:
		sameX = True
	if self.yLastPosition == self.position[1]:
		sameY = True

	#Actualizamos la posición anterior a la actual para la proxima llamada
	self.xLastPosition = self.position[0]
	self.yLastPosition = self.position[1]

	if sameX and (lastMove == character.RIGHT):
		self.rightBlock = True
		self.blockCount += 5
	elif sameX and (lastMove == character.LEFT):
		self.leftBlock = True
		self.blockCount += 5
	elif sameY and (lastMove == character.DOWN):
		self.downBlock = True
		self.blockCount += 5
	elif sameY and (lastMove == character.UP):
		self.upBlock = True
		self.blockCount += 5

	#Diferencia de dos para contemplar que el esprite no esté en el mismo sitio por distancia de menos de dos pixeles y se mueva igual
	if (xMoreDistance or (self.downBlock or self.upBlock)) and (xdiference > 0) and not self.rightBlock and not (self.rightBlock and sameXPlayer):
		#if xdiference < x:
		#	self.attack()
		self.move(character.RIGHT)
		self.lastMove = character.RIGHT
		#Desbloqueamos el resto de bloqueos
		if self.blockCount == 0:
			self.leftBlock = False
			self.downBlock = False
			self.upBlock = False
		else:
			self.blockCount -= 1
	elif (xMoreDistance or (self.downBlock or self.upBlock)) and (xdiference < 0) and not self.leftBlock and not (self.leftBlock and sameXPlayer):
		#if xdiference > x:
		#	self.attack()
		self.move(character.LEFT)
		self.lastMove = character.LEFT
		#Desbloqueamos el resto de bloqueos
		if self.blockCount == 0:
			self.rightBlock = False
			self.downBlock = False
			self.upBlock = False
		else:
			self.blockCount -= 1
	elif (not xMoreDistance or (self.rightBlock or self.leftBlock))  and (ydiference > 0) and not self.downBlock and not (self.downBlock and sameYPlayer):
		#if xdiference < y:
		#	self.attack()
		self.move(character.DOWN)
		self.lastMove = character.DOWN
		#Desbloqueamos el resto de bloqueos
		if self.blockCount == 0:
			self.rightBlock = False
			self.leftBlock = False
			self.upBlock = False
		else:
			self.blockCount -= 1
	elif (not xMoreDistance or (self.rightBlock or self.leftBlock))  and (ydiference < 0) and not self.upBlock and not (self.upBlock and sameYPlayer):
		#if xdiference > y:
		#	self.attack()
		self.move(character.UP)
		self.lastMove = character.UP
		#Desbloqueamos el resto de bloqueos
		if self.blockCount == 0:
			self.rightBlock = False
			self.leftBlock = False
			self.downBlock = False
		else:
			self.blockCount -= 1
	else:
		self.move(character.STILL)
		self.lastMove = character.STILL
		#Desbloqueamos el resto de bloqueos
		#self.rightBlock = False
		#self.leftBlock = False
		#self.downBlock = False
		#self.upBlock = False

def iaFollowsContinuos3(self, player):

	# Variables sobre la posicion anterior
	sameX = False
	sameY = False

	#intento de movimiento anterior
	lastMove = self.lastMove

	# Por ejemplo, intentara acercarse al jugador mas cercano en el eje x o y
	#Calcular distancias en eje x e y
	xdiference = player.position[0] - self.position[0]
	ydiference = player.position[1] - self.position[1]

	#misma x o y que jugador
	sameXPlayer = (player.position[0] == self.position[0])
	sameYPlayer = (player.position[1] == self.position[1])

	#Variable para conocer mayor distancia
	xMoreDistance = abs(xdiference) >= abs(ydiference)

	#Actualizamos variables sobre posición anterior
	if self.xLastPosition == self.position[0]:
		sameX = True
	if self.yLastPosition == self.position[1]:
		sameY = True

	#Actualizamos la posición anterior a la actual para la proxima llamada
	self.xLastPosition = self.position[0]
	self.yLastPosition = self.position[1]

	if sameX and (lastMove == character.RIGHT):
		self.rightBlock = True
	if sameX and (lastMove == character.LEFT):
		self.leftBlock = True
	if sameY and (lastMove == character.DOWN):
		self.downBlock = True
	if sameY and (lastMove == character.UP):
		self.upBlock = True

	if not self.rightBlock and xdiference > 2:
		self.move(character.RIGHT)
		self.lastMove = character.RIGHT
		self.leftBlock = False
		self.downBlock = False
		self.upBlock = False
	elif not self.leftBlock and xdiference < -2:
		self.move(character.LEFT)
		self.lastMove = character.LEFT
		self.rightBlock = False
		self.downBlock = False
		self.upBlock = False
	elif not self.downBlock and ydiference > 2:
		self.move(character.DOWN)
		self.lastMove = character.DOWN
		self.rightBlock = False
		self.leftBlock = False
		self.upBlock = False
	elif not self.upBlock and ydiference < -2:
		self.move(character.UP)
		self.lastMove = character.UP
		self.rightBlock = False
		self.leftBlock = False
		self.downBlock = False
	else:
		self.move(character.STILL)
		self.lastMove = character.STILL

def iaHorizontalGuardian(self, player):
	# Variables sobre la posicion anterior
	sameX = False

	#intento de movimiento anterior
	lastMove = self.lastMove

	#Actualizamos variables sobre posición anterior
	if self.xLastPosition == self.position[0]:
		sameX = True

	# Por ejemplo, intentara acercarse al jugador mas cercano en el eje x o y
	#Calcular distancias en eje x e y
	#ydiference = player.position[1] - self.position[1]

	#Actualizamos la posición anterior a la actual para la proxima llamada
	self.xLastPosition = self.position[0]

	if sameX and (lastMove == character.RIGHT):
		self.rightBlock = True
		self.leftBlock = False
	elif sameX and (lastMove == character.LEFT):
		self.leftBlock = True
		self.rightBlock = False

	#if (ydiference < 20) and (ydiference > -20):
	#	self.speed = self.initialSpeed + 0.05
	#else:
	#	self.speed = self.initialSpeed

	if not self.rightBlock:
		self.move(character.RIGHT)
		self.lastMove = character.RIGHT
	elif not self.leftBlock:
		self.move(character.LEFT)
		self.lastMove = character.LEFT

def iaHorizontalFollowGuardian(self, player):
	# Variables sobre la posicion anterior
	sameX = False

	#intento de movimiento anterior
	lastMove = self.lastMove

	#Actualizamos variables sobre posición anterior
	if self.xLastPosition == self.position[0]:
		sameX = True

	# Por ejemplo, intentara acercarse al jugador mas cercano en el eje x o y
	#Calcular distancias en eje x e y
	ydiference = player.position[1] - self.position[1]

	#Actualizamos la posición anterior a la actual para la proxima llamada
	self.xLastPosition = self.position[0]

	if sameX and (lastMove == character.RIGHT):
		self.rightBlock = True
		self.leftBlock = False
	elif sameX and (lastMove == character.LEFT):
		self.leftBlock = True
		self.rightBlock = False

	if getEuclideanDistance(self,player) < 100:
		iaFollowsContinuos3(self,player)
	else:
		if not self.rightBlock:
			self.move(character.RIGHT)
			self.lastMove = character.RIGHT
		elif not self.leftBlock:
			self.move(character.LEFT)
			self.lastMove = character.LEFT

def iaVerticalGuardian(self, player):
	# Variables sobre la posicion anterior
	sameY = False

	#intento de movimiento anterior
	lastMove = self.lastMove

	#Actualizamos variables sobre posición anterior
	if self.yLastPosition == self.position[1]:
		sameY = True

	# Por ejemplo, intentara acercarse al jugador mas cercano en el eje x o y
	#Calcular distancias en eje x e y
	#xdiference = player.position[0] - self.position[0]

	#Actualizamos la posición anterior a la actual para la proxima llamada
	self.yLastPosition = self.position[1]

	if sameY and (lastMove == character.UP):
		self.upBlock = True
		self.downBlock = False
	elif sameY and (lastMove == character.DOWN):
		self.downBlock = True
		self.upBlock = False

	#if (xdiference < 20) and (xdiference > -20):
	#	self.speed = self.initialSpeed + 0.05
	#else:
	#	self.speed = self.initialSpeed

	if not self.upBlock:
		self.move(character.UP)
		self.lastMove = character.UP
	elif not self.downBlock:
		self.move(character.DOWN)
		self.lastMove = character.DOWN

def iaVerticalFollowGuardian(self, player):
	# Variables sobre la posicion anterior
	sameY = False

	#intento de movimiento anterior
	lastMove = self.lastMove

	#Actualizamos variables sobre posición anterior
	if self.yLastPosition == self.position[1]:
		sameY = True

	# Por ejemplo, intentara acercarse al jugador mas cercano en el eje x o y
	#Calcular distancias en eje x e y
	xdiference = player.position[0] - self.position[0]

	#Actualizamos la posición anterior a la actual para la proxima llamada
	self.yLastPosition = self.position[1]

	if sameY and (lastMove == character.UP):
		self.upBlock = True
		self.downBlock = False
	elif sameY and (lastMove == character.DOWN):
		self.downBlock = True
		self.upBlock = False

	if getEuclideanDistance(self,player) < 100:
		iaFollowsContinuos3(self,player)
	else:
		if not self.upBlock:
			self.move(character.UP)
			self.lastMove = character.UP
		elif not self.downBlock:
			self.move(character.DOWN)
			self.lastMove = character.DOWN

def iaCubeGuardian(self, player):
	# Variables sobre la posicion anterior
	sameX = False
	sameY = False

	#intento de movimiento anterior
	lastMove = self.lastMove

	#Actualizamos variables sobre posición anterior
	if self.yLastPosition == self.position[1]:
		sameY = True
	if self.xLastPosition == self.position[0]:
		sameX = True

	# Por ejemplo, intentara acercarse al jugador mas cercano en el eje x o y
	#Calcular distancias en eje x e y
	#xdiference = player.position[0] - self.position[0]

	#Actualizamos la posición anterior a la actual para la proxima llamada
	self.yLastPosition = self.position[1]
	self.xLastPosition = self.position[0]

	#Contador de Bloqueos
	#self.blockCount = algo

	if sameX and (lastMove == character.RIGHT):
		self.rightBlock = True
		self.leftBlock = False
	elif sameX and (lastMove == character.LEFT):
		self.leftBlock = True
		self.rightBlock = False
	elif sameY and (lastMove == character.UP):
		self.upBlock = True
		self.downBlock = False
	elif sameY and (lastMove == character.DOWN):
		self.downBlock = True
		self.upBlock = False

	#if (xdiference < 20) and (xdiference > -20):
	#	self.speed = self.initialSpeed + 0.05
	#else:
	#	self.speed = self.initialSpeed
	if not self.rightBlock:
		self.move(character.RIGHT)
		self.lastMove = character.RIGHT
	elif not self.leftBlock:
		self.move(character.LEFT)
		self.lastMove = character.LEFT
	elif not self.upBlock:
		self.move(character.UP)
		self.lastMove = character.UP
	elif not self.downBlock:
		self.move(character.DOWN)
		self.lastMove = character.DOWN
