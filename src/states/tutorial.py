import pygame
from ..globals import *
from .state import State
from src.player_controller import PlayerController
from src.inventory_controller import InventoryController


class Tutorial(State):
    def __init__(self, tilemap):
        super().__init__(tilemap)
        self.tilemap = tilemap
        self.player_controller = PlayerController(self.tilemap.player.sprite)
        self.inventory_controller = InventoryController(self.tilemap.item_slots)

        for slot in PLAYER_INVENTORY.values():
            slot['amount'] = 0

        for seed in SEED_INVENTORY.values():
            seed['amount'] = 12

        PLAYER_MONEY['current'] = 100
    
    def handle_inputs(self, inputs):
        self.inventory_controller.handle_inputs(inputs)
        self.player_controller.handle_inputs(inputs)

        if (inputs[pygame.K_1] or inputs[pygame.K_2] or inputs[pygame.K_3]) and self.tilemap.tutorial_text.sprite.msg_index == 0:
            self.tilemap.tutorial_text.sprite.msg_index = 1

        if inputs[pygame.K_SPACE] and self.tilemap.plants and self.tilemap.tutorial_text.sprite.msg_index == 1:
             self.tilemap.tutorial_text.sprite.msg_index = 2

        if self.tilemap.tutorial_text.sprite.msg_index == 2:
            for plant in self.tilemap.plants:
                if plant.growth_cycle == 2:
                    self.tilemap.tutorial_text.sprite.msg_index = 3
                    break

        if self.tilemap.tutorial_text.sprite.msg_index == 3:
            for slot in PLAYER_INVENTORY.values():
                if slot['amount'] > 0:
                    self.tilemap.tutorial_text.sprite.msg_index = 4

        if inputs[pygame.K_ESCAPE]:
            self.quit = True
            self.next_state = 'main_menu'

        if inputs[pygame.K_m]:
            self.quit = True
            self.next_state = 'shop' 

    def update(self, dt):
        pass

    def draw(self, surf):
        pass
    