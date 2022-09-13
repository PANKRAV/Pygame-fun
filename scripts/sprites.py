from __future__ import annotations
from typing import TYPE_CHECKING
import physics as physics
import pygame as pg
from pygame.locals import *

#user defined
import variables as v
v.dt : float
if TYPE_CHECKING:
    import terrain







#super(Player, self).__init__()
class Sprite:
    sprite_count = 0

    def __init__(self, x : int , y : int , shape, color, height : int , width : int) -> None:
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.height = height
        self.width = width
        if self.shape == "rectangle" :
            self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        elif self.shape == "square":
            self.rect = pg.Rect(self.x, self.y, self.width, self.width)

        #to be assigned in some of the child classes
        self.ux, self.uy, self.μ, self.mass, self.isground = None, None, None, None, None 

        Sprite.sprite_count += 1


    def draw(self, screen):
        if self.shape == "circle" :
            pg.draw.circle(screen, self.color, (self.x, self.y), (self.height))
        else:
            pg.draw.rect(screen, self.color, self.rect)








class Player(Sprite):
    height = 100
    width = 50
    player_data = []

    def __init__(self, x, y) -> None:
        super().__init__(int(x), int(y), "rect", v.BLUE, 100, 50)
        #hitbox
        self.width = 50
        self.height = 100
        #hitbox//  
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.pressed = {
            "jump" : False,
            "right" : False,
            "left" : False,
            "shoot" : False,
            "sprint" : False
        }
        self.speed = 600
        self.jump = 2500
        self.mass = 600
        self.uy = 0
        self.ay = 0
        self.ux = 0
        self.ax = 0
        self.uxmax = 2000
        self.terminal_u = 0
        self.sprint = 200000
        self.isground = False
        #if isground = -1 self is in air
        #if isground = 0 self is on ground
        #if isground > 0 self is on a platform depending on number
        self.lifes = 4
        #state for platform or ground
        self.s = 0
        self.state = "vulnerable"
        self.μ = 0.45
        
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
        

        if not (v.friction or v.air_res):
            self.ux = 0
        self.acceleration()
        

        if self.pressed["jump"]:
            self.isground = -1
        elif int(self.y) >= (v.height - v.ground_height - self.height):
            self.isground = 0
        elif self.plat_check() :
            pass
        else:
            self.isground = - 1


#X-AXIS
        if self.pressed["right"]:
            self.ux = self.speed

        elif self.pressed["left"]:
            self.ux = - self.speed
#STOP


#------UPDATE X---------->
        self.ux += self.ax * v.dt * v.game_speed
        if self.ux != 0:
            if self.x < 0:
                self.x = 0
            elif self.x > v.width - self.width:
                self.x = v.width - self.width
            else:
                self.x += self.ux * v.dt * v.game_speed
#------------------------>




#Y-AXIS
        if self.pressed["jump"]:
            self.uy = - self.jump
            self.pressed["jump"] = False

        else:
            pass
#STOP


#-------UPDATE Y---------->        
        self.y += self.uy * v.dt * v.game_speed 

        if self.isground == -1:        
            self.uy += self.ay * v.dt * v.game_speed

        elif self.isground == 0:
            self.y = v.height - v.ground_height - self.height
            self.uy = 0

        elif self.isground > 0:
            self.y = v.plat_data[self.isground - 1].y - self.height
            self.uy = 0
            #platform staff here
            
        
#-------------------------->
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.draw(screen)






    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)






    def acceleration(self, platfrom = None):
        self.ax = 0
        self.ay = 0



        gravity = physics.Gravity(self)
        friction = physics.Friction(self)
        air_res = physics.Air_res(self)
        acc = physics.Acceleration.gather(v.acc_list)
        self.ax = acc["accx"]
        self.ay = acc["accy"]   

        

            
        
        if self.isground == 0:
            if self.ux > 0:
                if v.object_acceleration and self.pressed["sprint"] and self.pressed["right"]: 
                     self.ax += self.sprint

            elif self.ux < 0:
                if v.object_acceleration and self.pressed["sprint"] and self.pressed["left"]: 
                    self.ax -= self.sprint

        



    def plat_check(self):
        for plat in v.plat_data:
            plat : terrain.Platform
            if self.uy >= 0 :
 
                y = self.y - 20 >= plat.y - plat.height - self.height and self.y + self.height <= plat.y + 20
                x = self.x + self.width >= plat.x and self.x <= plat.x + plat.width       
                if x and y:
                    self.isground = plat.num
                    return True




class Enemy(Sprite):
    enemy_count = 0

    def __init__(self, x, y, moving : bool):
        super().__init__(x, y, "square", v.RED, 40, 40)
        self.moving = moving

        Enemy.enemy_count += 1

        




class Projectile(Sprite):
    pass











class State:
    def __init__(self):
        pass