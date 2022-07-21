from Pong.ball import Ball
from Pong.globals import DISPLAY_SIZE
from Pong.player import Player
from Pong.score import Timer


class Control():

    def __init__(self, points, speed_ball, limit_speed, speed_player,
                 limit_speed_player):

        self.size_playerX = DISPLAY_SIZE[0]*0.025
        self.size_playerY = DISPLAY_SIZE[1]*0.167

        self.player1 = Player(
            (self.size_playerX, self.size_playerY), speed_player, 'left',
            limit_speed_player)
        self.player2 = Player(
            (self.size_playerX, self.size_playerY), speed_player, 'right',
            limit_speed_player)

        self.size_ball = DISPLAY_SIZE[0]*0.02

        self.bola = Ball((self.size_ball, self.size_ball),
                         speed_ball, self.player1, self.player2, limit_speed)
        self.timer = Timer()
        self.time_aux = 0
        self.point = points
        self.limit_time = 100000

    def counter_control(self):
        self.player1.score.counter_score()
        self.player2.score.counter_score()

    def time_events(self, ms):
        self.time = (ms//1000)
        self.timer.displays_time(ms)
        if (self.time != self.time_aux):
            self.time_aux = (ms//1000)

    def check_win_for_time(self):
        self.time_at = self.timer.edit_ms_for_time(self.limit_time)
        self.time = self.timer.time
        # print(self.time, self.time_at)
        if self.time == self.time_at:
            if self.player1.score.points > self.player1.score.points:
                return True, 1
            elif self.player1.score.points > self.player1.score.points:
                return True, 2
            else:
                return True, 3
        return False, 0

    def check_win_for_point(self):
        # print(self.player1.score.points, self.point)
        # print(self.player2.score.points, self.point)
        if self.player1.score.points >= self.point:
            return True, 1
        if self.player2.score.points >= self.point:
            return True, 2
        return False, 0

    def reset_time_points(self):
        self.player1.score.points = 0
        self.player2.score.points = 0
