import pygame

from Pong.bola import Bola
from Pong.globais import PRETO, TELA
from Pong.placar import Placar
from Pong.player import Player


def run_Pong():
    fim = False
    frams = 30

    tempo = pygame.time.Clock()
    pygame.display.set_caption("Pong")

    player1 = Player((20, 100), 15)
    placar1 = Placar()
    bola = Bola((15, 15), 15, placar1)

    while not(fim):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim = True

        TELA.fill(PRETO)

        player1.realiza()
        player1.atualiza(pygame.key.get_pressed())

        bola.realiza()
        bola.atualiza(player1.imagem_retangulo)

        tempo.tick(frams)

        placar1.contagem()
        pygame.display.update()
