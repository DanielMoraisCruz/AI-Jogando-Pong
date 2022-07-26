import numpy as np
import pygame
from Neural.rede_neural import Rede_neural, error_calculator

from Pong.control import Control
from Pong.globals import BLACK, DISPLAY_SIZE, HAVE_FILES, WINDOW


class Game_run():
    """Inicia Jogo"""

    def __init__(self, frames) -> None:
        pygame.init()

        self.running, self.playing = True, True

        self.display = pygame.Surface(DISPLAY_SIZE)

        self.frames = frames  # frames por segundo
        self.time = pygame.time.Clock()  # Inicia o Contador
        # Determina que fica no topo da tela

        pygame.display.set_caption("Pong")

        # Cria os dois jogadores, setando-os como
        # player 1 (na esquerda) e player 2 (na direita)

        # Determina-se o Controlador de Eventos do Jogo,
        # passando como variaveis os dois jogadores
        if HAVE_FILES:
            self.control = Control(limit_point=10, speed_ball=5,
                                   limit_speed=40,
                                   file_1="rede_1.npy", file_2="rede_2.npy")
        else:
            self.control = Control(limit_point=10, speed_ball=5,
                                   limit_speed=40)

        self.win = False

    def run_Pong(self):
        if (self.win):
            self.control.reset_time_points()
            self.win = False

        self.rede_1 = Rede_neural(self.control.player_1, self.control.ball)
        self.rede_2 = Rede_neural(self.control.player_2, self.control.ball)

        self.key_player1 = self.rede_1.feed_forward()
        self.key_player2 = self.rede_2.feed_forward()

        self.control.player_1.realize()
        self.control.player_1.update(self.key_player1)
        self.control.player_2.realize()
        self.control.player_2.update(self.key_player2)

        self.control.ball.realize()
        self.control.ball.update()

        # self.error_1 = self.control.player_1.error
        # self.error_2 = self.control.player_2.error

        self.error_1 = error_calculator(self.control.player_1,
                                        self.control.ball, 100)
        self.error_2 = error_calculator(self.control.player_2,
                                        self.control.ball, 100)

        if self.control.player_1.training:
            print("player 1 esta jogando")
            self.rede_1.updates_weights(self.error_1)
        else:
            print("player 2 esta jogando")
            self.rede_2.updates_weights(self.error_2)

        self.time.tick(self.frames)
        self.control.time_events(pygame.time.get_ticks())
        self.control.counter_control()

        self.win_1, self.winier = self.control.check_win_for_point()

        # print(self.control.ball.speed)

        if (self.win_1):
            if self.winier == 1:
                self.control.player_1.score.set_points += 1
            if self.winier == 2:
                self.control.player_2.score.set_points += 1

            self.win = True

    def game_loop(self):
        while self.playing:
            self.check_events()

            self.display.fill(BLACK)

            WINDOW.blit(self.display, (0, 0))

            self.run_Pong()

            pygame.display.update()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_doc_weights(self.rede_1.initial_weights, "rede_1.npy")
                save_doc_weights(self.rede_2.initial_weights, "rede_2.npy")
                self.running, self.playing = False, False

    def run_game(self):

        if self.playing:
            self.game_loop()


def save_doc_weights(weights, name_file):
    weights_IL1N = weights.weights_input_layer_1N
    weights_IL2N = weights.weights_input_layer_2N
    weights_HL1N = weights.weights_hidden_layer_1N
    weights_HL2N = weights.weights_hidden_layer_2N
    output_weights = weights.output_weights
    with open(name_file, 'wb') as arq:
        np.save(arq, weights_IL1N)
        np.save(arq, weights_IL2N)
        np.save(arq, weights_HL1N)
        np.save(arq, weights_HL2N)
        np.save(arq, output_weights)
