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
        self.seconds = 0
        self.minutes = 0
        while self.time >= 60:
            self.minutes += 1
            self.time -= 60
        self.seconds = self.time

        if (self.seconds < 10):
            self.seconds = "0" + str(self.seconds)
        if (self.minutes < 10):
            self.minutes = "0" + str(self.minutes)
        self.result_time = (f"{self.minutes}:{self.seconds}")
        return self.result_time

    def edit_time_for_ms(self, time):
        self.minutes = int(time[0:1])
        self.seconds = int(time[3:4])
        self.ms = (self.minutes*60+self.seconds)*1000
        return self.ms
