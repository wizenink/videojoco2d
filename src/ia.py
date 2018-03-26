import character

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

	if sameX and lastMove==character.RIGHT:
		self.rightBlock = True
	elif sameX and lastMove==character.LEFT:
		self.leftBlock = True
	elif sameX and lastMove==character.DOWN:
		self.downBlock = True
	elif sameX and lastMove==character.UP:
		self.upBlock = True

	#Diferencia de dos para contemplar que el esprite no esté en el mismo sitio por distancia de menos de dos pixeles y se mueva igual
	if xMoreDistance and not self.rightBlock:
		#if xdiference < x:
		#	self.attack()
		self.move(character.RIGHT)
		self.lastMove = character.RIGHT
		#Desbloqueamos el resto de bloqueos
		self.leftBlock = False
		self.downBlock = False
		self.upBlock = False
	elif xMoreDistance and not self.leftBlock:
		#if xdiference > x:
		#	self.attack()
		self.move(character.LEFT)
		self.lastMove = character.LEFT
		#Desbloqueamos el resto de bloqueos
		self.rightBlock = False
		self.downBlock = False
		self.upBlock = False
	elif not xMoreDistance and not self.downBlock:
		#if xdiference < y:
		#	self.attack()
		self.move(character.DOWN)
		self.lastMove = character.DOWN
		#Desbloqueamos el resto de bloqueos
		self.rightBlock = False
		self.leftBlock = False
		self.upBlock = False
	elif not xMoreDistance and not self.upBlock:
		#if xdiference > y:
		#	self.attack()
		self.move(character.UP)
		self.lastMove = character.UP
		#Desbloqueamos el resto de bloqueos
		self.rightBlock = False
		self.leftBlock = False
		self.downBlock = False
	else:
		self.move(character.STILL)
		self.lastMove = character.STILL
		#Desbloqueamos el resto de bloqueos
		self.rightBlock = False
		self.leftBlock = False
		self.downBlock = False
		self.upBlock = False
			
		
		