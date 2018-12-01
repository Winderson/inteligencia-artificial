from problema_mochila import ProblemaMochila

class TabuSearch(object):

    def __init__(self, max_iteracoes, max_iteracoes_sem_melhora, tamanho_tabu_search):
        self.max_iteracoes = max_iteracoes
        self.max_iteracoes_sem_melhora = max_iteracoes_sem_melhora
        self.tamanho_tabu_search = tamanho_tabu_search
        self.lista_tabu = []

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
        self.lista_tabu.append(estado_atual)

        # Imprime a solucao
        solucao = ""
        for item in estado_atual.itens:
            solucao = solucao + "| TIPO:" + str(item.tipo) + " | QT:" + str(item.quantidade) + " |"
        print(f'{iteracao:03d} - VL:{problema.funcao_objetivo(estado_atual)} - MOCHILA:{solucao}')

        while iteracao < self.max_iteracoes and iteracao_sem_melhora < self.max_iteracoes_sem_melhora:

            # Gera um estado vizinho
            vizinho = problema.funcao_sucessora(estado_atual)

            # Imprime a solucao
            solucao = ""
            for item in vizinho.itens:
                solucao = solucao + "| TIPO:" + str(item.tipo) + " | QT:" + str(item.quantidade) + " |"
            print(f'{iteracao:03d} - VL:{problema.funcao_objetivo(vizinho)} - MOCHILA:{solucao}')


            # Verifica se o estado vizinho eh melhor que o atual
            custo_atual = problema.funcao_objetivo(estado_atual)
            custo_vizinho = problema.funcao_objetivo(vizinho)

            if custo_atual != -1 and custo_vizinho != -1 and not(self.existeNaListaTabu(vizinho)):

                if custo_vizinho > custo_atual:
                    print(f'>>>>>> ACHOU MELHOR! ATUAL = {custo_atual}  VIZINHO = {custo_vizinho} <<<<<<<<<')
                    estado_atual = vizinho
                    self.lista_tabu.append(estado_atual)
                    if len(self.lista_tabu) > self.tamanho_tabu_search:
                        self.lista_tabu.pop(-1)
                    iteracao_sem_melhora = 0
            iteracao += 1
            iteracao_sem_melhora += 1

        indice = len(self.lista_tabu)-1
        ranking = 1
        # while indice >= 0:
        #     # Imprime a solucao
        #     solucao = ""
        #     for item in self.lista_tabu[indice].itens:
        #         solucao = solucao + "| TIPO:{item.tipo} | QT:{item.quantidade} |"
        #     print(f' {ranking}º VL:{problema.funcao_objetivo(self.lista_tabu[indice])} - MOCHILA:{solucao}')
        #     indice = indice-1
        #     ranking = ranking+1

    def existeNaListaTabu(self,estado):
        i = 0
        while i<len(self.lista_tabu):
            if self.lista_tabu[i] == estado:
                print(f'>>>>>>>>>>>>>> JA INSERIDA NA LISTA TABU <<<<<<<<<<<<<<<<')
                return True
            i = i+1
        return False
