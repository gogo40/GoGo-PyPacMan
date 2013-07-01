# -*- coding: utf-8 -*-

"""
PyPacMan
Copyright (c) 2013 - Péricles Lopes Machado

This file is distributed under the MIT license. See LICENSE for details.
"""

import sys, pygame
from pypacman.ai import *
from pypacman.game import *

"""
Implementação da janela de visualização do jogo
"""
class Window:
	def __init__(self, G, ai, delay = 100):

		#controlador do jogo
		self.game = game_control.Game(G)

		#controlador da AI
		self.ai = ai


		self.delay  = delay
		#dimensao da celula
		self.dim_cell = 15

		#velocidade da celula
		self.speed = self.dim_cell

		#dimensao da tela
		self.n_cell = len(G);
		self.m_cell = len(G[0]);

		self.size = self.width, self.height = self.dim_cell * len(G[0]), self.dim_cell * len(G)

		self.screen = pygame.display.set_mode((self.width, self.height + 50))
		pygame.display.set_caption('PyPacMan')
		
		#cor do fundo
		self.BLACK = 0, 0, 0
		self.RED = (255, 0, 0)
		self.WHITE = (255, 255, 255)
		self.GREEN = (0, 255, 0)
		self.BLUE = (0, 0, 128)
		self.YELLOW = (255, 255, 0)

		self.color = self.BLACK


		#elementos do jogo
		self.empty = pygame.Surface((self.dim_cell, self.dim_cell))
		self.empty.fill(self.color)

		self.pacmano = pygame.image.load("imgs/pacman.png")
		self.pacman = self.pacmano = pygame.transform.smoothscale(self.pacmano, (self.dim_cell, self.dim_cell))

		self.fruta = pygame.image.load("imgs/fruta.png")
		self.fruta = pygame.transform.smoothscale(self.fruta, (self.dim_cell, self.dim_cell))
		
		self.fantasma = [
			pygame.image.load("imgs/fantasma1.png"),
			pygame.image.load("imgs/fantasma2.png"),
			pygame.image.load("imgs/fantasma3.png"),
			pygame.image.load("imgs/fantasma4.png")
		]

		self.fantasma[0] = pygame.transform.smoothscale(self.fantasma[0], (self.dim_cell, self.dim_cell))
		self.fantasma[1] = pygame.transform.smoothscale(self.fantasma[1], (self.dim_cell, self.dim_cell))
		self.fantasma[2] = pygame.transform.smoothscale(self.fantasma[2], (self.dim_cell, self.dim_cell))
		self.fantasma[3] = pygame.transform.smoothscale(self.fantasma[3], (self.dim_cell, self.dim_cell))

		self.parede = pygame.image.load("imgs/parede.png")
		self.parede = pygame.transform.smoothscale(self.parede, (self.dim_cell, self.dim_cell))
		
		#Fonte do jogo
		self.fonte = pygame.font.Font('fonts/astrolyt.ttf', 16)

		self.position = self.pacmano.get_rect()
		self.real_pos_pac_man = [0, 0] 
		self.d = [0, 0]
		self.dr = [0, 0]
		
		self.addGrid(G)

	"""
	Adiciona mensagem do jogo
	"""
	def addMsg(self, msg, color, x = 200, y = 200):
		msg = self.fonte.render(msg, True, color, self.BLACK)
		msg_rect = msg.get_rect()
		msg_rect = msg_rect.move(x, y)

		self.screen.blit(msg, msg_rect)

		pygame.display.flip()
		
	"""
	Adiciona Score do jogo
	"""
	def addScore(self, msg, score):
		msg = self.fonte.render(msg, True, self.BLUE, self.BLACK)
		msg_rect = msg.get_rect()
		msg_rect = msg_rect.move(0, self.height)

		self.screen.blit(msg, msg_rect)

		score = self.fonte.render(score, True, self.WHITE, self.BLACK)
		score_rect = score.get_rect()
		score_rect = score_rect.move(70, self.height)

		self.screen.blit(score, score_rect)

		pygame.display.flip()

	"""
	Adiciona grade do jogo
	"""
	def addGrid(self, G):
		self.G = G

	"""
	Pinta a tela do jogo
	"""
	def paintGrid(self):	
		for x in range(0, len(self.G[0])):
			for y in range(0, len(self.G)):
				if self.G[y][x] == '#':
					self.position = self.parede.get_rect()
					self.position = self.position.move(x * self.dim_cell, y * self.dim_cell)
					self.screen.blit(self.parede, self.position)
				elif self.G[y][x] == '+':
					self.position = self.pacman.get_rect()
					self.real_pos_pac_man = [y, x]
					self.position_pac_man = self.position.move(x * self.dim_cell, y * self.dim_cell)
					self.screen.blit(self.pacman, self.position_pac_man)
				elif self.G[y][x] == 'x' or self.G[y][x] == '*':
					self.position = self.fantasma[(x+y)%4].get_rect()
					self.position = self.position.move(x * self.dim_cell, y * self.dim_cell)
					self.screen.blit(self.fantasma[(x+y)%4], self.position)
				elif self.G[y][x] == 'o':
					self.position = self.fruta.get_rect()
					self.position = self.position.move(x * self.dim_cell, y * self.dim_cell)
					self.screen.blit(self.fruta, self.position)

	"""
	Atualiza posicao do fantasma
	"""
	def move_phantom(self, orig, dest):
		xo, yo = orig
		xf, yf = dest

		l = list(self.G[xo]);
		l[yo] = '.';
		self.G[xo] = "".join(l);

		l = list(self.G[xf]);
		l[yf] = '*';
		self.G[xf] = "".join(l);

		position =  self.fantasma[(xf+yf)%4].get_rect()
		positiono = position.move(yo * self.dim_cell, xo * self.dim_cell)
		self.screen.blit(self.empty, positiono)

		position =  self.fantasma[(xf+yf)%4].get_rect()
		positionf = position.move(yf * self.dim_cell, xf * self.dim_cell)
		self.screen.blit(self.fantasma[(xf+yf)%4], positionf)

		pygame.display.flip()
		

	"""
	Atualiza posicao do pacman
	"""
	def move_pac_man(self):		
		position = self.position_pac_man 
		real_pos = self.real_pos_pac_man
		
		xo, yo = real_pos

		x = (real_pos[0] + self.dr[0] + self.n_cell) % self.n_cell;
		y = (real_pos[1] + self.dr[1] + self.m_cell) % self.m_cell;
		
		"""
		Verifica se pac-man ainda vive
		"""
		if self.G[xo][yo] != '+':
			return False

		if self.G[x][y] == 'o':
			self.game.add_point(1)
			
		if self.G[x][y] == '.' or self.G[x][y] == 'o':
			self.real_pos_pac_man = [x, y]
			self.screen.blit(self.empty, position)
			
			l = list(self.G[real_pos[0]]);
			l[real_pos[1]]='.';
			self.G[real_pos[0]]="".join(l);

			l = list(self.G[x]);
			l[y]='+';
			self.G[x]="".join(l);

			N = self.dim_cell * self.n_cell
			M = self.dim_cell * self.m_cell

			self.position_pac_man[0] = (position[0] + self.d[0] + M) % M
			self.position_pac_man[1] = (position[1] + self.d[1] + N) % N

			self.screen.blit(self.pacman, self.position_pac_man)

			pygame.display.flip()
		return True

	"""
	Roda renderização do jogo e captura de movimentos do jogador e da AI
	"""
	def run(self):
		self.screen.fill(self.color)
		self.paintGrid()
		pygame.display.flip()
		
		is_running = True
		is_paused = False

		while is_running:
			for event in pygame.event.get():
				#Fecha janela
				if event.type == pygame.QUIT: 
					is_running = False
					break

				#Trata eventos da AI
				elif event.type == pygame.USEREVENT:

					#imprime grade
					if event.action == ai_control.PRINT_G:
						G = event.value
						for x in range(0, len(G)):
							print G[x]

					#imprime fantasmas
					elif event.action == ai_control.PRINT_P:
						print "Phatoms:"
						print event.value

					#move fantasma
					elif event.action == ai_control.MOVE_P:
						mov = event.value
						orig = event.origin
						
						self.move_phantom(orig, mov)

				#Trata Entrada de usuario
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
						is_paused = not is_paused
						#Pausa AI
						self.ai.call_pause()
						break
					elif event.key == pygame.K_ESCAPE:
						is_running = False
						break
					elif event.key == pygame.K_LEFT:
						self.d[0] = -self.speed
						self.d[1] = 0

						self.dr[1] = -1
						self.dr[0] = 0

						self.pacman = pygame.transform.rotate(self.pacmano, 360)
					elif event.key == pygame.K_RIGHT:
						self.d[0] = self.speed
						self.d[1] = 0

						self.dr[1] = 1
						self.dr[0] = 0

						self.pacman = pygame.transform.rotate(self.pacmano, 180)
					elif event.key == pygame.K_UP:
						self.d[0] = 0
						self.d[1] = -self.speed

						self.dr[1] = 0
						self.dr[0] = -1

						self.pacman = pygame.transform.rotate(self.pacmano, 270)
					elif event.key == pygame.K_DOWN:
						self.d[0] = 0
						self.d[1] = self.speed

						self.dr[1] = 0
						self.dr[0] = 1

						self.pacman = pygame.transform.rotate(self.pacmano, 90)
			
			self.addScore("Score:", self.game.get_score())
		
			if not is_paused:
				#Verifica se jogo acabou
				if self.game.is_over():
					self.addMsg("You win!              ", self.GREEN, 200, self.height)
					break

				#Move o pac man e verifica se ele tá vivo ainda
				if not self.move_pac_man():
					self.addMsg("You lose!             ", self.RED, 200, self.height)
					break

				self.addMsg("Press ENTER to pause.   ", self.WHITE, 200, self.height)
			else:
				self.addMsg("Paused.                    ", self.WHITE, 200, self.height)

			#Dorme um pouco
			pygame.time.delay(self.delay)

		#aguarda ESC ou QUIT
		self.addMsg("Press ESC to exit.", self.YELLOW, 500, self.height)
		while is_running:
			for event in pygame.event.get():
				#Fecha janela
				if event.type == pygame.QUIT: 
					is_running = False
					break

				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						is_running = False
						break
			pygame.time.delay(self.delay)

		#Desliga AI
		self.ai.call_exit()
			



