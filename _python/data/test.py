from PyScene import *
import pygame
class test(GameObj):
    def __init__(self, x, y, w, h):
        super().__init__(Vector2D(0, 0), 0, True, True, False)
        self.rect = pygame.Rect(x, y, w, h)
    def update(self):
        pass
    def render(self):
        self.render_to(Game.screen)
    def render_to(self, screen):
        
        pygame.draw.rect(screen, "blue", self.rect, 5)

