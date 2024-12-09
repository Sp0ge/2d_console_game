from project.src.players.player import Player
from project.src.inputs import arrows, wasd

class PlayersManager():
    def __init__(self, size:tuple):
        self.players = list()
        self.world_size = size
        
        self.__add_local_player__("wasd")
        self.__add_local_player__("arrows")
        
    def Players_update(self, map):
        for player in self.players:
            
            if player.type == "local" and \
                    player.controls == "wasd":
                player.player_action(
                    wasd.action_get(),
                    map)
            
            elif player.type == "local" and \
                    player.controls == "arrows":
                player.player_action(
                    arrows.action_get(), 
                    map)
            
            
    def __add_local_player__(self, controls="wasd"):
        id=len(self.players)
        
        local_player = Player(
            id=id,
            username=f"USER[{id}]",
            size=self.world_size,
            controls=controls
            )
        
        self.players.append(local_player)
        
    def get_players(self):
        return self.players