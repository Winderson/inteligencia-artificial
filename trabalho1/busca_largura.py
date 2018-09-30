#!/usr/bin/env python

from pprint import pprint
from typing import List

from problema import Problema


class BuscaEmLargura(object):

    def busca_largura(self, problema: Problema):
        print("Chegou aqui ----")

        borda = [problema.estado_inicial]
        memoria = [problema.estado_inicial]
        while True:
            if not borda:
                print('Falha ao encontrar solucao')
                return []
            estado = borda.pop(0)
            print(f'=' * 80)
            print(f'> Estado sendo avaliado:')
            print(f'{estado}')
            if problema.funcao_objetivo(estado):
                print('Solucao encontrada.')
                return problema.solucao(estado)
            sucessores = problema.funcao_sucessora(estado)
            borda.extend([x for x in sucessores if x not in memoria])
            memoria.extend([x for x in sucessores if x not in memoria])

            # print('-'*80)
            print('sucessores:')
            for x in sucessores:
                print(x)
            #
            print('*-*' * 80)
            print('memoria:')
            for x in memoria:
                print(x)
            print()

            # print('-' * 80)
            # print('borda DEPOIS:')
            # for x in borda:
            #     print(x)
            # print()

            # Adiciona os novos estados gerados na memoria
            memoria.extend(sucessores)

            print(f'> Estados sucessores: {len(sucessores)}')