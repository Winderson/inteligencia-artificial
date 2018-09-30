#!/usr/bin/env python

from busca_a_estrela import BuscaAEstrela
from busca_gulosa import BuscaGulosa
from problema_labirinto import ProblemaLabirinto
from problema import Problema


def main():
    # Definicao do problema do labirinto
    problema = ProblemaLabirinto()

    # Teste com busca gulosa
    busca = BuscaGulosa()
    solucao = busca.busca_gulosa(problema)


if __name__ == '__main__':
    main()
