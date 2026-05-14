import pygame
from ..globals import *


class ShopMoneyBox(pygame.sprite.Sprite):
    def __init__(self,rect):
        super().__init__()
        self.type = type(self).__name__.lower()
        self.image = pygame.surface.Surface((4,4))
        self.rect = rect
        self.msg_index = 0

    def update(self,dt):
        pass

    def draw_text(self,surf):
        font = FONT_LIBRARY['huge']
        money_amount = PLAYER_MONEY['current']
        text = font.render(f'${money_amount:02d}', False, 'black')
        textRect = text.get_rect()
        textRect.center = self.rect.centerx,  self.rect.centery
        surf.blit(text,textRect)

    def draw(self,surf,offset=0,alpha=1):
        self.draw_text(surf)