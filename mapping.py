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
    with open(r'' + MAPS[name]) as file:
        data = json.load(file)
        loading_map = GameMap(data["name"])
        for layer in data["layers"]:
            for y in range(0, len(layer["data"])):
                for x in range(0, len(layer["data"][y])):
                    if layer["type"] == "tile-set":
                        if layer["data"][y][x] > 0:
                            loading_map.tiles.append(
                                Tile(
                                    (x * TILE_SIZE, y * TILE_SIZE),
                                    layer["data"][y][x],
                                    layer["tile-set"]
                                )
                            )
    return loading_map
