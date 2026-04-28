import pygame
from ..globals import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,images,plant_ability):
        super().__init__()
        self.type = type(self).__name__.lower()
        self.pos = pos
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=pos)
        self.facing = 'down'
        self.plant_ability = plant_ability
        
    def move(self,direction):
        if direction == 'left':
            self.facing = 'left'
            self.image = self.images[2]
            if self.pos.x <= FARM_TOPLEFT[0]:
                return
            self.pos.x -= TILE_SIZE
        if direction == 'right':
            self.facing = 'right'
            self.image = self.images[3]
            if self.pos.x >= FARM_BOTTOMRIGHT[0]:
                return
            self.pos.x += TILE_SIZE
        if direction == 'up':
            self.facing = 'up'
            self.image = self.images[1]
            if self.pos.y <= FARM_TOPLEFT[1]:
                return
            self.pos.y -= TILE_SIZE
        if direction == 'down':
            self.facing = 'down'
            self.image = self.images[0]
            if self.pos.y >= FARM_BOTTOMRIGHT[1]:
                return
            self.pos.y += TILE_SIZE
        self.rect.topleft = self.pos

    def plant_seeds(self):
        plant_offset = None
        if self.facing == 'left':
            if self.pos.x <= FARM_TOPLEFT[0]:
                return
            plant_offset = pygame.Vector2(-TILE_SIZE,0)
        if self.facing == 'right':
            if self.pos.x >= FARM_BOTTOMRIGHT[0]:
                return
            plant_offset = pygame.Vector2(TILE_SIZE,0)
        if self.facing == 'up':
            if self.pos.y <= FARM_TOPLEFT[1]:
                return
            plant_offset = pygame.Vector2(0,-TILE_SIZE)
        if self.facing == 'down':
            if self.pos.y >= FARM_BOTTOMRIGHT[1]:
                return
            plant_offset = pygame.Vector2(0,TILE_SIZE)
            
        if plant_offset:
            plant_pos = self.pos + plant_offset
            self.plant_ability(plant_pos)

    def update(self,dt):
        pass

    def draw(self,surf,offset=0,alpha=1):
        #draw_rect = self.rect.move(-offset.x,-offset.y)
        draw_rect = self.rect
        surf.blit(self.image,draw_rect)