
% BASE DE CONHECIMENTO


animal(cachorro).
animal(gato).
animal(passaro).
animal(peixe).

homem(joao).
homem(jose).
homem(alberto).
homem(fabricio).
homem(jonatas).
homem(marcos).

mulher(silvia).
mulher(marcia).
mulher(claudia).
mulher(angela).
mulher(maria).

pai(joao, jose).
pai(joao, maria).

mae(silvia, jose).
mae(silvia, maria).

pai(alberto, joao).
pai(fabricio, alberto).
pai(jonatas, fabricio).

casados(joao, silvia).


bonita(cassia).


% variaveis comecam com letras maiuscula
% ; = OU
% , = E
irmao(X,Y) :-
	homem(X),
	pai(P,X),
	pai(P,Y),
	mae(M,X),
	mae(M,Y),
	not(X=Y).
	
irma(X,Y) :-
	mulher(X),
	mulher(X),
	pai(P, X),
	pai(P, Y),
	mae(M, X),
	mae(M, Y),
	not(X=Y).

% comando trace -> passo a passo

gerou(X, Y) :-
	pai(X, Y).
gerou(X, Y) :-
	mae(X, Y).

ancestral(X, Y) :-
	gerou(X, Y).

ancestral(X, Y) :-
	gerou(Z, Y),
	ancestral(X,Z).


% listing(homem) - Lista todos os homens


% Fatorial
fatorial(0, 1).
fatorial(1, 1).
%fatorial(N, FatX) :-
	%	Y is X - 1,
	%	fatorial(Y, FatY),
	%	FatX is 
	
% Listas dinamicas em Prolog
% [Cabeca | Cauda]
% cauda eh uma sublista com o resto

% Conta o numero de elementos de uma lista
num_elementos([],0).
num_elementos([Cabeca|Cauda], N):-
	num_elementos(Cauda, NC),
	N is NC + 1.
somatoria([],0).
somatoria([Cabeca | Cauda], S) :-
	somatoria(Cauda, SC),
	S is SC+Cabeca.

% Calcula a media dos elementos de uma lista

media([],0).
media(Lista, M) :-
	somatoria(Lista, S),
	num_elementos(Lista, N),
	M is S / N.

% Concatenadas: Concatena duas lista
% concatenadas(L1, L2, L3) => L3 = L1 + L2
% concatenadas([a,b],[c,d], L) => L = [a, b, c, d]
concatenadas([], L, L).
concatenadas([C | R], L2, [C | R2]) :-
	concatenadas(R, L2, R2).

% Verifica se um item pertence a uma lista
% pertence_a(4, [1, 2, 3, 4])

% _: variavel c_ringa - pode ser qualquer coisa 
pertence_a(X, [X | _]).

pertence_a(X, [_ | Cauda]):-
	pertence_a(X, Cauda).


% Listifica todos os termos de uma lista 
% listificadas([a,b], L) => L = [[a], [b]]

listificadas([], []).
listificadas([X|C1], [[X]|C2]):-
	listificadas(C1, C2).

% Remove repetidas

% Exercicio 1
% Ultimo
ultimo([Cabeca|Cauda], Cabeca):-
	num_elementos(Cauda, 0).
ultimo([Cabeca|Cauda],Y):-
	ultimo(Cauda,Y).


% Exercicio 2
% Lista o dobro de todos os elementos da lista dada como parametro
lista_dobro([],[]).
lista_dobro([Cabeca | Cauda], [Y | C2]) :-
	Y is Cabeca * 2,
	lista_dobro(Cauda, C2).



% Exercicio 4
invertidas([], []).
invertidas([Cabeca | Cauda], X):-
	invertidas(Cauda, Y),
	concatenadas(Y, [Cabeca], X).


elem_repetidas([],[]).
elem_repetidas([Cabeca | Cauda],[Cabeca | C2]) :-
	pertence_a(Cabeca, Cauda),
	elem_repetidas(Cauda, C2),
	not(pertence_a(Cabeca, C2)).
elem_repetidas([Cabeca | Cauda], L) :-
	not(pertence_a(Cabeca, Cauda)),
	elem_repetidas(Cauda,L).


sprit([], _,[],[]).
sprit([X|R], N, [X|[]],R):-
	N is 0.
sprit([Cabeca|Cauda], N, [X1,R1], L2):-
	N1 is N-1,
	sprit(R,N1,R1,L2).


% Estudo dirigido 

% Exercicio 1

% Exercicio 2 - Intercaladas

intercaladas([],[],[]).
intercaladas([],L,L).
intercaladas(L,[],L).
intercaladas([X|R1], [Y|R2], [X,Y|R3]):-
	intercaladas(R1,R2,R3).

% Exercicio 3 - Inserção ordenada

insercao_ord(N,[],[N]).
insercao_ord(N,[X|R],L):-
	N >= X,
	insercao_ord(N,R,L).
insercao_ord(N,[X|R],[N,X|R]):-
	N =< X.

% Exercicio 4 - Ordenada

ordenada([],[]).
ordenada([C1|Cauda], L):-
	insercao_ord(C1,L, L1),
	ordenada(Cauda,L).

% Remove repetidos

remove_repetidos([],[]).
remove_repetidos([X|C], [X|C1]):-
	not(pertence_a(X,C)),
	remove_repetidos(C,C1).
remove_repetidos([_|C],L):-
	remove_repetidos(C,L).

% Intersecao

intersecao([X|C], L2):-
	pertence_a(X,L2).

intersecao([_|C],L2):-
	intersecao(C,L2).

% Uniao

uniao(L1,L2, R):-
	concatenadas(L1,L2,R1),
	remove_repetidos(R1, R).

% Busca
busca(X,[],[X]).

busca(X,[C1|R1],R):-
	intersecao(X,C1),
	uniao(X,C1,Comp),
	busca(R1,Comp,R).	

busca(X,[C1|R1],[C1,R2]):-
	busca(X,C1,R2).

% Subculturas
sub_culturas([],[]).
sub_culturas([X|C],R):-
	sub_culturas(C,Comp);
	busca(X,Comp,R).



