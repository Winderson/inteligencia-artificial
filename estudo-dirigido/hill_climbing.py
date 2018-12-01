#!/usr/bin/env python
# Nome: Winderson Jose Barboza dos Santos
# Disciplina: Inteligencia Artificial
# Professor: Chaua
# Curso: Ciência da computação


from problema_mochila import ProblemaMochila

class HillClimbing(object):

    def __init__(self, max_iteracoes, max_iteracoes_sem_melhora):
        self.max_iteracoes = max_iteracoes
        self.max_iteracoes_sem_melhora = max_iteracoes_sem_melhora

    def executa(self, problema: ProblemaMochila):
        """Implementacao do hill climbing."""

        # Gera o estado inicial
        estado_atual = problema.estado_inicial

        # Criterios de parada
        # 1. numero maximo de iteracoes
        # 2. numero maximo de iteracoes sem melhora
        # 3. tempo maximo
        # 4. atingiu o objetivo

        # Loop principal
        iteracao = 0  # maximo de iteracoes
        iteracao_sem_melhora = 0  # maximo de iteracoes sem melhora

        while iteracao < self.max_iteracoes and iteracao_sem_melhora < self.max_iteracoes_sem_melhora:

            # Imprime a solucao
            solucao = ""
            for item in estado_atual.itens:
                solucao = solucao +"| TIPO:"+str(item.tipo)+" | QT:"+str(item.quantidade)+" |"
            print(f'{iteracao:03d} - VL:{problema.funcao_objetivo(estado_atual)} - MOCHILA:{solucao}')

            # Gera um estado vizinho
            vizinho = problema.funcao_sucessora(estado_atual)

            # Verifica se o estado vizinho eh melhor que o atual
            custo_atual = problema.funcao_objetivo(estado_atual)
            custo_vizinho = problema.funcao_objetivo(vizinho)

            if custo_atual != -1 and custo_vizinho != -1:
                if custo_vizinho > custo_atual:
                    print(f'>>>>>> ACHOU MELHOR! ATUAL = {custo_atual}  VIZINHO = {custo_vizinho} <<<<<<<<<')
                    estado_atual = vizinho
                    iteracao_sem_melhora = 0
            iteracao += 1
            iteracao_sem_melhora += 1