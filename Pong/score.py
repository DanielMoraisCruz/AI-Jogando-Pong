import pygame

from Pong.globals import WHITE, WINDOW


class Score():
    def __init__(self, type):
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.points = 0
        self.set_points = 0

        self.type = type

    def counter_score(self):
        self.text = self.font.render((f"{str(self.points)}"), 1, WHITE)
        self.text_pos = self.text.get_rect()

        distance = 55
        if self.type == 'right':
            self.text_pos.centerx = WINDOW.get_width()/2 + distance
        else:
            self.text_pos.centerx = WINDOW.get_width()/2 - distance

        WINDOW.blit(self.text, self.text_pos)
        WINDOW.blit(WINDOW, (0, 0))
