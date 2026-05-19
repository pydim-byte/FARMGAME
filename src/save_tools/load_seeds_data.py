import pygame
from ..globals import *


def load_seeds_data(seeds_data, save_file):
    for s in seeds_data:
        SEED_INVENTORY[save_file[s]['slot_number']]['amount'] = save_file[s]['amount']