from numpy import isin
import pygame as pg
from pygame.locals import *
import json
import pathlib
import os
from __future__ import annotations
from typing import TYPE_CHECKING
from scripts.sprites import Player


import terrain as t
import sprites
import gui
import variables as v


v.cwd =  pathlib.Path.cwd()


class Level:
    
    current = 0

    def __init__(self, platforms : list[t.Platform], enemies : list[sprites.Enemy], goal : t.Goal, buttons : list[gui.Button], player : sprites.Player):
        self.platfroms : list[t.Platform] = platforms
        self.enemies : list[sprites.Enemy] = enemies
        self.goal = goal
        self.player : sprites.Player = player
        self.buttons : list[gui.Button] = buttons
        self.num = Level.current


        Level.current += 1





    def run(self):
        self.player.plat_check()
        self.player.update(v.screen)
        self.player.goal_check(self.goal)
        self.player.draw()


        self.player.life_check()
        self.player.life_draw()



        for platform in self.platfroms :
            platform.update(self.player)
            platform.draw(v.screen)


        for enemy in self.enemies :
            enemy.update()
            enemy.draw(v.screen)


        for button in self.buttons :
            button.update()
            button.draw(v.screen)
            


    def end(self):
        Level.current += 1
        del self
        

            


    @classmethod
    def load(cls, _json : pathlib.Path) -> Level :
        platforms = []
        enemies = []
        buttons = []



        with _json.open(mode = "rt") as f :
            _json = f.read()
            _json = json.loads(_json)


        Player = sprites.Player(_json["player"]["x"], _json["player"]["y"])
        Goal = t.Goal((_json["goal"]["x"], _json["goal"["y"]]), _json["goal"]["size"], v.GREEN)


        for enemy in _json["enemies"] :
            for moving_enemy in enemy["moving_enemies"] :
                enemies.append(sprites.Moving_Enemy((moving_enemy["x"], moving_enemy["y"]), moving_enemy["u"]))

            for norm_enemy in enemy["norm_enemies"] :
                enemies.append(sprites.Enemy((norm_enemy["x"], norm_enemy["y"])))


            for air_enemy in enemy["air_enemies"] :
                ...


        for terrain in _json["terrain"] :
            for platform in terrain["platform"] :
                platforms.append(t.Platform(platform["x"], platform["y"], platform["width"], platform["height"], platform["color"], platform["μ"], platform["solid"], platform["rounded"]))

            for platform in terrain["moving_platform"] :
                platforms.append(t.Moving_Platform(platform["x"], platform["y"], platform["width"], platform["height"], platform["color"], platform["μ"], platform["ux"], platform["uy"], platform["travelx"], platform["travely"], platform["solid"], platform["rounded"], platform["player_required"], platform["follow_player"]))

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



        return cls(platforms, enemies, Goal, buttons, Player)




    def json_pack(self, name : str):
        ...