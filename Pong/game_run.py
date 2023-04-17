import numpy as np
import pygame
from matplotlib import pyplot as plt
from Neural.rede_neural import Rede_neural, error_calculator

from Pong.control import Control
from Pong.globals import BLACK, DISPLAY_SIZE, HAVE_FILES, WINDOW


def save_doc_weights(weights, name_file):
    weights_IL1N = weights.weights_input_layer_1N
    weights_IL2N = weights.weights_input_layer_2N
    weights_HL1N = weights.weights_hidden_layer_1N
    weights_HL2N = weights.weights_hidden_layer_2N
    output_weights = weights.output_weights

    with open(name_file, 'wb') as file:
        np.save(file, weights_IL1N)
        np.save(file, weights_IL2N)
        np.save(file, weights_HL1N)
        np.save(file, weights_HL2N)
        np.save(file, output_weights)


def save_item(item, name_file):
    with open(name_file, 'a') as file:
        file.write(str((item)) + "\n")


def graphic_plot(file):
    time_in_game = []
    with open(file, 'r') as file:
        arq_2 = file.readlines()
        arq_2 = [float(dado) for dado in arq_2]
    for i in range(len(arq_2)):
        time_in_game.append(i)

    plt.plot(time_in_game, arq_2)
    plt.show()


class Game_run():
    """Inicia Jogo"""

    def __init__(self, fps) -> None:
        pygame.init()

        self.running, self.playing = True, True

        self.display = pygame.Surface(DISPLAY_SIZE)

        self.frames = fps  # frames por segundo
        self.time = pygame.time.Clock()  # Inicia o Contador
        # Determina que fica no topo da tela

        pygame.display.set_caption("Pong")

        # Cria os dois jogadores, setando-os como
        # player 1 (na esquerda) e player 2 (na direita)

        # Determina-se o Controlador de Eventos do Jogo,
        # passando como variaveis os dois jogadores
        self._limit_point = 12
        self._speed_ball = 1
        self._limit_speed = 39  # A maior velosidade alcançada
        self._file_1 = "rede_1.npy"
        self._file_2 = "rede_2.npy"
        if HAVE_FILES:
            self.control = Control(self._limit_point, self._speed_ball,
                                   self._limit_speed,
                                   self._file_1, self._file_2)
        else:
            self.control = Control(self._limit_point,
                                   self._speed_ball,
                                   self._limit_speed)

        self.win = False

        self.count_i = 0
        self.salto = 10
        self.multi = 10

        self.game_type = (False, False)

    def run_Pong(self):
        if (self.win):
            self.control.reset_time_points()
            self.win = False

        # Criação da rede neural do agente da esquerda
        # E atualização do valores de entrada
        self.rede_1 = Rede_neural(self.control.player_1,  # posição do player
                                  self.control.ball)  # posição x e y da bola

        # Criação da rede neural do agente da esquerda
        # E atualização do valores de entrada
        self.rede_2 = Rede_neural(self.control.player_2,  # posição do player
                                  self.control.ball)  # posição x e y da bola

        self.key_player1 = self.rede_1.feed_forward()
        self.key_player2 = self.rede_2.feed_forward()

        # Erro atualizado a cada interação
        self.error_1 = error_calculator(self.control.player_1,
                                        self.control.ball, 1000)
        self.error_2 = error_calculator(self.control.player_2,
                                        self.control.ball, 1000)

        if self.count_i % self.salto == 0:
            save_item(abs(self.key_player1*self.multi),
                      "resultants_1.txt")
            save_item(abs(self.key_player2*self.multi),
                      "resultants_2.txt")

        self.control.player_1.realize()

        if self.game_type[0]:
            self.control.player_1.update(pygame.key.get_pressed(), 1)
        else:
            self.control.player_1.update(self.key_player1)

        self.control.player_2.realize()
        if self.game_type[1]:
            self.control.player_2.update(pygame.key.get_pressed(), 2)
        else:
            self.control.player_2.update(self.key_player2)

        self.control.ball.realize()
        self.control.ball.update()

        self.rede_1.updates_weights(self.error_1)
        self.rede_2.updates_weights(self.error_2)

        if self.count_i % self.salto == 0:
            save_item(abs(self.error_2*self.multi),
                      "errors_player_2.txt")
            save_item(abs(self.error_1*self.multi),
                      "errors_player_1.txt")
        self.count_i += 1

        self.time.tick(self.frames)
        self.control.time_events(pygame.time.get_ticks())
        self.control.counter_control()

        self.win_1, self.winier = self.control.check_win_for_point()

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
                save_doc_weights(self.rede_1.initial_weights,
                                 "rede_1.npy")
                save_doc_weights(self.rede_2.initial_weights,
                                 "rede_2.npy")

                if HAVE_FILES:
                    graphic_plot("errors_player_1.txt")
                    graphic_plot("errors_player_2.txt")
                    graphic_plot("speed_ball.txt")

                self.running, self.playing = False, False

    def run_game(self):

        if self.playing:
            self.game_loop()
