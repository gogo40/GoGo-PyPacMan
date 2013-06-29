# -*- coding: utf-8 -*-
from AI import * 

res = AI.Astar(G, dx, dy, Hstd, distE);

D = res['D'];
t = res['t'];
pi = res['pi'];
u = res['u'];

if D[t[0]][t[1]] != None:
	print "A distância entre s e t é: ", D[t[0]][t[1]]; 
	"""
	Descomente essa linha caso queira ver a sequencia de passos percorrido pelo jogador
	"""
	imprime_caminho(pi, t);
	"""
	Descomente essa linha se quiseres ver o caminho percorrido na grade
	"""
	#renderizar_caminho(pi, G, u);
else:
	print "Não existe caminho entre s e t!"
