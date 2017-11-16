import pygame
from pygame.locals import *

class Background:
	def __init__(self):
		self.image = pygame.image.load('assets/'+'Scrolling_Background.png').convert_alpha()
		self.x = 0
		self.y = -650
		self.speed = 5
	def scroll(self):
		self.y += (self.speed)
	def reset(self):
		self.y = -650
