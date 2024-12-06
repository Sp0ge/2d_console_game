import random
import time

from project.src.display import Display
from project.src.map.map import Map
from project.src.players.manager import PlayersManager 


class Main():
    def __init__(self) -> None:
        
        self.player_id = random.randint(1,9999)
        self.running = True
        self.MapModule = Map()
        self.PlManager = PlayersManager(self.MapModule.size)
        
    def start(self):
        while self.running:
            size, map = self.MapModule.get_map()
            self.PlManager.Players_update()
            players = self.PlManager.get_players()
            Display.show_all(size, map, players)
            time.sleep(0.005)
            
            
           
           
            