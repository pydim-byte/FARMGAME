import pygame
from pytmx import load_pygame
from .globals import *
from .objects.tile import Tile
from .objects.player import Player
from .objects.carrot import Carrot
from .objects.wheat import Wheat
from .objects.potatoe import Potatoe
from .objects.item_slot import ItemSlot
from .objects.menu_pointer import MenuPointer
from .objects.tutorial_text import TutorialText

class Tilemap:
    def __init__(self,map_name):
        self.map_name = map_name
        self.tilemap_path = f'assets/tilemap/{self.map_name}.tmx'
        self.tmx_data = load_pygame(self.tilemap_path)
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.visible_tiles = pygame.sprite.Group()
        self.plants = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.item_slots = pygame.sprite.Group()
        self.menu_pointers = pygame.sprite.Group()
        self.tutorial_text = pygame.sprite.GroupSingle()
        self.get_tiles()

    def harvest_plant(self,plant):
        plant.kill()
        if plant.type == 'carrot':
            PLAYER_INVENTORY[1]['amount'] += 4
        if plant.type == 'wheat':
            PLAYER_INVENTORY[2]['amount'] += 4
        if plant.type == 'potatoe':
            PLAYER_INVENTORY[3]['amount'] += 4

    def plant_seed(self,pos):
        for p in self.plants:
            if p.pos != pos:
                continue
            if p.growth_cycle == 2:
                self.harvest_plant(p)
            return
        
        active_seeds = 0
        for slot in self.item_slots:
            if slot.active:
                active_seeds = slot.slot_number
        
        if active_seeds == 1:
            img = self.get_images('carrot',3)
            plant = Carrot(pos,img)
        if active_seeds == 2:
            img = self.get_images('wheat',3)
            plant = Wheat(pos,img)
        if active_seeds == 3:
            img = self.get_images('potatoe',3)
            plant = Potatoe(pos,img)

        if active_seeds != 0:
            self.plants.add(plant)
            self.all_sprites.add(plant, layer=1)

    def load_player_data(self):
        pos_x = SAVE_FILES['current']['player_1']['pos_x']
        pos_y = SAVE_FILES['current']['player_1']['pos_y']
        facing = SAVE_FILES['current']['player_1']['facing']
        player_image = SAVE_FILES['current']['player_1']['image']

        player_pos = pygame.Vector2(pos_x,pos_y)
        player_images = self.get_images('player',4)

        self.player.add(Player(player_pos,player_images,self.plant_seed))
        self.player.sprite.facing = facing
        self.player.sprite.image = player_images[player_image]

    def load_plants_data(self,plants_data):
        for p in plants_data:
            plant_type = SAVE_FILES['current'][p]['type']
            plant_pos_x = SAVE_FILES['current'][p]['pos_x']
            plant_pos_y = SAVE_FILES['current'][p]['pos_y']
            plant_growth_cycle = SAVE_FILES['current'][p]['growth_cycle']
            plant_current_growth_time = SAVE_FILES['current'][p]['current_growth_time']

            plant_pos = pygame.Vector2(plant_pos_x,plant_pos_y)
            plant_images =  self.get_images(plant_type,3)
            if plant_type == 'carrot':
                plant = Carrot(plant_pos,plant_images)
            if plant_type == 'wheat':
                plant = Wheat(plant_pos,plant_images)
            if plant_type == 'potatoe':
                plant = Potatoe(plant_pos,plant_images)
            self.plants.add(plant)
            plant.growth_cycle = plant_growth_cycle
            plant.current_growth_time = plant_current_growth_time
            plant.image = plant.images[plant_growth_cycle]

    def load_slots_data(self,slots_data):
        for s in slots_data:
            slot_pos_x = SAVE_FILES['current'][s]['pos_x']
            slot_pos_y = SAVE_FILES['current'][s]['pos_y']
            slot_number = SAVE_FILES['current'][s]['slot_number']
            slot_active = SAVE_FILES['current'][s]['active']

            slot_pos = pygame.Vector2(slot_pos_x,slot_pos_y)
            slot_images =  self.get_images('item_slot',1)
            slot = ItemSlot(slot_pos,slot_images,slot_number)
            self.item_slots.add(slot)
            slot.active = slot_active

    def load_inventory_data(self,inventory_data):
        for i in inventory_data:
            PLAYER_INVENTORY[SAVE_FILES['current'][i]['slot_number']]['amount'] = SAVE_FILES['current'][i]['amount']

    def load_saves(self):
        plants_data = []
        slots_data = []
        inventory_data = []
        for obj in SAVE_FILES['current']:
            if obj.startswith('plant'):
                plants_data.append(obj)
            if obj.startswith('slot'):
                slots_data.append(obj)
            if obj.startswith('inventory'):
                inventory_data.append(obj)
        
        self.load_player_data()
        self.load_plants_data(plants_data)
        self.load_slots_data(slots_data)
        self.load_inventory_data(inventory_data)

        self.add_sprites(self.plants, 1)
        self.add_sprites(self.player.sprite, 2)
        self.add_sprites(self.item_slots, 0)

        print(self.plants)


    def get_tiles(self):
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer, 'data'):
                for x, y, img in layer.tiles():
                    pos = pygame.Vector2(x*TILE_SIZE, y*TILE_SIZE)
                    self.visible_tiles.add(Tile(pos, img))

        self.all_sprites.add(self.visible_tiles, layer=0)

        if self.map_name == 'farm' and SAVE_FILES['current']:
            self.load_saves()
            return

        for obj in self.tmx_data.objects:
            pos = pygame.Vector2(obj.x,obj.y)
            images = self.get_images(obj.properties['obj_type'],obj.properties['images_variation'])
            if obj.properties['obj_type'] == 'player':
                self.player.add(Player(pos,images,self.plant_seed))
            if obj.properties['obj_type'] == 'item_slot':
                self.item_slots.add(ItemSlot(pos,images,obj.properties['slot_number']))
            if obj.properties['obj_type'] == 'menu_pointer':
                self.menu_pointers.add(MenuPointer(pos,images,obj.properties['pointer_number']))
            if obj.properties['obj_type'] == 'tutorial_text':
                rect = pygame.rect.Rect(obj.x, obj.y, obj.width, obj.height)
                self.tutorial_text.add(TutorialText(rect))

        self.add_sprites(self.plants, 1)
        self.add_sprites(self.player.sprite, 2)
        self.add_sprites(self.item_slots, 0)
        self.add_sprites(self.menu_pointers, 0)
        self.add_sprites(self.tutorial_text, 1)

    def add_sprites(self,sprites,layer_num):
        if sprites == None:
            return
        self.all_sprites.add(sprites,layer=layer_num)

    def get_images(self,name,count):
        images = []
        for i in range(count):
            img = pygame.image.load(f'assets/images/{name}/{i}.png').convert_alpha()
            images.append(img)
        return images 


