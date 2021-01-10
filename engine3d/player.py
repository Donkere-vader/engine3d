import pygame

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
    def __init__(self, x, y, z):
        self.x, self.y, self.z = (x, y, z)
        self.looking = [0, 0]
        self.change_x = self.change_y = 0
        self.movement_queue = []

        self.events = [pygame.K_w, pygame.K_s, pygame.K_a,  pygame.K_d, pygame.K_SPACE, pygame.K_LCTRL, pygame.MOUSEMOTION]

    def event(self, e):
        if e.type == pygame.K_w:
            self.movement_queue.append(MOVEMENT.forward)
        elif e.type == pygame.K_s:
            self.movement_queue.append(MOVEMENT.backward)
        elif e.type == pygame.K_a:
            self.movement_queue.append(MOVEMENT.left)
        elif e.type == pygame.K_d:
            self.movement_queue.append(MOVEMENT.right)
        elif e.type == pygame.K_LCTRL:
            self.movement_queue.append(MOVEMENT.down)
        elif e.type == pygame.K_SPACE:
            self.movement_queue.append(MOVEMENT.up)
        elif e.type == pygame.MOUSEMOTION:
            y = e.rel[1]
            x = e.rel[0]
            if x > 0:
                self.movement_queue.append(MOVEMENT.turn_right)
            elif x < 0:
                self.movement_queue.append(MOVEMENT.turn_left)
            if y > 0:
                self.movement_queue.append(MOVEMENT.turn_up)
            elif y < 0:
                self.movement_queue.append(MOVEMENT.turn_down)

    def update(self, delta_time):
        while len(self.movement_queue):
            self.caculate_move(self.movement_queue[0])
            del self.movement_queue[0]

        for i in range(2):
            if self.looking[i] > 360:
                self.looking[i] -= 360
            elif self.looking[i] < -360:
                self.looking[i] += 360

    def caculate_move(self, move):
        if move == MOVEMENT.turn_left:
            self.looking[0] -= 0.1
        elif move == MOVEMENT.turn_right:
            self.looking[0] += 0.1
        elif move == MOVEMENT.turn_up:
            self.looking[1] -= 0.1
        elif move == MOVEMENT.turn_left:
            self.looking[1] += 0.1

    def __repr__(self):
        return f"<Player @ {(self.x,  self.y, self.z)} 00 ({self.looking})>"
