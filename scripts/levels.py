import pygame as pg
from pygame.locals import *
import json
from pathlib import Path


class Level:
    def __init__(self, platforms : list, enemies : list, goal : list, start : tuple):
        self.platfroms = platforms
        self.enemies = enemies
        self.goal = goal
        self.start = start






    def setup(self):
        pass


    def end(self):
        pass


    @classmethod
    def load(cls, _json : Path):
        pass