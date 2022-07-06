from platform import win32_edition

import pygame

from Pong.globais import WHITH, WINDOW, WINDOW_RECT
from Pong.placar import Placar


class Player:
    def __init__(self, tamanho, velicidade, tipo):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(WHITH)
        self.imagem_retangulo = self.imagem.get_rect()
        self.velicidade = velicidade
        self.tipo = tipo
        self.placar = Placar(self.tipo)
        if self.tipo == 'right':
            self.imagem_retangulo[0] = 5
        else:
            self.imagem_retangulo[0] = 790

        self.colide_key = True

    def move(self, x, y):
        self.imagem_retangulo[0] += x * self.velicidade
        self.imagem_retangulo[1] += y * self.velicidade

    def atualiza(self, tecla):
        if self.tipo == 'right':
            if tecla[pygame.K_w]:  # or tecla[pygame.K_w]:
                self.move(0, -1)

            if tecla[pygame.K_s]:  # or tecla[pygame.K_s]:
                self.move(0, 1)

        else:
            if tecla[pygame.K_UP]:  # or tecla[pygame.K_w]:
                self.move(0, -1)

            if tecla[pygame.K_DOWN]:  # or tecla[pygame.K_s]:
                self.move(0, 1)

        self.imagem_retangulo.clamp_ip(WINDOW_RECT)

    def realiza(self):
        WINDOW.blit(self.imagem, self.imagem_retangulo)
