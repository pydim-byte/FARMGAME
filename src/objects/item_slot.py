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
        self.empty = True

    def update(self,dt):
        if PLAYER_INVENTORY['carrots'] > 0 and self.slot_number == 2:
            self.empty = False

    def draw_text(self,surf):
        font = pygame.font.Font(None,12)
        item_count = PLAYER_INVENTORY['carrots']
        text = font.render(f'{item_count:02d}', True, 'black')
        textRect = text.get_rect()
        textRect.midbottom = self.rect.midbottom[0], self.rect.midbottom[1] - 4
        surf.blit(text,textRect)

    def draw(self,surf,offset=0,alpha=1):
        if self.empty:
            return
        #draw_rect = self.rect.move(-offset.x,-offset.y)
        draw_rect = self.rect
        surf.blit(self.image,draw_rect)
        self.draw_text(surf)