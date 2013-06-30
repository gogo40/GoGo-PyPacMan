import sys, pygame
import a_star
import time
from threading import *
from multiprocessing import Process, Queue

def ai_control(ai):
	is_running = 0
	
	while is_running < 20:
		ai.echo()
		is_running = is_running + 1

		time.sleep(0.2)
		

class AIControl:
	def __init__(self, G):
		self.G = G
		self.t = Thread(target=ai_control, args=(self,))
		self.l = Lock()

	def start(self):
		self.t.start()

	def wait(self):
		self.t.join()

	def lock(self):
		self.l.acquire()

	def unlock(self):
		self.l.release()

	def echo(self):
		for l in self.G:
			print l


