import pygame
from ..globals import *
from ..objects.carrot import Carrot
from ..objects.wheat import Wheat
from ..objects.potatoe import Potatoe
from ..objects.watermelon import Watermelon
from ..objects.pumkin import Pumkin
from ..objects.melon import Melon
from ..tilemap_tools.get_images import get_images
from ..tilemap_tools.harvest_plant import harvest_plant


plant_references = {
    1 : {'plant_class' : Carrot, 'plant_name' : 'carrot', 'seed_slot' :  SEED_INVENTORY[1], 'plant_amount' : 4},
    2 : {'plant_class' : Wheat, 'plant_name' : 'wheat', 'seed_slot' : SEED_INVENTORY[2], 'plant_amount' : 4},
    3 : {'plant_class' : Potatoe, 'plant_name' : 'potatoe', 'seed_slot' : SEED_INVENTORY[3], 'plant_amount' : 4},
    4 : {'plant_class' : Watermelon, 'plant_name' : 'watermelon', 'seed_slot' : SEED_INVENTORY[4], 'plant_amount' : 1},
    5 : {'plant_class' : Pumkin, 'plant_name' : 'pumlin', 'seed_slot' : SEED_INVENTORY[5], 'plant_amount' : 1},
    6 : {'plant_class' : Melon, 'plant_name' : 'melon', 'seed_slot' : SEED_INVENTORY[6], 'plant_amount' : 1},
}


class PlantSeed:
    def __init__(self,tilemap):
        self.tilemap = tilemap

    def __call__(self, pos):
        for p in self.tilemap.plants:
            if p.pos != pos:
                continue
            if p.growth_cycle == 2:
                harvest_plant(p)
            return
        
        active_seeds = None
        plant = None
        for slot in self.tilemap.item_slots:
            if slot.active:
                active_seeds = slot.slot_number
        
        if active_seeds != None and plant_references[active_seeds]['seed_slot']['amount'] >= plant_references[active_seeds]['plant_amount']:
            img = get_images(plant_references[active_seeds]['plant_name'],3)
            plant = plant_references[active_seeds]['plant_class'](pos, img)
            plant_references[active_seeds]['seed_slot']['amount'] -= plant_references[active_seeds]['plant_amount']
            self.tilemap.plants.add(plant)
            self.tilemap.all_sprites.add(plant, layer=1)