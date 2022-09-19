from __future__ import annotations
from typing import TYPE_CHECKING

from matplotlib.pyplot import axis
import pygame as pg
import variables as v
import physics

if TYPE_CHECKING:
    import sprites


class Terrain:
    terrain_count = 0

    def __init__(self, x, y, width, height, angle, color, solid = False, rounded = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle
        self.color = color
        self.rounded = rounded

        Terrain.terrain_count += 1


    @property
    def rect(self) :
        return pg.Rect(self.x, self.y, self.width, self.height)




    @rect.setter
    def rect(self, rect : pg.Rect) :
        self.x = rect.left
        self.y = rect.top
        self.width = rect.width
        self.height = rect.height



    def draw(self, screen = v.screen):
        pg.draw.rect(screen, self.color, self.rect, border_radius = self.rounded)




class Platform(Terrain):
    platform_count = 0

    def __init__(self, x, y, width, height, color, μ, solid = False, rounded = 0):
        super().__init__(x, y, width, height, 0, color, solid, rounded)
        self.num = Platform.platform_count + 1
        self.μ = μ 
        self.solid = solid
        self.iframes = 0

        Platform.platform_count += 1
        v.plat_data.append(self)



    def update(self, player : sprites.Player):
        if player.isground == self.num:
            ...





class Bouncer(Platform) :
    def __init__(self, x, y, width, height, color = v.GREEN, μ = 0, solid = True, rounded = 0):
        super().__init__(x, y, width, height, color, μ, solid, rounded = width//2)





class Moving_Platform(Platform):
    def __init__(self, x, y, width, height, color, μ, ux = 0, uy = 0, travelx = 0, travely = 0, solid = False, rounded = 0, player_required : bool = False, follow_player = True):
        super().__init__(x, y, width, height, color, μ, solid, rounded)
        self.player_required = player_required
        self.x0 = self.x
        self.y0 = self.y


        self.u = {"ux" : ux, "uy" : uy}

        if self.u["ux"] != 0 and self.u["uy"] != 0 :
            self.axis = "xy"

            if self.u["ux"] > 0 :
                self.startingx = + 1
            else:
                self.startingy = - 1

            if self.u["uy"] > 0 :
                self.startingy = + 1
            else:
                self.startingy = - 1

        elif self.u["ux"] != 0 :
            self.axis = "x"

            if self.u["ux"] > 0 :
                self.startingx = + 1
            else:
                self.startingy = - 1

        elif self.u["uy"] != 0 :
            self.axis = "y"
           
            if self.u["uy"] > 0 :
                self.startingy = + 1
            else:
                self.startingy = - 1

        else :
            self = Platform(x, y, width, height, color, μ, solid, rounded)


        self.travelx = travelx
        self.travely = travely
        self.follow_player = follow_player














    def update(self, player : sprites.Player):
        self.ux0 = self.u["ux"]
        self.uy0 = self.u["uy"]
        

        if self.player_required :
            if player.isground == self.num:
                self.x += self.u["ux"] * v.dt * v.game_speed

                if self.axis == "x" or self.axis == "xy":
                    if self.x <= self.x0 - self.travelx or self.x + self.width >= self.x0 + self.width + self.travelx :
                        self.u["ux"] = - self.u["ux"]




                self.y += self.u["uy"] * v.dt * v.game_speed

                if self.axis == "y" or self.axis == "xy":
                    if self.y <= self.travely or self.y + self.height >= v.height - self.travely :
                        self.u["uy"] = - self.u["uy"]




        else:
            self.x += self.u["ux"] * v.dt * v.game_speed

            if self.axis == "x" or self.axis == "xy":
                if self.x <= self.x0 - self.travelx or self.x + self.width >= self.x0 + self.width + self.travelx :
                    self.u["ux"] = - self.u["ux"]






            self.y += self.u["uy"] * v.dt * v.game_speed

            if self.axis == "y" or self.axis == "xy":
                if self.y <= self.travely or self.y + self.height >= v.height - self.travely :
                    self.u["uy"] = - self.u["uy"]



        #self.rect = pg.Rect(self.x, self.y, self.width, self.height)






class Wall(Terrain):
    wall_count = 0

    def __init__(self, x, y, width, height, color, solid = False):
        super().__init__(x, y, width, height, 90, color, solid)
        self.num = Wall.wall_count + 1

        Wall.wall_count += 1
        v.wall_data.append(self)







class Sticky_Wall(Wall):
    def __init__(self):
        ...









class Slope(Terrain):
    slope_count = 0

    def __init__(self, x, y, width, height, angle, color, solid = False):
        super().__init__(x, y, width, height, angle, color, solid)

        Slope.slope_count += 1







class Goal:
    ...