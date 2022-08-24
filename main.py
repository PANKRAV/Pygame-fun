import pygame as pg
from pygame.locals import *
import os
import sys
import numpy
import random
import time

#user defined
import variables as v

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"



def q():
    pg.quit()
    sys.exit()



pg.init()
pg.display.init()
pg.display.set_caption("my game")


screen = pg.display.set_mode((v.width, v.height), flags = pg.SHOWN)
screen.fill(v.BLACK)



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