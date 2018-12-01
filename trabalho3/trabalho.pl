% Nome: Winderson Jose Barboza dos Santos
% Disciplina: Inteligencia Artificial
% Professor: Chaua
% Curso: Ciência da computação

% Exercicio 1
% num_elementos
num_elementos([],0).
num_elementos([Cabeca|Cauda], N):-
	num_elementos(Cauda, NC),
	N is NC + 1.

% Exercicio 2 
% intercaladas
intercaladas([],[],[]).
intercaladas([],L,L).
intercaladas(L,[],L).
intercaladas([X|R1], [Y|R2], [X,Y|R3]):-
	intercaladas(R1,R2,R3).

% Exercicio 3 
% inserção ordenada
insercao_ord(N,[],[N]).
insercao_ord(N,[X|R],[X|L]):-
	N >= X,
	insercao_ord(N,R,L).
insercao_ord(N,[X|R],[N,X|R]):-
	N =< X.

% Exercicio 4
% ordenada
ordenada([],[]).
ordenada([C1|Cauda], L):-
	insercao_ord(C1,L, L1),
	ordenada(Cauda,L).

% Exercicio 5
% Subculturas
subcultura([],[]).
subcultura([X|C],R):-
	subcultura(C,Comp);
	busca(X,Comp,R).
