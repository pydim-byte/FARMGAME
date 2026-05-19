import pygame
from .globals import *
from .tilemap import Tilemap
from .states.farm import Farm
from .states.main_menu import MainMenu
from .states.tutorial import Tutorial
from .states.shop import Shop


states_reference = {'main_menu' : MainMenu,
                    'tutorial' : Tutorial,
                    'farm' : Farm,
                    'shop' : Shop}


def load_starting_state():
    tilemap = Tilemap('main_menu')
    state = states_reference['main_menu'](tilemap)
    GAME_STATES['current'] = 'main_menu'
    return tilemap, state


def flip_state(next_state):
    current_state = GAME_STATES['current']
    tilemap = Tilemap(next_state)
    state = states_reference[next_state](tilemap)
    GAME_STATES['previous'] = current_state
    GAME_STATES['current'] = next_state
    return tilemap, state
