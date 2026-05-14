import pygame
from ..globals import *


class ShopTutorialText(pygame.sprite.Sprite):
    def __init__(self,rect):
        super().__init__()
        self.type = type(self).__name__.lower()
        self.image = pygame.surface.Surface((4,4))
        self.rect = rect
        self.msg_index = 0

    def update(self,dt):
        pass

    def draw_text(self,surf):
        font = FONT_LIBRARY['medium']
        msg = 'вліво/вправо щоб обрати позицію'
        msg1 = 'пробіл - купити насіння/продати овочі'
        msg2 = 'Esc - завершити тренування'

        msgs = [msg, msg1, msg2]
        
        text = font.render(msgs[self.msg_index], False, 'black')
        textRect = text.get_rect()
        textRect.center = self.rect.centerx,  self.rect.centery
        surf.blit(text,textRect)

    def draw(self,surf,offset=0,alpha=1):
        if GAME_STATES['previous'] == 'tutorial':
            self.draw_text(surf)