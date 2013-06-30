import sys, pygame

class Window:
	def __init__(self, G):
		pygame.init()
		self.delay  = 100
		#dimensao da celula
		self.dim_cell = 15

		#velocidade da celula
		self.speed = self.dim_cell

		#dimensao da tela
		self.size = self.width, self.height = self.dim_cell * len(G[0]), self.dim_cell * len(G)
		self.screen = pygame.display.set_mode(self.size)

		#cor do fundo
		self.color = 0, 0, 0


		#elementos do jogo
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

		self.position = self.pacmano.get_rect()
		self.d = [0, 0]
		self.addGrid(G)

	def addGrid(self, G):
		self.G = []
		for x in range(0, len(G)):
			self.G.append("");
			for y in range(0, len(G[x])):
				self.G[x] += G[x][y]

	def paintGrid(self):
		for x in range(0, len(self.G[0])):
			for y in range(0, len(self.G)):
				if self.G[y][x] == '#':
					self.position = self.parede.get_rect()
					self.position = self.position.move(x * self.dim_cell, y * self.dim_cell)
					self.screen.blit(self.parede, self.position)
				elif self.G[y][x] == '+':
					self.position = self.pacman.get_rect()
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
		
	def run(self):
		print self.G

		self.screen.fill(self.color)
		self.paintGrid()
		pygame.display.flip()

		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						self.d[0] = -self.speed
						self.d[1] = 0
						self.pacman = pygame.transform.rotate(self.pacmano, 360)
					elif event.key == pygame.K_RIGHT:
						self.d[0] = self.speed
						self.d[1] = 0
						self.pacman = pygame.transform.rotate(self.pacmano, 180)
					elif event.key == pygame.K_UP:
						self.d[0] = 0
						self.d[1] = -self.speed
						self.pacman = pygame.transform.rotate(self.pacmano, 270)
					elif event.key == pygame.K_DOWN:
						self.d[0] = 0
						self.d[1] = self.speed
						self.pacman = pygame.transform.rotate(self.pacmano, 90)
				if event.type == pygame.KEYUP:
					self.d = [0, 0]

			

			#Atualiza posicao do pacman
			self.position = self.position_pac_man 

			if (self.position[0] + self.d[0] >= 0 and 
				self.position[0] + self.d[0] <= self.width - self.position[2] and
				self.position[1] + self.d[1] >= 0 and 
				self.position[1] + self.d[1] <= self.height - self.position[3]):

				self.position_pac_man = self.position.move(self.d)	
	
				self.screen.blit(self.pacman, self.position_pac_man)

				pygame.display.flip()

			pygame.time.delay(self.delay)



