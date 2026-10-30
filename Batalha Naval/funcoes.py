def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    posicoes.append([linha, coluna])
    if orientacao == 'vertical':
        for posicao in range(tamanho-1):
            linha +=1
            posicoes.append([linha, coluna])

    if orientacao == 'horizontal':
        for posicao in range(tamanho-1):
            coluna +=1
            posicoes.append([linha, coluna])    

    return posicoes






def preenche_frota(frota, nome, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome not in frota:
        frota[nome] = [posicoes]    
    else:
        frota[nome].append(posicoes)
    return frota


def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else: 
        tabuleiro[linha][coluna] = '-'
    return tabuleiro


def posiciona_frota(frota):
    grid = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
    ]

    for navio in frota:
        for embarcacao in frota[navio]:
            for coordenada in embarcacao:
                linha = coordenada[0]
                coluna = coordenada[1]

                grid[linha][coluna] = 1

    return grid
