import pygame
from ..globals import *


class MenuPointer(pygame.sprite.Sprite):
    def __init__(self,pos,images,pointer_num):
        super().__init__()
        self.type = type(self).__name__.lower()
        self.pos = pos
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=pos)
        self.pointer_num = pointer_num

        if self.pointer_num == 0:
            self.active = True
        else:
            self.active = False

    def update(self,dt):
        pass

    def draw(self,surf,offset=0,alpha=1):
        if self.active:
            draw_rect = self.rect
            surf.blit(self.image,draw_rect)