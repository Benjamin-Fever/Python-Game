from object_event import *
import pygame as pg


class GameObject:
    def __init__(self, game, label, pos,
                 image_loc="textures/missing_texture.png", depth=0, solid=True, visible=True, updatable=True, **kwargs):
        self.game = game
        self.label = label
        self.depth = depth
        self.updatable = updatable
        try:
            self.image = pg.image.load(image_loc).convert()
        except FileNotFoundError as error:
            if "No such file or directory" in str(error):
                self.image = pg.image.load(MISSING_TEXTURE).convert()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.solid = solid
        self.visible = visible
        for kwarg in kwargs:
            exec("self." + kwarg + "=" + str(kwargs[kwarg]))

    def update(self):
        listener(self)


class Tile:
    def __init__(self, pos, index, tile_set, depth=-1, updatable=True):
        self.index = index
        self.updatable = updatable
        self.tile_set = pg.image.load(tile_set).convert()
        self.image = pg.transform.chop(self.tile_set, (0, 0, index * 16, 0))
        self.depth = depth
        self.pos = pos
