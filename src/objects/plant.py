import pygame
from ..globals import *

class Plant(pygame.sprite.Sprite):
    def __init__(self,pos,images):
        super().__init__()
        self.type = type(self).__name__.lower()
        self.pos = pos
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=pos)

        self.growth_cycle = 0
        self.current_growth_time = 0
        self.max_growth_time = 5

    def grow(self,dt):
        if self.growth_cycle >= 2:
            return
        if self.current_growth_time >= self.max_growth_time:
            self.growth_cycle += 1
            self.image = self.images[self.growth_cycle]
            self.current_growth_time = 0
        self.current_growth_time += dt

    def update(self,dt):
        self.grow(dt)

    def draw(self,surf,offset=0,alpha=1):
        #draw_rect = self.rect.move(-offset.x,-offset.y)
        draw_rect = self.rect
        surf.blit(self.image,draw_rect)