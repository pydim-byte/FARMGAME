import pygame
from ..globals import *


class ItemSlot(pygame.sprite.Sprite):
    def __init__(self,pos,images,slot_number):
        super().__init__()
        self.type = type(self).__name__.lower()
        self.pos = pos
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=pos)

        self.slot_number = slot_number
        self.active = False
        if self.slot_number == 1:
            self.active = True

    def update(self,dt):
        pass

    def draw_text(self,surf):
        font = FONT_LIBRARY['tiny']
        item_count = PLAYER_INVENTORY[self.slot_number]['amount']
        text = font.render(f'{item_count:02d}', False, 'black')
        textRect = text.get_rect()
        textRect.midbottom = self.rect.midbottom[0] + 320, self.rect.midbottom[1] - 2
        surf.blit(text,textRect)

    def draw(self,surf,offset=0,alpha=1):
        if self.active:
            draw_rect = self.rect
            surf.blit(self.image,draw_rect)
        self.draw_text(surf)