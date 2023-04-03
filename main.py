import cores
from tabuleiro import print_tabuleiro
from verificacao import verifica_ataque_bot, verifica_ataque_jogador
from random import randint
from posicionamento import navios_aleatorios, local_navio


# Função principal
def main():
    # Tabuleiro com os navios do bot
    tabuleiro_bot = [['0']*6 for x in range(6)]
    # Tabuleiro do bot que vai aparecer para o jogador
    tabuleiro_bot_escondido = [['0']*6 for x in range(6)]
    # Tabuleiro do jogador
    tabuleiro_jogador = [['0']*6 for x in range(6)]
    # Embarcações afundadas
    player = 0
    bot = 0

    # Gerar as embarações aleatórias para o bot
    navios_aleatorios(tabuleiro_bot, 5)
    navios_aleatorios(tabuleiro_bot, 4)
    navios_aleatorios(tabuleiro_bot, 3)
    navios_aleatorios(tabuleiro_bot, 2)
    navios_aleatorios(tabuleiro_bot, 2)
    # Posicionamento das embarcações do jogador
    local_navio(tabuleiro_jogador)
    # Quebra de linha
    print()

    # Enquanto alguem não venceu
    while True:
        # Verifica se alguem já venceu o jogo
        if player == 16:
            print(cores.BLUE + 'Jogador venceu!' + cores.RESET)
            break
        if bot == 16:
            print(cores.BLUE + 'Bot venceu!' + cores.RESET)
            break
        # Mostra os tabuleiros
        print('Seu tabuleiro: ')
        print_tabuleiro(tabuleiro_jogador)
        print('Tabuleiro do bot ')
        print_tabuleiro(tabuleiro_bot_escondido)
        # Recebe uma posição para ser atacada pelo jogador
        lin = int(input('Digite a LINHA para o ataque: '))
        col = int(input('Digite a COLUNA para o ataque: '))
        # Quebra de linha
        print()
        # Faz a verificação se o ataque foi efetivo
        if verifica_ataque_jogador(tabuleiro_bot,
                                   tabuleiro_bot_escondido,
                                   lin-1, col-1):
            print('\nJogador ' + cores.BLUE + 'acertou!' + cores.RESET)
            player += 1
        else:
            print('Jogador ' + cores.RED + 'errou!' + cores.RESET)
        # Posição aleatória de ataque para o bot
        lin = randint(0, 5)
        col = randint(0, 5)
        # verifica se o ataque do bot foi efetivo
        if verifica_ataque_bot(tabuleiro_jogador, lin-1, col-1):
            print('Bot ' + cores.BLUE + 'acertou!' + cores.RESET)
            bot += 1
        else:
            print('Bot ' + cores.RED + 'errou!' + cores.RESET)
        # Quebra de linha
        print()

    # Printa os tabuleiro após o final do jogo
    print('Seu tabuleiro: ')
    print_tabuleiro(tabuleiro_jogador)
    print('\nTabuleiro do Bot: ')
    print_tabuleiro(tabuleiro_bot)


# Utilizado para a declaração da função main()
if __name__ == "__main__":
    main()
