import pygame

from Pong.globais import BRANCO, TELA


class Placar():
    def __init__(self, tipo):
        pygame.font.init()
        self.fonte = pygame.font.Font(None, 36)
        self.pontos = 0

        self.tipo = tipo

    def contagem(self):
        self.text = self.fonte.render(str(self.pontos), 1, BRANCO)
        self.textpos = self.text.get_rect()

        if self.tipo == 'right':
            self.textpos.centerx = TELA.get_width()/2 + 15
        else:
            self.textpos.centerx = TELA.get_width()/2 - 15

        TELA.blit(self.text, self.textpos)
        TELA.blit(TELA, (0, 0))
