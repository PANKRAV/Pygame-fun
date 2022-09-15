import pygame as pg
from pygame.locals import *
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys
import numpy
import random
import time

#user defined
import variables as v
import sprites
import utility as util
import terrain as t










pg.init()
pg.display.init()
pg.display.set_caption("my game")


v.screen : pg.Surface
v.screen.fill(v.BLACK)


player = sprites.Player(100, 1000 - v.ground_height - sprites.Player.height)
platform1 = t.Platform(300, 400, 200, 80, v.RED, 0.6, True)
platform2 = t.Platform(700, 600, 200, 25, v.GREEN, 0.6)
#enemies



clock = pg.time.Clock()
clock.tick(v.fps)
start_time = time.time()





if __name__ == "__main__":
    while True:
        clock.tick(v.fps)
        now = time.time()
        v.dt = now - start_time
        start_time = time.time()

        v.screen.fill((12, 24, 36))
        #edafos
        pg.draw.rect(v.screen, v.BROWN, (0, (v.height - v.ground_height), v.width, v.ground_height))

        for event in pg.event.get():
            if event.type == QUIT:
                util.q()

            if event.type == KEYDOWN:

                if (event.key == K_SPACE or event.key == K_UP ) and player.isground != -1:
                    player.pressed["jump"] = True
                elif event.key == K_d or event.key == K_RIGHT:
                    player.pressed["right"] = True
                elif event.key == K_a or event.key == K_LEFT:
                    player.pressed["left"] = True
                if event.key == K_LSHIFT:
                    #if player.pressed["left"] or player.pressed["right"]:
                    player.pressed["sprint"] = True


            if event.type == KEYUP:

                if event.key == K_d or event.key == K_RIGHT:
                    player.pressed["right"] = False
                elif event.key == K_a or event.key == K_LEFT:
                    player.pressed["left"] = False
                elif event.key == K_LSHIFT:
                    player.pressed["sprint"] = False



        player.plat_check()
        player.update(v.screen)
        player.draw(v.screen)
        platform1.update(player)
        platform1.draw(v.screen)
        platform2.update(player)
        platform2.draw(v.screen)
        pg.display.flip()


        