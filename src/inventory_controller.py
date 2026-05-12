import pygame

class InventoryController:
    def __init__(self,inventory):
        self.inventory = inventory

    def handle_inputs(self,inputs):
        if inputs['1']:
            for slot in self.inventory:
                slot.active = False
                if slot.slot_number == 1:
                    slot.active = True
        if inputs['2']:
            for slot in self.inventory:
                slot.active = False
                if slot.slot_number == 2:
                    slot.active = True
        if inputs['3']:
            for slot in self.inventory:
                slot.active = False
                if slot.slot_number == 3:
                    slot.active = True
        