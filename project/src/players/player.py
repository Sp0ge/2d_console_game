import random

class Player():
    def __init__(self, id:int, username:str, size:tuple, type:str="local", controls:str ="wasd"):
        self.username = username
        self.id = id
        self.controls = controls
        self.type = type
        
        self.health = 100
        self.ammo = 25
        self.skin = "⚪"
        self.modifications = []  

        self.pos = [
            random.randint(0 + size[0]//3, size[1] - size[0]//3),
            random.randint(0 + size[1]//3, size[0] - size[1]//3)
        ]

    def player_action(self, actions):
        self.last_pos = self.pos
        if actions[0]:
            self.pos[0] -= 1 
        if actions[1]:
            self.pos[1] -= 1 
        if actions[2]:
            self.pos[0] += 1 
        if actions[3]:
            self.pos[1] += 1 
        
        
        