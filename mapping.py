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
        loading_map = GameMap(data["Name"])
        for y in range(0, len(data['Tile Map'])):
            for x in range(0, len(data['Tile Map'][y])):
                loading_map.tiles.append(Tile((x * 16, y * 16), data['Tile Map'][y][x], "textures/tileset.gif"))
    return loading_map
