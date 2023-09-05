import time as tm

from Pong.ball import Ball
from Pong.globals import DISPLAY_SIZE
from Pong.player import Player
from time_1 import Timer


class Control():
    def __init__(self, limit_point, speed_ball, limit_speed,
                 file_1=0, file_2=0):

        self.size_player_x = DISPLAY_SIZE[0]*0.02
        self.size_player_y = DISPLAY_SIZE[1]*0.15
        self.speed_player = speed_ball*2
        self.player_1 = Player((self.size_player_x, self.size_player_y),
                               self.speed_player, 'left', file_1)
        self.player_2 = Player((self.size_player_x, self.size_player_y),
                               self.speed_player, 'right', file_2)

        self.size_ball = DISPLAY_SIZE[0]*0.02
        self.ball = Ball((self.size_ball, self.size_ball),
                         speed_ball, limit_speed,
                         self.player_1, self.player_2)

        self.timer = Timer()
        self.limit_point = limit_point

    def counter_control(self):
        self.player_1.score.counter_score()
        self.player_2.score.counter_score()

    def time_events(self, ms):
        self.timer.displays_time(ms)

    def check_win_for_point(self):
        if self.player_1.score.points >= self.limit_point:
            return True, 1
        if self.player_2.score.points >= self.limit_point:
            return True, 2
        return False, 0

    def reset_time_points(self):
        tm.sleep(0.5)

        self.player_1.score.points = 0
        self.player_2.score.points = 0
