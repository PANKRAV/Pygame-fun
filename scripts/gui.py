import pygame as pg
from pygame.locals import *


import variables as v



class Button :
    def __init__(self, x, y, width, height, color, action : function, text : str = "", rounded = 0):
        self.x = x
        self.y = y
        self.widith = width
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
        if self.pressed :
            self.action()
            self.pressed = False
        else:
            if v.mouse :
                self.hasfocus = True
            
            else:
                self.hasfocus = False



        if self.hasfocus:
            pass

class Text :
    def __init__(self) :
        pass