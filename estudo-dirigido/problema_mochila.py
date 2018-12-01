from problema import Problema
from random import random, randint
import copy


class ProblemaMochila(Problema):
    class Item(object):
        def __init__(self):
            self.tipo = 0;
            self.peso = 0.0
            self.valor = 0
            self.quantidade = 0
            self.quantidadeDisponivel = 0

    class Estado(object):
        def __init__(self):
            self.itens = []

        def __eq__(self, estado):
            i = 0
            validador = False
            while (i < len(self.itens)):
                i2 = 0
                validador = False
                while (i2 < len(estado.itens)):
                    if estado.itens[i2].tipo == self.itens[i].tipo and estado.itens[i2].valor == self.itens[i].valor \
                            and estado.itens[i2].quantidade == self.itens[i].quantidade:
                            validador = True
                    i2 = i2+1

                if not(validador):
                    break;
                i = i+1
            return validador


    # Variaveis
    itens_default = []
    capacidade_mochila = 0.0

    def __init__(self):
        self.itens_disponiveis()

    @property
    def estado_inicial(self):
        estado = ProblemaMochila.Estado()
        estado.itens = []
        return estado

    def funcao_objetivo(self, estado):
        total = 0
        peso_total_itens = 0

        # Verifico cada item
        # coletando o peso total de cada item multiplicado
        # pela quantidade de items desse tipo existentes na mochila
        # para validar se o peso é menor ou igual a capacidade
        indice = 0
        while (indice < len(estado.itens)):
            if estado.itens[indice].quantidade <= estado.itens[indice].quantidadeDisponivel:
                total = total + (estado.itens[indice].quantidade * estado.itens[indice].valor)
                peso_total_itens = peso_total_itens + (estado.itens[indice].quantidade * estado.itens[indice].peso)
            else:
                # Se a quantidade do item for maior que a quantidade
                # disponivel o estado se torna inválido
                return -1
            indice = indice + 1

        # Peso total dos item na mochila é menor ou
        # igual a capacidade

        if peso_total_itens <= self.capacidade_mochila:
            return total
        else:
            return -1

    def funcao_sucessora(self, estado):
        aleatorios = []
        for item in self.itens_default:
            aleatorio_item = randint(0, 100) / 100
            itemAux = ProblemaMochila.Item()
            aux_qt = (item.quantidadeDisponivel + 1)
            aux_div = 1 / aux_qt
            aux_cont = 0
            indice = 0
            while (indice < aux_qt):
                if aleatorio_item < 1:
                    if aleatorio_item <= (aux_div * (indice + 1)):
                        itemAux.quantidade = indice
                        itemAux.quantidadeDisponivel = item.quantidadeDisponivel
                        itemAux.peso = item.peso
                        itemAux.tipo = item.tipo
                        itemAux.valor = item.valor
                        break;
                else:
                    itemAux.quantidade = 0
                    itemAux.quantidadeDisponivel = item.quantidadeDisponivel
                    itemAux.peso = item.peso
                    itemAux.tipo = item.tipo
                    itemAux.valor = item.valor
                    break;
                indice = indice + 1
            aleatorios.append(itemAux)

        vizinho = copy.deepcopy(estado)
        vizinho.itens = aleatorios

        # if not(self.verificaSeVizinho(estado,vizinho)) and len(estado.itens) > 0:
        #     self.funcao_sucessora(estado)

        return vizinho

    """
        Rotina que verifica se o estado gerado é vizinho ou nao
    """
    def verificaSeVizinho(self, estado_atual, estado_gerado):
        i = 0
        while(i<len(estado_atual.itens)):
            i2 = 0
            while(i2<len(estado_gerado.itens)):
                if estado_atual.itens[i].tipo == estado_gerado.itens[i2].tipo and \
                        estado_atual.itens[i].quantidade == estado_gerado.itens[i2].quantidade:
                    return True
                i2 +=1
            i += 0
        return False


    """
        Rotina responsável por setar os valores dafaults
    """

    def itens_disponiveis(self):
        # Item (descricao)  | Peso (kg) | Valor
        #       1           |     3     |   40
        #       2           |     5     |   100
        #       3           |     2     |   50

        # Quantidade de itens
        # item 1 = 3
        # item 2 = 2
        # item 3 = 5

        # Definicao item 1
        item1 = ProblemaMochila.Item()
        item1.quantidadeDisponivel = 3
        item1.tipo = 1
        item1.peso = 3  # Kg
        item1.valor = 40

        # Definicao item 2
        item2 = ProblemaMochila.Item()
        item2.quantidadeDisponivel = 2
        item2.tipo = 2
        item2.peso = 5  # kg
        item2.valor = 100

        # Definicao item 3
        item3 = ProblemaMochila.Item()
        item3.quantidadeDisponivel = 5
        item3.tipo = 3
        item3.peso = 2  # Kg
        item3.valor = 50

        self.itens_default.append(item1)
        self.itens_default.append(item2)
        self.itens_default.append(item3)
        self.capacidade_mochila = 20  # Kg
