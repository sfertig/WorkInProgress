from PyScene import *
import pygame
class btn(GameObj):
    def __init__(self, x, y, w, h, text, font):
        super().__init__(Vector2D(0, 0), 0, True, True, False)
        
        self.dim = Vector2D(w, h)
        self.rect = pygame.Rect(x, y, w, h)
        self._rect = pygame.Rect(0, 0, w, h)
        
        self.text = self.child(Text(font, text, "white", Vector2D(w//2, h//2), visible=False))
        #self._tRect = self.text
        self.sub = SubScreen(x, y, w, h, "black", Game.screen)
        
        #btn attributes
        self.hovered = False
        self.pressed = False
        self.w = 0
        self.minW = -1
        self.maxW = 2
    def update(self):
        
        mpos = self.sub.local_mouse_pos().to_int()
        self.hovered = self._rect.collidepoint(mpos)
        if self.hovered: self.w = self.maxW
        else: self.w = self.minW
        
        if Game.click and self.hovered: self.pressed = True
        else: self.pressed = False
        
        if self.pressed: self.w = 0
    def render(self):
        
        self.sub.clear()
        
        pygame.draw.rect(self.sub.screen, "white", self._rect, self.w)
        
        self.text.render_to(self.sub.screen)
        
        self.sub.render()
    def render_to(self, screen):
        
        #render a debugging rect onto the screen
        
        pygame.draw.rect(screen, "white", (self.rect))

