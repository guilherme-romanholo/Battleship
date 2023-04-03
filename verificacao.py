def ponto_valido(lin, col, n, coin, tab):
    # Verifica se o navio vai ser posicionado na vertical ou horizontal
    if coin == 1:
        # Verifica se o ponto é valido para posicionar
        for i in range(lin, lin+n):
            # Caso ele quebre alguma condição ele retorna falso
            if i < 0 or i > 5 or tab[i][col] != '0':
                return False
    else:
        # Verifica se o ponto é valido para posicionar
        for i in range(col, col+n):
            # Caso ele quebre alguma condição ele retorna falso
            if i < 0 or i > 5 or tab[lin][i] != '0':
                return False
    # Se não, retornamos verdadeiro
    return True


# Verifica a posição atacada pelo jogador
def verifica_ataque_jogador(tab, tab_esc, lin, col):
    # Caso a posição já foi atacada anteriormente
    if tab_esc[lin][col] == 'X':
        return False
    # Caso a posição possua alguma embarcação
    if tab[lin][col] not in '0-':
        tab_esc[lin][col] = 'X'
        return True
    # Caso a posição não possua nenhuma embarcação
    else:
        tab_esc[lin][col] = '-'
        tab[lin][col] = '-'
        return False


def verifica_ataque_bot(tab, lin, col):
    # Caso a posição já foi atacada anteriormente
    if tab[lin][col] == 'X':
        return False
    # Caso a posição possua alguma embarcação
    if tab[lin][col] not in '0-':
        tab[lin][col] = 'X'
        return True
    # Caso a posição não possua nenhuma embarcação
    else:
        tab[lin][col] = '-'
        return False
