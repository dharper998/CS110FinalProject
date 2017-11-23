import pygame
from pygame.locals import *

class Background:
	def __init__(self):
		self.image = pygame.image.load('assets/'+'Scrolling_Background.png').convert_alpha()
		self.x = 0
		self.y = -650
		self.speed = 3.0

	def scroll(self):
		#Move the background down by the current speed
		self.y += self.speed

	def reset(self):
		#Reset the background to its original position
		self.y = -650

	def speedup(self):
		#Increase the background speed up to a max of 5
		if self.speed < 5.0:
			self.speed += 0.25

	def slowdown(self):
		#Decrease the background speed down to a min of 2
		if self.speed > 2.0:
			self.speed -= 0.25

	def speedreset(self):
		self.speed = 3.0
