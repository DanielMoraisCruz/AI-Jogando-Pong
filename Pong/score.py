import pygame

from Pong.globals import WHITE, WINDOW


class Score():
    def __init__(self, tipo):
        pygame.font.init()
        self.fonte = pygame.font.Font(None, 36)
        self.points = 0

        self.tipo = tipo

    def counter_score(self):
        self.text = self.fonte.render((f"{str(self.points)}"), 1, WHITE)
        self.textpos = self.text.get_rect()

        distancia = 55
        if self.tipo == 'right':
            self.textpos.centerx = WINDOW.get_width()/2 + distancia
        else:
            self.textpos.centerx = WINDOW.get_width()/2 - distancia

        WINDOW.blit(self.text, self.textpos)
        WINDOW.blit(WINDOW, (0, 0))


class Timer():

    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.time = self.edit_ms_for_time()

    def displays_time(self, ms):
        self.time = self.edit_ms_for_time(ms)

        self.text = self.font.render(self.time, 1, WHITE)
        self.textpos = self.text.get_rect()

        self.barra = self.font.render("|          |", 1, WHITE)
        self.barrapos = self.barra.get_rect()

        self.barrapos.centerx = WINDOW.get_width()/2
        self.textpos.centerx = WINDOW.get_width()/2

        WINDOW.blit(self.text, self.textpos)
        WINDOW.blit(self.barra, self.barrapos)
        WINDOW.blit(WINDOW, (0, 0))

    def edit_ms_for_time(self, ms=0):
        time = (ms//1000)
        s = 0
        m = 0
        while time >= 60:
            m += 1
            time -= 60
        s = time

        if (s < 10):
            s = "0" + str(s)
        if (m < 10):
            m = "0" + str(m)
        x = (f"{m}:{s}")
        return x

    def edit_time_for_ms(self, time):
        m = time[0:1]
        s = time[3:4]
        ms = (m*60+s)*1000
        return ms
