import pygame

fim = False
tamanho_tela = 800, 600
tela = pygame.display.set_mode(tamanho_tela)
tela_retangulo = tela.get_rect()

PRETO = 0, 0, 0
BRANCO = 255, 255, 255


class Player:
    def __init__(self, tamanho):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(BRANCO)
        self.imagem_retangulo = self.imagem.get_rect()
        self.velicidade = 1
        self.imagem_retangulo[0] = 20

    def move(self, x, y):
        self.imagem_retangulo[0] += x * self.velicidade
        self.imagem_retangulo[1] += y * self.velicidade

    def atualiza(self, tecla):
        if tecla[pygame.K_UP]:  # or tecla[pygame.K_w]:
            self.move(0, -1)

        if tecla[pygame.K_DOWN]:  # or tecla[pygame.K_s]:
            self.move(0, 1)

        self.imagem_retangulo.clamp_ip(tela_retangulo)
        # if tecla[pygame.K_LEFT]:
        #     self.move(-1, 0)

        # if tecla[pygame.K_RIGHT]:
        #     self.move(1, 0)

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)


player1 = Player((20, 100))


while not(fim):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim = True

    player1.atualiza(pygame.key.get_pressed())

    tela.fill(PRETO)
    player1.realiza()
    pygame.display.update()
