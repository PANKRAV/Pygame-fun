from tkinter import Y
import pygame as pg
from pygame.locals import *


import variables as v
import utility as util

pressed = False


class Button :

    def __init__(self, x, y, width, height, color, action, focusaction, text : str = "", rounded = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height       
        self.color = color
        self.old_color = color
        self.action = action
        self.focusactionnum = focusaction
        self.text = text
        self.rounded = rounded
        self.pressed = False
        self.hasfocus = False
        

    @property
    def rect(self) :
        return pg.Rect(self.x, self.y, self.width, self.height)




    @rect.setter
    def rect(self, rect : pg.Rect) :
        self.x = rect.left
        self.y = rect.top
        self.width = rect.width
        self.height = rect.height




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
                self.focusaction(self.focusactionnum)



        if self.hasfocus:
            self.focusaction(self.focusactionnum)





    @staticmethod
    def action1():
        util.q()



   
    def focusaction(self, action = 0):
        if action == 0 :
            if self.hasfocus :
                self.color = v.ORANGE

            else :
                self.color = self.old_color
            
            






class Text :
    def __init__(self, txt, pos : tuple, bg = v.screen_color) :
        self.txt = txt
        self.pos = pos
        self.bg = bg








class Menu :
    def __init__(self) -> None:
        pass