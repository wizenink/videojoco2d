# https://sivasantosh.wordpress.com/2012/07/16/basic-sound-handling-pygame/
import pygame
import time, sys, os
sys.path.insert(0,"../")
from sound.SoundCte import *
'''
class GeneralSoundManager:
 
  def __init__(self, propertiesFile):
    # init all the submodules
    GAME_EFFECT =
    if propertiesFile is None
      propertiesFile = "DEFAULT_PROPERTIES_FILE.txt"
    effectSM = EffectSoundManager.init(propertiesFile)
    musicSM = MusicSoundManager.init(propertiesFile)
    menuSM = MenuSoundManager.init(propertiesFile)
   
  def manage(self, eventList):
   
    while True:
      for event in eventList:
        if event.type == GAME_EFFECT_EVENT: # o definir lista de eventos que corresponden a un efecto y ver si esta en ella
          effectSM.manage(event)
        if event.type == GAME_MUSIC_EVENT:
          musicSM.manage(event)
        if event.type == GAME_MENU_EVENT:
          menuSM.manage(event)
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
   
   
  class EffectSoundManager
    def __init__(self, propertiesFile):
      #init sonidos de effectos
      # load sound files

      MAIN_CHARACTER_ATTACK_SOUND = pygame.mixer.Sound('test.ogg')
      # o para poder cargar desde archivo de texto
      MAIN_CHARACTER_ATTACK_SOUND = SoundResourceLoader.load(propertiesFile, "MAIN_CHARACTER_ATTACK")
      text_file = open("filename.dat", "r")
      lines = text_file.read().split(',')
      print lines
      print len(lines)
      text_file.close()
     
    def manage(event):
      if event.type == MAIN_CHARACTER_ATTACK:
          MAIN_CHARACTER_ATTACK_SOUND.play()
      if event.type == MAIN_CHARACTER_HIT:
          MAIN_CHARACTER_HIT_SOUND.play()
      if event.type == CURRENT_ENEMY_ATTACK:
          CURRENT_ENEMY_ATTACK_SOUND.play()
      if event.type == CURRENT_ENEMY_HIT:
          CURRENT_ENEMY_HIT_SOUND.play()
  class SoundResourceLoader
    def load(propertiesFile, soundName)
        properties = new Properties(propertiesFile)
        return pygame.mixer.Sound(properties.getPropertie(soundName))


'''
'''
import os
CONTEXT							= os.getcwd()  
CONTEXT = '/home/miguel/Descargas/videojoco2d-master/'
             
EFFECT_PRIORITY = 1
MUSIC_PRIORITY = 1
MENU_PRIORITY = 1

EFFECT_CHANNEL = 0
EFFECT_CHANNEL2 = 4
MUSIC_CHANNEL = 1
MENU_CHANNEL = 2
MENU_CHANNEL2 = 3

if pygame.mixer.get_init() is None:
	pygame.mixer.init()

def load():

	#ambiente
	AMBIENTEAGUASPLASHS_SOUND		= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteAguaSplash.ogg'		)
	AMBIENTEANDARARENACORTO_SOUND	= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteAndarArenaCorto.ogg'	) 	
	AMBIENTEANDARRAMAS_SOUND		= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteAndarRamas.ogg'		) 	
	AMBIENTEBOSQUECORTO_SOUND		= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteBosqueCorto.ogg'		) 	
	AMBIENTECASCADA1_SOUND			= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteCascada1.ogg'			)	
	AMBIENTECASCADA2_SOUND			= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteCascada2.ogg'			) 	
	AMBIENTECASCOTESCAIDA_SOUND		= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteCascotesCaida.ogg'		) 	
	AMBIENTECOLISEO_SOUND			= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteColiseo.ogg' 			)
	AMBIENTEFUEGO1_SOUND			= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteFuego1.ogg'			)	
	AMBIENTEFUEGO2_SOUND			= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteFuego2.ogg'			)	 	
	AMBIENTEFUEGONOLOOP_SOUND		= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteFuegoNoLoop.ogg'		) 	
	AMBIENTEGENTEPANICO_SOUND		= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteGentePanico.ogg'		) 	
	AMBIENTEGENTEPANICOCORTO_SOUND	= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteGentePanicoCorto.ogg'	) 	
	AMBIENTEGENTESUSURROS_SOUND		= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteGenteSusurros.ogg'		) 	
	AMBIENTEGRANJA_SOUND			= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteGranja.ogg'			) 	
	AMBIENTEHOJASMANIPULAR_SOUND	= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteHojasManipular.ogg'	) 
	AMBIENTELLUVIA_SOUND			= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteLluvia.ogg'			) 	
	AMBIENTENOCHE_SOUND				= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteNoche.ogg'				) 	
	AMBIENTEPISARTIERRA_SOUND 		= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbientePisarTierra.ogg'		) 	
	AMBIENTERATA1_SOUND				= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteRata1.ogg'				) 	
	AMBIENTERATA2_SOUND				= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteRata2.ogg'				) 	
	AMBIENTERATA3_SOUND				= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteRata3.ogg'				) 	
	AMBIENTERATA4_SOUND				= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteRata4.ogg'				) 	
	AMBIENTERIO1_SOUND				= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteRio1.ogg'				) 	
	AMBIENTERIO2_SOUND				= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteRio2.ogg'				) 	
	AMBIENTEVIENTO_SOUND			= pygame.mixer.Sound(CONTEXT+'res/sound/Ambiente/AmbienteViento.ogg'			)


	#armas
	ARMADAGAIMPACTO_SOUND	 	= pygame.mixer.Sound(CONTEXT+'res/sound/Armas/ArmaDagaImpacto.ogg'		)	
	ARMAESPADAATAQUE1_SOUND		= pygame.mixer.Sound(CONTEXT+'res/sound/Armas/ArmaEspadaAtaque1.ogg'	)		
	ARMAESPADAATAQUE2_SOUND		= pygame.mixer.Sound(CONTEXT+'res/sound/Armas/ArmaEspadaAtaque2.ogg'	)		
	ARMAESPADAEQUIPAR_SOUND		= pygame.mixer.Sound(CONTEXT+'res/sound/Armas/ArmaEspadaEquipar.ogg'	)		
	ARMAESPADAIMPACTO_SOUND		= pygame.mixer.Sound(CONTEXT+'res/sound/Armas/ArmaEspadaImpacto.ogg'	)		
	ARMAFLECHAATAQUE1_SOUND		= pygame.mixer.Sound(CONTEXT+'res/sound/Armas/ArmaFlechaAtaque1.ogg'	)		
	ARMAFLECHAATAQUE2_SOUND		= pygame.mixer.Sound(CONTEXT+'res/sound/Armas/ArmaFlechaAtaque2.ogg'	)		
	ARMAFLECHAIMPACTO1_SOUND	= pygame.mixer.Sound(CONTEXT+'res/sound/Armas/ArmaFlechaImpacto1.ogg'	)	
	ARMAFLECHAIMPACTO2_SOUND	= pygame.mixer.Sound(CONTEXT+'res/sound/Armas/ArmaFlechaImpacto2.ogg'	)		
	ARMAHORCAATAQUE_SOUND		= pygame.mixer.Sound(CONTEXT+'res/sound/Armas/ArmaHorcaAtaque.ogg' 		)	
	ARMAHORCAIMPACTO_SOUND		= pygame.mixer.Sound(CONTEXT+'res/sound/Armas/ArmaHorcaImpacto.ogg' 	)	
	ARMAHORCAIMPACTO2_SOUND		= pygame.mixer.Sound(CONTEXT+'res/sound/Armas/ArmaHorcaImpacto2.ogg' 	)	
	ARMAMAGIAATAQUE_SOUND		= pygame.mixer.Sound(CONTEXT+'res/sound/Armas/ArmaMagiaAtaque.ogg' 		)	
	ARMAMANOTAZOIMPACTO_SOUND	= pygame.mixer.Sound(CONTEXT+'res/sound/Armas/ArmaManotazoImpacto.ogg' 	)	
	ARMAPUNHOIMPACTO_SOUND		= pygame.mixer.Sound(CONTEXT+'res/sound/Armas/ArmaPunhoImpacto.ogg' 	)	

	#menu
	CLICK_SOUND 		= pygame.mixer.Sound(CONTEXT+'res/sound/Menu/click.ogg'			)
	CLICK_2_SOUND		= pygame.mixer.Sound(CONTEXT+'res/sound/Menu/click_2.ogg'		) 	
	LOAD_SOUND			= pygame.mixer.Sound(CONTEXT+'res/sound/Menu/load.ogg'			)	
	MISC_MENU_SOUND		= pygame.mixer.Sound(CONTEXT+'res/sound/Menu/misc_menu.ogg'		)
	MISC_MENU_2_SOUND	= pygame.mixer.Sound(CONTEXT+'res/sound/Menu/misc_menu_2.ogg'	)	
	MISC_MENU_3_SOUND	= pygame.mixer.Sound(CONTEXT+'res/sound/Menu/misc_menu_3.ogg'	)	
	MISC_MENU_4_SOUND	= pygame.mixer.Sound(CONTEXT+'res/sound/Menu/misc_menu_4.ogg'	)	
	MISC_SOUND_SOUND	= pygame.mixer.Sound(CONTEXT+'res/sound/Menu/misc_sound.ogg'	)	
	NEGATIVE_SOUND		= pygame.mixer.Sound(CONTEXT+'res/sound/Menu/negative.ogg'		)
	NEGATIVE_2_SOUND	= pygame.mixer.Sound(CONTEXT+'res/sound/Menu/negative_2.ogg'	)	
	POSITIVE_SOUND		= pygame.mixer.Sound(CONTEXT+'res/sound/Menu/positive.ogg'		)
	SAVE_SOUND			= pygame.mixer.Sound(CONTEXT+'res/sound/Menu/save.ogg'			)
	SHARP_ECHO_SOUND	= pygame.mixer.Sound(CONTEXT+'res/sound/Menu/sharp_echo.ogg'	)

		
	#musica

	MUSICA1_SOUND = pygame.mixer.music.load(CONTEXT+'res/sound/Musica/Musica1.ogg')
	MUSICA2_SOUND = pygame.mixer.music.load(CONTEXT+'res/sound/Musica/Musica2.ogg')
	MUSICA3_SOUND = pygame.mixer.music.load(CONTEXT+'res/sound/Musica/Musica3.ogg')

	MUSICA5_SOUND = pygame.mixer.music.load(CONTEXT+'res/sound/Musica/Musica5.ogg')

	MUSICA6_SOUND = pygame.mixer.music.load(CONTEXT+'res/sound/Musica/Musica6.ogg')

	MUSICA_PLAY = pygame.mixer.music.play()
	#personajes
	PERSONAJEGRITOSTANDARD_SOUND	= pygame.mixer.Sound(CONTEXT+'res/sound/Personajes/PersonajeGritoStandard.ogg'	) 	
	PERSONAJEVIDABAJA_SOUND			= pygame.mixer.Sound(CONTEXT+'res/sound/Personajes/PersonajeVidaBaja.ogg' 		)
	PERSONAJESGRITOHOMBRE_SOUND 	= pygame.mixer.Sound(CONTEXT+'res/sound/Personajes/PersonajesGritoHombre.ogg'	)
'''
class GeneralSoundManager():
	
	def __init__(self, context):
		
		self.CONTEXT	= context
					 
		self.EFFECT_PRIORITY = 1
		self.MUSIC_PRIORITY = 1
		self.MENU_PRIORITY = 1

		if pygame.mixer.get_init() is None:
			pygame.mixer.init()
		
		#ambiente
		self.AMBIENTEAGUASPLASHS_SOUND		= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteAguaSplash.ogg'		)
		self.AMBIENTEANDARARENACORTO_SOUND	= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteAndarArenaCorto.ogg'	) 	
		self.AMBIENTEANDARRAMAS_SOUND		= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteAndarRamas.ogg'		) 	
		self.AMBIENTEBOSQUECORTO_SOUND		= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteBosqueCorto.ogg'		) 	
		self.AMBIENTECASCADA1_SOUND			= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteCascada1.ogg'			)	
		self.AMBIENTECASCADA2_SOUND			= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteCascada2.ogg'			) 	
		self.AMBIENTECASCOTESCAIDA_SOUND		= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteCascotesCaida.ogg'		) 	
		self.AMBIENTECOLISEO_SOUND			= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteColiseo.ogg' 			)
		self.AMBIENTEFUEGO1_SOUND			= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteFuego1.ogg'			)	
		self.AMBIENTEFUEGO2_SOUND			= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteFuego2.ogg'			)	 	
		self.AMBIENTEFUEGONOLOOP_SOUND		= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteFuegoNoLoop.ogg'		) 	
		self.AMBIENTEGENTEPANICO_SOUND		= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteGentePanico.ogg'		) 	
		self.AMBIENTEGENTEPANICOCORTO_SOUND	= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteGentePanicoCorto.ogg'	) 	
		self.AMBIENTEGENTESUSURROS_SOUND		= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteGenteSusurros.ogg'		) 	
		self.AMBIENTEGRANJA_SOUND			= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteGranja.ogg'			) 	
		self.AMBIENTEHOJASMANIPULAR_SOUND	= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteHojasManipular.ogg'	) 
		self.AMBIENTELLUVIA_SOUND			= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteLluvia.ogg'			) 	
		self.AMBIENTENOCHE_SOUND				= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteNoche.ogg'				) 	
		self.AMBIENTEPISARTIERRA_SOUND 		= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbientePisarTierra.ogg'		) 	
		self.AMBIENTERATA1_SOUND				= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteRata1.ogg'				) 	
		self.AMBIENTERATA2_SOUND				= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteRata2.ogg'				) 	
		self.AMBIENTERATA3_SOUND				= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteRata3.ogg'				) 	
		self.AMBIENTERATA4_SOUND				= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteRata4.ogg'				) 	
		self.AMBIENTERIO1_SOUND				= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteRio1.ogg'				) 	
		self.AMBIENTERIO2_SOUND				= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteRio2.ogg'				) 	
		self.AMBIENTEVIENTO_SOUND			= pygame.mixer.Sound(self.CONTEXT+'res/sound/Ambiente/AmbienteViento.ogg'			)


		#armas
		self.ARMADAGAIMPACTO_SOUND	 	= pygame.mixer.Sound(self.CONTEXT+'res/sound/Armas/ArmaDagaImpacto.ogg'		)	
		self.ARMAESPADAATAQUE1_SOUND		= pygame.mixer.Sound(self.CONTEXT+'res/sound/Armas/ArmaEspadaAtaque1.ogg'	)		
		self.ARMAESPADAATAQUE2_SOUND		= pygame.mixer.Sound(self.CONTEXT+'res/sound/Armas/ArmaEspadaAtaque2.ogg'	)		
		self.ARMAESPADAEQUIPAR_SOUND		= pygame.mixer.Sound(self.CONTEXT+'res/sound/Armas/ArmaEspadaEquipar.ogg'	)		
		self.ARMAESPADAIMPACTO_SOUND		= pygame.mixer.Sound(self.CONTEXT+'res/sound/Armas/ArmaEspadaImpacto.ogg'	)		
		self.ARMAFLECHAATAQUE1_SOUND		= pygame.mixer.Sound(self.CONTEXT+'res/sound/Armas/ArmaFlechaAtaque1.ogg'	)		
		self.ARMAFLECHAATAQUE2_SOUND		= pygame.mixer.Sound(self.CONTEXT+'res/sound/Armas/ArmaFlechaAtaque2.ogg'	)		
		self.ARMAFLECHAIMPACTO1_SOUND	= pygame.mixer.Sound(self.CONTEXT+'res/sound/Armas/ArmaFlechaImpacto1.ogg'	)	
		self.ARMAFLECHAIMPACTO2_SOUND	= pygame.mixer.Sound(self.CONTEXT+'res/sound/Armas/ArmaFlechaImpacto2.ogg'	)		
		self.ARMAHORCAATAQUE_SOUND		= pygame.mixer.Sound(self.CONTEXT+'res/sound/Armas/ArmaHorcaAtaque.ogg' 		)	
		self.ARMAHORCAIMPACTO_SOUND		= pygame.mixer.Sound(self.CONTEXT+'res/sound/Armas/ArmaHorcaImpacto.ogg' 	)	
		self.ARMAHORCAIMPACTO2_SOUND		= pygame.mixer.Sound(self.CONTEXT+'res/sound/Armas/ArmaHorcaImpacto2.ogg' 	)	
		self.ARMAMAGIAATAQUE_SOUND		= pygame.mixer.Sound(self.CONTEXT+'res/sound/Armas/ArmaMagiaAtaque.ogg' 		)	
		self.ARMAMANOTAZOIMPACTO_SOUND	= pygame.mixer.Sound(self.CONTEXT+'res/sound/Armas/ArmaManotazoImpacto.ogg' 	)	
		self.ARMAPUNHOIMPACTO_SOUND		= pygame.mixer.Sound(self.CONTEXT+'res/sound/Armas/ArmaPunhoImpacto.ogg' 	)	

		#menu
		self.CLICK_SOUND 		= pygame.mixer.Sound(self.CONTEXT+'res/sound/Menu/click.ogg'			)
		self.CLICK_2_SOUND		= pygame.mixer.Sound(self.CONTEXT+'res/sound/Menu/click_2.ogg'		) 	
		self.LOAD_SOUND			= pygame.mixer.Sound(self.CONTEXT+'res/sound/Menu/load.ogg'			)	
		self.MISC_MENU_SOUND		= pygame.mixer.Sound(self.CONTEXT+'res/sound/Menu/misc_menu.ogg'		)
		self.MISC_MENU_2_SOUND	= pygame.mixer.Sound(self.CONTEXT+'res/sound/Menu/misc_menu_2.ogg'	)	
		self.MISC_MENU_3_SOUND	= pygame.mixer.Sound(self.CONTEXT+'res/sound/Menu/misc_menu_3.ogg'	)	
		self.MISC_MENU_4_SOUND	= pygame.mixer.Sound(self.CONTEXT+'res/sound/Menu/misc_menu_4.ogg'	)	
		self.MISC_SOUND_SOUND	= pygame.mixer.Sound(self.CONTEXT+'res/sound/Menu/misc_sound.ogg'	)	
		self.NEGATIVE_SOUND		= pygame.mixer.Sound(self.CONTEXT+'res/sound/Menu/negative.ogg'		)
		self.NEGATIVE_2_SOUND	= pygame.mixer.Sound(self.CONTEXT+'res/sound/Menu/negative_2.ogg'	)	
		self.POSITIVE_SOUND		= pygame.mixer.Sound(self.CONTEXT+'res/sound/Menu/positive.ogg'		)
		self.SAVE_SOUND			= pygame.mixer.Sound(self.CONTEXT+'res/sound/Menu/save.ogg'			)
		self.SHARP_ECHO_SOUND	= pygame.mixer.Sound(self.CONTEXT+'res/sound/Menu/sharp_echo.ogg'	)

			
		#musica
		'''
		self.MUSICA1_SOUND = pygame.mixer.music.load(self.CONTEXT+'res/sound/Musica/Musica1.ogg')
		self.MUSICA2_SOUND = pygame.mixer.music.load(self.CONTEXT+'res/sound/Musica/Musica2.ogg')
		self.MUSICA3_SOUND = pygame.mixer.music.load(self.CONTEXT+'res/sound/Musica/Musica3.ogg')
		self.MUSICA4_SOUND = pygame.mixer.music.load(self.CONTEXT+'res/sound/Musica/Musica4.ogg')
		self.MUSICA5_SOUND = pygame.mixer.music.load(self.CONTEXT+'res/sound/Musica/Musica5.ogg')
		self.MUSICA6_SOUND = pygame.mixer.music.load(self.CONTEXT+'res/sound/Musica/Musica6.ogg')
		'''

		#personajes
		self.PERSONAJEGRITOSTANDARD_SOUND	= pygame.mixer.Sound(self.CONTEXT+'res/sound/Personajes/PersonajeGritoStandard.ogg'	) 	
		self.PERSONAJEVIDABAJA_SOUND			= pygame.mixer.Sound(self.CONTEXT+'res/sound/Personajes/PersonajeVidaBaja.ogg' 		)
		self.PERSONAJESGRITOHOMBRE_SOUND 	= pygame.mixer.Sound(self.CONTEXT+'res/sound/Personajes/PersonajesGritoHombre.ogg'	)	
		
	def generalSoundManage(self, event, repeat = 0):


		if event < GAME_SOUND_EFFECT_EVENT: 
			self.effectManage(event, self.EFFECT_PRIORITY, repeat)
		elif event < GAME_SOUND_MUSIC_EVENT:
			self.musicManage(event, self.MUSIC_PRIORITY, repeat)
		elif event < GAME_SOUND_MENU_EVENT:
			self.menuManage(event, self.MENU_PRIORITY, repeat)
		else:
			print("evento desconocido")

			  
	def effectManage(self, event, priority, repeat):


		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTEAGUASPLASHS:
			  self.AMBIENTEAGUASPLASHS_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTEANDARARENACORTO:
			  self.AMBIENTEANDARARENACORTO_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTEANDARRAMAS:
			  self.AMBIENTEANDARRAMAS_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTEBOSQUECORTO:
			  self.AMBIENTEBOSQUECORTO_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTECASCADA1:
			  self.AMBIENTECASCADA1_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTECASCADA2:
			  self.AMBIENTECASCADA2_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTECASCOTESCAIDA:
			  self.AMBIENTECASCOTESCAIDA_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTECOLISEO:
			  self.AMBIENTECOLISEO_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTEFUEGO1:
			  self.AMBIENTEFUEGO1_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTEFUEGO2:
			  self.AMBIENTEFUEGO2_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTEFUEGONOLOOP:
			  self.AMBIENTEFUEGONOLOOP_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTEGENTEPANICO:
			  self.AMBIENTEGENTEPANICO_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTEGENTEPANICOCORTO:
			  self.AMBIENTEGENTEPANICOCORTO_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTEGENTESUSURROS:
			  self.AMBIENTEGENTESUSURROS_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTEGRANJA:
			  self.AMBIENTEGRANJA_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTEHOJASMANIPULAR:
			  self.AMBIENTEHOJASMANIPULAR_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTELLUVIA:
			  self.AMBIENTELLUVIA_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTENOCHE:
			  self.AMBIENTENOCHE_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTEPISARTIERRA:
			  self.AMBIENTEPISARTIERRA_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTERATA1:
			  self.AMBIENTERATA1_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTERATA2:
			  self.AMBIENTERATA2_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTERATA3:
			  self.AMBIENTERATA3_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTERATA4:
			  self.AMBIENTERATA4_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTERIO1:
			  self.AMBIENTERIO1_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTERIO2:
			  self.AMBIENTERIO2_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_AMBIENTEVIENTO:
			  self.AMBIENTEVIENTO_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_ARMADAGAIMPACTO:
			  self.ARMADAGAIMPACTO_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_ARMAESPADAATAQUE1:
			  self.ARMAESPADAATAQUE1_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_ARMAESPADAATAQUE2:
			  self.ARMAESPADAATAQUE2_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_ARMAESPADAEQUIPAR:
			  self.ARMAESPADAEQUIPAR_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_ARMAESPADAIMPACTO:
			  self.ARMAESPADAIMPACTO_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_ARMAFLECHAATAQUE1:
			  self.ARMAFLECHAATAQUE1_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_ARMAFLECHAATAQUE2:
			  self.ARMAFLECHAATAQUE2_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_ARMAFLECHAIMPACTO1:
			  self.ARMAFLECHAIMPACTO1_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_ARMAFLECHAIMPACTO2:
			  self.ARMAFLECHAIMPACTO2_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_ARMAHORCAATAQUE:
			  self.ARMAHORCAATAQUE_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_ARMAHORCAIMPACTO:
			  self.ARMAHORCAIMPACTO_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_ARMAHORCAIMPACTO2:
			  self.ARMAHORCAIMPACTO2_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_ARMAMAGIAATAQUE:
			  self.ARMAMAGIAATAQUE_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_ARMAMANOTAZOIMPACTO:
			  self.ARMAMANOTAZOIMPACTO_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_ARMAPUNHOIMPACTO:
			  self.ARMAPUNHOIMPACTO_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_PERSONAJEGRITOSTANDARD:
			  self.PERSONAJEGRITOSTANDARD_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_PERSONAJEVIDABAJA:
			  self.PERSONAJEVIDABAJA_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_PERSONAJESGRITOHOMBRE:
			  self.PERSONAJESGRITOHOMBRE_SOUND.play()
			  
		if event == GAME_SOUND_EFFECT_EVENT_STOP:
			pygame.mixer.stop()
		if event == GAME_SOUND_EFFECT_EVENT_PAUSE:
			pygame.mixer.pause()
		if event == GAME_SOUND_EFFECT_EVENT_RESUME:
			pygame.mixer.unpause()

		  
	def musicManage(self, event, priority, repeat):
	  
		if event == GAME_SOUND_MUSIC_EVENT_MUSIC_1:
			self.loadMusic('Musica1')
			pygame.mixer.music.play(repeat)
				
		if event == GAME_SOUND_MUSIC_EVENT_MUSIC_2:
			self.loadMusic('Musica2')
			pygame.mixer.music.play(repeat)
			  
		if event == GAME_SOUND_MUSIC_EVENT_MUSIC_3:
			self.loadMusic('Musica3')
			pygame.mixer.music.play(repeat)
			  
		if event == GAME_SOUND_MUSIC_EVENT_MUSIC_4:
			self.loadMusic('Musica4')
			pygame.mixer.music.play(repeat)
			  
		if event == GAME_SOUND_MUSIC_EVENT_MUSIC_5:
			self.loadMusic('Musica5')
			pygame.mixer.music.play(repeat)
			  
		if event == GAME_SOUND_MUSIC_EVENT_MUSIC_6:
			self.loadMusic('Musica6')
			pygame.mixer.music.play(repeat)
			  
		if event == GAME_SOUND_MUSIC_EVENT_MUSIC_STOP:
			pygame.mixer.music.stop()
			  
		if event == GAME_SOUND_MUSIC_EVENT_MUSIC_PAUSE:
			pygame.mixer.music.pause()
			  
		if event == GAME_SOUND_MUSIC_EVENT_MUSIC_RESUME:
			pygame.mixer.music.unpause()



	def menuManage(self, event, priority, repeat):


		if event == GAME_SOUND_MENU:
			self.LOAD_SOUND.play()
			
		if event == GAME_SOUND_MENU_EVENT_MOVE_UP:
			self.MISC_MENU_SOUND.play()
			
		if event == GAME_SOUND_MENU_EVENT_MOVE_DOWN:
			self.MISC_MENU_SOUND.play()
			
		if event == GAME_SOUND_MENU_EVENT_MOVE_LEFT:
			self.MISC_MENU_SOUND.play()
			
		if event == GAME_SOUND_MENU_EVENT_MOVE_RIGHT:
			self.MISC_MENU_SOUND.play()
			
		if event == GAME_SOUND_MENU_EVENT_OK:
			self.POSITIVE_SOUND.play()
			
		if event == GAME_SOUND_MENU_EVENT_CANCEL:
			self.NEGATIVE_SOUND.play()
			
		if event == GAME_SOUND_MENU_EVENT_EXIT:
			self.SAVE_SOUND.play()
			
	def loadMusic(self, filename):
		pygame.mixer.music.load(self.CONTEXT+'res/sound/Musica/'+filename+'.ogg')

   
def main():
	soundManager = main2()
	soundManager.generalSoundManage(GAME_SOUND_MENU_EVENT_OK)
	time.sleep(5)
	soundManager.generalSoundManage(GAME_SOUND_MENU_EVENT_CANCEL)
	time.sleep(5)
	soundManager.generalSoundManage(GAME_SOUND_MENU_EVENT_MOVE_LEFT)
	time.sleep(5)



