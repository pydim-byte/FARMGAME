import pygame
from ..globals import *
from ..objects.carrot import Carrot
from ..objects.wheat import Wheat
from ..objects.potatoe import Potatoe
from ..objects.watermelon import Watermelon
from ..objects.pumkin import Pumkin
from ..objects.melon import Melon

from ..tilemap_tools.get_images import get_images


def load_plants_data(plants_data, save_file, tilemap):
    for p in plants_data:
        plant_type = save_file[p]['type']
        plant_pos_x = save_file[p]['pos_x']
        plant_pos_y = save_file[p]['pos_y']
        plant_growth_cycle = save_file[p]['growth_cycle']
        plant_current_growth_time = save_file[p]['current_growth_time']

        plant_pos = pygame.Vector2(plant_pos_x,plant_pos_y)
        plant_images =  get_images(plant_type,3)
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
        tilemap.plants.add(plant)
        plant.growth_cycle = plant_growth_cycle
        plant.current_growth_time = plant_current_growth_time
        plant.image = plant.images[plant_growth_cycle]