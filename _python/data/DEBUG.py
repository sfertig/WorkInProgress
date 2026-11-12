from PyScene import *
import pygame
class DEBUG(GameObj):
    def __init__(self):
        super().__init__(Vector2D(0, 0), 0, True, True, True)
    def update(self):
        
        if Keys.is_pressed(Keys.escape): Game.quit() #for debug / testing
    def render(self):
        pass

