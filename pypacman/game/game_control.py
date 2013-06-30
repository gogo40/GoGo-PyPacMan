# -*- coding: utf-8 -*-

"""
PyPacMan
Copyright (c) 2013 - Péricles Lopes Machado

This file is distributed under the MIT license. See LICENSE for details.
"""

"""
Classe que controla o game
"""
class Game:
	def __init__(self, G):
		self.score = 0
		self.G = G

	def add_point(self, point):
		self.score = self.score + point

	def get_score(self):
		return "%09d  " % self.score

	def print_score(self):
		print "Score:"
		print self.score

	def is_over(self):
		n_fruit = 0	
		for x in range(0, len(self.G)):
			for y in range(0, len(self.G[x])):
				if self.G[x][y] == 'o':
					n_fruit = n_fruit + 1
		return n_fruit == 0 

