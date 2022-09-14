from __future__ import annotations
from typing import TYPE_CHECKING
from aifc import Error
import pygame as pg
from pygame.locals import *
import math

#user defined
if TYPE_CHECKING or True:
    import sprites
    import terrain as t



def collision(sprite1: sprites.Sprite, sprite2: sprites.Sprite|t.Terrain) -> bool:


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

    elif isinstance(sprite2, t.Terrain):
        sprite2 : t.Terrain

    else:
        assert isinstance(sprite2, sprites.Sprite) or isinstance(sprite2, t.Terrain)
#---------------->


    x = sprite1.x < sprite2.x + sprite2.width and sprite1.x + sprite1.width > sprite2.x
    y = sprite1.y < sprite2.y + sprite2.height and sprite1.y + sprite1.height > sprite2.y

    if x and y:

        return True
    else:

        return False










def linear_system(a, b, c, d ) -> tuple:
    x = 0
    y = 0

    return x , y


