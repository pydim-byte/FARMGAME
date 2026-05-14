import pygame
from pytmx import load_pygame
from .globals import *
from .objects.tile import Tile
from .objects.player import Player
from .objects.carrot import Carrot
from .objects.wheat import Wheat
from .objects.potatoe import Potatoe
from .objects.watermelon import Watermelon
from .objects.pumkin import Pumkin
from .objects.melon import Melon
from .objects.item_slot import ItemSlot
from .objects.menu_pointer import MenuPointer
from .objects.tutorial_text import TutorialText
from .objects.shop_slot import ShopSlot
from .objects.shop_money_box import ShopMoneyBox
from .objects.shop_tutorial_text import ShopTutorialText

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
        self.shop_money_box = pygame.sprite.GroupSingle()
        self.shop_slots = pygame.sprite.Group()
        self.shop_tutorial_text = pygame.sprite.GroupSingle()
        self.get_tiles()

    def harvest_plant(self,plant):
        plant.kill()
        if plant.type == 'carrot':
            PLAYER_INVENTORY[1]['amount'] += 4
        if plant.type == 'wheat':
            PLAYER_INVENTORY[2]['amount'] += 4
        if plant.type == 'potatoe':
            PLAYER_INVENTORY[3]['amount'] += 4
        if plant.type == 'watermelon':
            PLAYER_INVENTORY[4]['amount'] += 1
        if plant.type == 'pumkin':
            PLAYER_INVENTORY[5]['amount'] += 1
        if plant.type == 'melon':
            PLAYER_INVENTORY[6]['amount'] += 1

    def plant_seed(self,pos):
        for p in self.plants:
            if p.pos != pos:
                continue
            if p.growth_cycle == 2:
                self.harvest_plant(p)
            return
        
        active_seeds = 0
        plant = None
        for slot in self.item_slots:
            if slot.active:
                active_seeds = slot.slot_number
        
        if active_seeds == 1 and SEED_INVENTORY[active_seeds]['amount'] >= 4:
            img = self.get_images('carrot',3)
            plant = Carrot(pos,img)
            SEED_INVENTORY[active_seeds]['amount'] -= 4
        if active_seeds == 2 and SEED_INVENTORY[active_seeds]['amount'] >= 4:
            img = self.get_images('wheat',3)
            plant = Wheat(pos,img)
            SEED_INVENTORY[active_seeds]['amount'] -= 4
        if active_seeds == 3 and SEED_INVENTORY[active_seeds]['amount'] >= 4:
            img = self.get_images('potatoe',3)
            plant = Potatoe(pos,img)
            SEED_INVENTORY[active_seeds]['amount'] -= 4
        if active_seeds == 4 and SEED_INVENTORY[active_seeds]['amount'] >= 1:
            img = self.get_images('watermelon',3)
            plant = Watermelon(pos,img)
            SEED_INVENTORY[active_seeds]['amount'] -= 1
        if active_seeds == 5 and SEED_INVENTORY[active_seeds]['amount'] >= 1:
            img = self.get_images('pumkin',3)
            plant = Pumkin(pos,img)
            SEED_INVENTORY[active_seeds]['amount'] -= 1
        if active_seeds == 6 and SEED_INVENTORY[active_seeds]['amount'] >= 1:
            img = self.get_images('melon',3)
            plant = Melon(pos,img)
            SEED_INVENTORY[active_seeds]['amount'] -= 1

        if active_seeds != 0 and plant != None:
            self.plants.add(plant)
            self.all_sprites.add(plant, layer=1)

    def load_player_data(self,save_file):
        pos_x = save_file['player_1']['pos_x']
        pos_y = save_file['player_1']['pos_y']
        facing = save_file['player_1']['facing']
        player_image = save_file['player_1']['image']

        player_pos = pygame.Vector2(pos_x,pos_y)
        player_images = self.get_images('player',4)

        self.player.add(Player(player_pos,player_images,self.plant_seed))
        self.player.sprite.facing = facing
        self.player.sprite.image = player_images[player_image]

    def load_plants_data(self,plants_data,save_file):
        for p in plants_data:
            plant_type = save_file[p]['type']
            plant_pos_x = save_file[p]['pos_x']
            plant_pos_y = save_file[p]['pos_y']
            plant_growth_cycle = save_file[p]['growth_cycle']
            plant_current_growth_time = save_file[p]['current_growth_time']

            plant_pos = pygame.Vector2(plant_pos_x,plant_pos_y)
            plant_images =  self.get_images(plant_type,3)
            if plant_type == 'carrot':
                plant = Carrot(plant_pos,plant_images)
            if plant_type == 'wheat':
                plant = Wheat(plant_pos,plant_images)
            if plant_type == 'potatoe':
                plant = Potatoe(plant_pos,plant_images)
            if plant_type == 'watermelon':
                plant = Watermelon(plant_pos,plant_images)
            if plant_type == 'pumkin':
                plant = Pumkin(plant_pos,plant_images)
            if plant_type == 'melon':
                plant = Melon(plant_pos,plant_images)
            self.plants.add(plant)
            plant.growth_cycle = plant_growth_cycle
            plant.current_growth_time = plant_current_growth_time
            plant.image = plant.images[plant_growth_cycle]

    def load_slots_data(self,slots_data,save_file):
        for s in slots_data:
            slot_pos_x = save_file[s]['pos_x']
            slot_pos_y = save_file[s]['pos_y']
            slot_number = save_file[s]['slot_number']
            slot_active = save_file[s]['active']

            slot_pos = pygame.Vector2(slot_pos_x,slot_pos_y)
            slot_images =  self.get_images('item_slot',1)
            slot = ItemSlot(slot_pos,slot_images,slot_number)
            self.item_slots.add(slot)
            slot.active = slot_active

    def load_inventory_data(self,inventory_data,save_file):
        for i in inventory_data:
            PLAYER_INVENTORY[save_file[i]['slot_number']]['amount'] = save_file[i]['amount']

    def load_seeds_data(self,seeds_data,save_file):
        for s in seeds_data:
            SEED_INVENTORY[save_file[s]['slot_number']]['amount'] = save_file[s]['amount']

    def load_saves(self,save_file):
        plants_data = []
        slots_data = []
        inventory_data = []
        seeds_data = []
        for obj in save_file:
            if obj.startswith('plant'):
                plants_data.append(obj)
            if obj.startswith('slot'):
                slots_data.append(obj)
            if obj.startswith('inventory'):
                inventory_data.append(obj)
            if obj.startswith('seed'):
                seeds_data.append(obj)
            
        
        self.load_player_data(save_file)
        self.load_plants_data(plants_data,save_file)
        self.load_slots_data(slots_data,save_file)
        self.load_inventory_data(inventory_data,save_file)
        self.load_seeds_data(seeds_data,save_file)
        PLAYER_MONEY['current'] = save_file['money']

        self.add_sprites(self.plants, 1)
        self.add_sprites(self.player.sprite, 2)
        self.add_sprites(self.item_slots, 0)

    def get_tiles(self):
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer, 'data'):
                for x, y, img in layer.tiles():
                    pos = pygame.Vector2(x*TILE_SIZE, y*TILE_SIZE)
                    self.visible_tiles.add(Tile(pos, img))

        self.all_sprites.add(self.visible_tiles, layer=0)

        if self.map_name == 'farm' and SAVE_FILES['current']:
            self.load_saves(SAVE_FILES['current'])
            return
        elif self.map_name == 'farm' and not SAVE_FILES['current']:
            for slot in PLAYER_INVENTORY.values():
                slot['amount'] = 0

            for number,seed in enumerate(SEED_INVENTORY.values()):
                if number <= 2:
                    seed['amount'] = 12
                else:
                    seed['amount'] = 4

            PLAYER_MONEY['current'] = 100

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
            if obj.properties['obj_type'] == 'shop_slot':
                self.shop_slots.add(ShopSlot(pos,images,obj.properties['slot_number']))
            if obj.properties['obj_type'] == 'shop_money_box':
                rect = pygame.rect.Rect(obj.x, obj.y, obj.width, obj.height)
                self.shop_money_box.add(ShopMoneyBox(rect))
            if obj.properties['obj_type'] == 'shop_tutorial_text':
                rect = pygame.rect.Rect(obj.x, obj.y, obj.width, obj.height)
                self.shop_tutorial_text.add(ShopTutorialText(rect))

        self.add_sprites(self.plants, 1)
        self.add_sprites(self.player.sprite, 2)
        self.add_sprites(self.item_slots, 0)
        self.add_sprites(self.menu_pointers, 0)
        self.add_sprites(self.tutorial_text, 1)
        self.add_sprites(self.shop_slots, 0)
        self.add_sprites(self.shop_money_box, 1)
        self.add_sprites(self.shop_tutorial_text, 1)

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


