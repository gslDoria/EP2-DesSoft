
    from funcoes import define_posicoes, preenche_frota, posicao_valida, posiciona_frota, faz_jogada, afundados, monta_tabuleiros

    frota = {}
    frota['porta-aviões'] = []
    frota['navio-tanque'] = []
    frota['contratorpedeiro'] = []
    frota['submarino'] = []

    tamanhos = {
        'porta-aviões' : 4,
        'navio-tanque' : 3,
        'contratorpedeiro' : 2,
        'submarino' : 1
    }


    quantidades = {
    'porta-aviões' : 1,
        'navio-tanque' : 2,
        'contratorpedeiro' : 3,
        'submarino' : 4
    }

    for navio in quantidades:
        for quantidade in range(quantidades[navio]):
            print (f'Insira as informações referentes ao navio {navio} que possui tamanho {tamanhos[navio]}')
            linha = int(input('linha: '))
            coluna = int(input('coluna: '))

            if navio != 'submarino':
                orientacao = int(input('[1] Vertical [2] Horizontal > '))
                if orientacao == 1:
                    orientacao = 'vertical'
                elif orientacao == 2:
                    orientacao = 'horizontal'
            else:
                orientacao = 'horizontal'
            valida = posicao_valida(frota, linha, coluna, orientacao, tamanhos[navio])

            while valida != True:
                print('Esta posição não está válida!')
                print (f'Insira as informações referentes ao navio {navio} que possui tamanho {tamanhos[navio]}')
                linha = int(input('linha: '))
                coluna = int(input('coluna: '))
                

                if navio != 'submarino':
                    orientacao = int(input('[1] Vertical [2] Horizontal > '))
                    if orientacao == 1:
                        orientacao = 'vertical'
                    elif orientacao == 2:
                        orientacao = 'horizontal'
                else:
                    orientacao = 'horizontal'

                valida = posicao_valida(frota, linha, coluna, orientacao, tamanhos[navio])
            frota = preenche_frota(frota, navio, linha, coluna, orientacao, tamanhos[navio])
                
                    

                

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}




tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)
    
jogando = True

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    linha_ataque = int(input('Jogador, qual linha deseja atacar? '))

    while linha_ataque > 9 or linha_ataque < 0:
        print('Linha inválida!')
        linha_ataque = int(input('Jogador, qual linha deseja atacar? '))


    coluna_ataque = int(input('Jogador, qual coluna deseja atacar? '))

    while coluna_ataque > 9 or coluna_ataque < 0:
        print('Coluna inválida!')
        coluna_ataque = int(input('Jogador, qual coluna deseja atacar? '))


    while tabuleiro_oponente[linha_ataque][coluna_ataque] == 'X' or tabuleiro_oponente[linha_ataque][coluna_ataque] == '-':
        print(f'A posição linha {linha_ataque} e coluna {coluna_ataque} já foi informada anteriormente!')

        linha_ataque = int(input('Jogador, qual linha deseja atacar? '))

        while linha_ataque > 9 or linha_ataque < 0:
            print('Linha inválida!')
            linha_ataque = int(input('Jogador, qual linha deseja atacar? '))


        coluna_ataque = int(input('Jogador, qual coluna deseja atacar? '))

        while coluna_ataque > 9 or coluna_ataque < 0:
            print('Coluna inválida!')
            coluna_ataque = int(input('Jogador, qual coluna deseja atacar? '))

    
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_ataque, coluna_ataque)

    quantidade_afundados = afundados(frota_oponente, tabuleiro_oponente )

    if quantidade_afundados == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
