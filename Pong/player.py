import pygame
from Neural.rede_neural import Initial_weights

from Pong.globals import WHITE, WINDOW, WINDOW_RECT
from Pong.score import Score


class Player:
    def __init__(self, height, speed, type, limit_speed_player):
        self.image = pygame.Surface(height)
        self.image.fill(WHITE)
        self.img_rect_player = self.image.get_rect()

        self.type = type
        self.score = Score(self.type)
        if self.type == 'right':
            self.img_rect_player[0] = 5
        else:
            self.img_rect_player[0] = 790

        self.collide_key = True

        self.player_pos_y = self.img_rect_player.centery
        self.speed = speed
        self.limit_speed = limit_speed_player

        self.initial_weights = Initial_weights()
        self.error = 0

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
            if key >= 0.7:  # key[pygame.K_UP]:
                self.move(-1)

            elif key <= 0.3:  # key[pygame.K_DOWN]:
                self.move(1)

        self.img_rect_player.clamp_ip(WINDOW_RECT)

    def realize(self):
        WINDOW.blit(self.image, self.img_rect_player)
