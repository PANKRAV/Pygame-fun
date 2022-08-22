import pygame as pg
from pygame.locals import *
import os
import sys
import numpy
import random

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"


pg.init()
pg.display.init()

pg.display.set_caption("my game")



def q():
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    while True:
        pass