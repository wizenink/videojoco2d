#
# Script que genera el archivo de coordenadas del sprite
#
import configparser

config = configparser.ConfigParser()
config['walk'] = {  'frames': '9',
                    'rectx': '64',
                    'recty': '64',
                    'starty': '576'}

with open('demo.data', 'w') as configfile:
    config.write(configfile)
