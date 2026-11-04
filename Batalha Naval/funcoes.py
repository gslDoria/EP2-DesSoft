



def define_posicoes(linha, coluna, orientacao, tamanho):

    posicoes = []
    posicoes.append([linha, coluna])
    if orientacao == 'vertical':
        for posicao in range(tamanho-1):
            linha += 1
            posicoes.append([linha, coluna])

    if orientacao == 'horizontal':
        for posicao in range(tamanho-1):
            coluna += 1
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
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    for navio in frota:
        for embarcacao in frota[navio]:
            for coordenada in embarcacao:
                linha = coordenada[0]
                coluna = coordenada[1]

                grid[linha][coluna] = 1

    return grid


def afundados(frota, tabuleiro):
    quantidade = 0

    for navio in frota:
        for embarcacao in frota[navio]:
            tamanho = 0
            acertos = 0

            for coordenada in embarcacao:
                linha = coordenada[0]
                coluna = coordenada[1]

                tamanho += 1
                if tabuleiro[linha][coluna] == 'X':
                    acertos += 1

            if tamanho == acertos:
                quantidade += 1

    return quantidade



def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in posicoes:
        linha = posicao[0]
        coluna = posicao[1]

        if linha > 9 or coluna > 9:
            return False
        elif linha < 0 or coluna < 0:
            return False
        for navio in frota:
            for embarcacao in frota[navio]:
                for coordenada in embarcacao:
                    if linha == coordenada[0] and coluna == coordenada[1]:
                        return False
    
    return True


    
def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto 

