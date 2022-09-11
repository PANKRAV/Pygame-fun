import pygame as pg
import variables as v


class Terrain:
    def __init__(self, x, y, width, height, angle, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.angle = angle




    def draw(self, screen = v.screen):
        pg.draw.rect(screen, self.color, self.rect)




class Platorm(Terrain):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, 0, color)








class Moving_Platform(Platorm):
    def __init__(self):
        pass
        





class Wall(Terrain):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, 90, color)







class Sticky_Wall(Wall):
    def __init__(self):
        pass









class Slope(Terrain):
    def __init__(self, x, y, width, height, angle, color):
        super().__init__(x, y, width, height, angle, color)