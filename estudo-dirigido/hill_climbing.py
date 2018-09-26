#!/usr/bin/env python

class HillClimbing(object):

    def __init__(self, max_iteracoes, max_iteracoes_sem_melhora):
        self.max_iteracoes = max_iteracoes
        self.max_iteracoes_sem_melhora = max_iteracoes_sem_melhora

    def executa(self, problema):
        estado_atual = problema.estado_inicial
        i = 0
        j = 0

        while i < self.max_iteracoes or j < self.max_iteracoes_sem_melhora:
            print(f"{i:03d} - {estado_atual} - {problema.funcao_objetivo(estado_atual)}")
            vizinho = problema.funcao_sucessora(estado_atual)
            custo_atual = problema.funcao_objetivo(estado_atual)
            custo_vizinho = problema.funcao_objetivo(vizinho)
            if custo_vizinho < custo_atual:
                print(f'achou melhor! atual = {custo_atual}  vizinho {custo_vizinho}')
                estado_atual = vizinho
                j = 0
            i += 1
            j += 1