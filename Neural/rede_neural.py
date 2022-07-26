from asyncio.windows_events import NULL
from random import uniform
from threading import Thread

import numpy as np
from Pong.globals import DISPLAY_SIZE


class Initial_weights():
    def __init__(self, file=NULL) -> None:

        if file != NULL:
            with open(file, 'rb') as arq:
                self.weights_input_layer_1N = np.load(arq)
                self.weights_input_layer_2N = np.load(arq)
                self.weights_hidden_layer_1N = np.load(arq)
                self.weights_hidden_layer_2N = np.load(arq)
                self.output_weights = np.load(arq)
        else:
            self.weights_input_layer_1N = self.random_weights(4)
            self.weights_input_layer_2N = self.random_weights(4)
            self.weights_hidden_layer_1N = self.random_weights(2)
            self.weights_hidden_layer_2N = self.random_weights(2)
            self.output_weights = self.random_weights(2)

    def random_weights(self, n):
        return np.array([uniform(-1, 1) for i in range(n)])


class Rede_neural(Thread):
    def __init__(self, player, ball, bias=-1):
        # ball_speed, player_speed

        self.player_pos_y = player.player_pos_y / DISPLAY_SIZE[1]
        self.ball_pos_x = ball.ball_pos_x / DISPLAY_SIZE[0]
        self.ball_pos_y = ball.ball_pos_y / DISPLAY_SIZE[1]

        self.inputs = np.array([self.player_pos_y, self.ball_pos_x,
                                self.ball_pos_y, bias])

        self.initial_weights = player.initial_weights

        self.weights_IL_1N = self.initial_weights.weights_input_layer_1N
        self.weights_IL_2N = self.initial_weights.weights_input_layer_2N

        self.weights_HL_1N = self.initial_weights.weights_hidden_layer_1N
        self.weights_HL_2N = self.initial_weights.weights_hidden_layer_2N

        self.output_weights = self.initial_weights.output_weights

    def feed_forward(self):

        self.sum_inputs_weights_IL_1N = np.sum(self.inputs *
                                               self.weights_IL_1N)

        self.output_IL_1N = self.tan_hyper(self.sum_inputs_weights_IL_1N)

        self.sum_inputs_weights_2N = np.sum(self.inputs * self.weights_IL_2N)
        self.output_IL_2N = self.tan_hyper(self.sum_inputs_weights_2N)

        self.outputs_array_IL_1N = np.array([self.output_IL_1N,
                                             self.output_IL_1N])

        self.sum_outputs_WH_1N = np.sum(self.outputs_array_IL_1N *
                                        self.weights_HL_1N)

        self.output_HL_1N = self.tan_hyper(self.sum_outputs_WH_1N)

        self.outputs_array_IL_2N = np.array([self.output_IL_1N,
                                             self.output_IL_2N])

        self.sum_outputs_WH_2N = np.sum(self.outputs_array_IL_2N *
                                        self.output_IL_2N)

        self.output_HL_2N = self.tan_hyper(self.sum_outputs_WH_2N)

        self.outputs_array_OW = np.array([self.output_HL_1N,
                                          self.output_HL_2N])

        self.sum_outputs_OW = np.sum(self.outputs_array_OW *
                                     self.output_weights)

        self.resultant = self.sigmoid(self.sum_outputs_OW)

        # with open('ff_resultant.txt', 'a') as arq:
        #     arq.write(str((self.resultant)) + "\n")

        return self.resultant

    def tan_hyper(self, x):
        self.th = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
        return self.th

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def updates_weights(self, error, alpha=0.01):

        for i in range(len(self.initial_weights.output_weights)):
            if i == 0:
                self.input = self.output_HL_1N
            elif i == 1:
                self.input = self.output_HL_2N

            self.initial_weights.output_weights[i] += (
                alpha * self.input * error)

        for i in range(len(self.initial_weights.weights_hidden_layer_1N)):
            if i == 0:
                self.input1 = self.output_IL_1N
            if i == 1:
                self.input1 = self.output_IL_2N

            self.initial_weights.weights_hidden_layer_1N[i] += (
                alpha * self.input1 * error)

        for i in range(len(self.initial_weights.weights_hidden_layer_2N)):
            if i == 0:
                self.input2 = self.output_IL_1N
            if i == 1:
                self.input2 = self.output_IL_2N

            self.initial_weights.weights_hidden_layer_2N[i] += (
                alpha * self.input2 * error)

        for i in range(len(self.initial_weights.weights_input_layer_1N)):
            self.initial_weights.weights_input_layer_1N[i] += (
                alpha * self.inputs[i] * error)

        for i in range(len(self.initial_weights.weights_input_layer_2N)):
            self.initial_weights.weights_input_layer_2N[i] += (
                alpha * self.inputs[i] * error)

        # print(self.resultant)

        # with open('data_weights.txt', 'a') as arq:
        #     arq.write(str((self.weights_IL_1N)) + " " +
        #               str((self.weights_IL_2N)) + "\n" +
        #               str((self.weights_HL_1N)) + " " +
        #               str((self.weights_HL_2N)) + "\n" +
        #               str((self.output_weights)) + "\n")
#
        # with open('data_resultant.txt', 'a') as arq:
        #     arq.write(str((self.resultant)) + "\n")


def error_calculator(player, ball, weights):
    player.error = (player.player_pos_y-ball.ball_pos_y)/weights
    return player.error
