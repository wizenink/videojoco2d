from director import Director 
from menu import menu

if __name__ == '__main__':
	#Director
	director = Director()
	#Escena menu
	scene = Menu(director)
	#Apilamos escena
	director.pushScene(escena)
	#Ejecutamos el juego
	director.run()
	#Finalizamos cuando termine el loop
	pygame.quit()