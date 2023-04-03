from random import randint
import cores
from verificacao import ponto_valido
from tabuleiro import print_tabuleiro
# Função para gerar navios aleatórios


# Função para posicionar o navio na matriz
def posicionar_navio(lin, col, n, coin, tab):
    # Verifica se é na vertical ou horizontal
    if coin == 1:
        # Coloca o elemento colorido na matriz
        for i in range(lin, lin+n):
            tab[i][col] = cores.GREEN + str(n) + cores.RESET
    else:
        # Coloca o elemento colorido na matriz
        for i in range(col, col+n):
            tab[lin][i] = cores.GREEN + str(n) + cores.RESET


def navios_aleatorios(tab, n):
    # Gera o número para sabermos se vai ser na horizontal ou vertical
    coin = randint(0, 1)
    # Posição do navio aleatória enquanto não acharmos uma posição válida
    while True:
        lin = randint(0, 5)
        col = randint(0, 5)
        if ponto_valido(lin, col, n, coin, tab):
            break
    # Quando acharmos, posicionamos o navio
    posicionar_navio(lin, col, n, coin, tab)


# Função para o posicionamento manual dos navios do jogador
def local_navio(tab):
    # Controla o tamanho do navio
    i = 5
    f = False
    # Posicionamos o navio no tabuleiro
    while True:
        print_tabuleiro(tab)
        # Validação do ponto digitado
        while True:
            print('Por favor digite uma posição válida')
            lin = int(input(f'LINHA de inicio para o navio de {i} espaços: '))
            col = int(input(f'COLUNA de inicio para o navio de {i} espaços: '))
            vert_hor = int(
                input('Posicionamento: [0]Horizontal [1]Vertical: '))
            if ponto_valido(lin-1,
                            col-1,
                            i,
                            vert_hor,
                            tab) and (str(vert_hor) in '01'):
                break
        # Posicionamento na matriz
        posicionar_navio(lin-1, col-1, i, vert_hor, tab)
        # Passamos para o navio com tamanho menor
        i -= 1
        # Verficação de quando vamos parar o laço
        # Após o posicionamento do segundo submarino
        if f:
            break
        if i == 1:
            i += 1
            f = True
