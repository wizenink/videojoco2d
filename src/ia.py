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