import pygame
from datetime import datetime as dt
from .config import SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT
from .player import Player
from .world import World


class Game:
    def __init__(self):
        pass

    def setup(self):
        self.win = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
        pygame.display.set_caption(SCREEN_TITLE)
        self.run = True

        # player
        self.player = Player(self, 0, 0, 0)

        # world
        self.world = World("wall")

        # control
        self.keys_down = []

    def start(self):
        self.setup()
        self.last_time = dt.now()
        self.main_loop()

    def main_loop(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                else:
                    self.event(event)

            delta_time = self.last_time - dt.now()

            self.update(delta_time)
            self.win.fill((0, 0, 0))
            self.draw()
            pygame.display.update()

            self.last_time = dt.now()

    def event(self, e):
        if e.type in self.player.events:
            self.player.event(e)

        if e.type == pygame.KEYDOWN:
            self.keys_down.append(e.key)
        if e.type == pygame.KEYUP:
            if e.key in self.keys_down:
                self.keys_down.remove(e.key)

    def update(self, delta_time):
        self.player.update(delta_time)

    def draw(self):
        self.player.draw()
