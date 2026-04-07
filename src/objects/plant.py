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

    def update(self,dt):
        pass

    def draw(self,surf,offset=0,alpha=1):
        draw_rect = self.rect.move(-offset.x,-offset.y)
        surf.blit(self.image,draw_rect)