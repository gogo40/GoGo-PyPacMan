import sys, pygame
import a_star
import time
from threading import *
from multiprocessing import Queue

EXIT = 1
PRINT_G = 2

def ai_control(ai):
	is_running = True

	while is_running:
		for event in ai.get():
			if event.type == EXIT:
				is_running = False
				break

		if is_running:
			evt = pygame.event.Event(pygame.USEREVENT, {"action" : PRINT_G, "value" : ai.G})
			pygame.event.post(evt)

			time.sleep(0.2)

class AIEvent:
	def __init__(self, tp, value = {}):
		self.__dict__ = value
		self.type = tp

class AIControl:
	def __init__(self, G):
		self.G = G
		self.t = Thread(target=ai_control, args=(self,))
		self.l = Lock()
		self.evts = Queue()

	def put(self, evt):
		self.evts.put(evt)

	def call_exit(self):
		self.put(AIEvent(EXIT))
	
	def get(self):
		if self.evts.empty():
			return []
		return [self.evts.get()]

	def start(self):
		self.t.start()

	def wait(self):
		self.t.join()



