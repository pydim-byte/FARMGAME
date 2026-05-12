import pygame
from ..globals import *


class TutorialText(pygame.sprite.Sprite):
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
        msg = 'натисніть 1/2/3, щоб обрати насіння'
        msg1 = 'натисніть пробіль, щоб посадити'
        msg2 = 'зачекайте...'
        msg3 = 'натисніть пробіль, щоб зібрати врожай'
        msg4 = 'натисність Esc, щоб вийти'

        msgs = [msg, msg1, msg2, msg3, msg4]
        
        text = font.render(msgs[self.msg_index], False, 'black')
        textRect = text.get_rect()
        textRect.center = self.rect.centerx,  self.rect.centery
        surf.blit(text,textRect)

    def draw(self,surf,offset=0,alpha=1):
        self.draw_text(surf)