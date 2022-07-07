import pygame

from Pong.globais import WHITH, WINDOW, WINDOW_RECT
from Pong.placar import Placar


class Player:
    def __init__(self, tamanho, velicidade, tipo):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(WHITH)
        self.img_rect_player = self.imagem.get_rect()
        self.velicidade = velicidade
        self.tipo = tipo
        self.placar = Placar(self.tipo)
        if self.tipo == 'right':
            self.img_rect_player[0] = 5
        else:
            self.img_rect_player[0] = 790

        self.colide_key = True

    def move(self, x, y):
        self.img_rect_player[0] += x * self.velicidade
        self.img_rect_player[1] += y * self.velicidade

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

        self.img_rect_player.clamp_ip(WINDOW_RECT)

    def realiza(self):
        WINDOW.blit(self.imagem, self.img_rect_player)
