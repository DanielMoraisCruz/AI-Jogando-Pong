import pygame

from Pong.control import Control
from Pong.globais import PRETO, TELA
from Pong.player import Player


def run_Pong():
    fim = False
    frams = 30

    tempo = pygame.time.Clock()
    pygame.display.set_caption("Pong")

    player1 = Player((20, 100), 15, 'left')
    player2 = Player((20, 100), 15, 'right')
    control = Control(player1, player2)

    while not(fim):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim = True

        TELA.fill(PRETO)

        control.player1.realiza()
        control.player1.atualiza(pygame.key.get_pressed())

        control.player2.realiza()
        control.player2.atualiza(pygame.key.get_pressed())

        control.bola.realiza()
        control.bola.atualiza()

        tempo.tick(frams)

        control.contagem()

        pygame.display.update()
