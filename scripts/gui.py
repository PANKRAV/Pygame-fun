from tkinter import Y
import pygame as pg
from pygame.locals import *


import variables as v
import utility as util

pressed = False


class Button :

    def __init__(self, x, y, width, height, color, action, text : str = "", rounded = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.color = color
        self.action = action
        self.text = text
        self.rounded = rounded
        self.pressed = False
        self.hasfocus = False



    def draw(self, screen = v.screen):
        pg.draw.rect(screen, self.color, self.rect)


    def update(self) :
        x = v.mouse[0] >= self.x and v.mouse[0] <= self.x + self.width       
        y = v.mouse[1] <= self.y + self.height and v.mouse[1] >= self.y
        

        if self.pressed :
            self.action()
            self.pressed = False
        else:
            if x and y :
                self.hasfocus = True
                if pressed :
                    self.pressed = True
            
            else:
                self.hasfocus = False



        if self.hasfocus:
            pass





    @staticmethod
    def action1():
        util.q()





class Text :
    def __init__(self) :
        pass








class Menu :
    def __init__(self) -> None:
        pass