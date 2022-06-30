import pygame

from Pong.globais import BRANCO, TELA


class Placar():
    def __init__(self, tipo):
        pygame.font.init()
        self.fonte = pygame.font.Font(None, 36)
        self.pontos = 0

        self.tipo = tipo

    def contagem(self):
        self.text = self.fonte.render((f"{str(self.pontos)}"), 1, BRANCO)
        self.textpos = self.text.get_rect()

        distancia = 55
        if self.tipo == 'right':
            self.textpos.centerx = TELA.get_width()/2 + distancia
        else:
            self.textpos.centerx = TELA.get_width()/2 - distancia

        TELA.blit(self.text, self.textpos)
        TELA.blit(TELA, (0, 0))


def edit_tempo(ms):
    tempo = (ms//1000)
    s = 0
    m = 0
    while tempo >= 60:
        m += 1
        tempo -= 60
    s = tempo

    if (s < 10):
        s = "0" + str(s)
    if (m < 10):
        m = "0" + str(m)

    return (f"{m}:{s}")


class Timer():

    def __init__(self):
        pygame.font.init()
        self.fonte = pygame.font.Font(None, 36)

    def exibe_tempo(self, ms):
        self.tempo = edit_tempo(ms)

        self.text = self.fonte.render(self.tempo, 1, BRANCO)
        self.textpos = self.text.get_rect()

        self.barra = self.fonte.render("|          |", 1, BRANCO)
        self.barrapos = self.barra.get_rect()

        self.barrapos.centerx = TELA.get_width()/2
        self.textpos.centerx = TELA.get_width()/2

        TELA.blit(self.text, self.textpos)
        TELA.blit(self.barra, self.barrapos)
        TELA.blit(TELA, (0, 0))
