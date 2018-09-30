#!/usr/bin/env python
from math import sqrt

from problema import Problema

class BuscaAEstrela(object):

    def busca_a_estrela(self, problema: Problema):
        borda = [problema.estado_inicial]
        memoria = [problema.estado_inicial]
        while True:
            if not borda:
                print('Falha ao encontrar solucao')
                return []
            estado = borda.pop(0)
            print(f'> Estado sendo avaliado:')
            print(f'{estado}')
            if problema.funcao_objetivo(estado):
                print('\n >>>> Solucao encontrada <<<< \n')
                return problema.solucao(estado)
            sucessores = problema.funcao_sucessora(estado)
            borda.extend([x for x in sucessores if x not in memoria])
            memoria.extend([x for x in sucessores if x not in memoria])
            print('sucessores:')
            for x in sucessores:
                print(x)
            print('*-*' * 80)
            print('memoria:')
            for x in memoria:
                print(x)
            print()
            memoria.extend(sucessores)
            print(f'> Estados sucessores: {len(sucessores)}')

