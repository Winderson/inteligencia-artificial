#!/usr/bin/env python
from math import sqrt

from problema import Problema

arquivoMaze01 = 'arquivos/maze01.txt'
arquivoMaze02 = 'arquivos/maze02.txt'

class ProblemaLabirinto(Problema):

    class Estado(object):
        def __init__(self):
            file = open(arquivoMaze02, 'r')
            labirinto = file.readlines()
            file.close()
            self.linha = 0
            self.coluna = 0
            self.bloco = ''
            self.labirinto = labirinto
            self.pai = None
            self.custo = 0
            self.acao = ''

        def copy(self):
            estado = ProblemaLabirinto.Estado()
            estado.linha = self.linha  # .copy()
            estado.coluna = self.coluna  # .copy()
            estado.bloco = self.coluna  # .copy()
            estado.labirinto = self.labirinto
            estado.acao = self.acao
            if self.pai is not None:
                estado.pai = self.pai.copy()
            return estado

        def __repr__(self):
            return f'\n Linha: [{self.linha}] Coluna: [{self.coluna}] - {self.acao}'

        def __eq__(self, other):
            return self.linha == other.linha and self.coluna == other.coluna


    @property
    def estado_inicial(self):
        estado = ProblemaLabirinto.Estado()
        estado.linha = 1
        estado.coluna = 0
        estado.bloco = estado.labirinto[estado.linha][estado.coluna]
        return estado


    def solucao(self, estado):
        solucao_final = []
        while estado.pai is not None:
            solucao_final.append(estado)
            estado = estado.pai
        solucao_final.append(estado)
        return solucao_final.reverse()


    def funcao_objetivo(self, estado):
        return estado.bloco == 'S'


    def __validar_restricoes(self, estado):
        if estado.bloco == ' ' or estado.bloco == 'E' or estado.bloco == 'S':
            return estado
        else:
            return None


    def __mover_esquerda(self, estado_pai, labirinto, acao):
        estado = estado_pai.copy()
        estado.acao = acao
        estado.linha = estado_pai.linha
        estado.coluna = estado_pai.coluna - 1
        estado.bloco = estado.labirinto[estado.linha][estado.coluna]
        estado.pai = estado_pai
        return self.__validar_restricoes(estado)


    def __mover_direita(self, estado_pai, labirinto, acao):
        estado = estado_pai.copy()
        estado.acao = acao
        estado.linha = estado_pai.linha
        estado.coluna = estado_pai.coluna + 1
        estado.bloco = labirinto[estado.linha][estado.coluna]
        estado.pai = estado_pai
        return self.__validar_restricoes(estado)


    def __mover_cima(self, estado_pai, labirinto, acao):
        estado = estado_pai.copy()
        estado.acao = acao
        estado.linha = estado_pai.linha - 1
        estado.coluna = estado_pai.coluna
        estado.bloco = labirinto[estado.linha][estado.coluna]
        estado.pai = estado_pai
        return self.__validar_restricoes(estado)


    def __mover_baixo(self, estado_pai, labirinto, acao):
        estado = estado_pai.copy()
        estado.acao = acao
        estado.linha = estado_pai.linha + 1
        estado.coluna = estado_pai.coluna
        estado.bloco = labirinto[estado.linha][estado.coluna]
        estado.pai = estado_pai
        return self.__validar_restricoes(estado)


    def funcao_sucessora(self, estado):
        sucessores = []
        a1 = self.__mover_esquerda(estado, estado.labirinto, 'ESQUERDA')
        a2 = self.__mover_direita(estado, estado.labirinto, 'DIREITA')
        a3 = self.__mover_cima(estado, estado.labirinto, 'CIMA')
        a4 = self.__mover_baixo(estado, estado.labirinto, 'BAIXO')
        if a1: sucessores.append(a1)
        if a2: sucessores.append(a2)
        if a3: sucessores.append(a3)
        if a4: sucessores.append(a4)
        return sucessores

    def heuristica(self, estado):
        pass