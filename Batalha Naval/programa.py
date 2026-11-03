
from funcoes import define_posicoes, preenche_frota, posicao_valida

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

print(frota)
            
                

            
