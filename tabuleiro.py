import cores


# Função para printar o tabuleiro
def print_tabuleiro(tab):
    print('    1 2 3 4 5 6')
    print('   ------------')
    numero_da_fileira = 1
    # Laço para percorrer a matriz
    for i in range(0, 6):
        # Imprime o numero da fileira
        print(numero_da_fileira, '|', end=" ")
        numero_da_fileira += 1
        for j in range(0, 6):
            # Condições para imprimir a matriz colorida
            if tab[i][j] == 'X':
                print(cores.RED + tab[i][j] + cores.RESET, end=" ")
            elif tab[i][j] == '-':
                print(cores.BLUE + tab[i][j] + cores.RESET, end=" ")
            else:
                print(tab[i][j], end=" ")
        # Print para quebrar a liha
        print()
