import pygame

class PlayerController:
    def __init__(self,player):
        self.player = player

    def handle_inputs(self,inputs):
        move_direction = None
        if inputs['left']:
            move_direction = 'left'
        if inputs['right']:
            move_direction = 'right'
        if inputs['up']:
            move_direction = 'up'
        if inputs['down']:
            move_direction = 'down'
        if move_direction:
            self.player.move(move_direction)

        if inputs['space']:
            self.player.plant_seeds()