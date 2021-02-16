from sprites import *
from settings import *
import json


class GameMap:
    def __init__(self, name):
        self.name = name
        self.objects = []
        self.tiles = []
        self.background = (255, 255, 255)


class Camera:
    def __init__(self):
        pass


def load_map(name):
    x = 0
    with open(r'' + MAPS[name]) as file:
        data = json.load(file)
        loading_map = GameMap(data["name"])
        for layer in data["layers"]:
            for column in range(0, len(layer["data"])):
                for row in range(0, len(layer["data"][column])):
                    if layer["type"] == "tile-set":
                        if layer["data"][column][row] > 0:
                            x += 1
                            print(x)
                            loading_map.tiles.append(
                                Tile(
                                    (column * TILE_SIZE, row * TILE_SIZE),
                                    layer["data"][column][row],
                                    layer["tile-set"]
                                )
                            )
    print(loading_map)
    return loading_map
