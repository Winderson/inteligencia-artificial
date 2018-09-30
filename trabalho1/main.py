#!/usr/bin/env python
from pprint import pprint

from busca_largura import BuscaEmLargura
from problema_torre_hanoi import ProblemaTorreHanoi
from problema import Problema


def main():
    # Definicao do problema dos canibais
    problema = ProblemaTorreHanoi()
    busca = BuscaEmLargura()
    solucao = busca.busca_largura(problema)
    pprint(solucao)

if __name__ == '__main__':
    main()