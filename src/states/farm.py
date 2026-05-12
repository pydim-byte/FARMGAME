import pygame
from .state import State
from src.player_controller import PlayerController
from src.inventory_controller import InventoryController


class Farm(State):
    def __init__(self, tilemap):
        super().__init__(tilemap)
        self.tilemap = tilemap
        self.player_controller = PlayerController(self.tilemap.player.sprite)
        self.inventory_controller = InventoryController(self.tilemap.item_slots)
    
    def handle_inputs(self, inputs):
        self.inventory_controller.handle_inputs(inputs)
        self.player_controller.handle_inputs(inputs)

    def update(self, dt):
        pass

    def draw(self, surf):
        pass
    