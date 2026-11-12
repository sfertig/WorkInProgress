from PyScene import *
import pygame
from .btn import btn
class Levels(Scene):
    def __init__(self):
        super().__init__("Levels")
        self.Title = Text(Assets.get_font('D_TITLE'), 'Level Selection:', [255, 255, 255], Vector2D(*[280, 50]), 'center', 0, True, True, True, False)
        self.back = btn(12, 90, 64, 40, 'back', Assets.get_font('D35'))
        self.back.pos = Vector2D(*[12, 90])
    def update(self):
        
        if self.back.pressed: Game.scenes["main"]()
    def render(self):
        pass

