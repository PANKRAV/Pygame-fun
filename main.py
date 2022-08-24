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






def q():
    pg.quit()
    sys.exit()



pg.init()
pg.display.init()
pg.display.set_caption("my game")


screen = pg.display.set_mode((v.width, v.height), flags = pg.SHOWN)
screen.fill(v.BLACK)


player = sprites.Player(100, 1000 - v.ground_height - sprites.Player.height)


clock = pg.time.Clock()
clock.tick(v.fps)
start_time = time.time()





if __name__ == "__main__":
    while True:
        clock.tick(v.fps)
        now = time.time()
        dt = now - start_time
        start_time = time.time()

        screen.fill((12, 24, 36))
        #edafos
        pg.draw.rect(screen, v.BROWN, (0, (v.height - v.ground_height), v.width, v.ground_height))

        for event in pg.event.get():
            if event.type == QUIT:
                q()

            if event.type == KEYDOWN:

                if event.key == K_SPACE or event.key == K_UP:
                    player.pressed["jump"] = True
                elif event.key == K_d or event.key == K_RIGHT:
                    player.pressed["right"] = True
                elif event.key == K_a or event.key == K_LEFT:
                    player.pressed["left"] = True


            if event.type == KEYUP:

                if event.key == K_d or event.key == K_RIGHT:
                    player.pressed["right"] = False
                elif event.key == K_a or event.key == K_LEFT:
                    player.pressed["left"] = False



        player.update()
        player.draw(screen)
        pg.display.flip()


        