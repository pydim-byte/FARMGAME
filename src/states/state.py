import pygame


class State():
    def __init__(self,tilemap):
        self.done = False
        self.quit = False
        self.next_state = None
        
    def startup(self):
        pass 
    
    def handle_inputs(self,inputs):
        pass

    def update(self,dt):
        pass

    def draw(self, surf):
        pass