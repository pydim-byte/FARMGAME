import pygame
from ..globals import *


class ShopSlot(pygame.sprite.Sprite):
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

    def draw_price(self,surf):
        font = FONT_LIBRARY['big']
        money_number = abs(PRICE_LIST[self.slot_number]['money'])
        text = font.render(f'${money_number:02d}', False, 'black')
        textRect = text.get_rect()
        textRect.center = self.rect.centerx, self.rect.centery - 32
        surf.blit(text,textRect)

    def draw_current_amount(self,surf):
        font = FONT_LIBRARY['tiny']
        if self.slot_number <= 6:
            current_amount = SEED_INVENTORY[self.slot_number]['amount']
        else:
            current_amount = PLAYER_INVENTORY[self.slot_number-6]['amount']
        text = font.render(f'{current_amount:02d}', False, 'black')
        textRect = text.get_rect()
        textRect.midbottom = self.rect.midbottom[0], self.rect.midbottom[1] - 66
        surf.blit(text,textRect)

    def draw(self,surf,offset=0,alpha=1):
        if self.active:
            draw_rect = self.rect
            surf.blit(self.image,draw_rect)
        self.draw_price(surf)
        self.draw_current_amount(surf)
