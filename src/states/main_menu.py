import pygame
from .state import State


class MainMenu(State):
    def __init__(self, tilemap):
        super().__init__(tilemap)
        self.tilemap = tilemap
        self.current_pointer = 0
        self.max_pointer = 1
        
    def handle_inputs(self, inputs):
        if inputs['up']:
            self.current_pointer -= 1
        if self.current_pointer < 0:
            self.current_pointer = 1
        if inputs['down']:
            self.current_pointer += 1
        if self.current_pointer > self.max_pointer:
            self.current_pointer = 0

        if inputs['space']:
            self.quit = True
            if self.current_pointer == 0:
                self.next_state = 'farm'
            if self.current_pointer == 1:
                self.next_state = 'tutorial'

    def update_pointers(self):
        for pointer in self.tilemap.menu_pointers:
            if pointer.pointer_num != self.current_pointer:
                pointer.active = False
                continue
            pointer.active = True

    def update(self, dt):
        self.update_pointers()

    def draw(self, surf):
        pass
    