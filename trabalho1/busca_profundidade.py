#!/usr/bin/env python

from pprint import pprint
from typing import List

from problema import Problema


class BuscaEmProfundidade(object):

    def busca_profundidade(self, problema: Problema):
        borda = [problema.estado_inicial]
        while True:
            if not borda:
                print('Falha ao encontrar solucao')
                return []
            estado = borda.pop(-1)
            print(f'=' * 80)
            print(f'> Estado sendo avaliado:')
            print(f'{estado}')
            print(estado)
            print(type(estado))
            if problema.funcao_objetivo(estado):
                print('Solucao encontrada.')
                return problema.solucao(estado)
            borda.append(problema.funcao_sucessora(estado))