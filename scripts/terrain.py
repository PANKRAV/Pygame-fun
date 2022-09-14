from __future__ import annotations
from typing import TYPE_CHECKING
import pygame as pg
import variables as v
if TYPE_CHECKING:
    import sprites


class Terrain:
    terrain_count = 0

    def __init__(self, x, y, width, height, angle, color, solid = False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.angle = angle
        self.color = color

        Terrain.terrain_count += 1




    def draw(self, screen = v.screen):
        pg.draw.rect(screen, self.color, self.rect)




class Platform(Terrain):
    platform_count = 0

    def __init__(self, x, y, width, height, color, μ, solid = False):
        super().__init__(x, y, width, height, 0, color, solid)
        self.num = Platform.platform_count + 1
        self.μ = μ 
        self.solid = solid
        self.iframes = 0

        Platform.platform_count += 1
        v.plat_data.append(self)



    def update(self, player : sprites.Player):
        if player.isground == self.num:
            pass




class Moving_Platform(Platform):
    def __init__(self):
        pass






class Wall(Terrain):
    wall_count = 0

    def __init__(self, x, y, width, height, color, solid = False):
        super().__init__(x, y, width, height, 90, color, solid)
        self.num = Wall.wall_count + 1

        Wall.wall_count += 1
        v.wall_data.append(self)







class Sticky_Wall(Wall):
    def __init__(self):
        pass









class Slope(Terrain):
    slope_count = 0

    def __init__(self, x, y, width, height, angle, color, solid = False):
        super().__init__(x, y, width, height, angle, color, solid)

        Slope.slope_count += 1