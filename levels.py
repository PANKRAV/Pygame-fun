import pygame as pg
from pygame.locals import *


class Level:
    def __init__(self, platforms : list, enemies : list, goal : list, start : tuple):
        self.platfroms = platforms
        self.enemies = enemies
        self.goal = goal
        self.start = start