import pygame as pg
from pygame.locals import *
import json
from pathlib import Path


class Level:
    def __init__(self, platforms : list, enemies : list, goal : list, buttons : list, start : tuple):
        self.platfroms = platforms
        self.enemies = enemies
        self.goal = goal
        self.start = start
        self.buttons = buttons
        self.num = 0






    def setup(self):
        ...


    def end(self):
       ...


    @classmethod
    def load(cls, _json : Path):
        ...



    def json_pack(self, name : str):
        ...