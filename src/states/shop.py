import pygame,os,json
from .state import State
from .. globals import *


class Shop(State):
    def __init__(self, tilemap):
        super().__init__(tilemap)
        self.tilemap = tilemap
        
    def handle_inputs(self, inputs):
        if inputs['esc']:
            if GAME_STATES['previous'] == 'tutorial':
                self.quit = True
                self.next_state = 'main_menu'
            else:
                self.quit = True
                self.next_state = GAME_STATES['previous']
                self.save_game()

        if inputs['left']:
            acitve_slot = None
            for slot in self.tilemap.shop_slots:
                if slot.active:
                    acitve_slot = slot.slot_number
                slot.active = False

            acitve_slot -= 1
            if acitve_slot <= 0:
                acitve_slot = 12

            for slot in self.tilemap.shop_slots:
                if slot.slot_number == acitve_slot:
                    slot.active = True
                    break
            if GAME_STATES['previous'] == 'tutorial' and self.tilemap.shop_tutorial_text.sprite.msg_index == 0:
                self.tilemap.shop_tutorial_text.sprite.msg_index = 1
                
        if inputs['right']:
            acitve_slot = None
            for slot in self.tilemap.shop_slots:
                if slot.active:
                    acitve_slot = slot.slot_number
                slot.active = False

            acitve_slot += 1
            if acitve_slot >= 13:
                acitve_slot = 1

            for slot in self.tilemap.shop_slots:
                if slot.slot_number == acitve_slot:
                    slot.active = True
                    break
            if GAME_STATES['previous'] == 'tutorial' and self.tilemap.shop_tutorial_text.sprite.msg_index == 0:
                self.tilemap.shop_tutorial_text.sprite.msg_index = 1

        if inputs['space']:
            acitve_slot = None
            for slot in self.tilemap.shop_slots:
                if slot.active:
                    acitve_slot = slot.slot_number
                    if acitve_slot <= 6:
                        if PLAYER_MONEY['current'] >= -PRICE_LIST[acitve_slot]['money']:
                            SEED_INVENTORY[acitve_slot]['amount'] += PRICE_LIST[acitve_slot]['changes']
                            PLAYER_MONEY['current'] += PRICE_LIST[acitve_slot]['money']
                    else:
                        if PLAYER_INVENTORY[acitve_slot-6]['amount'] >= -PRICE_LIST[acitve_slot]['changes']:
                            PLAYER_INVENTORY[acitve_slot-6]['amount'] += PRICE_LIST[acitve_slot]['changes']
                            PLAYER_MONEY['current'] += PRICE_LIST[acitve_slot]['money']
                    if GAME_STATES['previous'] == 'tutorial' and self.tilemap.shop_tutorial_text.sprite.msg_index == 1:
                        self.tilemap.shop_tutorial_text.sprite.msg_index = 2

    def save_game(self):
        with open('save_file.json') as file:
            save_file = json.load(file)
        
        save_file['inventory_slot_1']['amount'] = PLAYER_INVENTORY[1]['amount']
        save_file['inventory_slot_2']['amount'] = PLAYER_INVENTORY[2]['amount']
        save_file['inventory_slot_3']['amount'] = PLAYER_INVENTORY[3]['amount']
        save_file['inventory_slot_4']['amount'] = PLAYER_INVENTORY[4]['amount']
        save_file['inventory_slot_5']['amount'] = PLAYER_INVENTORY[5]['amount']
        save_file['inventory_slot_6']['amount'] = PLAYER_INVENTORY[6]['amount']

        save_file['seed_slot_1']['amount'] = SEED_INVENTORY[1]['amount']
        save_file['seed_slot_2']['amount'] = SEED_INVENTORY[2]['amount']
        save_file['seed_slot_3']['amount'] = SEED_INVENTORY[3]['amount']
        save_file['seed_slot_4']['amount'] = SEED_INVENTORY[4]['amount']
        save_file['seed_slot_5']['amount'] = SEED_INVENTORY[5]['amount']
        save_file['seed_slot_6']['amount'] = SEED_INVENTORY[6]['amount']

        save_file['money'] = PLAYER_MONEY['current']

        SAVE_FILES['current'] = json.dumps(save_file)
        with open('save_file.json', 'w') as file:
            json.dump(save_file, file)
        with open('save_file.json') as file:
            SAVE_FILES['current'] = json.load(file)


    def update(self, dt):
        pass

    def draw(self, surf):
        pass
    