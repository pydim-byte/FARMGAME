import pygame
from ..globals import *
from ..objects.player import Player
from ..tilemap_tools.get_images import get_images
from ..tilemap_tools.plant_seed import PlantSeed


def load_player_data(save_file, tilemap):
    pos_x = save_file['player_1']['pos_x']
    pos_y = save_file['player_1']['pos_y']
    facing = save_file['player_1']['facing']
    player_image = save_file['player_1']['image']

    player_pos = pygame.Vector2(pos_x,pos_y)
    player_images = get_images('player',4)

    tilemap.player.add(Player(player_pos,player_images,PlantSeed(tilemap)))
    tilemap.player.sprite.facing = facing
    tilemap.player.sprite.image = player_images[player_image]