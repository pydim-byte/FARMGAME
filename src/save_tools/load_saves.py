import pygame
from ..globals import *
from .load_player_data import load_player_data
from .load_plants_data import load_plants_data
from .load_slots_data import load_slots_data
from .load_inventory_data import load_inventory_data
from .load_seeds_data import load_seeds_data
from ..tilemap_tools.add_sprites import add_sprites


def load_saves(tilemap):
    plants_data = []
    slots_data = []
    inventory_data = []
    seeds_data = []
    
    for obj in SAVE_FILES['current']:
        if obj.startswith('plant'):
            plants_data.append(obj)
        if obj.startswith('slot'):
            slots_data.append(obj)
        if obj.startswith('inventory'):
            inventory_data.append(obj)
        if obj.startswith('seed'):
            seeds_data.append(obj)
        
    load_player_data(SAVE_FILES['current'], tilemap)
    load_plants_data(plants_data, SAVE_FILES['current'], tilemap)
    load_slots_data(slots_data, SAVE_FILES['current'], tilemap)
    load_inventory_data(inventory_data, SAVE_FILES['current'])
    load_seeds_data(seeds_data, SAVE_FILES['current'])
    PLAYER_MONEY['current'] = SAVE_FILES['current']['money']

    add_sprites(tilemap.all_sprites, tilemap.plants, 1)
    add_sprites(tilemap.all_sprites, tilemap.player, 2)
    add_sprites(tilemap.all_sprites, tilemap.item_slots, 0)
