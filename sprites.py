from object_event import *
import math
import pygame as pg


def load_image(img_loc):
    image = pg.image.load(MISSING_TEXTURE)
    try:
        image = pg.image.load(img_loc)
    except Exception as error:
        print("Error loading image:", error, "\nLoading missing texture instead...")
    return image.convert()


class GameObject:
    def __init__(self, game, label, pos, image_loc=MISSING_TEXTURE, depth=0, solid=True, visible=True, **kwargs):
        self.game = game
        self.label = label
        self.depth = depth
        self.image = load_image(image_loc)
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.solid = solid
        self.visible = visible
        for kwarg in kwargs:
            exec("self." + kwarg + "=" + str(kwargs[kwarg]))

    def update(self):
        listener(self)


class Tile:
    def __init__(self, pos, index, tile_set, depth=-1):
        self.index = index
        self.depth = depth
        self.pos = pos
        self.tile_set = load_image(tile_set)
        self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
        y = (math.ceil(index / (self.tile_set.get_width() / TILE_SIZE)))
        x = (index - (math.floor(index / (self.tile_set.get_width() / TILE_SIZE)) * 18))
        self.image.blit(self.tile_set, (0, 0), pg.Rect((x - 1) * 16, (y - 1) * 16, 16, 16))
