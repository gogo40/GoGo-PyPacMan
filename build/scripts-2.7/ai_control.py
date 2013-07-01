# -*- coding: utf-8 -*-

"""
PyPacMan
Copyright (c) 2013 - Péricles Lopes Machado

This file is distributed under the MIT license. See LICENSE for details.
"""

import sys, pygame
import a_star
import time
import threading
import Queue


"""
MACROS DO SISTEMA DE AI
"""
"""
FINALIZA AI
"""
EXIT = 1
"""
IMPRIME GRADE
"""
PRINT_G = 2
"""
IMPRIME FANTASMAS
"""
PRINT_P = 3
"""
MOVE FANTASMA
"""
MOVE_P = 4
"""
PAUSE APERTADO
"""
PAUSE = 5

"""
Copia e marca uma grade
"""
def copy_g(G, p):
	new_G = []
	for x in range(0, len(G)):
		new_G.append("")
		for y in range(0, len(G[x])):
			if x == p[0] and y == p[1]:
				new_G[x] = new_G[x] + 'x'
			else: 
				new_G[x] = new_G[x] + G[x][y]
	return new_G


"""
Encontra fantasmas da grade
"""
def find_phantoms(G):
	phantoms = []

	for x in range(0, len(G)):
		for y in range(0, len(G[x])):
			if G[x][y] == '*':
				phantoms.append((x,y))

	return phantoms

"""
Controla o movimento dos fantasmas
"""
def ai_control(ai):
	is_running = True
	is_paused = False

	while is_running:
		for event in ai.get():
			if event.type == EXIT:
				is_running = False
				break
			elif event.type == PAUSE:
				is_paused = not is_paused

		if is_running and (not is_paused):
			"""	
			#Mensagens de depuração		
			evt = pygame.event.Event(pygame.USEREVENT, {"action" : PRINT_G, "value" : ai.G})
			pygame.event.post(evt)
			"""

			#Localiza fantasmas da grade
			pht = find_phantoms(ai.G)

			for p in pht:
				#copia e marca a grade
				G = copy_g(ai.G, p)

				#encontra menor caminho para o pacman
				res = a_star.a_star(G)

				if res != None:
					caminho = []
					pi = res['pi']
					t = res['t']
					a_star.gera_caminho(caminho, pi, t);

					#envia decisao da AI
					if len(caminho) > 1:
						evt = pygame.event.Event(pygame.USEREVENT, {"action" : MOVE_P, "value" : caminho[1], 
	"origin" : p, "dest": t})
						pygame.event.post(evt)

		time.sleep(ai.speed)


"""
Eventos da AI, utilizado para comunicação da AI com o resto do sistema
"""
class AIEvent:
	def __init__(self, tp, value = {}):
		self.__dict__ = value
		self.type = tp

"""
Classe de controle da AI
"""
class AIControl:

	"""
	Speed controla a velocidade dos fantasmas
	"""
	def __init__(self, G, speed = 0.8):
		self.G = G
		self.t = threading.Thread(target=ai_control, args=(self,))
		self.evts = Queue.Queue()
		self.speed = speed

	def put(self, evt):
		self.evts.put(evt)

	def call_exit(self):
		self.put(AIEvent(EXIT))

	def call_pause(self):
		self.put(AIEvent(PAUSE))
	
	def get(self):
		if self.evts.empty():
			return []
		return [self.evts.get()]

	def start(self):
		self.t.start()

	def wait(self):
		self.t.join()



