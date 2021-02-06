from mapping import *
from sprites import *
from settings import *
from algorithms import *
from math import *
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
        self.camera = [0, 0]

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
        self.screen.fill((0, 0, 0))
        for draw in sort_draw_hierarchy(self.objects + self.loaded_map.tiles):
            self.screen.blit(draw.image, (draw.pos[0]-self.camera[0], draw.pos[1]-self.camera[1]))

    def update(self):
        for obj in self.objects:
            obj.update()
        pg.display.update()


if __name__ == '__main__':
    window = Game()
    window.start()
