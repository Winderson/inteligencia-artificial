#!/usr/bin/env python

from problema import Problema


class ProblemaTorreHanoi(Problema):
    torreA = []
    torreB = []
    torreC = []

    class Estado(object):
        def __init__(self):
            self.torreA = []
            self.torreB = []
            self.torreC = []
            self.pai = None
            self.custo = 0
            self.acao = ''

        def copy(self):
            estado = ProblemaTorreHanoi.Estado()
            estado.torreA = self.torreA.copy()
            estado.torreB = self.torreB.copy()
            estado.torreC = self.torreC.copy()
            return estado

        def __repr__(self):
            return f' \n Torre A: {self.torreA} \n Torre B: {self.torreB} \n Torre C: {self.torreC}'

        def __eq__(self, estado):
            return self.torreA == estado.torreA and self.torreB == estado.torreB and self.torreC == estado.torreC

    @property
    def estado_inicial(self):
        estado = ProblemaTorreHanoi.Estado()
        estado.torreA = [5, 4, 3, 2, 1]
        estado.torreB = []
        estado.torreC = []
        estado.pai = None
        return estado

    def solucao(self, estado):
        solucao_final = []
        while estado.pai is not None:
            solucao_final.append(estado)
            estado = estado.pai
        solucao_final.append(estado)
        return solucao_final.reverse()

    def funcao_objetivo(self, estado):
        return estado.torreC == [5, 4, 3, 2, 1]

    def __mover_teste(self, estado_pai, acao):
        estado = estado_pai.copy()
        estado.acao = acao
        tamA = len(estado.torreA)
        tamB = len(estado.torreB)
        tamC = len(estado.torreC)
        if acao == 'A->B' and tamA > 0 and (tamB == 0 or estado.torreA[tamA - 1] < estado.torreB[tamB - 1]):
            estado.torreB.append(estado.torreA.pop(-1))
        elif acao == 'A->C' and tamA > 0 and (tamC == 0 or estado.torreA[tamA - 1] < estado.torreC[tamC - 1]):
            estado.torreC.append(estado.torreA.pop(-1))
        elif acao == 'B->A' and tamB > 0 and (tamA == 0 or estado.torreB[tamB - 1] < estado.torreA[tamA - 1]):
            estado.torreA.append(estado.torreB.pop(-1))
        elif acao == 'B->C' and tamB > 0 and (tamC == 0 or estado.torreB[tamB - 1] < estado.torreC[tamC - 1]):
            estado.torreC.append(estado.torreB.pop(-1))
        elif acao == 'C->A' and tamC > 0 and (tamA == 0 or estado.torreC[tamC - 1] < estado.torreA[tamA - 1]):
            estado.torreA.append(estado.torreC.pop(-1))
        elif acao == 'C->B' and tamC > 0 and (tamB == 0 or estado.torreC[tamC - 1] < estado.torreB[tamB - 1]):
            estado.torreB.append(estado.torreC.pop(-1))
        else:
            return None
        estado.pai = estado_pai
        return estado

    def __valida_restricoes(self, estado):
        print(estado)
        print(estado.torreA)
        print(estado.torreB)
        print(estado.torreC)

    def funcao_sucessora(self, estado):
        sucessores = []
        a1 = self.__mover_teste(estado, 'A->B')
        a2 = self.__mover_teste(estado, 'A->C')
        a3 = self.__mover_teste(estado, 'B->A')
        a4 = self.__mover_teste(estado, 'B->C')
        a5 = self.__mover_teste(estado, 'C->A')
        a6 = self.__mover_teste(estado, 'C->B')

        if a1: sucessores.append(a1)
        if a2: sucessores.append(a2)
        if a3: sucessores.append(a3)
        if a4: sucessores.append(a4)
        if a5: sucessores.append(a5)
        return sucessores
