import pygame

# Estrutura básica do jogo:

# Inicializar o jogo.

pygame.init()

tamanho_tela = (800, 800)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Brick Breaker do Maumau")

tamanho_bola = 15
bola = pygame.Rect(100,500, tamanho_bola, tamanho_bola)
tamanho_jogador = 110
jogador = pygame.Rect(0, 750, tamanho_jogador, 15)

qtde_blocos_linha = 8
qtde_linhas_blocos = 5
qtde_total_blocos = qtde_blocos_linha * qtde_linhas_blocos

def criar_blocos(qtde_blocos_linha, qtde_linhas_blocos):
    altura = tamanho_tela[1]
    largura_tela = tamanho_tela[0]
    largura_bloco = largura_tela / 8 - 5
    altura_bloco = 15
    distancia_entre_linhas = altura_bloco + 10

    blocos = []

#criar os blocos

    for j in range(qtde_linhas_blocos):
        for i in range(qtde_blocos_linha):
            #criar o bloco
            bloco = pygame.Rect(i * (largura_bloco + 5), j * distancia_entre_linhas, largura_bloco, altura_bloco)
            #adicionar esse bloco na lista de blocos
            blocos.append(bloco)

    return blocos

#criar biblioteca de cores

cores = {
    "branco": (255, 255, 255),
    "preto": (0, 0, 0),
    "amarelo": (255, 255, 0),
    "azul": (0, 0, 255),
    "verde": (0, 255, 0),
    "vermelho": (255, 0, 0),
    "Brick Breaker": (30, 30, 200)
}

fim_jogo = False
pontuacao = 0
movimento_bola = [1, -1]

# Desenhar a parte visual na tela (parte gráfica).

def desenhar_inicio_jogo():
    tela.fill(cores["preto"])
    pygame.draw.rect(tela, cores["azul"], jogador)
    pygame.draw.rect(tela, cores["branco"], bola)

def desenhar_blocos(blocos):
    for bloco in blocos:
        pygame.draw.rect(tela, cores["verde"], bloco)

# Criar as funções do jogo.

def movimentar_jogador(evento):
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_RIGHT:
            if (jogador.x + tamanho_jogador) < tamanho_tela[0]:
                jogador.x = jogador.x + 5
        if evento.key == pygame.K_LEFT:
            if jogador.x > 0:
                jogador.x = jogador.x - 5

def movimentar_bola(bola):
    movimento = movimento_bola
    bola.x = bola.x + movimento[0]
    bola.y = bola.y + movimento[1]

    if bola.x <= 0:
        movimento[0] = - movimento[0]
    if bola.y <= 0:
        movimento[1] = - movimento[1]
    if bola.x + tamanho_bola >= tamanho_tela[0]:
        movimento[0] = - movimento[0]
    if bola.y + tamanho_bola >= tamanho_tela[1]:
        movimento = None

    if jogador.collidepoint(bola.x, bola.y):
        movimento[1] = - movimento[1]
    for bloco in blocos:
        if bloco.collidepoint(bola.x, bola.y):
            blocos.remove(bloco)
            movimento[1] = - movimento[1]
    return movimento

def atualizar_pontuacao(pontuacao):
    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f"Pontuação: {pontuacao}", 1, cores["amarelo"])
    texto2 = fonte.render(f"Brick Breaker", 1, cores["Brick Breaker"])
    tela.blit(texto,(0,780))
    tela.blit(texto2, (660,780))
    if pontuacao >= qtde_total_blocos:
        return True
    else:
        return False

blocos = criar_blocos(qtde_blocos_linha, qtde_linhas_blocos)

# Criar um loop infinito.

while not fim_jogo:
    desenhar_inicio_jogo()
    desenhar_blocos(blocos)
    fim_jogo = atualizar_pontuacao(qtde_total_blocos - len(blocos))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = True

    movimentar_jogador(evento)
    movimento_bola = movimentar_bola(bola)

    if not movimento_bola:
        fonte = pygame.font.Font(None, 100)
        texto3 = fonte.render(f"GAME OVER", 1, cores["Brick Breaker"])
        tela.blit(texto3, (200,400))
        
        
    pygame.time.wait(1)
    pygame.display.flip()
pygame.quit()



