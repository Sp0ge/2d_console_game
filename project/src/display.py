import os

class Display:
    def show_all(size, world_matrix, players):
        for player in players:
            world_matrix[player.pos[0]][player.pos[1]] = player.skin
        os.system("cls||clear")
        for row in world_matrix:
            print(''.join(map(str,row)))
        
        
        