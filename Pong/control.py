from Pong.bola import Bola
from Pong.placar import Timer


class Control():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.bola = Bola((15, 15), 4, self.player1, self.player2)
        self.timer = Timer()
        self.tempo_aux = 0

    def contagem(self):
        self.player1.placar.contagem()
        self.player2.placar.contagem()

    def time_evets(self, ms):
        self.tempo = (ms//1000)
        self.timer.exibe_tempo(ms)
        if (self.tempo != self.tempo_aux):
            self.tempo_aux = (ms//1000)

    def check_win(self, m, s):
        self.tempo = self.timer.return_time()
        if self.tempo == (f"{m}:{s}"):
            return True
        return False
