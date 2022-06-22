from Pong.bola import Bola


class Control():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.bola = Bola((15, 15), 15, self.player1, self.player2)

    def contagem(self):
        self.player1.placar.contagem()
        self.player2.placar.contagem()
