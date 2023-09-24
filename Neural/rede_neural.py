from random import uniform

import numpy as np

from Pong.globals import DISPLAY_SIZE


class Initial_weights():
    # Constructor
    def __init__(self, player_file=0) -> None:
        # If player_file is not empty
        if player_file != 0:
            # Open the file and save the weights in the following variables
            with open(player_file, 'rb') as file:
                self.weights_input_layer_1N = np.load(file)
                self.weights_input_layer_2N = np.load(file)
                self.weights_hidden_layer_1N = np.load(file)
                self.weights_hidden_layer_2N = np.load(file)
                self.output_weights = np.load(file)
        # If player_file is empty
        else:
            # Create random weights for each variable
            self.weights_input_layer_1N = self.random_weights(4)
            self.weights_input_layer_2N = self.random_weights(4)
            self.weights_hidden_layer_1N = self.random_weights(2)
            self.weights_hidden_layer_2N = self.random_weights(2)
            self.output_weights = self.random_weights(2)

    # Function to generate random weights
    def random_weights(self, n: int) -> np.ndarray:
        return np.array([uniform(-1, 1) for i in range(n)])


class Rede_neural():
    def __init__(self, player, ball, bias=-1):

        self.player_pos_y = player.player_pos_y / DISPLAY_SIZE[1]
        self.ball_pos_x = ball.ball_pos_x / DISPLAY_SIZE[0]
        self.ball_pos_y = ball.ball_pos_y / DISPLAY_SIZE[1]

        self.inputs = np.array([self.player_pos_y, self.ball_pos_x,
                                self.ball_pos_y, bias])

        # Gerando/retornando Pesos iniciais
        self.initial_weights = player.initial_weights

        # Pesos das camadas de entrada
        self.weights_IL_1N = self.initial_weights.weights_input_layer_1N
        self.weights_IL_2N = self.initial_weights.weights_input_layer_2N

        # Pesos das camadas ocultas
        self.weights_HL_1N = self.initial_weights.weights_hidden_layer_1N
        self.weights_HL_2N = self.initial_weights.weights_hidden_layer_2N

        # Pesos da camada de Saída
        self.output_weights = self.initial_weights.output_weights

    def activate(self, inputs, weights, activation_function):
        # Somando a multiplicação de entradas e pesos
        self.sum_inputs_weights = np.sum(inputs * weights)
        # Aplicando a Função de Ativação
        return activation_function(self.sum_inputs_weights)

    def feed_forward(self):
        # Inserindo Entradas e pesos do 1N na função de ativação
        self.output_IL_1N = self.activate(self.inputs,
                                          self.weights_IL_1N,
                                          tan_hyper)

        # Inserindo Entradas e pesos do 2N na função de ativação
        self.output_IL_2N = self.activate(self.inputs,
                                          self.weights_IL_2N,
                                          tan_hyper)

        # Criando array com saída do 1N e 2N
        self.array_IL_1N_2N = np.array([self.output_IL_1N,
                                        self.output_IL_2N])

        # Inserindo as saídas de 1N_2N e os pesos do HL_1N na
        # função de ativação
        self.output_HL_1N = self.activate(self.array_IL_1N_2N,
                                          self.weights_HL_1N,
                                          tan_hyper)

        # Inserindo as saídas de 1N_2N e os pesos do HL_2N na
        # função de ativação
        self.output_HL_2N = self.activate(self.array_IL_1N_2N,
                                          self.output_IL_2N,
                                          tan_hyper)

        # Criando array com saída do HL_1N e HL_2N
        self.array_OW = np.array([self.output_HL_1N,
                                  self.output_HL_2N])

        # Inserindo as saídas dos 1N e 2N Ocultos e os
        # pesos do Neurônio de Saida na função de ativação
        self.resultant = self.activate(self.array_OW,
                                       self.output_weights,
                                       sigmoid)

        return self.resultant

    def norma_upw(self, inputs_weights, alpha_,
                  error_, inp=None, out_1=None, out_2=None):
        for i in range(len(inputs_weights)):
            if i == 0:
                inp = out_1
            elif i == 1:
                inp = out_2
            inputs_weights[i] += (alpha_ * inp * error_)

    def updates_weights(self, error, alpha=0.001):

        # Faz a alteração dos pesos do Neurônio da camada de saída
        self.norma_upw(
            inputs_weights=self.initial_weights.output_weights,
            alpha_=alpha,
            error_=error,
            inp=self.inputs,
            out_1=self.output_HL_1N,
            out_2=self.output_HL_2N
        )

        # Faz a alteração dos pesos do 1N da camada oculta
        self.norma_upw(
            inputs_weights=self.initial_weights.weights_hidden_layer_1N,
            alpha_=alpha,
            error_=error,
            inp=self.inputs,
            out_1=self.output_IL_1N,
            out_2=self.output_IL_2N
        )

        # Faz a alteração dos pesos do 2N da camada oculta
        self.norma_upw(
            inputs_weights=self.initial_weights.weights_hidden_layer_2N,
            alpha_=alpha,
            error_=error,
            inp=self.inputs,
            out_1=self.output_IL_1N,
            out_2=self.output_IL_2N
        )

        # Faz a alteração dos pesos do 1N da camada de entrada
        for i in range(len(self.initial_weights.weights_input_layer_1N)):
            self.initial_weights.weights_input_layer_1N[i] += (
                alpha * self.inputs[i] * error)

        # Faz a alteração dos pesos do 2N da camada de entrada
        for i in range(len(self.initial_weights.weights_input_layer_2N)):
            self.initial_weights.weights_input_layer_2N[i] += (
                alpha * self.inputs[i] * error)


def error_calculator(player, ball, weights):
    player.error = (player.player_pos_y - ball.ball_pos_y)/weights
    return player.error


def tan_hyper(x):
    th = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
    return th


def sigmoid(x):  # Função Logística
    return 1 / (1 + np.exp(-x))
