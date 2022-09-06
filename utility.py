from aifc import Error
import pygame as pg
from pygame.locals import *
import math

#user defined
import sprites



def collision(sprite1: sprites.Sprite, sprite2: sprites.Sprite) -> bool:


#SPRITE1
    if isinstance(sprite1, sprites.Player):
        sprite1 : sprites.Player

    elif isinstance(sprite1, sprites.Enemy):
        sprite1 : sprites.Enemy

    elif isinstance(sprite1, sprites.Projectile):
        sprite1 : sprites.Projectile
    
    else:
        assert isinstance(sprite1, sprites.Sprite)
#----------------->


#SPRITE2
    if isinstance(sprite2, sprites.Player):
        sprite2 : sprites.Player

    elif isinstance(sprite2, sprites.Enemy):
        sprite2 : sprites.Enemy

    elif isinstance(sprite2, sprites.Projectile):
        sprite2 : sprites.Projectile
    else:
        assert isinstance(sprite2, sprites.Sprite)
#---------------->

    
    if True:
        return True
    elif True:
        return True