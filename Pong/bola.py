import random

import pygame

from Pong.globais import BRANCO, TELA, TELA_RETANGULO


class Bola:
    def __init__(self, tamanho, velocidade, player1, player2):
        self.altura, self.largura = tamanho
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(BRANCO)
        self.imagem_retangulo = self.imagem.get_rect()
        self.velocidade = velocidade
        self.set_bola()

        self.colide_key = True

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
        self.imagem_retangulo.x = TELA_RETANGULO.centerx
        self.imagem_retangulo.y = TELA_RETANGULO.centery

        self.velo = [x, y]

        self.pos = list(TELA_RETANGULO.center)

    def colide_parede(self):
        self.botton_altura = (self.imagem_retangulo.y >
                              TELA_RETANGULO.bottom - self.altura)
        self.right_largura = (self.imagem_retangulo.x >
                              TELA_RETANGULO.right - self.largura)

        if self.imagem_retangulo.y <= 0 or self.botton_altura:
            self.velo[1] *= -1

        if self.imagem_retangulo.x <= 0 or self.right_largura:
            self.velo[0] *= -1
            self.colide_key = False

            if self.right_largura:
                self.player1.placar.pontos += 1

            if self.imagem_retangulo.x <= 0:
                self.player2.placar.pontos += 1

    def colide_player(self, player):
        ajuste = (player[0], player[1], player[2]+1, player[3]+1)
        if self.imagem_retangulo.colliderect(ajuste):
            # self.placar.pontos += 1
            self.velo[0] *= -1
            self.velocidade += 1

    def move(self):
        self.pos[0] += self.velo[0] * self.velocidade
        self.pos[1] += self.velo[1] * self.velocidade
        self.imagem_retangulo.center = self.pos

    def espera(self):
        self.colide_key = True

    def atualiza(self):
        self.colide_parede()
        if self.colide_key:
            self.colide_player(self.player1.imagem_retangulo)
            self.colide_player(self.player2.imagem_retangulo)
        else:
            self.espera()
        self.move()

    def realiza(self):
        TELA.blit(self.imagem, self.imagem_retangulo)
