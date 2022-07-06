import pygame

from Pong.menu import MainMenu
from Pong.control import Control
from Pong.globais import BLACK, DISPLAY_SIZE, WHITH, WINDOW
from Pong.player import Player


class Game_run():
    """Inicia Jogo"""

    def __init__(self, frams) -> None:
        pygame.init()

        self.runing, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY = False, False
        self.START_KEY, self.BACK_KEY = False, False

        self.display = pygame.Surface(DISPLAY_SIZE)

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

        self.main_menu = MainMenu(self)
        self.curr_menu = self.main_menu

    def run_Pong(self):
        self.player1.realiza()
        self.player1.atualiza(pygame.key.get_pressed())
        self.player2.realiza()
        self.player2.atualiza(pygame.key.get_pressed())

        self.control.bola.realiza()
        self.control.bola.atualiza()

        self.tempo.tick(self.frams)

        self.control.time_evets(pygame.time.get_ticks())
        self.control.contagem()

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.display.fill(BLACK)

            WINDOW.blit(self.display, (0, 0))

            self.run_Pong()

            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runing, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY = False, False
        self.START_KEY, self.BACK_KEY = False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, WHITH)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)


'''def run_Pong():
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

        WINDOW.fill(BLACK)

        control.player1.realiza()
        control.player1.atualiza(pygame.key.get_pressed())

        control.player2.realiza()
        control.player2.atualiza(pygame.key.get_pressed())

        control.bola.realiza()
        control.bola.atualiza()

        tempo.tick(frams)

        control.time_evets(pygame.time.get_ticks())

        control.contagem()

        if control.check_win():
            ...

        pygame.display.update()
'''
