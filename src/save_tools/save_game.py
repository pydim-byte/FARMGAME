import json
from ..globals import *


def save_game(tilemap):
    plants = {}
    for plant in tilemap.plants:
        plants[f'plant_{plant.pos.x}_{plant.pos.y}'] = {'type' : plant.type,
                                        'pos_x' : plant.pos.x,
                                        'pos_y' : plant.pos.y,
                                        'growth_cycle' : plant.growth_cycle,
                                        'current_growth_time' : plant.current_growth_time}

    player = {'player_1' : {'pos_x' : tilemap.player.sprite.pos.x,
                            'pos_y' : tilemap.player.sprite.pos.y,
                            'facing' : tilemap.player.sprite.facing}}
    if tilemap.player.sprite.facing == 'down':
        player['player_1']['image'] = 0
    if tilemap.player.sprite.facing == 'up':
        player['player_1']['image'] = 1
    if tilemap.player.sprite.facing == 'left':
        player['player_1']['image'] = 2
    if tilemap.player.sprite.facing == 'right':
        player['player_1']['image'] = 3

    item_slots = {}
    for slot in tilemap.item_slots:
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