import pygame
from ..globals import *
from ..objects.tile import Tile
from ..objects.player import Player
from ..objects.item_slot import ItemSlot
from ..objects.menu_pointer import MenuPointer
from ..objects.tutorial_text import TutorialText
from ..objects.shop_slot import ShopSlot
from ..objects.shop_money_box import ShopMoneyBox
from ..objects.shop_tutorial_text import ShopTutorialText
from .get_images import get_images
from .add_sprites import add_sprites
from .plant_seed import PlantSeed
from ..save_tools.load_saves import load_saves


def get_tiles(tilemap):
    for layer in tilemap.tmx_data.visible_layers:
        if hasattr(layer, 'data'):
            for x, y, img in layer.tiles():
                pos = pygame.Vector2(x*TILE_SIZE, y*TILE_SIZE)
                tilemap.visible_tiles.add(Tile(pos, img))
    tilemap.all_sprites.add(tilemap.visible_tiles, layer=0)

    if tilemap.map_name == 'farm' and SAVE_FILES['current']:
        load_saves(tilemap)
        return
    elif tilemap.map_name == 'farm' and not SAVE_FILES['current']:
        for slot in PLAYER_INVENTORY.values():
            slot['amount'] = 0
        for number,seed in enumerate(SEED_INVENTORY.values()):
            if number <= 2:
                seed['amount'] = 12
            else:
                seed['amount'] = 4
        PLAYER_MONEY['current'] = 100

    for obj in tilemap.tmx_data.objects:
        pos = pygame.Vector2(obj.x,obj.y)
        images = get_images(obj.properties['obj_type'],obj.properties['images_variation'])
        rect = pygame.rect.Rect(obj.x, obj.y, obj.width, obj.height)
        if obj.properties['obj_type'] == 'player':
            tilemap.player.add(Player(pos,images,PlantSeed(tilemap)))
        if obj.properties['obj_type'] == 'item_slot':
            tilemap.item_slots.add(ItemSlot(pos,images,obj.properties['slot_number']))
        if obj.properties['obj_type'] == 'menu_pointer':
            tilemap.menu_pointers.add(MenuPointer(pos,images,obj.properties['pointer_number']))
        if obj.properties['obj_type'] == 'tutorial_text':
            tilemap.tutorial_text.add(TutorialText(rect))
        if obj.properties['obj_type'] == 'shop_slot':
            tilemap.shop_slots.add(ShopSlot(pos,images,obj.properties['slot_number']))
        if obj.properties['obj_type'] == 'shop_money_box':
            tilemap.shop_money_box.add(ShopMoneyBox(rect))
        if obj.properties['obj_type'] == 'shop_tutorial_text':
            tilemap.shop_tutorial_text.add(ShopTutorialText(rect))

    add_sprites(tilemap.all_sprites, tilemap.plants, 1)
    add_sprites(tilemap.all_sprites, tilemap.player, 2)
    add_sprites(tilemap.all_sprites, tilemap.item_slots, 0)
    add_sprites(tilemap.all_sprites, tilemap.menu_pointers, 0)
    add_sprites(tilemap.all_sprites, tilemap.tutorial_text, 1)
    add_sprites(tilemap.all_sprites, tilemap.shop_slots, 0)
    add_sprites(tilemap.all_sprites, tilemap.shop_money_box, 1)
    add_sprites(tilemap.all_sprites, tilemap.shop_tutorial_text, 1)
