TILE_SIZE = 32
FARM_TOPLEFT = 32,64
FARM_BOTTOMRIGHT = 512,256

TUTORIAL_TOPLEFT = 64,64
TUTORIAL_BOTTOMRIGHT = 480,224

FONT_LIBRARY = {}

PLAYER_INVENTORY = {
    1 : {'amount' : 0},
    2 : {'amount' : 0},
    3 : {'amount' : 0},
    4 : {'amount' : 0},
    5 : {'amount' : 0},
    6 : {'amount' : 0},
}

SEED_INVENTORY = {
    1 : {'amount' : 12},
    2 : {'amount' : 12},
    3 : {'amount' : 12},
    4 : {'amount' : 4},
    5 : {'amount' : 4},
    6 : {'amount' : 4},
}

PRICE_LIST = {
    1 : {'money' : -10, 'product' : PLAYER_INVENTORY[1]['amount'], 'changes' : 4},
    2 : {'money' : -10, 'product' : PLAYER_INVENTORY[2]['amount'], 'changes' : 4},
    3 : {'money' : -10, 'product' : PLAYER_INVENTORY[3]['amount'], 'changes' : 4},
    4 : {'money' : -10, 'product' : PLAYER_INVENTORY[4]['amount'], 'changes' : 4},
    5 : {'money' : -10, 'product' : PLAYER_INVENTORY[5]['amount'], 'changes' : 4},
    6 : {'money' : -10, 'product' : PLAYER_INVENTORY[6]['amount'], 'changes' : 4},

    7 : {'money' : 4, 'product' : SEED_INVENTORY[1]['amount'], 'changes' : -4},
    8 : {'money' : 4, 'product' : SEED_INVENTORY[2]['amount'], 'changes' : -4},
    9 : {'money' : 4, 'product' : SEED_INVENTORY[3]['amount'], 'changes' : -4},
    10 : {'money' : 50, 'product' : SEED_INVENTORY[4]['amount'], 'changes' : -1},
    11 : {'money' : 50, 'product' : SEED_INVENTORY[5]['amount'], 'changes' : -1},
    12 : {'money' : 50, 'product' : SEED_INVENTORY[6]['amount'], 'changes' : -1},
}

PLAYER_MONEY = {'current' : 100}

GAME_STATES = {'current' : None, 'previous' : None}

SAVE_FILES = {'current' : None, 'tutorial' : None}