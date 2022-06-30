import pygame

from Pong.control import Control
from Pong.globais import PRETO, TELA
from Pong.player import Player


class Game_run():
    """Inicia Jogo"""

    def __init__(self, frams) -> None:
        self.run = False  # determina se o jogo está iniciado
        self.frams = frams  # frams por segundo
        self.tempo = pygame.time.Clock()  # Inicia o Contador
        # Determina que fica no topo da tela
        pygame.display.set_caption("Pong")

        # Cria os dois jogadores, setando-os como
        # player 1 (na esquerda) e player 2 (na direita)
        self.player1 = Player((20, 100), 15, 'left')
        self.player2 = Player((20, 100), 15, 'right')

        # Determina-se o Controlador de Eventos do Jogo,
        # passando como variaveis os dois jogadores
        self.control = Control(self.player1, self.player2)
        self.run_Pong()

    def run_Pong(self):
        while not(self.run):
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.run = True
            TELA.fill(PRETO)
            self.control.player1.realiza()
            self.control.player1.atualiza(pygame.key.get_pressed())
            self.control.player2.realiza()
            self.control.player2.atualiza(pygame.key.get_pressed())
            self.control.bola.realiza()
            self.control.bola.atualiza()
            self.tempo.tick(self.frams)
            self.control.time_evets(pygame.time.get_ticks())
            self.control.contagem()
            pygame.display.update()


def run_Pong():
    fim = False
    frams = 60

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

        control.time_evets(pygame.time.get_ticks())

        control.contagem()

        pygame.display.update()
