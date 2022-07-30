from asyncio.windows_events import NULL

import pygame
from Neural.rede_neural import Initial_weights

from Pong.globals import DISPLAY_SIZE, WHITE, WINDOW, WINDOW_RECT
from Pong.score import Score


class Player:
    def __init__(self, height, speed, type, file=NULL):
        self.image = pygame.Surface(height)
        self.image.fill(WHITE)
        self.img_rect_player = self.image.get_rect()

        self.type = type
        self.score = Score(self.type)
        if self.type == 'left':
            self.img_rect_player[0] = 0
        else:
            self.img_rect_player[0] = DISPLAY_SIZE[0]-10

        self.collide_key = True

        self.player_pos_y = self.img_rect_player.centery / DISPLAY_SIZE[1]
        self.speed = speed

        self.initial_weights = Initial_weights(file)
        self.error = 0

        self.training = True

    def move(self, y):
        self.img_rect_player[1] += y * self.speed
        # self.img_rect_player[0] += x * self.speed

        self.player_pos_y = self.img_rect_player.centery

    def update(self, key):
        if self.type == 'right':
            if key >= 0.8:  # key[pygame.K_w]:
                self.move(-1)

            elif key <= 0.2:  # key[pygame.K_s]:
                self.move(1)

        else:
            if key >= 0.8:  # key[pygame.K_UP]:
                self.move(-1)

            elif key <= 0.2:  # key[pygame.K_DOWN]:
                self.move(1)
        self.img_rect_player.clamp_ip(WINDOW_RECT)

    def realize(self):
        WINDOW.blit(self.image, self.img_rect_player)
