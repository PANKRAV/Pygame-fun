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



class Player(Sprite):
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
        self.speed = 600
        self.jump = 1500
        self.mass = 350
        self.uy = 0
        self.ux = 0
        self.uxmax = 2000
        self.isground = False
        #if isground = -1 self is in air
        #if isground = 0 self is on ground
        #if isground > 0 self is on a platform depending on number
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
        

        if self.pressed["jump"]:
            self.isground = -1
        elif int(self.y) >= (v.height - v.ground_height - self.height):
            self.isground = 0
        elif False:
            pass#platform check
        else:
            self.isground = - 1


#X-AXIS
        if self.pressed["right"]:
            self.ux = self.speed

        elif self.pressed["left"]:
            self.ux = - self.speed
#STOP

#Y-AXIS
        if self.pressed["jump"]:
            self.uy = - self.jump
            self.pressed["jump"] = False

        else:
            pass
#STOP

#------UPDATE X---------->
        if self.ux != 0:
            if self.x < 0:
                self.x = 0
            elif self.x > v.width - self.width:
                self.x = v.width - self.width
            else:
                self.x += self.ux * v.dt * v.game_speed
#------------------------>


#-------UPDATE Y---------->        
        self.y += self.uy * v.dt * v.game_speed 

        if self.isground == -1:        
            self.uy += self.mass * v.g * v.dt * v.game_speed

        elif self.isground == 0:
            self.y = v.height - v.ground_height - self.height
            self.uy = 0

        else:
            pass
            self.uy = 0
            #platform staff here
            
        
#-------------------------->
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.draw(screen)


    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)








class Platform:
    pass


class Enemy(Sprite):
    pass


class Projectile(Sprite):
    pass


class State:
    def __init__(self):
        pass