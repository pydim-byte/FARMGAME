import pygame
from ..globals import *


def load_inventory_data(inventory_data,save_file):
    for i in inventory_data:
        PLAYER_INVENTORY[save_file[i]['slot_number']]['amount'] = save_file[i]['amount']