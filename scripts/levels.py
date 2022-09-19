import pygame as pg
from pygame.locals import *
import json
from pathlib import Path
from __future__ import annotations
from typing import TYPE_CHECKING


import terrain as t
import sprites
import gui


class Level:
    
    current = 0

    def __init__(self, platforms : list[t.Platform], enemies : list[sprites.Enemy], goal : list[t.Goal], buttons : list[gui.Button], start : tuple[int]):
        self.platfroms = platforms
        self.enemies = enemies
        self.goal = goal
        self.start = start
        self.buttons = buttons
        self.num = 0






    def setup(self):
        ...


    def end(self):
        Level.current += 1
        del self
        

            


    @classmethod
    def load(cls, _json : Path):
        ...



    def json_pack(self, name : str):
        ...