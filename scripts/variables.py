import pygame as pg
from pygame.locals import *
import pathlib


#COLORS
WHITE = (255, 255, 255 )
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (255, 248, 220)
CYAN = (173, 216, 230)
LIGHT_BLACK = (25, 25, 25)
YELLOW = (255, 255, 224)
ORANGE = (255, 165 ,0) 



#LENGTHS
height = 1000
width = 1200
ground_height = 100




#CORDINATES





#PATHS
images = None
sounds = None

#DATA
acc_list = []
plat_data = []
enemy_data = []
wall_data = []
sprite_data = []



#FUNCTIONAL
game_speed = 1
g = 10
fps = 2400
screen = pg.display.set_mode((width, height), flags = pg.SHOWN)
dt = None
ρ = 1 #air density constant
groundμ = 0.25 #ground friction
#switches
object_acceleration = True
friction = True
air_res = True
