import random

import pygame
from Neural.rede_neural import error_calculator

from Pong.globals import WHITE, WINDOW, WINDOW_RECT


class Ball:
    def __init__(self, size, speed, limit_speed, player_1, player_2):
        self.height, self.width = size

        self.image = pygame.Surface(size)
        self.image.fill(WHITE)
        self.img_rect_ball = self.image.get_rect()

        self.initial_speed = speed
        self.speed = speed
        self.limit_speed = limit_speed
        self.set_bola()

        self.player_1 = player_1
        self.player_2 = player_2

        self.ball_pos_x = self.img_rect_ball.x
        self.ball_pos_y = self.img_rect_ball.y

    def random(self):
        while True:
            num = random.uniform(-1, 1)
            if num > -0.3 and num < 0.3:
                continue
            else:
                return num

    def set_bola(self):
        if self.speed > self.initial_speed:
            save_item(self.speed, "SAVES/speed_ball.txt")

        self.speed = self.initial_speed
        x = self.random()
        y = self.random()
        self.img_rect_ball.x = WINDOW_RECT.centerx
        self.img_rect_ball.y = WINDOW_RECT.centery

        self.ball_pos_x = WINDOW_RECT.centerx
        self. ball_pos_y = WINDOW_RECT.centery

        self.speed_tuple = [x, y]

        self.pos = list(WINDOW_RECT.center)

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

            # Caso onde o Player 1 (Esquerda) marcou um ponto
            if self.right_width:
                self.player_1.score.points += 1
                # PLayer 2 (Direita) é penalizado
                self.player_2.error = error_calculator(self.player_2,
                                                       self, 100)
                # Reinicia a posição da bola
                self.set_bola()

            # Caso onde o Player 2 (Direita) marcou um ponto
            if self.img_rect_ball.x <= 0:
                self.player_2.score.points += 1
                # PLayer 1 (Esquerda) é penalizado
                self.player_1.error = error_calculator(self.player_2,
                                                       self, 100)
                # Reinicia a posição da bola
                self.set_bola()

    def collide_player(self, player):
        self.rect_player = player.img_rect_player
        adjust = (self.rect_player[0]+1, self.rect_player[1]+1,
                  self.rect_player[2]+1, self.rect_player[3]+1)

        self.collided_player = self.img_rect_ball.colliderect(adjust)

        if self.collided_player:
            self.speed_tuple[0] *= -1

            if self.speed < self.limit_speed:
                self.speed += 1
                player.speed = self.speed

            self.collide_key = False

            player.error = 0

    def move(self):
        self.pos[0] += self.speed_tuple[0] * self.speed
        self.pos[1] += self.speed_tuple[1] * self.speed
        self.img_rect_ball.center = self.pos

    def update(self):
        self.wall_collider()
        self.ball_pos_x = self.img_rect_ball.x
        self.ball_pos_y = self.img_rect_ball.y
        self.collide_player(self.player_1)
        self.collide_player(self.player_2)
        self.move()

    def realize(self):
        WINDOW.blit(self.image, self.img_rect_ball)


def save_item(item, name_file):
    with open(name_file, 'a') as file:
        file.write(str((item)) + "\n")
