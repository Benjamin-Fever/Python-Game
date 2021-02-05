from mapping import *
from sprites import *
from settings import *
from algorithms import *
from math import *
from copy import deepcopy
import pygame as pg


class Game:
    def __init__(self):
        pg.display.init()
        pg.display.set_caption(TITLE)
        self.map = "test_map"
        self.loaded_map = None
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.objects = []
        self.tiles = []
        self.clock = pg.time.Clock()
        self.running = True

    def start(self):
        self.objects.append(GameObject(window, "player", (64, 64), "textures/player.png", can_move=True))
        self.objects.append(GameObject(window, "wall", (380, 64), "textures/wall.png"))
        self.loaded_map = load_map(self.map)
        while self.running:
            self.clock.tick(FPS)
            pg.display.set_caption(TITLE + " FPS:" + str(floor(self.clock.get_fps())))
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def draw(self):
        for draw in sort_draw_hierarchy(self.objects + self.loaded_map.tiles):
            if draw.updatable:
                try:
                    self.screen.blit(draw.image, draw.rect)
                except AttributeError as error:
                    if str(error) == "'Tile' object has no attribute 'rect'":
                        self.screen.blit(draw.image, draw.pos)
                draw.updatable = False

    def update(self):
        for obj in self.objects:
            obj.update()
        pg.display.update()


if __name__ == '__main__':
    window = Game()
    window.start()
