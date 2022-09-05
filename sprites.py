import pygame as pg
from pygame.locals import *

#user defined
import variables as v
v.dt : float



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
    height = 100
    width = 50
    player_data = []

    def __init__(self, x, y) -> None:
        self.width = 50
        self.height = 100
        self.x = int(x)
        self.y = int(y)  
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
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
        self.ux = 0
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


    def update(self, screen):
        self.ux = 0

        if self.pressed["right"]:
            self.ux = self.speed

        elif self.pressed["left"]:
            self.ux = - self.speed

        elif self.pressed["jump"]:
            self.uy = self.jump

        else:
            pass


        if self.ux != 0:
            if self.x <= 0 or self.x >= v.width - self.width:
                self.x = 0
            else:
                self.x += self.ux * v.dt * v.game_speed


        

        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        Player.draw(v.screen)


    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)










class State:
    def __init__(self):
        pass