import pygame
from pygame.locals import *

class Background:
	def __init__(self):
		self.image = pygame.image.load('assets/'+'Scrolling_Background.png').convert_alpha()
		self.x = 0
		self.y = -650
		self.speed = 3.0

	def scroll(self):
		self.y += (self.speed)

	def reset(self):
		self.y = -650

	def speedup(self):
		if self.speed < 5.0:
			self.speed += 0.25
	def slowdown(self):
		if self.speed > 2.0:
			self.speed -= 0.25
