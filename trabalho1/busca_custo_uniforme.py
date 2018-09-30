#!/usr/bin/env python


from problema_torre_hanoi import ProblemaTorreHanoi


class BuscaCustoUniforme():

    def busca_custo_uniforme(self, problema: ProblemaTorreHanoi):
        borda = [problema.estado_inicial]
        memoria = [problema.estado_inicial]
        while True:
            if not borda:
                print('Falha ao encontrar solucao')
                return []
            estado = borda.pop(-1)
            print(f'> Estado sendo avaliado:')
            print(f'{estado}')
            if problema.funcao_objetivo(estado):
                print('\n >>>> Solucao encontrada <<<< \n')
                return problema.solucao(estado)
            sucessores = problema.funcao_sucessora(estado)
            borda.extend([x for x in sucessores if x not in memoria])
            memoria.extend([x for x in sucessores if x not in memoria])
            for x in sucessores:
                print(x)
            for x in memoria:
                print(x)
            print()
            memoria.extend(sucessores)
            print(f'> Estados sucessores: {len(sucessores)}')