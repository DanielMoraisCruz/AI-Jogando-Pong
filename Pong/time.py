import pygame

from Pong.globals import WHITE, WINDOW


class Timer():

    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.time = self.edit_ms_for_time()

    def displays_time(self, ms):
        self.time = self.edit_ms_for_time(ms)

        self.text = self.font.render(self.time, 1, WHITE)
        self.text_pos = self.text.get_rect()

        self.bar = self.font.render("|          |", 1, WHITE)
        self.bar_pos = self.bar.get_rect()

        self.bar_pos.centerx = WINDOW.get_width()/2
        self.text_pos.centerx = WINDOW.get_width()/2

        WINDOW.blit(self.text, self.text_pos)
        WINDOW.blit(self.bar, self.bar_pos)
        WINDOW.blit(WINDOW, (0, 0))

    def edit_ms_for_time(self, ms=0):
        self.time = (ms//1000)
        self.s = 0
        self.m = 0
        while self.time >= 60:
            self.m += 1
            self.time -= 60
        self.s = self.time

        if (self.s < 10):
            self.s = "0" + str(self.s)
        if (self.m < 10):
            self.m = "0" + str(self.m)
        self.x = (f"{self.m}:{self.s}")
        return self.x

    def edit_time_for_ms(self, time):
        self.m = time[0:1]
        self.s = time[3:4]
        self.ms = (self.m*60+self.s)*1000
        return self.ms
