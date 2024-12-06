from .conf import Textures

class map_generator:
    def gen_zero(size):
        map = list()
        for y in range(0,size[1]+1):
            row = list()
            for x in range(0,size[0]+1):
                if y == 0 or y == size[1] or \
                    x == 0 or x == size[0]:
                    row.append(Textures.wall)
                else:
                    row.append(Textures.air)
            map.append(row)
        return map

    