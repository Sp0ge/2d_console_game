from project.src.players.player import Player
from project.src.inputs import arrows, wasd

class PlayersManager():
    def __init__(self, size:tuple):
        self.players = list()
        self.world_size = size
        
        self.__add_local_player__()
        
    def Players_update(self):
        for player in self.players:
            if player.type == "local":
                keys_actions = wasd.action_get()
                player.player_action(keys_actions)
        
    def __add_local_player__(self):
        id=len(self.players)
        
        local_player = Player(
            id=id,
            username=f"USER[{id}]",
            size=self.world_size,
            controls="wasd"
            )
        
        self.players.append(local_player)
        
    def get_players(self):
        return self.players