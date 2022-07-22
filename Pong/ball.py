import random

import pygame

from Pong.globals import WHITE, WINDOW, WINDOW_RECT


class Ball:
    def __init__(self, size, speed, player1, player2, limit_speed):
        self.height, self.width = size

        self.image = pygame.Surface(size)
        self.image.fill(WHITE)
        self.img_rect_ball = self.image.get_rect()

        self.speed = speed
        self.limit_speed = limit_speed
        self.set_bola()

        self.player1 = player1
        self.player2 = player2

    def random(self):
        while True:
            num = random.uniform(-1.0, 1.0)
            if num > -0.5 and num < 0.5:
                continue
            else:
                return num

    def set_bola(self):
        x = self.random()
        y = self.random()
        self.img_rect_ball.x = WINDOW_RECT.centerx
        self.img_rect_ball.y = WINDOW_RECT.centery

        self.speed_tuple = [x, y]

        self.pos = list(WINDOW_RECT.center)

        if self.speed > self.limit_speed:
            self.speed = self.limit_speed

    def wall_collider(self):
        self.bottom_height = (self.img_rect_ball.y >
                              WINDOW_RECT.bottom - self.height)
        self.right_width = (self.img_rect_ball.x >
                            WINDOW_RECT.right - self.width)

        if self.img_rect_ball.y <= 0 or self.bottom_height:
            self.speed_tuple[1] *= -1

        if self.img_rect_ball.x <= 0 or self.right_width:
            self.speed_tuple[0] *= -1
            self.collide_key = False

            if self.right_width:
                self.player1.score.points += 1
                self.set_bola()

            if self.img_rect_ball.x <= 0:
                self.player2.score.points += 1
                self.set_bola()

    def collide_player(self, player):
        adjust = (player[0]+1, player[1]+1, player[2]+1, player[3]+1)
        if self.img_rect_ball.colliderect(adjust):
            # self.score.points += 1
            self.speed_tuple[0] *= -1
            self.speed += 1
            self.collide_key = False

    def move(self):
        self.pos[0] += self.speed_tuple[0] * self.speed
        self.pos[1] += self.speed_tuple[1] * self.speed
        self.img_rect_ball.center = self.pos

    def actualize(self):
        self.wall_collider()
        self.collide_player(self.player1.img_rect_player)
        self.collide_player(self.player2.img_rect_player)
        self.move()

    def realize(self):
        WINDOW.blit(self.image, self.img_rect_ball)
