from PyScene import *
import pygame
from .btn import btn
from .Levels import Levels
from .DEBUG import DEBUG
class main(Scene):
    def __init__(self):
        super().__init__("main")
        self.Title = Text(Assets.get_font('D_TITLE'), 'Work In Progress', [255, 255, 255], Vector2D(*[928, 64]), 'center', 0, True, True, True, False)
        self.TitleRect = Rect(752, 111, 350, 2, [255, 255, 255], 0, 0, True, False, True, False)
        self.quitBtn = btn(880, 224, 96, 64, 'Quit', Assets.get_font('D45'))
        self.quitBtn.pos = Vector2D(*[1840, 448])
        self.InfoText = Text(Assets.get_font('D35'), 'A game by sfertig', [255, 255, 255], Vector2D(*[108, 1065]), 'center', 1, True, True, True, False)
        self.DEBUGER = DEBUG()
        self.DEBUGER.pos = Vector2D(*[0, 0])
        self.testBtn = btn(0, 1054, 214, 24, '', Assets.get_font('D35'))
        self.testBtn.pos = Vector2D(*[57, 1684])
        self.startBtn = btn(880, 128, 96, 64, 'Start', Assets.get_font('D45'))
        self.startBtn.pos = Vector2D(*[848, 128])
    def update(self):
        
        if self.quitBtn.pressed: Game.quit()
        elif self.startBtn.pressed: Levels()
    def render(self):
        pass

