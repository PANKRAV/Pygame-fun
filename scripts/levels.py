from numpy import isin
import pygame as pg
from pygame.locals import *
import json
import pathlib
import os
from __future__ import annotations
from typing import TYPE_CHECKING


import terrain as t
import sprites
import gui
import variables as v


v.cwd =  pathlib.Path.cwd()


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
    def load(cls, _json : pathlib.Path) -> Level :
        
        with _json.open(mode = "rt") as f :
            _json = f.read()
            _json = json.loads(_json)


        Player = sprites.Player(_json["player"]["x"], _json["player"]["y"])
        Goal = t.Goal((_json["goal"]["x"], _json["goal"["y"]]), _json["goal"]["size"], v.GREEN)


        for enemy in _json["enemy"] :
            if isinstance(enemy, sprites.Moving_Enemy ) :
                pass

            else :
                pass


        for terrain in _json["terrain"] :
            for platform in terrain["platform"] :
                pass

            for moving_platform in terrain["moving_platform"] :
                pass

            for bouncer in terrain["bouncer"] :
                pass

            for wall in terrain["wall"] :
                pass

            for sticky_wall in terrain["sticky_wall"] :
                pass

            for slope in terrain["slope"] :
                pass



        env_data = _json["enviroment"]
        v.groundμ = env_data["μ"]
        v.ρ = env_data["ρ"]
        v.screen_color = env_data["background_color"]
        v.g = env_data["g"]
        v.game_speed = env_data["game_speed"]




    def json_pack(self, name : str):
        ...