from project.src.map.generation import map_generator 
from copy import deepcopy

class Map():
    def __init__(self, size=tuple((40,40))):
        self.size = size
        self.map = []
        
        self.gen_map()
        
    def gen_map(self):
        self.map = map_generator.gen_zero(self.size)
        
    def get_map(self):
        map = deepcopy(self.map)
        size = deepcopy(self.size)
        return tuple(size), list(map)