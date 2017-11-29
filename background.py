import pygame
from pygame.locals import *

class Background:
	def __init__(self):
		self.image = pygame.image.load('assets/'+'Scrolling_Background.png').convert_alpha()
		self.x = 0
		self.y = -650
		self.speed = 3.0

	def scroll(self):
		'''
		Moves the background down by the current speed
		Paramlist: none
		Return: none
		'''
		self.y += self.speed

	def reset(self):
		'''
		Resets the background to its original position
		Paramlist: none
		Return: none
		'''
		self.y = -650

	def speedup(self):
		'''
		Increases the backgrounds scrolling speed to a max of 5
		Paramlist: none
		Return: none
		'''
		if self.speed < 5.0:
			self.speed += 0.25

	def slowdown(self):
		'''
		Decreases the backgrounds scrolling speed to a min of 2
		Paramlist: none
		Return: none
		'''
		if self.speed > 2.0:
			self.speed -= 0.25

	def speedreset(self):
		'''
		Resets the scrolling speed to its original value
		Paramlist: none
		Return: none
		'''
		self.speed = 3.0
