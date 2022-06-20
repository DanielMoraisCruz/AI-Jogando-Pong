import pygame

from globais import BRANCO, TELA_RETANGULO, TELA


class Player:
    def __init__(self, tamanho, velicidade):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(BRANCO)
        self.imagem_retangulo = self.imagem.get_rect()
        self.velicidade = velicidade
        self.imagem_retangulo[0] = 20

    def move(self, x, y):
        self.imagem_retangulo[0] += x * self.velicidade
        self.imagem_retangulo[1] += y * self.velicidade

    def atualiza(self, tecla):
        if tecla[pygame.K_UP]:  # or tecla[pygame.K_w]:
            self.move(0, -1)

        if tecla[pygame.K_DOWN]:  # or tecla[pygame.K_s]:
            self.move(0, 1)

        self.imagem_retangulo.clamp_ip(TELA_RETANGULO)

    def realiza(self):
        TELA.blit(self.imagem, self.imagem_retangulo)
