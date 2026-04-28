import pygame
from pytmx import load_pygame
from .globals import *
from .objects.tile import Tile
from .objects.player import Player
from .objects.plant import Plant
from .objects.item_slot import ItemSlot

class Tilemap:
    def __init__(self):
        self.tilemap_path = f'assets/tilemap/tilemap.tmx'
        self.tmx_data = load_pygame(self.tilemap_path)
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.visible_tiles = pygame.sprite.Group()
        self.plants = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.item_slots = pygame.sprite.Group()
        self.get_tiles()

    def get_tiles(self):
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer, 'data'):
                for x, y, img in layer.tiles():
                    pos = pygame.Vector2(x*TILE_SIZE, y*TILE_SIZE)
                    self.visible_tiles.add(Tile(pos, img))

        for obj in self.tmx_data.objects:
            pos = pygame.Vector2(obj.x,obj.y)
            images = self.get_images(obj.properties['obj_type'],obj.properties['images_variation'])
            if obj.properties['obj_type'] == 'player':
                self.player.add(Player(pos,images,self.plant_seed))
            if obj.properties['obj_type'] == 'item_slot':
                self.item_slots.add(ItemSlot(pos,images,obj.properties['slot_number']))

        self.all_sprites.add(self.visible_tiles, layer=0)
        self.all_sprites.add(self.plants, layer=1)
        self.all_sprites.add(self.player.sprite, layer=2)
        self.all_sprites.add(self.item_slots, layer=3)

    def harvest_plant(self,plant):
        plant.kill()
        PLAYER_INVENTORY['carrots'] += 4

    def plant_seed(self,pos):
        for p in self.plants:
            if p.pos != pos:
                continue
            if p.growth_cycle == 2:
                self.harvest_plant(p)
            return
        img = self.get_images('plant',3)
        plant = Plant(pos,img)
        self.plants.add(plant)
        self.all_sprites.add(plant, layer=1)

    def get_images(self,name,count):
        images = []
        for i in range(count):
            img = pygame.image.load(f'assets/images/{name}/{i}.png').convert_alpha()
            images.append(img)
        return images 


