import numpy as np
import random
from random import uniform
from threading import Thread

import pygame
from pygame.locals import *

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

gameOver = False
TAMANHO = (800, 600)

tela = pygame.display.set_mode(TAMANHO)
tela_retangulo = tela.get_rect()

pygame.display.set_caption("rede neural jogando pong")

posicaoYraquete = 0


class Raquete:
    def __init__(self, tamanho):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(VERDE)
        self.imagem_retangulo = self.imagem.get_rect()
        self.imagem_retangulo[0] = 0

    def move(self, y):
        self.imagem_retangulo[1] += y * 10

        global posicaoYraquete
        posicaoYraquete = self.imagem_retangulo.centery

    def atualiza(self, tecla):
        if tecla > 0.5:
            self.move(-1)
        elif tecla < 0.5:
            self.move(1)
        self.imagem_retangulo.clamp_ip(tela_retangulo)

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)


posicaoYbola = 0

posicaoXbola = 0

erro = 0


class Bola:
    def __init__(self, tamanho):
        self.altura, self.largura = tamanho
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(VERMELHO)
        self.imagem_retangulo = self.imagem.get_rect()
        self.setBola()
        global erro
        self.erro = 0

    def aleatorio(self):
        while True:
            num = random.uniform(-1, 1)
            if num > -0.5 and num < 0.5:
                continue
            else:
                return num

    def setBola(self):
        x = self.aleatorio()
        y = self.aleatorio()
        self.imagem_retangulo.x = tela_retangulo.centerx
        self.imagem_retangulo.y = tela_retangulo.centery
        self.velo = [x, y]
        self.pos = list(tela_retangulo.center)

    def colideParede(self):
        if self.imagem_retangulo.y <= 0 or self.imagem_retangulo.y > tela_retangulo.bottom - self.altura:
            self.velo[1] *= -1

        if self.imagem_retangulo.x <= 0 or self.imagem_retangulo.x > tela_retangulo.right - self.largura:
            self.velo[0] *= -1
            if self.imagem_retangulo.x <= 0:
                placar1.pontos -= 1
                print("bateu na parede !")

    def move(self):
        self.pos[0] += self.velo[0] * 4
        self.pos[1] += self.velo[1] * 4
        self.imagem_retangulo.center = self.pos

    def colideRaquete(self, raqueteRect):
        if self.imagem_retangulo.colliderect(raqueteRect):
            self.velo[0] *= -1
            placar1.pontos += 1
            print('voce defendeu')

            global erro
            erro = 0

    def atualiza(self, raqueteRect):
        self.colideParede()
        global posicaoYbola, posicaoXbola
        posicaoYbola = self.imagem_retangulo.y
        posicaoXbola = self.imagem_retangulo.x
        self.colideRaquete(raqueteRect=raqueteRect)
        self.move()

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)


class Placar:
    def __init__(self):
        pygame.font.init()
        self.fonte = pygame.font.Font(None, 36)
        self.pontos = 0

    def contagem(self):
        self.text = self.fonte.render(
            "Pontos = " + str(self.pontos), 1, (255, 255, 255))
        self.textpos = self.text.get_rect()
        self.textpos.centerx = tela.get_width() / 2
        tela.blit(self.text, self.textpos)
        tela.blit(tela, (0, 0))


raquete = Raquete((10, 100))
ball = Bola((15, 15))
placar1 = Placar()

tecla = 0


pesosPrimeiroNeuronioCamadaEntrada = np.array(
    [uniform(-1, 1) for i in range(4)])
pesosSegundoNeuronioCamadaEntrada = np.array(
    [uniform(-1, 1) for i in range(4)])

pesosPrimeiroNeuronioCamadaOculta = np.array(
    [uniform(-1, 1) for i in range(2)])
pesosSegundoNeuronioCamadaOculta = np.array([uniform(-1, 1) for i in range(2)])

pesosNeuronioDeSaida = np.array([uniform(-1, 1) for i in range(2)])


class RedeNeural(Thread):
    def __init__(self, YRaquete, XBolinha, YBola, bias=-1):

        self.entradas = np.array([YRaquete, XBolinha, YBola, bias])
        global pesosPrimeiroNeuronioCamadaEntrada, pesosSegundoNeuronioCamadaEntrada, pesosPrimeiroNeuronioCamadaOculta, pesosSegundoNeuronioCamadaOculta

        self.pesosPrimeiroNeuronioCamadaEntrada = pesosPrimeiroNeuronioCamadaEntrada
        self.pesosSegundoNeuronioCamadaEntrada = pesosSegundoNeuronioCamadaEntrada

        self.pesosPrimeiroNeuronioCamadaOculta = pesosPrimeiroNeuronioCamadaOculta
        self.pesosSegundoNeuronioCamadaOculta = pesosSegundoNeuronioCamadaOculta

        self.pesosNeuronioDeSaida = pesosNeuronioDeSaida

    def feedforward(self):

        self.saidaPrimeiroNeuronioCamadaEntrada = round(self.tangenteHiperbolica(
            np.sum(self.entradas * self.pesosPrimeiroNeuronioCamadaEntrada)), 6)

        self.saidaSegundoNeuronioCamadaEntrada = round(self.tangenteHiperbolica(
            np.sum(self.entradas * self.pesosSegundoNeuronioCamadaEntrada)), 6)

        self.saidaPrimeiroNeuronioCamadaOculta = round(self.tangenteHiperbolica(np.sum(np.array(
            [self.saidaPrimeiroNeuronioCamadaEntrada, self.saidaPrimeiroNeuronioCamadaEntrada]) * self.pesosPrimeiroNeuronioCamadaOculta)), 6)

        self.saidaSegundoNeuronioCamadaOculta = round(self.tangenteHiperbolica(
            np.sum(np.array([self.saidaPrimeiroNeuronioCamadaEntrada, self.saidaSegundoNeuronioCamadaEntrada]) * self.saidaSegundoNeuronioCamadaEntrada)), 6)

        self.resultado = round(self.sigmoid(np.sum(np.array(
            [self.saidaPrimeiroNeuronioCamadaOculta, self.saidaSegundoNeuronioCamadaOculta]) * self.pesosNeuronioDeSaida)), 6)

        return self.resultado

    def tangenteHiperbolica(self, x):

        th = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
        return th

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def atualizaPesos(self, erro, alpha=0.01):

        for i in range(len(pesosNeuronioDeSaida)):
            if i == 0:
                entrada = self.saidaPrimeiroNeuronioCamadaOculta
            elif i == 1:
                entrada = self.saidaSegundoNeuronioCamadaOculta

            pesosNeuronioDeSaida[i] += \
                (alpha * entrada * erro)

        for i in range(len(pesosPrimeiroNeuronioCamadaOculta)):
            if i == 0:
                entrada1 = self.saidaPrimeiroNeuronioCamadaEntrada
            if i == 1:
                entrada1 = self.saidaSegundoNeuronioCamadaEntrada

            pesosPrimeiroNeuronioCamadaOculta[i] += (
                alpha * entrada1 * erro)

        for i in range(len(pesosSegundoNeuronioCamadaOculta)):
            if i == 0:
                entrada2 = self.saidaPrimeiroNeuronioCamadaEntrada
            if i == 1:
                entrada2 = self.saidaSegundoNeuronioCamadaEntrada

            pesosSegundoNeuronioCamadaOculta[i] += (
                alpha * entrada2 * erro)

        for i in range(len(pesosPrimeiroNeuronioCamadaEntrada)):
            pesosPrimeiroNeuronioCamadaEntrada[i] += (
                alpha * self.entradas[i] * erro)

        for i in range(len(pesosSegundoNeuronioCamadaEntrada)):
            pesosSegundoNeuronioCamadaEntrada[i] += (
                alpha * self.entradas[i] * erro)

        print(self.resultado)


while not gameOver:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gameOver = True

    rede = RedeNeural(posicaoYraquete/600, posicaoXbola/800, posicaoYbola/600)
    tecla = rede.feedforward()

    with open('dadosTreinamento.txt', 'a') as arquivo:
        arquivo.write(str(posicaoYraquete) + " " +
                      str(posicaoXbola) + " " +
                      str(posicaoYbola) + " " +
                      str(tecla) + "\n")

    tela.fill(PRETO)
    raquete.realiza()
    ball.realiza()
    raquete.atualiza(tecla)
    ball.atualiza(raquete.imagem_retangulo)

    erro = (posicaoYraquete - posicaoYbola) / 100
    rede.atualizaPesos(erro)

    placar1.contagem()
    pygame.display.update()
