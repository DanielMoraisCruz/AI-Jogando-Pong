import pygame

global BLACK, WHITH, FIM, DISPLAY_SIZE, WINDOW, WINDOW_RECT
BLACK = (0, 0, 0)
WHITH = (255, 255, 255)


DISPLAY_SIZE = 800, 600
WINDOW = pygame.display.set_mode(DISPLAY_SIZE)
WINDOW_RECT = WINDOW.get_rect()
