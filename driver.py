import pygame
from pygame.locals import *

class Driver:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.driverimg = pygame.image.load('taxi.png')

    def setupCar(self, gamedisplay):
        gamedisplay.blit(self.driverimage, (self.x, self.y))

    def moveLeft(self, K_LEFT):
        self.x -= 1
        return self.x

    def moveRight(self,K_RIGHT):
        self.x += 1
        return self.x

    def moveUp(self, K_UP):
	    self.y +=1
	    return self.y

    def moveDown(self,K_DOWN):
	    self.y-=1
	    return self.y
