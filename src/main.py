from director import Director 
from scenes import menu
import pygame

if __name__ == '__main__':
	#Director
	pygame.init()
	pygame.mouse.set_visible(0)
	director = Director()
	#Escena menu
	scene = menu.Menu(director)
	#Apilamos escena
	director.pushScene(scene)
	#Ejecutamos el juego
	director.run()
	#Finalizamos cuando termine el loop
	pygame.quit()