import pygame as pg
from pygame.locals import *

#user defined
import variables as v



#vars
plat_data = []
enemy_data = ["enemy"]
projectile_data = ["projectile"]



#super(Player, self).__init__()
class Sprite:

    def __init__(self,x ,y, shape, color) -> None:
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color



class Player:

    player_data = []

    def __init__(self, x, y) -> None:
        self.width = 50
        self.height = 100
        self.rect = pg.Rect(x, y, self.width, self.height)
        self.x = int(x)
        self.y = int(y)  
        self.color = v.BLUE
        self.pressed = {
            "jump" : False,
            "right" : False,
            "left" : False,
            "shoot" : False
        }
        self.speed = 350
        self.jump = 1000
        self.mass = 350
        self.uy = 0
        self.isground = False
        self.lifes = 4
        #state for platform or ground
        self.s = 0
        self.state = "vulnerable"
        self.μ = 0
        
        Player.player_data.append({
            "width" : self.width,
            "height" : self.height,
            "x" : self.x,
            "y" : self.y,
            "speed" : self.speed,
            "jump" : self.jump,
            "uy" : self.uy,
            "lifes" : self.lifes
        })
        



    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)










class State:
    def __init__(self):
        pass