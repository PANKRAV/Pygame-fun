from __future__ import annotations
import pygame as pg
from pygame.locals import *
import math
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    import sprites
import variables as v


v.acc_list = []


class Force:
    pass




class Acceleration:
    
    def __init__(self, type : str, sprite : sprites.Sprite):
        self.type = type
        self.body = sprite
        self.value = 0



    @staticmethod
    def gather(acc : list = v.acc_list) -> dict:
        accx, accy = 0, 0

        for item in acc:
            item : Acceleration
            if item.type == "x":
                accx += item.value

            elif item.type == "y":
                accy += item.value

            elif item.type == "xy":
                accx += item.value["x"]
                accy += item.value["y"]

            else:
                print("Acceleration type not assigned")
        
        v.acc_list = []

        return {"accx" : accx, "accy" : accy}

            

class Generic(Acceleration):
    def __init__(self, sprite: sprites.Sprite, ax, ay):
        super().__init__("xy", sprite)
        self.value = {"x" : ax, "y" : ay}

        if self.value["x"] != 0 or self.value["y"] != 0:
            v.acc_list.append(self)



class Gravity(Acceleration):
    def __init__(self, sprite : sprites.Sprite):
        super().__init__("y", sprite)

        if sprite.isground == - 1:
            self.value = sprite.mass * v.g
        else:
            self.value = 0
        
        if self.value != 0:
            v.acc_list.append(self)



class Friction(Acceleration):
    def __init__(self, sprite : sprites.Sprite):
        super().__init__("x", sprite)

        if v.friction:
            
            if sprite.isground == 0:
                if sprite.ux > 0 : 
                    self.value = - v.groundμ * sprite.μ * sprite.mass * v.g
                elif sprite.ux < 0 : 
                    self.value = v.groundμ * sprite.μ * sprite.mass * v.g

            elif sprite.isground > 0:
                if sprite.ux > 0 :
                    self.value = - v.plat_data[sprite.isground - 1].μ * sprite.μ * sprite.mass *v.g
                elif sprite.ux < 0 : 
                    self.value = v.plat_data[sprite.isground - 1].μ * sprite.μ * sprite.mass *v.g

            elif sprite.isground == None:
                print("Bad Sprite")

    
        if self.value != 0:
            v.acc_list.append(self)



class Air_res(Acceleration):
    def __init__(self, sprite : sprites.Sprite):
        super().__init__("xy", sprite)
        self.value = {"x" : 0, "y" : 0}

        
        if v.air_res:
            if not (sprite.ux < 20 and sprite.ux > -20):
                self.value["x"] = - sprite.ux * v.ρ
            
            if not (sprite.uy < 1 and sprite.uy > -1):
                self.value["y"] = - sprite.uy * v.ρ

        if self.value["x"] != 0 or self.value["y"] != 0:
            v.acc_list.append(self)
