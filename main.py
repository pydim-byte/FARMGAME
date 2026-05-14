import sys,os,pygame,json
import os.path
from src.globals import *
from src.tilemap import Tilemap
from src.player_controller import PlayerController
from src.inventory_controller import InventoryController

from src.states.farm import Farm
from src.states.main_menu import MainMenu
from src.states.tutorial import Tutorial
from src.states.shop import Shop

DISPLAY_WIDTH, DISPLAY_HEIGHT = 1152, 640
SCREEN_WIDTH, SCREEN_HEIGHT = 576, 320
FPS = 60
pygame.display.set_caption("FARMGAME")

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        pygame.mixer.music.load('assets/audio/fun.mp3')
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer_music.play(-1)
        
        FONT_LIBRARY['tiny'] = pygame.font.Font('assets/fonts/micro5.ttf',10)
        FONT_LIBRARY['big'] = pygame.font.Font('assets/fonts/micro5.ttf',16)
        FONT_LIBRARY['huge'] = pygame.font.Font('assets/fonts/micro5.ttf',36)

        FONT_LIBRARY['medium'] = pygame.font.Font('assets/fonts/digital.ttf',22)

        self.display = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
        self.screen = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.states = {'main_menu' : MainMenu,
                       'tutorial' : Tutorial,
                        'farm' : Farm,
                        'shop' : Shop}

        if os.path.isfile('save_file.json'):
            with open('save_file.json') as file:
                SAVE_FILES['current'] = json.load(file)

        self.tilemap = Tilemap('main_menu')
        self.state_name = 'main_menu'
        self.state = self.states[self.state_name](self.tilemap)
        GAME_STATES['current'] = self.state_name

        self.inputs = {'left' : False, 'right' : False, 'up' : False, 'down' : False, 
                       'space' : False, 'esc' : False, 'm' : False, 
                       '1' : False, '2' : False, '3' : False, '4' : False, '5' : False, '6' : False,}

    def handle_events(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.inputs['left'] = True
            if event.key == pygame.K_RIGHT:
                self.inputs['right'] = True
            if event.key == pygame.K_UP:
                self.inputs['up'] = True
            if event.key == pygame.K_DOWN:
                self.inputs['down'] = True
            if event.key == pygame.K_SPACE:
                self.inputs['space'] = True
            if event.key == pygame.K_ESCAPE:
                self.inputs['esc'] = True
            if event.key == pygame.K_m:
                self.inputs['m'] = True
            if event.key == pygame.K_1:
                self.inputs['1'] = True
            if event.key == pygame.K_2:
                self.inputs['2'] = True
            if event.key == pygame.K_3:
                self.inputs['3'] = True
            if event.key == pygame.K_4:
                self.inputs['4'] = True
            if event.key == pygame.K_5:
                self.inputs['5'] = True
            if event.key == pygame.K_6:
                self.inputs['6'] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.inputs['left'] = False
            if event.key == pygame.K_RIGHT:
                self.inputs['right'] = False
            if event.key == pygame.K_DOWN:
                self.inputs['down'] = False
            if event.key == pygame.K_UP:
                self.inputs['up'] = False
            if event.key == pygame.K_SPACE:
                self.inputs['space'] = False
            if event.key == pygame.K_ESCAPE:
                self.inputs['esc'] = False
            if event.key == pygame.K_m:
                self.inputs['m'] = False
            if event.key == pygame.K_1:
                self.inputs['1'] = False
            if event.key == pygame.K_2:
                self.inputs['2'] = False
            if event.key == pygame.K_3:
                self.inputs['3'] = False
            if event.key == pygame.K_4:
                self.inputs['4'] = False
            if event.key == pygame.K_5:
                self.inputs['5'] = False
            if event.key == pygame.K_6:
                self.inputs['6'] = False

    def handle_inputs(self):
        self.state.handle_inputs(self.inputs)
        self.inputs = {'left' : False, 'right' : False, 'up' : False, 'down' : False, 
                       'space' : False, 'esc' : False, 'm' : False, 
                       '1' : False, '2' : False, '3' : False, '4' : False, '5' : False, '6' : False,}

    def flip_state(self):
        current_state = self.state_name
        next_state = self.state.next_state
        self.state.done = False
        self.tilemap = Tilemap(next_state)
        self.state = self.states[next_state](self.tilemap)
        GAME_STATES['previous'] = current_state
        GAME_STATES['current'] = next_state
        self.state_name = next_state

    def save_game(self):
        plants = {}
        for plant in self.tilemap.plants:
            plants[f'plant_{plant.pos.x}_{plant.pos.y}'] = {'type' : plant.type,
                                           'pos_x' : plant.pos.x,
                                           'pos_y' : plant.pos.y,
                                           'growth_cycle' : plant.growth_cycle,
                                           'current_growth_time' : plant.current_growth_time}

        player = {'player_1' : {'pos_x' : self.tilemap.player.sprite.pos.x,
                                'pos_y' : self.tilemap.player.sprite.pos.y,
                                'facing' : self.tilemap.player.sprite.facing}}
        if self.tilemap.player.sprite.facing == 'down':
            player['player_1']['image'] = 0
        if self.tilemap.player.sprite.facing == 'up':
            player['player_1']['image'] = 1
        if self.tilemap.player.sprite.facing == 'left':
            player['player_1']['image'] = 2
        if self.tilemap.player.sprite.facing == 'right':
            player['player_1']['image'] = 3

        item_slots = {}
        for slot in self.tilemap.item_slots:
            item_slots[f'slot_{slot.slot_number}'] = {'pos_x' : slot.pos.x, 
                                                      'pos_y' : slot.pos.y, 
                                                      'slot_number' : slot.slot_number, 
                                                      'active' : slot.active}

        inventory = {'inventory_slot_1' : {'slot_number' : 1, 'amount' : PLAYER_INVENTORY[1]['amount']},
                     'inventory_slot_2' : {'slot_number' : 2, 'amount' : PLAYER_INVENTORY[2]['amount']},
                     'inventory_slot_3' : {'slot_number' : 3, 'amount' : PLAYER_INVENTORY[3]['amount']},
                     'inventory_slot_4' : {'slot_number' : 4, 'amount' : PLAYER_INVENTORY[4]['amount']},
                     'inventory_slot_5' : {'slot_number' : 5, 'amount' : PLAYER_INVENTORY[5]['amount']},
                     'inventory_slot_6' : {'slot_number' : 6, 'amount' : PLAYER_INVENTORY[6]['amount']},}
        
        seeds_inventory = {'seed_slot_1' : {'slot_number' : 1, 'amount' : SEED_INVENTORY[1]['amount']},
                           'seed_slot_2' : {'slot_number' : 2, 'amount' : SEED_INVENTORY[2]['amount']},
                           'seed_slot_3' : {'slot_number' : 3, 'amount' : SEED_INVENTORY[3]['amount']},
                           'seed_slot_4' : {'slot_number' : 4, 'amount' : SEED_INVENTORY[4]['amount']},
                           'seed_slot_5' : {'slot_number' : 5, 'amount' : SEED_INVENTORY[5]['amount']},
                           'seed_slot_6' : {'slot_number' : 6, 'amount' : SEED_INVENTORY[6]['amount']},}

        player_money = {'money' : PLAYER_MONEY['current']}

        saved_objets = {}
        saved_objets.update(plants)
        saved_objets.update(player)
        saved_objets.update(item_slots)
        saved_objets.update(inventory)
        saved_objets.update(seeds_inventory)
        saved_objets.update(player_money)
        with open('save_file.json', 'w') as file:
            json.dump(saved_objets, file)
        with open('save_file.json') as file:
            SAVE_FILES['current'] = json.load(file)

    def update(self,dt):
        if self.state.quit:
            self.state.done = True
            self.flip_state()   
        self.state.update(dt)
        self.tilemap.all_sprites.update(dt)
        if GAME_STATES['current'] == 'farm':
            self.save_game()

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
