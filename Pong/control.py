from Pong.ball import Ball
from Pong.placar import Timer


class Control():

    def __init__(self, player1, player2, points, vel_ball, limit_vel):
        self.player1 = player1
        self.player2 = player2
        self.bola = Ball((15, 15), vel_ball, self.player1,
                         self.player2, limit_vel)
        self.timer = Timer()
        self.time_aux = 0
        self.point = points
        self.limit_time = 100000

    def counter_control(self):
        self.player1.placar.counter_placar()
        self.player2.placar.counter_placar()

    def time_evets(self, ms):
        self.time = (ms//1000)
        self.timer.displays_time(ms)
        if (self.time != self.time_aux):
            self.time_aux = (ms//1000)

    def check_win_for_time(self):
        self.time_at = self.timer.edit_ms_for_time(self.limit_time)
        self.time = self.timer.time
        # print(self.time, self.time_at)
        if self.time == self.time_at:
            if self.player1.placar.pontos > self.player1.placar.pontos:
                return True, 1
            elif self.player1.placar.pontos > self.player1.placar.pontos:
                return True, 2
            else:
                return True, 3
        return False, 0

    def check_win_for_point(self):
        # print(self.player1.placar.pontos, self.point)
        # print(self.player2.placar.pontos, self.point)
        if self.player1.placar.pontos == self.point:
            return True, 1
        if self.player2.placar.pontos == self.point:
            return True, 2
        return False, 0
