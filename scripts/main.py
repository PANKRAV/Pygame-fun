import pygame as pg
from pygame.locals import *
import pygame_gui
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys
import numpy
import random
import time
import asyncio

#user defined
import variables as v
import sprites
import utility as util
import terrain as t
import gui










pg.init()
pg.display.init()
pg.display.set_caption("my game")


v.screen : pg.Surface
v.screen.fill(v.screen_color)


player = sprites.Player(100, 1000 - v.ground_height - sprites.Player.height)
platform1 = t.Platform(300, 400, 200, 80, v.RED, 0.6, True, 20)
platform2 = t.Platform(700, 600, 200, 25, v.GREEN, 0.6)
platform3 = t.Moving_Platform(800, 200, 200, 70, v.BLUE, 0.8, 200, 0, 400, 0)
platform4 = t.Moving_Platform(200, 100, 200, 70, v.ORANGE, 0.7, 100, 0, 200, 0, player_required = True   )
#enemies
enemy1 = sprites.Moving_Enemy((0, v.height - v.ground_height - sprites.Enemy.height), 30)
button = gui.Button(0, 0, 40, 40, v.RED, gui.Button.action1, 0)



clock = pg.time.Clock()
clock.tick(v.fps)
start_time = time.time()





if __name__ == "__main__":
    while True:
        v.mouse = pg.mouse.get_pos()
        clock.tick(v.fps)
        now = time.time()
        v.dt = now - start_time
        start_time = time.time()

        v.screen.fill((12, 24, 36))
        #edafos
        pg.draw.rect(v.screen, v.BROWN, (0, (v.height - v.ground_height), v.width, v.ground_height))

        for event in pg.event.get():
            event : pg.event

            if event.type == QUIT:
                util.q()

            if event.type == KEYDOWN:
                

                if (event.key == K_SPACE or event.key == K_UP ) and player.isground != -1:
                    player.pressed["jump"] = True
                elif event.key == K_d or event.key == K_RIGHT:
                    player.pressed["right"] = True
                elif event.key == K_a or event.key == K_LEFT:
                    player.pressed["left"] = True
                elif event.key == K_LSHIFT:
                    #if player.pressed["left"] or player.pressed["right"]:
                    player.pressed["sprint"] = True



            if event.type == KEYUP:

                if event.key == K_d or event.key == K_RIGHT:
                    player.pressed["right"] = False
                elif event.key == K_a or event.key == K_LEFT:
                    player.pressed["left"] = False
                elif event.key == K_LSHIFT:
                    player.pressed["sprint"] = False



            if event.type == pg.MOUSEBUTTONDOWN and pg.mouse.get_pressed()[0]:
                left_click = True

            gui.pressed = False
            if event.type == pg.MOUSEBUTTONUP and left_click:
                    gui.pressed = True
                    left_click = False





        player.plat_check()
        player.update(v.screen)
        player.draw(v.screen)
        player.life_check()

        player.life_draw(v.screen)
        platform1.update(player)
        platform1.draw(v.screen)
        platform2.update(player)
        platform2.draw(v.screen)
        platform3.update(player)
        platform3.draw(v.screen)
        platform4.update(player)
        platform4.draw(v.screen)
        enemy1.update()
        enemy1.draw(v.screen)
        button.update()
        button.draw(v.screen)


        pg.display.flip()


