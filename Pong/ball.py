import random

import pygame

from Pong.globais import WHITH, WINDOW, WINDOW_RECT


class Ball:
    def __init__(self, tamanho, velocidade, player1, player2, limite_vel):
        self.altura, self.largura = tamanho

        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(WHITH)
        self.img_rect_ball = self.imagem.get_rect()

        self.velocidade = velocidade
        self.limite_vel = limite_vel
        self.set_bola()

        self.player1 = player1
        self.player2 = player2

    def aleatorio(self):
        while True:
            num = random.uniform(-1.0, 1.0)
            if num > -0.5 and num < 0.5:
                continue
            else:
                return num

    def set_bola(self):
        x = self.aleatorio()
        y = self.aleatorio()
        self.img_rect_ball.x = WINDOW_RECT.centerx
        self.img_rect_ball.y = WINDOW_RECT.centery

        self.velo = [x, y]

        self.pos = list(WINDOW_RECT.center)

        if self.velocidade > self.limite_vel:
            self.velocidade = self.limite_vel

    def colide_parede(self):
        self.botton_altura = (self.img_rect_ball.y >
                              WINDOW_RECT.bottom - self.altura)
        self.right_largura = (self.img_rect_ball.x >
                              WINDOW_RECT.right - self.largura)

        if self.img_rect_ball.y <= 0 or self.botton_altura:
            self.velo[1] *= -1

        if self.img_rect_ball.x <= 0 or self.right_largura:
            self.velo[0] *= -1
            self.colide_key = False

            if self.right_largura:
                self.player1.placar.pontos += 1
                self.set_bola()

            if self.img_rect_ball.x <= 0:
                self.player2.placar.pontos += 1
                self.set_bola()

    def colide_player(self, player):
        ajuste = (player[0]+1, player[1]+1, player[2]+1, player[3]+1)
        if self.img_rect_ball.colliderect(ajuste):
            # self.placar.pontos += 1
            self.velo[0] *= -1
            self.velocidade += 1
            self.colide_key = False

    def move(self):
        self.pos[0] += self.velo[0] * self.velocidade
        self.pos[1] += self.velo[1] * self.velocidade
        self.img_rect_ball.center = self.pos

    def atualiza(self):
        self.colide_parede()
        self.colide_player(self.player1.img_rect_player)
        self.colide_player(self.player2.img_rect_player)
        self.move()

    def realiza(self):
        WINDOW.blit(self.imagem, self.img_rect_ball)
