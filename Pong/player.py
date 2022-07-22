import pygame

from Pong.globals import WHITE, WINDOW, WINDOW_RECT
from Pong.score import Score


class Player:
    def __init__(self, height, speed, type, limit_speed_player):
        self.image = pygame.Surface(height)
        self.image.fill(WHITE)
        self.img_rect_player = self.image.get_rect()

        self.speed = speed
        self.limit_speed = limit_speed_player

        self.type = type
        self.score = Score(self.type)
        if self.type == 'right':
            self.img_rect_player[0] = 5
        else:
            self.img_rect_player[0] = 790

        self.collide_key = True

    def move(self, x, y):
        self.img_rect_player[0] += x * self.speed
        self.img_rect_player[1] += y * self.speed

    def actualize(self, key):
        if self.type == 'right':
            if key[pygame.K_w]:
                self.move(0, -1)

            if key[pygame.K_s]:
                self.move(0, 1)

        else:
            if key[pygame.K_UP]:
                self.move(0, -1)

            if key[pygame.K_DOWN]:
                self.move(0, 1)

        self.img_rect_player.clamp_ip(WINDOW_RECT)

    def realize(self):
        WINDOW.blit(self.image, self.img_rect_player)
