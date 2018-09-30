#!/usr/bin/env python


from busca_largura import BuscaEmLargura
from busca_profundidade import BuscaEmProfundidade
from busca_custo_uniforme import BuscaCustoUniforme
from problema_torre_hanoi import ProblemaTorreHanoi
from problema import Problema


def main():
    # Definicao do problema dos canibais
    problema = ProblemaTorreHanoi()

    # Teste com busca em profundidade
    # busca = BuscaEmLargura()
    # solucao = busca.busca_largura(problema)

    # Teste com busca em profundidade
    # busca = BuscaEmProfundidade()
    # solucao = busca.busca_profundidade(problema)

    # Teste com busca uniforme
    busca = BuscaCustoUniforme()
    solucao = busca.busca_custo_uniforme(problema)

if __name__ == '__main__':
    main()
