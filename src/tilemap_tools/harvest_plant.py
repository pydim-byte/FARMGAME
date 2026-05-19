import pygame
from ..globals import *


harvest_reference = {
    'carrot' : {'inventory_slot' :  PLAYER_INVENTORY[1], 'harvest_amount' : 4},
    'wheat' : {'inventory_slot' : PLAYER_INVENTORY[2], 'harvest_amount' : 4},
    'potatoe' : {'inventory_slot' : PLAYER_INVENTORY[3], 'harvest_amount' : 4},
    'watermelon' : {'inventory_slot' : PLAYER_INVENTORY[4], 'harvest_amount' : 1},
    'pumkin' : {'inventory_slot' : PLAYER_INVENTORY[5], 'harvest_amount' : 1},
    'melon' : {'inventory_slot' : PLAYER_INVENTORY[6], 'harvest_amount' : 1},
}

def harvest_plant(plant):
    plant.kill()
    harvest_reference[plant.type]['inventory_slot']['amount'] += harvest_reference[plant.type]['harvest_amount']
