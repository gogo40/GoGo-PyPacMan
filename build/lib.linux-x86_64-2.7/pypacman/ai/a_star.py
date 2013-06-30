# -*- coding: utf-8 -*-

"""
PyPacMan
Copyright (c) 2013 - Péricles Lopes Machado

This file is distributed under the MIT license. See LICENSE for details.
"""


"""
Algoritmo A* 
Autores: 
    Peter Hart, Nils Nilsson and Bertram Raphael 
Implmentador:
 	Péricles Lopes Machado [gogo40] (pericles.raskolnikoff.gmail.com)
Tipo: 
    Grafos
Descrição: 
    O Algoritmo A* é uma generalização do algoritmo de Dijkstra que
permite acelerar a busca com uma heuristica que utiliza propriedades do grafo 
para estimar a distância para o destino. Este algoritmo é ideal quando aplicados
em grades ou representações espaciais e em situações em que já conhecemos a
posição do destino.

Complexidade: 
    O(|E| log |V|)
Dificuldade: 
    medio
Referências:
    [1] http://en.wikipedia.org/wiki/A*_search_algorithm
    [2] http://falapericles.blogspot.com.br/2009/05/o-algoritmo.html
"""

from heapq import *;
from math import *;

"""
Gera vetor contendo o caminho
"""
def gera_caminho(caminho, pi, u):
	ux = u[0];
	uy = u[1];

	if pi[ux][uy] == None:
		caminho.append(u)
	else:
		gera_caminho(caminho, pi, pi[ux][uy]);
		caminho.append(u)

"""
Função para imprimir o caminho
"""
def imprime_caminho(pi, u):
	ux = u[0];
	uy = u[1];

	if pi[ux][uy] == None:
		print u;
	else:
		imprime_caminho(pi, pi[ux][uy]);
		print u;

"""
Função para 'renderizar' o jogador numa posição da grade
"""
def renderizar_grade(G, ux, uy):
	l = list(G[ux]);
	l[uy] = 'x';
	G[ux] = "".join(l);

	for i in range(0, len(G)):
		print " ", G[i];

	print "---------";

	l = list(G[ux]);
	l[uy] = '.';
	G[ux] = "".join(l);

"""
Função para 'renderizar' a trajetória percorrida
"""
def renderizar_caminho(pi, G, u):
	ux = u[0];
	uy = u[1];

	if pi[ux][uy] == None:
		renderizar_grade(G, ux, uy);
	else:
		renderizar_caminho(pi, G, pi[ux][uy]);
		renderizar_grade(G, ux, uy);

"""
Heurística que estima a distancia para o destino: (Heuristica padrão)

H(p, t) = sqrt((p.x - t.x)^2 + (p.y - t.y)^2)

Nesse código utilizamos o quadrado da distância euclidiana como estimativa.
"""

def h_std(s, t):
	Dx = s[0] - t[0];
	Dy = s[1] - t[1];
	return sqrt(Dx * Dx + Dy * Dy);

"""
Métrica Euclidiana
"""
def dist_e(s, t):
	Dx = s[0] - t[0];
	Dy = s[1] - t[1];
	return sqrt(Dx * Dx + Dy * Dy);

"""
Movimentacoes padrão
"""
dx_std = [-1,  0,  0,  1];
dy_std = [ 0, -1,  1,  0];

"""
Função que aplica o A* a uma grade
Este algoritmo utiliza uma grade para realizar a busca.
A origem é marcada com o símbolo 'x' e o destino é marcado
com o simbolo '+'.
Uma região desobstruída é marcada por '.'.
Uma fruta é representada por 'o'.
Um fantasma é representado por '*'.

G é a grade.
dx, dy representam os deslocamentos possíveis em um movimento.
H é a heuristica utilizada
dist é a métrica.
"""

def a_star(G, dx = dx_std, dy = dy_std, H = h_std, dist = dist_e):
	"""
	Localizando a posição do jogador ('x') e do destino ('+')
	e inicializa matriz com estimativa de distância D.
	"""

	D = [];
	pi = [];
	t = None
	for x in range(0, len(G)):
		D += [[]];
		pi += [[]];
		for y in range(0, len(G[x])):
			D[x] += [None];
			pi[x] += [None];
			if G[x][y] == 'x':
				s = (x, y);
				l = list(G[x]);
				l[y] = '.';
				G[x] = "".join(l);
			elif G[x][y] == '+':
				t = (x, y);
	if t == None:
		return None

	Q = [];

	D[s[0]][s[1]] = 0;
	heappush(Q, (0, s));

	"""
	Enquanto a fila de prioridade não estiver vazia tente verificar se o topo
	da fila é melhor opção de rota para se chegar nos adjascentes. Como o topo
	já é o mínimo, então garante-se que D[u] já está minimizado no momento.
	"""
	while Q:
		p = heappop(Q)[1];

		u = (p[0], p[1]);
		ux = u[0];
		uy = u[1];

		"""
		Como já chegamos no destino, podemos parar a busca
		"""
		if u == t:
			break;

		for i in range(0, len(dx)):
			vx = (u[0] + dx[i] + len(G)) % len(G);
			vy = (u[1] + dy[i] + len(G[vx])) % len(G[vx]);

			v = (vx, vy);

			duv = dist(u, v); 
			if (D[vx][vy] > D[ux][uy] + duv or D[vx][vy] == None) and (G[vx][vy] == '.' or G[vx][vy] == '+' or G[vx][vy] == '*' or G[vx][vy] == 'o'):
				D[vx][vy] = D[ux][uy] + duv;
				pi[vx][vy] = u;
				"""
				A única diferença entre o A* e o dijkstra é o modo como é ordenado a heap.
				No caso, ela utiliza a heurítica H que procura colocar no topo os pontos mais
				próximos do destino.
				"""
				heappush(Q, (D[vx][vy] + H(v, t), v));
	return {'D':D, 't': t, 'pi': pi, 'u': u, 's': s};



