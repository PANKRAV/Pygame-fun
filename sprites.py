import pygame as pg
from pygame.locals import *



class Sprite:

    def __init__(self,x ,y, shape, color) -> None:
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color



class Player(Sprite):

    def __init__(self) -> None:
        super(Player, self).__init__()
        