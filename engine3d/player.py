from .config import RAYS, SCREEN_WIDTH, SCREEN_HEIGHT
import pygame
import math
from .functions import radian_to


class Movement:
    up = "up"
    down = "down"
    left = "left"
    right = "right"
    forward = "forward"
    backward = "backwards"
    turn_right = "turn_right"
    turn_left = "turn_left"
    turn_up = "turn_up"
    turn_down = "turn_down"


MOVEMENT = Movement()


class Player:
    speed = 1
    events = [pygame.MOUSEMOTION]
    fov = 90

    def __init__(self, parent, x, y, z):
        self.game = parent
        self.x, self.y, self.z = (x, y, z)
        self.looking = [0, 0]
        self.change_x = self.change_y = self.change_z = 0
        self.ray_ranges = []

    def event(self, e):
        # looking (mouse)
        if e.type == pygame.MOUSEMOTION:
            self.looking[0] += e.rel[0] * 2
            self.looking[1] += e.rel[1] * 2

    def movement(self):
        looking_x = math.radians(self.looking[0])

        for key in self.game.keys_down:
            if key in [pygame.K_w, pygame.K_s]:
                self.change_x += math.cos(looking_x) * (-1 if key == pygame.K_s else 1)
                self.change_z += math.sin(looking_x) * (-1 if key == pygame.K_s else 1)
                print(self.change_x, self.change_z)
            elif key in [pygame.K_a, pygame.K_d]:
                self.change_x += math.sin(looking_x) * (-1 if key == pygame.K_a else 1)
                self.change_z += math.cos(looking_x) * (-1 if key == pygame.K_a else 1)

            elif key == pygame.K_SPACE:
                self.change_y += self.speed
            elif key == pygame.K_LCTRL:
                self.change_y -= self.speed

    def between_circle_margins(self, num):
        if num > 360:
            return num - 260
        if num < 0:
            return num + 360
        return num


    def update(self, delta_time):
        for i in range(2):
            if self.looking[i] > 360:
                self.looking[i] -= 360
            elif self.looking[i] < 0:
                self.looking[i] += 360

        self.movement()

        self.x += self.change_x
        self.y += self.change_y
        self.z += self.change_z
        self.change_x = self.change_y = self.change_z = 0

    def shoot_rays(self):
        image = [
            ["." for _2 in range(RAYS[0])] for _ in range(RAYS[1])
        ]  # matrix of shape (RAYS[1], RAYS[0])

        # calculate ranges for rays
        self.calculate_ray_ranges()

        # calculate and schoot rays
        y_ray_gap = self.fov // RAYS[1]
        xz_angle = self.fov // RAYS[0]

        for y in range(RAYS[1]):
            y_angle = y_ray_gap * y + (y_ray_gap / 2)
            for x in range(RAYS[0]):
                xz_angle = xz_angle * x + (xz_angle / 2)

                # correct for fov
                fov_margin = (180 - self.fov) / 2

                xz_angle = self.between_circle_margins(xz_angle + fov_margin + self.looking[0])
                y_angle = self.between_circle_margins(y_angle + fov_margin + self.looking[1])

                image[y][x] = "#" if self.ray(xz_angle, y_angle) else "."

        return image

    def ray(self, xz_angle, y_angle) -> bool:
        """ "Shoots" a ray into the specified direction and returns True if it hits something """
        xz_angle, y_angle = math.radians(xz_angle) % (2 * math.pi), math.radians(y_angle) % (2 * math.pi)

        # print("\n\n")

        # print(self)
        # print(xz_angle, y_angle)
        for rnge in self.ray_ranges:
            # print(min(rnge[0]), max(rnge[0]), min(rnge[1]), max(rnge[1]))
            if min(rnge[0]) <= xz_angle <= max(rnge[0]) and min(rnge[1]) <= y_angle <= max(rnge[1]):
                return True

        return False

    def calculate_ray_ranges(self):
        self.ray_ranges = []

        for cube in self.game.world.walls:
            xz_angle_corner_1 = radian_to((self.x, self.z), (cube[0][0], cube[0][2]))
            y_angle_corner_1 = radian_to((self.y, self.z), (cube[0][1], cube[0][2]))
            xz_angle_corner_2 = radian_to((self.x, self.z), (cube[1][0], cube[1][2]))
            y_angle_corner_2 = radian_to((self.y, self.z), (cube[1][1], cube[1][2]))
            self.ray_ranges.append(
                (
                    (xz_angle_corner_1, y_angle_corner_1),
                    (xz_angle_corner_2, y_angle_corner_2)
                )
            )

    def draw(self):
        image = self.shoot_rays()

        column_width_px = SCREEN_WIDTH / RAYS[0]
        row_height_px = SCREEN_HEIGHT / RAYS[1]

        for y in range(RAYS[1]):
            for x in range(RAYS[0]):
                color = (255, 255, 255) if image[y][x] == "#" else (0, 0, 0)

                pygame.draw.rect(
                    self.game.win,
                    color,
                    (
                        x * column_width_px,
                        y * row_height_px,
                        (x + 1) * column_width_px,
                        (y + 1) * row_height_px,
                    )
                )

    def __repr__(self):
        return f"<Player @ {(self.x,  self.y, self.z)} OO ({self.looking})>"
