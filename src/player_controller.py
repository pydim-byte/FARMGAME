import pygame

class PlayerController:
    def __init__(self,player):
        self.player = player

    def handle_inputs(self,inputs):
        move_direction = None
        if inputs[pygame.K_LEFT]:
            move_direction = 'LEFT'
        if inputs[pygame.K_RIGHT]:
            move_direction = 'RIGHT'
        if inputs[pygame.K_UP]:
            move_direction = 'UP'
        if inputs[pygame.K_DOWN]:
            move_direction = 'DOWN'
        if move_direction:
            self.player.move(move_direction)

        if inputs[pygame.K_SPACE]:
            self.player.plant_seeds()