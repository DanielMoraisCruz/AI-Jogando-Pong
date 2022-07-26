import time as tm

from Pong.ball import Ball
from Pong.globals import DISPLAY_SIZE
from Pong.player import Player
from Pong.time import Timer


class Control():

    def __init__(self, limit_point, speed_ball, limit_speed, speed_player,
                 limit_speed_player):

        self.size_playerX = DISPLAY_SIZE[0]*0.02
        self.size_playerY = DISPLAY_SIZE[1]*0.15
        self.player_1 = Player(
            (self.size_playerX, self.size_playerY), speed_player, 'left',
            limit_speed_player)
        self.player_2 = Player(
            (self.size_playerX, self.size_playerY), speed_player, 'right',
            limit_speed_player)

        self.size_ball = DISPLAY_SIZE[0]*0.02
        self.ball = Ball((self.size_ball, self.size_ball),
                         speed_ball, self.player_1, self.player_2, limit_speed)

        self.timer = Timer()
        self.time_aux = 0
        self.limit_point = limit_point
        self.time_up_speed = '00:30'

    def counter_control(self):
        self.player_1.score.counter_score()
        self.player_2.score.counter_score()

    def time_events(self, ms):
        self.time_game = self.timer.edit_ms_for_time(ms)
        if self.time_game == self.time_up_speed:
            self.player_1.speed += 1
            self.player_2.speed += 1
            self.new_time = self.timer.edit_time_for_ms(
                self.time_up_speed)+(30*1000)
            self.time_up_speed = self.timer.edit_ms_for_time(self.new_time)

        self.timer.displays_time(ms)

    def check_win_for_point(self):
        # print(self.player_1.score.points, self.point)
        # print(self.player_2.score.points, self.point)
        if self.player_1.score.points >= self.limit_point:
            return True, 1
        if self.player_2.score.points >= self.limit_point:
            return True, 2
        return False, 0

    def reset_time_points(self):
        tm.sleep(0.5)
        self.player_1.score.points = 0
        self.player_2.score.points = 0
