import sys,os,pygame
from src.tilemap import Tilemap
from src.player_controller import PlayerController

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

        self.display = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
        self.screen = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.tilemap = Tilemap()
        self.player_controller = PlayerController(self.tilemap.player.sprite)
        self.inputs = {'left' : False, 'right' : False, 'up' : False, 'down' : False, 'space' : False}

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

    def handle_inputs(self):
        self.player_controller.handle_inputs(self.inputs)
        self.inputs = {'left' : False, 'right' : False, 'up' : False, 'down' : False, 'space' : False}

    def update(self,dt):
        self.tilemap.all_sprites.update(dt)

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
