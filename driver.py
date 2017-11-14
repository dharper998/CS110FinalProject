import pygame
from pygame.locals import *
import random

class Driver:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.driverimg = pygame.image.load("taxi.png")

    def setupCar(self, gamedisplay):
        gamedisplay.blit(self.driverimage, (self.x, self.y))

    def moveLeft(self):
        self.x -= 10

    def moveRight(self):
        self.x += 10
