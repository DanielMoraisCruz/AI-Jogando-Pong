import pygame
from Neural.rede_neural import Rede_neural

from Pong.control import Control
from Pong.globals import BLACK, DISPLAY_SIZE, WINDOW


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
        self.control = Control(limit_point=100, speed_ball=8,
                               limit_speed=8, speed_player=10,
                               limit_speed_player=10)

        self.win = False

    def run_Pong(self):
        if (self.win):
            self.control.reset_time_points()
            self.win = False

        # print("Bola X e Y: ", self.ball_pos_x, self.ball_pos_y)
        # print("player_1: ", self.player1_pos_y)
        # print("player_2: ", self.player2_pos_y)

        self.rede_1 = Rede_neural(self.control.player_1, self.control.ball)
        self.rede_2 = Rede_neural(self.control.player_2, self.control.ball)

        self.key_player1 = self.rede_1.feed_forward()
        self.key_player2 = self.rede_2.feed_forward()

        with open('data_training.txt', 'a') as arq:
            arq.write(str((self.key_player1)) + "\n")
            arq.write(str((self.key_player2)) + "\n")

        self.control.player_1.realize()
        self.control.player_1.update(self.key_player1)
        self.control.player_2.realize()
        self.control.player_2.update(self.key_player2)

        self.control.ball.realize()
        self.control.ball.update()

        self.error_1 = self.rede_1.error_calculator(self.control.player_1,
                                                    self.control.ball, 100)
        self.error_2 = self.rede_2.error_calculator(self.control.player_2,
                                                    self.control.ball, 100)

        self.rede_1.updates_weights(self.error_1)
        self.rede_2.updates_weights(self.error_2)

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
                self.running, self.playing = False, False

    def run_game(self):

        if self.playing:
            self.game_loop()
