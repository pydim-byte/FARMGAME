import pygame
from pytmx import load_pygame
from .globals import *
from .objects.tile import Tile
from .objects.player import Player
from .objects.carrot import Carrot
from .objects.wheat import Wheat
from .objects.potatoe import Potatoe
from .objects.watermelon import Watermelon
from .objects.pumkin import Pumkin
from .objects.melon import Melon
from .objects.item_slot import ItemSlot
from .objects.menu_pointer import MenuPointer
from .objects.tutorial_text import TutorialText
from .objects.shop_slot import ShopSlot
from .objects.shop_money_box import ShopMoneyBox
from .objects.shop_tutorial_text import ShopTutorialText
from .tilemap_tools.get_tiles import get_tiles 


class Tilemap:
    def __init__(self,map_name):
        self.map_name = map_name
        self.tilemap_path = f'assets/tilemap/{self.map_name}.tmx'
        self.tmx_data = load_pygame(self.tilemap_path)
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.visible_tiles = pygame.sprite.Group()
        self.plants = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.item_slots = pygame.sprite.Group()
        self.menu_pointers = pygame.sprite.Group()
        self.tutorial_text = pygame.sprite.GroupSingle()
        self.shop_money_box = pygame.sprite.GroupSingle()
        self.shop_slots = pygame.sprite.Group()
        self.shop_tutorial_text = pygame.sprite.GroupSingle()
        get_tiles(self)
