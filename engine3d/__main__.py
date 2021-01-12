import pygame
from datetime import datetime as dt
from .config import SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT
from .player import Player
from .world import World
from .functions import translate_triangle
import math


class Game:
    def __init__(self):
        pass

    def setup(self):
        self.win = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
        pygame.display.set_caption(SCREEN_TITLE)
        self.run = True

        # player
        self.player = Player(self, 45, 10, 50)
        self.player.looking[0] = 270

        # world
        self.world = World("wall")

        # control
        self.keys_down = []
        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)

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
        # stop if q is pressed
        if pygame.K_q in self.keys_down:
            self.keys_down.remove(pygame.K_q)
            self.run = False

        # update player
        # print(self.world.walls)
        self.player.update(delta_time)

    def draw(self):
        self.player.draw()

        # MINIMAP
        pygame.draw.rect(
            self.win,
            (255, 255, 255),
            (0, 0, 101, 101)
        )

        pygame.draw.rect(
            self.win,
            (0, 0, 0),
            (0, 0, 100, 100)
        )

        for cube in self.world.walls:
            pygame.draw.rect(
                self.win,
                (255, 255, 255),
                (
                    cube.corners[0][0],
                    cube.corners[0][1],
                    cube.corners[1][0] - cube.corners[0][0],
                    cube.corners[1][1] - cube.corners[0][1]
                )
            )

        # draw player
        pygame.draw.circle(
            self.win,
            (0, 0, 255),
            (max(0, self.player.x), max(0, self.player.z)),
            5
        )

        # draw looking direction
        rad_looking = math.radians(self.player.looking[0])
        line_x = math.cos(rad_looking)
        line_z = math.sin(rad_looking)

        dx, dz = translate_triangle(line_x, line_z, 1, 120)

        pygame.draw.line(
            self.win,
            (255, 0, 0),
            (self.player.x, self.player.z),
            (self.player.x + dx, self.player.z + dz)
        )

        # draw Rays
        for ray in self.player.ray_angles[0]:
            x_ray = math.radians(ray[0])
            x = math.cos(x_ray)
            z = math.sin(x_ray)
            # print(x_ray, x, z)
            dx, dz = translate_triangle(x, z, 1, 100)
            pygame.draw.line(
                self.win,
                (0, 255, 0),
                (self.player.x, self.player.z),
                (self.player.x + dx, self.player.z + dz)
            )
