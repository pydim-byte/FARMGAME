import pygame, json
import os.path
from .globals import *


def load_assets():
    pygame.mixer.music.load('assets/audio/fun.mp3')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer_music.play(-1)
    
    FONT_LIBRARY['tiny'] = pygame.font.Font('assets/fonts/micro5.ttf',10)
    FONT_LIBRARY['big'] = pygame.font.Font('assets/fonts/micro5.ttf',16)
    FONT_LIBRARY['huge'] = pygame.font.Font('assets/fonts/micro5.ttf',36)
    FONT_LIBRARY['medium'] = pygame.font.Font('assets/fonts/digital.ttf',22)

    if os.path.isfile('save_file.json'):
        with open('save_file.json') as file:
            SAVE_FILES['current'] = json.load(file)