import pygame

class InventoryController:
    def __init__(self,inventory):
        self.inventory = inventory

    def handle_inputs(self,inputs):
        if inputs[pygame.K_1]:
            for slot in self.inventory:
                slot.active = False
                if slot.slot_number == 1:
                    slot.active = True
        if inputs[pygame.K_2]:
            for slot in self.inventory:
                slot.active = False
                if slot.slot_number == 2:
                    slot.active = True
        if inputs[pygame.K_3]:
            for slot in self.inventory:
                slot.active = False
                if slot.slot_number == 3:
                    slot.active = True
        if inputs[pygame.K_4]:
            for slot in self.inventory:
                slot.active = False
                if slot.slot_number == 4:
                    slot.active = True
        if inputs[pygame.K_5]:
            for slot in self.inventory:
                slot.active = False
                if slot.slot_number == 5:
                    slot.active = True
        if inputs[pygame.K_6]:
            for slot in self.inventory:
                slot.active = False
                if slot.slot_number == 6:
                    slot.active = True
        