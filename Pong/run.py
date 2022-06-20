import pygame

from bola import Bola
from globais import PRETO, TELA
from player import Player

fim = False

tempo = pygame.time.Clock()
pygame.display.set_caption("Pong")

player1 = Player((20, 100), 5)
bola = Bola((15, 15), 5)

while not(fim):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim = True

    TELA.fill(PRETO)
    player1.realiza()
    player1.atualiza(pygame.key.get_pressed())
    bola.realiza()
    bola.atualiza(player1.imagem_retangulo)

    tempo.tick(60)

    pygame.display.update()
