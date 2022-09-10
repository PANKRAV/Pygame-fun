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




class Accelaretion:
    
    def __init__(self, type : str, sprite : sprites.Sprite):
        self.type = type
        self.body = sprite
        self.value = 0



    @staticmethod
    def gather(acc : list = v.acc_list) -> dict:
        accx, accy = 0, 0

        for item in acc:
            item : Accelaretion
            if item.type == "x":
                accx += item.value

            elif item.type == "y":
                accy += item.value

            elif item.type == "xy":
                accx += item.value["x"]
                accy += item.value["y"]

            else:
                print("accelaretion type not assigned")
        
        v.acc_list = []

        return {"accx" : accx, "accy" : accy}

            


    
class Gravity(Accelaretion):
    def __init__(self, sprite : sprites.Sprite):
        super().__init__("y", sprite)

        if sprite.isground == - 1:
            self.value = sprite.mass * v.g
        else:
            self.value = 0
        
        if self.value != 0:
            v.acc_list.append(self)



class Friction(Accelaretion):
    def __init__(self, sprite : sprites.Sprite):
        super().__init__("x", sprite)

        if v.friction:
            if sprite.isground == 0:
                if sprite.ux > 0 : 
                    self.value = - v.groundμ * sprite.μ * sprite.mass * v.g
                elif sprite.ux < 0 : 
                    self.value = v.groundμ * sprite.μ * sprite.mass * v.g

            elif sprite.isground > 0:
                pass #platform things

            elif sprite.isground == None:
                print("Bad Sprite")

    
        if self.value != 0:
            v.acc_list.append(self)



class Air_res(Accelaretion):
    def __init__(self, sprite : sprites.Sprite):
        super().__init__("xy", sprite)
        self.value = {"x" : 0, "y" : 0}

        if v.air_res:
            self.value["x"] = - sprite.ux * v.ρ
            self.value["y"] = - sprite.uy * v.ρ

        if self.value["x"] != 0 or self.value["y"] != 0:
            v.acc_list.append(self)