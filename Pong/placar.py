import pygame

from globais import BRANCO, TELA


class Placar():
    def __init__(self):
        pygame.font.init()
        self.fonte = pygame.font.Font(None, 36)
        self.pontos = 10

    def contagem(self):
        self.text = self.fonte.render(str(self.pontos), 1, BRANCO)
        self.textpos = self.text.get_rect()
        self.textpos.centerx = TELA.get_width()/2
        TELA.blit(self.text, self.textpos)
        TELA.blit(TELA, (0, 0))
