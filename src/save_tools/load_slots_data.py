import pygame
from ..globals import *
from ..objects.item_slot import ItemSlot
from ..tilemap_tools.get_images import get_images


def load_slots_data(slots_data, save_file, tilemap):
    for s in slots_data:
        slot_pos_x = save_file[s]['pos_x']
        slot_pos_y = save_file[s]['pos_y']
        slot_number = save_file[s]['slot_number']
        slot_active = save_file[s]['active']

        slot_pos = pygame.Vector2(slot_pos_x,slot_pos_y)
        slot_images =  get_images('item_slot',1)
        slot = ItemSlot(slot_pos,slot_images,slot_number)
        tilemap.item_slots.add(slot)
        slot.active = slot_active