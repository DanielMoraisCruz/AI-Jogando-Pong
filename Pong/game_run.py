import pygame

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
        self.control = Control(points=10, speed_ball=40,
                               limit_speed=100, speed_player=15,
                               limit_speed_player=50)

    def run_Pong(self):
        self.control.player1.realize()
        self.control.player1.actualize(pygame.key.get_pressed())
        self.control.player2.realize()
        self.control.player2.actualize(pygame.key.get_pressed())

        self.control.bola.realize()
        self.control.bola.actualize()

        self.time.tick(self.frames)

        self.control.time_events(pygame.time.get_ticks())
        self.control.counter_control()

        self.win_1, self.winier = self.control.check_win_for_point()
        self.win_2, self.winier = self.control.check_win_for_time()

        if (self.win_1 or self.win_2):
            self.control.reset_time_points()

    def game_loop(self):
        while self.playing:
            self.check_events()

            self.display.fill(BLACK)

            WINDOW.blit(self.display, (0, 0))

            self.run_Pong()

            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY = False, False
        self.START_KEY, self.BACK_KEY = False, False

    def run_game(self):

        if self.playing:
            self.game_loop()
