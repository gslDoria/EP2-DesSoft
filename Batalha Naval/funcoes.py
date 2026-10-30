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