#!/usr/bin/env python
# Nome: Winderson Jose Barboza dos Santos
# Disciplina: Inteligencia Artificial
# Professor: Chaua
# Curso: Ciência da computação



from hill_climbing import HillClimbing
from problema_mochila import ProblemaMochila
from tabu_search import TabuSearch

def main():
    problema = ProblemaMochila()
    #hill_climbing = HillClimbing(max_iteracoes=100, max_iteracoes_sem_melhora=100)
    #hill_climbing.executa(problema)

    tabu_search = TabuSearch(max_iteracoes=100, max_iteracoes_sem_melhora=100, tamanho_tabu_search=100000)
    tabu_search.executa(problema)


if __name__ == '__main__':
    main()