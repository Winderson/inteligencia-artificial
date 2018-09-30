# Inteligência artificial
### Winderson Jose B. dos Santos

## Trabalho 1

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

## Trabalho 2

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

## Estudo dirigido

#### Classe HillClimbing
