import sys,os,pygame,json
import os.path
from src.globals import *
from src.tilemap import Tilemap
from src.aseets_loader import load_assets
from src.state_manager import load_starting_state, flip_state
from src.save_tools.save_game import save_game
from src.player_controller import PlayerController
from src.inventory_controller import InventoryController

from src.states.farm import Farm
from src.states.main_menu import MainMenu
from src.states.tutorial import Tutorial
from src.states.shop import Shop


pygame.display.set_caption("FARMGAME")


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        load_assets()

        self.display = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
        self.screen = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.inputs = {pygame.K_LEFT : False, pygame.K_RIGHT : False, pygame.K_UP : False, pygame.K_DOWN : False, 
                       pygame.K_SPACE : False, pygame.K_ESCAPE : False, pygame.K_m : False, 
                       pygame.K_1 : False, pygame.K_2 : False, pygame.K_3 : False, pygame.K_4 : False, pygame.K_5 : False, pygame.K_6 : False,}

        self.tilemap, self.state = load_starting_state()

    def handle_events(self,event):
        if event.type == pygame.KEYDOWN:
            for inpput_key in self.inputs:
                if event.key == inpput_key:
                    self.inputs[inpput_key] = True

        if event.type == pygame.KEYUP:
            for inpput_key in self.inputs:
                if event.key == inpput_key:
                    self.inputs[inpput_key] = False

    def handle_inputs(self):
        self.state.handle_inputs(self.inputs)
        self.inputs = {k:False for k in self.inputs}

    def update(self,dt):
        if self.state.quit:
            self.state.done = True
            self.tilemap, self.state = flip_state(self.state.next_state)   
        self.state.update(dt)
        self.tilemap.all_sprites.update(dt)
        if GAME_STATES['current'] == 'farm':
            save_game(self.tilemap)

    def draw(self):
        self.display.fill('white')
        for sprite in self.tilemap.all_sprites:
            sprite.draw(self.screen)
        self.display.blit((pygame.transform.scale(self.screen, self.display.get_rect().size)),(0,0))
        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.handle_events(event)

            dt = self.clock.tick(FPS) / 1000
            dt = min(0.01,dt)
            self.handle_inputs()
            self.update(dt)
            self.draw()


game = Game()
game.run()
