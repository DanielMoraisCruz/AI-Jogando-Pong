import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

DISPLAY_SIZE = 800, 600
FPS = 400

WINDOW = pygame.display.set_mode(DISPLAY_SIZE)
WINDOW_RECT = WINDOW.get_rect()

HAVE_FILES = True  # ,False  # ,
PLOT_RESULTS = True  # ,False  # ,
# Caso queria treinar um novo conjunto de agentes Troque para False
