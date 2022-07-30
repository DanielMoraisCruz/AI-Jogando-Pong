import time as tm
from asyncio.windows_events import NULL

from Neural.rede_neural import error_calculator

from Pong.ball import Ball
from Pong.globals import DISPLAY_SIZE
from Pong.player import Player
from Pong.time import Timer


class Control():

    def __init__(self, limit_point, speed_ball, limit_speed,
                 file_1=NULL, file_2=NULL):

        self.size_player_x = DISPLAY_SIZE[0]*0.02
        self.size_player_y = DISPLAY_SIZE[1]*0.15
        self.speed_player = speed_ball*1.5
        self.player_1 = Player((self.size_player_x, self.size_player_y),
                               self.speed_player, 'left', file_1)
        self.player_2 = Player((self.size_player_x, self.size_player_y),
                               self.speed_player, 'right', file_2)

        self.size_ball = DISPLAY_SIZE[0]*0.02
        self.ball = Ball((self.size_ball, self.size_ball),
                         speed_ball, limit_speed, self.player_1, self.player_2)

        self.timer = Timer()
        self.time_aux = 0
        self.limit_point = limit_point
        self.time_up_speed = '00:30'

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
        if self.player_1.score.points > self.player_2.score.points:
            self.player_1.error = 0
            self.player_2.error = error_calculator(self.player_2,
                                                   self.ball, 10)

            self.player_1.training = False
            self.player_2.training = True

        elif self.player_2.score.points > self.player_1.score.points:
            self.player_2.error = 0
            self.player_1.error = error_calculator(self.player_1,
                                                   self.ball, 10)

            self.player_2.training = False
            self.player_1.training = True

        self.player_1.score.points = 0
        self.player_2.score.points = 0
