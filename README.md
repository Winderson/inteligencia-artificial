# Inteligência artificial
### Winderson Jose B. dos Santos

## :blue_book: Trabalho 1

#### Classe BuscaEmLargura
##### Métodos
- busca_largura(problema:Problema)

#### Classe BuscaEmProfundidade
##### Métodos
- busca_profundidade(problema:Problema)

#### Classe BuscaCustoUniforme
##### Métodos
- busca_custo_uniforme(problema:Problema)

#### Classe Problema (template)
##### Métodos
- estado_inicial()
- solucao(estado)
- funcao_objetivo(estado)
- funcao_sucessora(estado)

#### Classe ProblemaTorreHanoi(Problema)
##### Classe
- Estado()
##### Métodos
- estado_inicial()
- solucao(estado)
- funcao_objetivo(estado)
- funcao_sucessora(estado)
- mover_objeto(estado, acao)

## :blue_book: Trabalho 2

#### Classe Problema (template)
##### Métodos
- estado_inicial()
- solucao(estado)
- funcao_objetivo(estado)
- funcao_sucessora(estado)

#### Classe BuscaGulosa (template)
##### Métodos
- busca_a_estrela()

#### Classe BuscaAEstrela (template)
##### Métodos
- busca_a_estrela()

#### Classe ProblemaLabirinto(Problema)
##### Classe
- Estado()
##### Métodos
- estado_inicial()
- solucao(estado)
- funcao_objetivo(estado)
- funcao_sucessora(estado)
- validar-restricoes(estado, acao)
- mover_esquerda(estado,labirinto, acao)
- mover_direita(estado,labirinto, acao)
- mover_cima(estado,labirinto, acao)
- mover_baixo(estado,labirinto, acao)
- heuristica(estado)

## :blue_book: Estudo dirigido

#### Classe Item
##### Atributos
- tipo
- peso
- valor
- quantidade
- quantidadeDisponivel

#### Classe Estado
##### Atributos
- itens[]

#### Classe ProblemaMochila()
##### Métodos
- estado_inicial()
- solucao(estado)
- funcao_objetivo(estado)
- funcao_sucessora(estado)
- verificaSeVizinho(estado_atual, estado_gerado)
- itens_disponiveis()

#### Classe HillClimbing()
##### Métodos
- executa(ProblemaMochila)

#### Classe TabuSearch()
##### Métodos
- executa(ProblemaMochila)

## :blue_book: Trabalho 3
##### Arquivo
- trabalho.pl
##### Predicados
- num_elementos
- intercaladas.
- inserção ordenada
- ordenada
- subcultura
